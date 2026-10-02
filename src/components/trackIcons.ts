// The one list of track section icon names. The content schema validates
// against it and TrackIcon.astro draws each one, so a name can't exist in
// one place and not the other.
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
] as const;

export type TrackIconName = (typeof trackIcons)[number];
