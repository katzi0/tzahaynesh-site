---
status: ready-for-agent
scope: design system + home page
---

# Design system and home page

## Problem Statement

צהיינש אדל־קרוט has no site of her own. Her copy is written, her five מסלולים are
settled, and the stack is chosen — but nothing is built, and there is no visual system
for anyone to build against.

A candidate theme now exists: a warm sand-and-sage palette with Frank Ruhl Libre over
Assistant, close enough to the existing סקיצה to be the same design language, and
measurably better on contrast. The page shipped with it, however, contradicts decisions
this project has already recorded. It shows four services instead of five and omits
הדרכת הורים — the audience she ranked first. It labels a nav item bare הדרכה, the one
label [ADR 0002](../adr/0002-five-tracks-not-four.md) forbids because Hebrew uses that
word both for supervising therapists and for guiding parents. It writes השירותים שלנו,
first person plural, on the site whose entire purpose is to separate her from a
two-person venture. And it fills the hero with an illustrated therapy room where the
brief asks for her portrait.

So the theme is usable and the page is not, and without an explicit decision the two
arrive together.

## Solution

Adopt the theme as the project's design system — its palette, type scale and component
shapes — corrected where it falls short of WCAG 2.0 AA, and rebuild the home page from
the copy deck rather than porting the supplied markup.

A visitor lands on one identity-led page. Within the first moments they read who she is
in her own words, see the credentials that make the claim real, and find five clearly
named doors — טיפול, הדרכת הורים, הדרכה וייעוץ למטפלים, הרצאות והכשרות, ארגונים
ואקדמיה — each labelled so unambiguously that a parent never opens a page written for
clinicians. ענווה תרבותית appears prominently and as one domain among several, never as
the whole of her.

For whoever builds the rest, the outcome is a token layer, a set of page primitives, and
one route proving them, so the remaining eight routes are assembly rather than design.

This build's job is narrower than a launch: it is the page that goes in front of her for
reaction, not a page that goes live. It carries the corrected structure and the theme
translated into an accessible system, but stands in openly — via a visible draft marker
and two honestly empty content slots, the portrait and the contact details — for what is
still missing. A nav that resolves in full, including stub אודות and מאמרים pages, lets
her judge the site's whole shape rather than four-fifths of it.

## User Stories

### Visitors choosing a route

1. As a parent at war with my adolescent, I want a door labelled הדרכת הורים, so that I
   do not have to work out whether a page about טיפול is meant for me or for my child.
2. As a parent, I want that door to say plainly that I am the client and my child is not
   in treatment, so that I know what I would be signing up for.
3. As an adult in a period of transition, I want a door labelled טיפול, so that I can
   tell in one glance that she treats people like me.
4. As a therapist seeking supervision, I want a door named for therapists rather than a
   bare הדרכה, so that I am not competing with parents for the same ambiguous link.
5. As a team leader in a welfare service, I want הרצאות והכשרות named as its own track,
   so that I can see she does bookable professional formats and not only clinical work.
6. As an HR manager, I want ארגונים ואקדמיה stated separately, so that I understand she
   works with organizations and not only with individuals.
7. As a training-programme coordinator, I want the academic side visible in the same
   track, so that I know she can teach inside a curriculum.
8. As any visitor, I want the five doors laid out as one scannable list, so that I can
   compare them without scrolling back and forth between cards.
9. As a visitor who arrives certain of what they want, I want to reach the right track
   without reading the identity section first, so that the page does not tax me for
   already knowing.
10. As a visitor who follows a track link, I want to arrive at a real page, so that the
    site does not dead-end me at the moment I commit.

### Visitors assessing whether to trust her

11. As a prospective client, I want her positioning line in her own voice at the top of
    the page, so that I get a sense of the person and not only the service list.
12. As a prospective client, I want to see her face, so that the first impression is a
    human being rather than an illustration of furniture.
13. As a professional vetting her, I want her credentials stated plainly and compactly,
    so that I can verify she is qualified without hunting through prose.
14. As a professional, I want to see מדריכה רשומה stated explicitly, so that I know her
    supervision is recognised.
