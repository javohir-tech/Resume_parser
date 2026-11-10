export const fonts = [
  "Inter",
  "Roboto",
  "Merriweather",
  "Playfair Display",
  "Lato",
  "Poppins",
  "Nunito",
] as const;

export type AppFont = typeof fonts[number]
