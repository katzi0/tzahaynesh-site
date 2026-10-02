import type { TrackIconName } from "./trackIcons";

// Content types in the professional library (ספרייה מקצועית). Each type has
// one Hebrew label, one icon and one link verb, so every card of a type
// looks and reads the same. "Mine" is not a type: one of her own pieces can
// be an article, a lecture or a podcast, so ownership is a separate flag.
export const libraryTypes = {
  article: { label: "מאמר", plural: "מאמרים", icon: "article", action: "לקריאה" },
  research: { label: "מחקר", plural: "מחקרים", icon: "research", action: "לקריאה" },
  chapter: { label: "פרק מספר", plural: "פרקים", icon: "book", action: "לפרטים" },
  video: { label: "סרטון", plural: "סרטונים", icon: "video", action: "לצפייה" },
  podcast: { label: "פודקאסט", plural: "פודקאסטים", icon: "podcast", action: "להאזנה" },
  lecture: { label: "הרצאה", plural: "הרצאות", icon: "lecture", action: "לצפייה" },
  recommendation: { label: "המלצת קריאה", plural: "המלצות קריאה", icon: "bookmark", action: "לפרטים" },
} as const satisfies Record<
  string,
  { label: string; plural: string; icon: TrackIconName; action: string }
>;

export type LibraryType = keyof typeof libraryTypes;

export const libraryTypeKeys = Object.keys(libraryTypes) as [LibraryType, ...LibraryType[]];
