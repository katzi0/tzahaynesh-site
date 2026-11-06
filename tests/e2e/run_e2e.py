"""Full Playwright pass over the built site.

Usage:
  npm run build && npx astro preview --port 4321 &
  (cd tests/e2e && npm i --no-save axe-core@4)
  python3 tests/e2e/run_e2e.py http://127.0.0.1:4321/tzahaynesh-site/ <out_dir>

Needs Playwright for Python with Chromium (pip install playwright;
playwright install chromium).

Screenshots every page at three widths, and checks per page: HTTP status,
lang/dir, a single h1 and no skipped heading levels, alt text on images,
console errors, horizontal overflow, internal links, noindex and the draft
bar, axe-core WCAG 2.0 A/AA. Plus interactions: skip link, mobile nav
toggle, library filters, and the no-JavaScript fallbacks.
"""
import json
import pathlib
import sys
import urllib.parse
import urllib.request

from playwright.sync_api import sync_playwright

BASE = sys.argv[1].rstrip("/") + "/"
OUT = pathlib.Path(sys.argv[2])
AXE = (pathlib.Path(__file__).parent / "node_modules/axe-core/axe.min.js").read_text()

PAGES = {
    "home": "",
    "about": "about/",
    "library": "library/",
    "track-therapy": "tracks/therapy/",
    "track-parent-guidance": "tracks/parent-guidance/",
    "track-supervision": "tracks/supervision/",
    "track-lectures-training": "tracks/lectures-training/",
    "track-organizations-academia": "tracks/organizations-academia/",
}
VIEWPORTS = {
    "mobile-375": {"width": 375, "height": 812},
    "tablet-768": {"width": 768, "height": 1024},
    "desktop-1440": {"width": 1440, "height": 900},
}

results = {"pages": {}, "interactions": {}, "links": {}}
failures = []


def fail(where, msg):
    failures.append(f"{where}: {msg}")


def status_of(url):
    try:
        req = urllib.request.Request(url, method="GET")
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:  # noqa: BLE001
        return str(e)


