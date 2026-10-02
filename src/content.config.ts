import { defineCollection, z } from "astro:content";
import { file, glob } from "astro/loaders";
import { trackIcons } from "./components/trackIcons";
import { libraryTypeKeys } from "./components/libraryTypes";

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
    // Her opening line, set under the title.
    tagline: z.string().optional(),
    // Her opening paragraphs, before the first section heading.
    // Paragraphs anywhere on a track page may mark her emphasis as **…**.
    intro: z.array(z.string()).min(1).optional(),
    // Her full text for the track, once she supplies it. When present the
    // page renders these sections instead of the audience/format/scope stub.
    // Icons come from a fixed set in TrackIcon.astro so every track shares
    // one stroke, size and palette.
    sections: z
      .array(
        z.object({
          icon: z.enum(trackIcons),
          heading: z.string(),
          paragraphs: z.array(z.string()).min(1),
        }),
      )
      .optional(),
    // Closing statement set apart after the sections.
    closing: z.string().optional(),
    // Show audience/format/scope as a closing panel after the sections. Off
    // for tracks whose full text already covers its audience in a section.
    showDetails: z.boolean().default(false),
  }),
});

// The professional library (ספרייה מקצועית): material she collects and
// curates, her own and others'. One YAML list so she can add an item
// without touching code. Items link out; nothing of anyone else's is
// hosted here.
const library = defineCollection({
  loader: file("src/content/library.yaml"),
  schema: z.object({
    type: z.enum(libraryTypeKeys),
    title: z.string(),
    // Author, speaker or source, as it should be credited.
    creator: z.string(),
    year: z.number().int().optional(),
    // Her note on why it's here. This is what makes it curation rather
    // than a list of links.
    note: z.string(),
    url: z.string().url().optional(),
    // Her own work, whatever its type.
    mine: z.boolean().default(false),
  }),
});

export const collections = { tracks, library };
