import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

// The five מסלולים, as one collection. Nav, the home-page track list, the
// track stub pages, and the footer all read from this — nothing hard-codes
// a track name or route a second time. This is what makes ADR 0002's ban on
// bare הדרכה enforceable: there is exactly one place a label could go wrong.
// See docs/specs/0001-design-system-and-home-page.md, "Canonical labels come
// from content, not markup".
const tracks = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/tracks" }),
  schema: z.object({
    // Fixed display and nav order — 1 through 5, per the spec.
    order: z.number().int().min(1).max(5),
    // Canonical Hebrew label. Must match CONTEXT.md exactly.
    title: z.string(),
    // Route segment under /tracks/.
    slug: z.string(),
    // Full audience line, verbatim from brief §06. Used on the track stub
    // page, not compressed.
    audience: z.string(),
    // One-line description for the home-page track row, compressed from her
    // own §06 audience/format/scope fields. Flag every one of these as a
    // compression of her words when handing the build back to her — see
    // "Track row descriptions are compressed from her own words" in the spec.
    summary: z.string(),
    // Format line from brief §06, for the stub page.
    format: z.string(),
    // Scope line from brief §06, for the stub page.
    scope: z.string(),
  }),
});

export const collections = { tracks };
