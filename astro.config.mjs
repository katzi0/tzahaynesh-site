import { defineConfig } from "astro/config";

// Static output, no client JS beyond the nav toggle. See
// docs/specs/0001-design-system-and-home-page.md, "Stack and delivery".
//
// site/base target the GitHub Pages review deploy (a project site serves
// under /<repo>/, not the domain root — every internal href in the
// components reads import.meta.env.BASE_URL for this reason). This is a
// temporary review URL, not tzahaynesh.co.il — swap both back when the real
// domain is registered and this moves to its permanent host.
export default defineConfig({
  output: "static",
  site: "https://katzi0.github.io",
  base: "/tzahaynesh-site/",
  compressHTML: true,
});
