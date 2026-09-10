import type { Resume } from "./types";

export const useResumeStore = defineStore("resume", () => {
  const personalInfo = reactive<Resume>({
    fullname: "",
    title: "",
    email: "",
    phone: "",
    location: "",
    website: "",
    summary: "",
    skills: [],
    education: [],
    experience: [],
    languages: [],
  });

  const designInfo = reactive({
    title_color: "",
    text_color: "",
    accent_color: "",
    name_font: "Inter",
    heading_font: "Inter",
  });

  const fontOptions = [
    "Inter",
    "Roboto",
    "Merriweather",
    "Playfair Display",
    "Lato",
    "Poppins",
    "Nunito",
  ];

 const colorOptions = [
  { name: "red", hex: "#ef4444" },
  { name: "orange", hex: "#f97316" },
  { name: "amber", hex: "#f59e0b" },
  { name: "yellow", hex: "#eab308" },
  { name: "lime", hex: "#84cc16" },
  { name: "green", hex: "#22c55e" },
  { name: "emerald", hex: "#10b981" },
  { name: "teal", hex: "#14b8a6" },
  { name: "cyan", hex: "#06b6d4" },
  { name: "sky", hex: "#0ea5e9" },
  { name: "blue", hex: "#3b82f6" },
  { name: "indigo", hex: "#6366f1" },
  { name: "violet", hex: "#8b5cf6" },
  { name: "purple", hex: "#a855f7" },
  { name: "fuchsia", hex: "#d946ef" },
  { name: "pink", hex: "#ec4899" },
  { name: "rose", hex: "#f43f5e" },
];

  function handleChangeFont(font : string){
    designInfo.heading_font = font
  }

  function handleChangeColor(hex : string){
    designInfo.title_color = hex
  }

  return { personalInfo, designInfo, fontOptions, colorOptions , handleChangeFont , handleChangeColor };
});