15. As a visitor curious about ענווה תרבותית, I want her own definition of it, so that I
    do not read it as expertise about particular populations.
16. As a visitor from any background, I want cultural humility framed as a way of meeting
    any person, so that I do not assume the site is addressed only to someone else.
17. As a visitor, I want ענווה תרבותית to sit alongside her other work rather than
    dominate the page, so that I understand its actual place in what she does.
18. As a visitor ready to act, I want a clear way to make contact from the home page, so
    that deciding and acting are not separated by another navigation step.

### Visitors with access needs

19. As a keyboard user, I want a visible focus ring on every interactive element, so that
    I never lose my place on the page.
20. As a keyboard user, I want a skip link to the main content, so that I do not tab
    through the whole nav on every page.
21. As a screen-reader user, I want the page in correct heading order with one h1, so
    that I can navigate by structure.
22. As a screen-reader user, I want her portrait to carry real alt text and the
    decorative shapes to carry none, so that I hear what matters and not what does not.
23. As a screen-reader user, I want the page marked he and rtl, so that the text is
    announced in the right language and direction.
24. As a low-vision user, I want every piece of body text to clear 4.5:1 against its
    background, so that I can read the page without assistive zoom.
25. As a low-vision user, I want body copy set at a normal weight rather than light, so
    that Hebrew letterforms stay legible at small sizes.
26. As a user who zooms to 200%, I want the layout to reflow without horizontal
    scrolling, so that I can read a line without dragging.
27. As a user sensitive to motion, I want smooth scrolling and transitions suppressed
    when I have asked the system for reduced motion, so that the page does not make me
    unwell.
28. As a colour-blind user, I want link state signalled by more than colour, so that I
    can tell a hovered or focused link from an ordinary one.
29. As a user on a slow connection, I want fonts and images not to block the first paint,
    so that I can start reading before everything arrives.
30. As a mobile user, I want the nav to work when JavaScript has not loaded, so that a
    failed script does not cost me the whole site.

### The subject

31. As צהיינש, I want my name spelled צהיינש אדל־קרוט everywhere it appears, so that the
    site does not repeat the Tzahinash error of earlier drafts.
32. As צהיינש, I want the site to hold my full professional breadth, so that I am not
    reduced to lectures, or to one population, or to cultural humility alone.
33. As צהיינש, I want the site written in the first person singular, so that it reads as
    mine and not as an organization's.
34. As צהיינש, I want no mention of the joint venture's name, so that the separation the
    commissioner asked for actually holds.
35. As צהיינש, I want the page to feel warm, calm and professional at once, so that it
    matches how the work actually feels.
36. As צהיינש, I want to be able to replace my portrait later without a developer, so
    that a better photograph is not a build task.
37. As צהיינש, I want the track labels and the nav to come from one place, so that
    renaming a track later does not leave the old name somewhere I cannot see.

### Whoever builds the rest

38. As the next builder, I want every colour, size and radius expressed as a named token,
    so that I can build a new route without inventing values.
39. As the next builder, I want the token names to match the downloaded theme's own
    vocabulary rather than the superseded סקיצה, so that the design system stays
    traceable to its source file.
40. As the next builder, I want the five tracks defined as content rather than markup, so
    that adding a sixth or reordering them is a data edit.
41. As the next builder, I want one built route demonstrating every primitive, so that I
    have a worked example rather than a stylesheet.
42. As the next builder, I want the accessibility requirements met in the primitives
    themselves, so that I inherit them instead of re-deriving them per page.
43. As the commissioner, I want the brand-name decision isolated to a single content
    field, so that reversing it stays a one-line edit.

### Her, reviewing this draft

44. As צהיינש, I want a visible line marking this as a draft for review, so that if I
    forward it, nobody mistakes it for the live site.
45. As צהיינש, I want the portrait frame to show me what's missing rather than a stand-in
    photo, so that I am not reacting to a photo I never approved.
46. As צהיינש, I want the contact section to show the channels I chose — WhatsApp, phone,
    email, form — with their details visibly empty, so that I am prompted for exactly
    what's missing rather than guessing.
