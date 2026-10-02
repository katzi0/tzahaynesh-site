// The one list of icon names for track sections and library items. The
// content schemas validate against it and TrackIcon.astro draws each one,
// so a name can't exist in one place and not the other.
export const trackIcons = [
  "people",
  "integrate",
  "dialogue",
  "compass",
  "context",
  "family",
  "roots",
  "network",
  "book",
  "seedling",
  "calendar",
  "clock",
  "article",
  "research",
  "video",
  "podcast",
  "lecture",
  "bookmark",
] as const;

export type TrackIconName = (typeof trackIcons)[number];