with sync_playwright() as p:
    browser = p.chromium.launch()
    all_links = set()

    for vp_name, vp in VIEWPORTS.items():
        ctx = browser.new_context(viewport=vp, locale="he-IL")
        for name, path in PAGES.items():
            page = ctx.new_page()
            console_errors = []
            page.on("console", lambda m, ce=console_errors: ce.append(m.text) if m.type == "error" else None)
            page.on("pageerror", lambda e, ce=console_errors: ce.append(str(e)))
            resp = page.goto(BASE + path, wait_until="networkidle")
            page.evaluate("document.fonts.ready")
            where = f"{name}@{vp_name}"
            r = results["pages"].setdefault(name, {})
            info = page.evaluate(
                """() => {
                  const hs = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')]
                    .filter(h => h.offsetParent !== null || getComputedStyle(h).position === 'fixed')
                    .map(h => +h.tagName[1]);
                  let skip = null;
                  for (let i = 1; i < hs.length; i++) if (hs[i] > hs[i-1] + 1) { skip = `h${hs[i-1]}→h${hs[i]}`; break; }
                  return {
                    title: document.title,
                    lang: document.documentElement.lang,
                    dir: document.documentElement.dir,
                    h1: document.querySelectorAll('h1').length,
                    firstHeading: hs[0] ?? null,
                    headingSkip: skip,
                    imgsNoAlt: [...document.images].filter(i => !i.hasAttribute('alt')).length,
                    overflowX: document.documentElement.scrollWidth - window.innerWidth,
                    noindex: !!document.querySelector('meta[name=robots][content*=noindex]'),
                    draftBar: !!document.querySelector('.draft-bar'),
                    articlesLinks: [...document.querySelectorAll('a')].filter(a => /\\/articles/.test(a.getAttribute('href')||'') || a.textContent.trim() === 'מאמרים').length,
                    links: [...document.querySelectorAll('a[href]')].map(a => a.href),
                  };
                }"""
            )
            for href in info.pop("links"):
                u = urllib.parse.urlsplit(href)
                if u.netloc == urllib.parse.urlsplit(BASE).netloc:
                    all_links.add(urllib.parse.urlunsplit((u.scheme, u.netloc, u.path, "", "")))
            info["status"] = resp.status if resp else None
            info["consoleErrors"] = console_errors
            r[vp_name] = info

            if info["status"] != 200: fail(where, f"HTTP {info['status']}")
            if info["lang"] != "he" or info["dir"] != "rtl": fail(where, f"lang/dir {info['lang']}/{info['dir']}")
            if info["h1"] != 1: fail(where, f"{info['h1']} h1 elements")
            if info["firstHeading"] != 1: fail(where, f"first heading is h{info['firstHeading']}")
            if info["headingSkip"]: fail(where, f"heading level skip {info['headingSkip']}")
            if info["imgsNoAlt"]: fail(where, f"{info['imgsNoAlt']} images without alt")
            if info["overflowX"] > 1: fail(where, f"horizontal overflow {info['overflowX']}px")
            if not info["noindex"]: fail(where, "missing noindex")
            if not info["draftBar"]: fail(where, "missing draft bar")
            if info["articlesLinks"]: fail(where, f"{info['articlesLinks']} links to מאמרים")
            if console_errors: fail(where, f"console errors {console_errors}")

            shot = OUT / vp_name / f"{name}.jpg"
            shot.parent.mkdir(parents=True, exist_ok=True)
            page.screenshot(path=str(shot), full_page=True, type="jpeg", quality=80)

            if vp_name == "desktop-1440":
                page.add_script_tag(content=AXE)
                axe = page.evaluate(
                    """async () => {
                      const r = await axe.run(document, { runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa'] } });
                      return r.violations.map(v => ({ id: v.id, impact: v.impact, help: v.help, nodes: v.nodes.length,
                        targets: v.nodes.slice(0, 3).map(n => n.target.join(' ')) }));
                    }"""
                )
                r["axe"] = axe
                for v in axe:
                    fail(name, f"axe {v['id']} ({v['impact']}): {v['help']} x{v['nodes']} e.g. {v['targets']}")
            page.close()
        ctx.close()

    # Internal links resolve.
    for link in sorted(all_links):
        st = status_of(link)
        results["links"][link] = st
        if st != 200:
            fail("links", f"{link} -> {st}")

    I = results["interactions"]

    # Skip link is the first Tab stop and moves focus to main.
    ctx = browser.new_context(viewport=VIEWPORTS["desktop-1440"])
    page = ctx.new_page()
    page.goto(BASE, wait_until="networkidle")
    page.keyboard.press("Tab")
    first = page.evaluate("() => ({ text: document.activeElement.textContent.trim(), href: document.activeElement.getAttribute('href') })")
    I["firstTabStop"] = first
    if not (first["href"] or "").startswith("#"):
        fail("skip-link", f"first tab stop is {first}")
    ring = page.evaluate("() => getComputedStyle(document.activeElement).outlineStyle")
    I["focusOutline"] = ring
    if ring in ("none", ""):
        fail("focus", "no visible outline on first tab stop")
    ctx.close()

    # Mobile nav toggle.
    ctx = browser.new_context(viewport=VIEWPORTS["mobile-375"])
    page = ctx.new_page()
    page.goto(BASE, wait_until="networkidle")
    before = page.locator("#mainNav").is_visible()
    page.click("#navToggle")
    after = page.locator("#mainNav").is_visible()
    expanded = page.get_attribute("#navToggle", "aria-expanded")
    nav_labels = page.locator("#mainNav a").all_inner_texts()
    I["mobileNav"] = {"visibleBefore": before, "visibleAfter": after, "ariaExpanded": expanded, "labels": nav_labels}
    if before or not after or expanded != "true":
        fail("mobile-nav", f"toggle state before={before} after={after} aria-expanded={expanded}")
    page.screenshot(path=str(OUT / "mobile-375" / "home-nav-open.jpg"), type="jpeg", quality=80)
    if "הרצאות והכשרות" not in [l.strip() for l in nav_labels]:
        fail("mobile-nav", f"short lectures label missing: {nav_labels}")
    if any(l.strip() == "מאמרים" for l in nav_labels):
        fail("mobile-nav", "מאמרים still in nav")
    ctx.close()

    # Library filters.
    ctx = browser.new_context(viewport=VIEWPORTS["desktop-1440"])
    page = ctx.new_page()
    page.goto(BASE + "library/", wait_until="networkidle")
    vis = lambda: page.evaluate("() => [...document.querySelectorAll('.library-item')].filter(i => !i.hidden).map(i => [i.dataset.type, i.dataset.topic, i.dataset.mine])")
    total = len(vis())
    lib = {"total": total, "filtersVisible": page.locator("[data-filters]").is_visible()}
    page.click('.filter-chip[data-type="exercise"]')
    ex = vis(); lib["exercise"] = len(ex)
    if not ex or any(t != "exercise" for t, _, _ in ex): fail("library", f"type filter wrong: {ex}")
    page.click('.filter-chip[data-type="all"]')
    page.click('.filter-chip[data-topic="parenting"]')
    par = vis(); lib["parenting"] = len(par)
    if not par or any(tp != "parenting" for _, tp, _ in par): fail("library", f"topic filter wrong: {par}")
    page.click('.filter-chip[data-type="song"]')
    combo = vis(); lib["song+parenting"] = len(combo)
    lib["emptyMessageShown"] = page.locator("[data-empty]").is_visible()
    if combo or not lib["emptyMessageShown"]: fail("library", f"song+parenting should be empty with message: {combo}")
    page.click('.filter-chip[data-type="all"]')
    page.click('.filter-chip[data-topic="all"]')
    page.click("[data-mine-toggle]")
    mine = vis(); lib["mine"] = len(mine)
    if not mine or any(m != "true" for _, _, m in mine): fail("library", f"mine toggle wrong: {mine}")
    lib["status"] = page.inner_text("[data-status]")
    page.click("[data-mine-toggle]")
    page.click('.filter-chip[data-topic="culture"]')
    page.screenshot(path=str(OUT / "desktop-1440" / "library-filtered-culture.jpg"), full_page=True, type="jpeg", quality=80)
    I["library"] = lib
    ctx.close()

    # Without JavaScript: nav present, library shows every item, filters hidden.
    ctx = browser.new_context(viewport=VIEWPORTS["mobile-375"], java_script_enabled=False)
    page = ctx.new_page()
    page.goto(BASE, wait_until="networkidle")
    nojs_nav = page.locator("#mainNav").is_visible()
    page.goto(BASE + "library/", wait_until="networkidle")
    nojs_items = page.locator(".library-item").count()
    nojs_filters = page.locator("[data-filters]").is_visible()
    I["noJs"] = {"navVisible": nojs_nav, "libraryItems": nojs_items, "filtersVisible": nojs_filters}
    if not nojs_nav: fail("no-js", "nav hidden without JS")
    if nojs_items != total or nojs_filters: fail("no-js", f"library without JS items={nojs_items} filters={nojs_filters}")
    ctx.close()

    # Reduced motion: no smooth scrolling.
    ctx = browser.new_context(viewport=VIEWPORTS["desktop-1440"], reduced_motion="reduce")
    page = ctx.new_page()
    page.goto(BASE, wait_until="networkidle")
    sb = page.evaluate("() => getComputedStyle(document.documentElement).scrollBehavior")
    I["reducedMotionScrollBehavior"] = sb
    if sb == "smooth": fail("reduced-motion", "smooth scrolling not suppressed")
    ctx.close()

    browser.close()

results["failures"] = failures
(OUT / "results.json").write_text(json.dumps(results, ensure_ascii=False, indent=2))
print(json.dumps({"failures": failures, "interactions": results["interactions"], "links": len(results["links"])}, ensure_ascii=False, indent=2))