47. As צהיינש, I want every track's one-line description flagged as compressed from my
    own words, so that I can correct the compression instead of auditing new copy.
48. As צהיינש, I want the full nav, including אודות and מאמרים as placeholders, so that I
    can judge the whole site's shape rather than a partial one.

## Implementation Decisions

### The theme is adopted, the supplied page is not

The downloaded stylesheet becomes the project's design system. The downloaded markup is
reference only; the home page is written from the copy deck in the build brief. Nothing
in the supplied `index.html` ships as-is.

### Token vocabulary stays as the theme defines it

Renaming the theme's tokens to match the סקיצה was considered and reversed. The סקיצה is
superseded as a palette — nothing will be read against it going forward — so renaming
would buy consistency with a document nobody consults, at the cost of drift from the
source file the values actually came from. `--sage`, `--terracotta`, `--bg`, `--ink`,
`--ink-2` and `--muted` are kept exactly as declared in the downloaded stylesheet.

### Palette values corrected for AA

Measured against the theme's own ground (`--bg`), two foreground values miss 4.5:1. Each
gets one corrected value, used everywhere that token is used — no split between a
decorative and a text variant, so there is one value to apply and nothing to misjudge.

| Token | Theme value | Measured | Corrected value | New ratio |
|---|---|---|---|---|
| `--muted` | `#7A7266` on `--bg` | 4.41:1 | `#6E6659` | 5.26:1 |
| `--terracotta` | `#A9613F` on `--bg` | 4.36:1 | `#9B5636` | 5.16:1 |
| `--sage` | `#3F5A48` on `--bg` | 7.05:1 | unchanged | — |
| white on sage button | — | 7.59:1 | unchanged | — |
| footer muted | `#BCB6A9` on `#2A2A26` | 7.14:1 | unchanged | — |

`--terracotta` is the link hover colour and therefore carries state; the existing
underline on hover stays, so state is never signalled by colour alone.

### Body weight varies by size, not globally

The theme sets all body copy at weight 300. Weight 400 replaces it for card and
track-row text at 15.5px, where thin Hebrew letterforms cost legibility. The hero lede
keeps weight 300 at 18.5px, where the size carries the weight without a legibility cost
and the lightness is part of the calm the brief asks for. Weight is decided per context,
not set once for the whole page.

### The one artistic gesture

Brief §08 calls for artistic treatment to enter once, deliberately, not throughout. The
gesture is typographic: her positioning line (brief §07, HOME · HERO) is set large in
Frank Ruhl Libre as its own full-width section between the hero and the credentials
strip, rather than folded into the hero as sub-text. It needs no illustration asset and
puts her own sentence, not decoration, at the centre of the page. The arched portrait
frame is kept, but as structure, not as the artistic moment.

### Light theme only, structured for a later dark one

The site ships light-only. Dark mode doubles the surface that has to be contrast-checked,
and this spec ships without automated contrast checking. Tokens are declared in a single
block so that a `prefers-color-scheme` override plus a `data-theme` escape hatch can be
added in one place later, following the pattern the build brief document already uses.

### Accessibility lands in the primitives

Per [ADR 0003](../adr/0003-accessibility-to-wcag-aa.md), and absent from both the theme
and the סקיצה today:

- a visible `:focus-visible` ring on every interactive element, built into the shared
  styles rather than per component
- a skip link to main content as the first focusable element
- a `prefers-reduced-motion` guard over smooth scrolling and any transition
- physical offsets in the decorative hero shapes converted to logical properties, so RTL
  is expressed by the document rather than by hand-mirrored coordinates
- one `h1` per page and no skipped heading levels
- real alt text on the portrait; decorative shapes hidden from assistive technology

### Home page structure

A visible draft bar — "טיוטה לעיון, ספטמבר 2026" — sits above the header, minimal and
quiet, so the page cannot be mistaken for live if she forwards it. Below it, one
identity-led page carrying the whole argument, in this order: header with the full nav,
hero with the empty portrait slot, the positioning-line section (the one artistic
gesture), credentials strip, the five מסלולים, a ענווה תרבותית section, and a contact
section, then footer.

