import { defineConfig } from "astro/config";

// Static output, no client JS beyond the nav toggle. See
// docs/specs/0001-design-system-and-home-page.md, "Stack and delivery".
export default defineConfig({
  output: "static",
  site: "https://tzahaynesh.co.il",
  compressHTML: true,
});
