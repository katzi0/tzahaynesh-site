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
  // Material people can use themselves, such as a regulation exercise.
  exercise: { label: "תרגיל", plural: "תרגילים וכלים", icon: "breath", action: "לתרגול" },
  song: { label: "שיר", plural: "שירים", icon: "music", action: "להאזנה" },
} as const satisfies Record<
  string,
  { label: string; plural: string; icon: TrackIconName; action: string }
>;

export type LibraryType = keyof typeof libraryTypes;

export const libraryTypeKeys = Object.keys(libraryTypes) as [LibraryType, ...LibraryType[]];

// Topics cut across types: a podcast and an exercise can both be about
// parenting. Optional per item; the library offers a topic filter only for
// topics that have items.
export const libraryTopics = {
  parenting: "הורות",
  culture: "תרבות וזהות",
  regulation: "ויסות ורגש",
  practice: "עבודה מקצועית",
} as const;

export type LibraryTopic = keyof typeof libraryTopics;

export const libraryTopicKeys = Object.keys(libraryTopics) as [LibraryTopic, ...LibraryTopic[]];