The nav carries all seven items from the brief's sitemap — the five tracks plus אודות
and מאמרים — not only what this spec builds. אודות and מאמרים ship as minimal stub pages
(heading only; אודות adds one line noting the biography is pending her confirmation per
[ADR 0001](../adr/0001-omitting-the-joint-venture-name.md)) so the nav resolves in full
and she can judge the site's whole shape rather than a partial one.

The contact section anchors the header and hero CTAs and shows the four channels she
chose — WhatsApp, phone, email, form — each labelled with its value visibly empty rather
than invented. Nothing in it could be mistaken for a real number or address.

The five tracks render as a stacked row list — the pattern already in the סקיצה — not as
the theme's 2×2 card grid. Five is an odd count and a two-column grid strands the fifth;
the row list also gives each track room for the one-line scope that tells a visitor
whether the door is theirs.

Track order is fixed: טיפול, הדרכת הורים, הדרכה וייעוץ למטפלים, הרצאות והכשרות, ארגונים
ואקדמיה.

### Canonical labels come from content, not markup

The five track labels, their one-line descriptions and their routes live in a single
content collection. Nav, track rows and footer all read from it. This is what makes
[ADR 0002](../adr/0002-five-tracks-not-four.md)'s prohibition enforceable: bare הדרכה
cannot appear in one place and not another, because there is only one place. It also
sets the content-collection convention that Decap will later edit.

### Track row descriptions are compressed from her own words

Each track row's one-line description is compressed from her own audience, format and
scope fields in brief §06, inventing no new claims about her practice. Every compressed
line is flagged in the handback to her as a compression of her words, not new copy, so
her review is a correction of emphasis rather than an audit of marketing language written
in her voice.

### Copy corrections against the supplied page

- השירותים שלנו is removed. The site is written in the first person singular.
- The logo tagline drops bare הדרכה. Either it qualifies the term or it uses a different
  word.
- פסיכותרפיה אישית and ייעוץ מערכתי are not canonical labels and do not appear. The five
  track names are the only names used for the five tracks.
- ענווה תרבותית is stated in her own definition — a way of meeting any person — never as
  knowledge about particular populations, and never framed as מודעות בינתרבותית.

### Hero shows an honestly empty portrait slot

The theme's arched hero frame is kept as the portrait shape and the illustrated therapy
room is dropped. Warmth comes from photography, per the design brief. Her portrait has
not been supplied, so rather than filling the frame with a stock or illustrated stand-in,
it ships visibly empty — a sand-toned block with a subtle border and a small Hebrew
caption asking for the photo ("כאן תופיע תמונת הפורטרט שלך"). A stand-in photo risks
being read as a proposal she has to react to and then have removed; an honest gap reads
as a request instead. The image is a content field rather than a hard-coded asset, so she
can replace it herself once it is supplied.

### Five minimal track routes

Track links must not dead-end. Five routes are created carrying only the canonical title,
the audience line and the scope line from the build brief. They are explicitly stubs;
their real content is a separate spec each.

### Stack and delivery

Astro with static output, per the build brief. No client JavaScript beyond the nav
toggle, which degrades to a plain visible nav list when JavaScript is absent. Fonts are
self-hosted rather than loaded from a third-party CDN, so that first paint does not
depend on an external origin and visitors — people looking for a therapist — are not
exposed to one.

This build is verified locally: rendered in-browser and checked against the manual
checklist below, not published as a hosted artifact or shared link. It is not put in
front of her from a public URL in this pass — a page carrying her real name and
professional claims functions as the real site to anyone who finds it, and her
joint-venture page is still live ([ADR 0001](../adr/0001-omitting-the-joint-venture-name.md),
brief §10). When it is ready to send her, it goes out from a Netlify or Vercel preview
deploy under a `noindex` header, as a separate and deliberate step, not from this build.

## Testing Decisions

