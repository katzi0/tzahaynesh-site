// Her emphasis in track content files is marked **…**.

// HTML for set:html: escapes everything, then turns **…** into <strong>,
// so a paragraph can't inject any other markup.
export const emphasize = (text: string) =>
  text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");

// Plain text, for places that can't carry markup (meta description).
export const plain = (text: string) => text.replace(/\*\*/g, "");