**No automated tests are written for this spec.** That was decided explicitly. It is
recorded here rather than left implicit, because it means the WCAG 2.0 AA commitment in
ADR 0003 rests entirely on the checklist below being run — there is nothing that fails a
build when a token drifts or a heading level is skipped.

There is no prior art to follow: the repository contains no test suite today.

### What a good test here would look like, when one is written

The seam is the built HTML, not the components. A test should assert what a visitor or a
screen reader can observe — that five tracks are present and named canonically, that no
nav label is bare הדרכה, that heading levels do not skip, that the portrait has alt text,
that every foreground/background pair clears its ratio. It should not assert which
component rendered a section, what a prop was called, or what class name a node carries.
Written that way, the tests survive a redesign; written against internals, they have to
be rewritten alongside the thing they were meant to protect.

### Manual checklist, run before this spec is considered done

1. Every text/background pair on the built page measured at ≥4.5:1, or ≥3:1 for text at
   or above 24px / 19px bold.
2. Tab through the whole page. A focus ring is visible at every stop, the skip link is
   the first stop, and focus order follows reading order.
3. With JavaScript disabled, the nav is present and every link works.
4. Heading outline read top to bottom: one h1, no skipped level.
5. Screen-reader pass over the hero and track list — portrait alt text is meaningful,
   decorative shapes are silent, track labels are unambiguous out of context.
6. Zoom to 200% and to 400%: no horizontal scrolling, no clipped text.
7. With reduced motion requested at OS level, no smooth scroll and no transitions.
8. Every canonical term checked against `CONTEXT.md`: no bare הדרכה, no השירותים שלנו,
   no מודעות בינתרבותית, no joint-venture name, name spelled צהיינש אדל־קרוט.
9. All five tracks present, correctly ordered, each link resolving to a real page.
10. Rendered at 375px, 768px and 1440px.

## Out of Scope

- **Real About and Articles content.** Both ship as minimal stub pages so the nav
  resolves (see Home page structure); their real content is separate work. About is
  additionally blocked on the brand-name confirmation in brief §04 and gated by
  [ADR 0001](../adr/0001-omitting-the-joint-venture-name.md); the isolated-field
  convention it needs is established by this spec, but the page's real content is not
  written.
- **Real track-page content.** Five stubs only. Each track gets its own spec.
- **A dedicated contact page or working form.** The home page's contact section shows the
  four channels with their values visibly empty. An actual form, and the phone number,
  public email and clinic-address values themselves, are all open items.
- **Decap CMS configuration**, including the Hebrew field labels that make it usable.
- **Accessibility statement page.** Required before launch; needs content from her.
- **Testimonials.** Needs the institutional-only boundary confirmed with her first.
- **Dark mode.**
- **Any English or Arabic version.** Hebrew only, RTL, decided.
- **Domain registration, hosting and deployment.**
- **Taking down her page on the existing joint site.** Required before launch, not a
  build task.

## Further Notes

**This spec was revised after a grilling session with the commissioner on 21 Sep 2026.**
Five decisions reversed or sharpened what the first draft assumed: token names stay as
the theme declares them rather than matching the superseded סקיצה; the AA colour fixes
are single corrected values, not split text/decorative variants; body weight varies by
context instead of one global 300→400 swap; the portrait slot ships honestly empty rather
than with a stand-in image; and the nav ships complete, with אודות and מאמרים as stubs,
rather than showing only what this build implements.

**The one blocker does not block this spec.** The brand-name question gates the About
page only. Design and the home page proceed around it.

**Her portrait is the critical missing asset.** The hero is designed for it and reads as
unfinished without it. She has photographs; only permission and delivery are outstanding.

**On her stated design reference.** Asked which sites she liked, she named the existing
joint venture's site. Inheriting its visual language would work against the separation
this project exists to create. The theme adopted here is independent of it. Worth asking
her what she likes *about* that site — the warmth, the clarity, the photography — rather
than treating the reference as a brief.

**Provenance of the contrast figures.** All ratios above were computed against the
theme's own declared token values, not estimated.

**Where this spec and the glossary disagree, the glossary wins.** `CONTEXT.md` at the
repository root is canonical.
