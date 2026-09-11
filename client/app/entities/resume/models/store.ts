import type { Resume } from "./types";

export type ResumeColor = { name: string; hex: string };

export const useResumeStore = defineStore("resume", () => {
  const personalInfo = reactive<Resume>({
    fullname: "",
    title: "",
    email: "",
    phone: "",
    location: "",
    website: "",
    github_link: "",
    linkedin_link: "",
    summary: "",
    skills: [],
    education: [],
    experience: [],
    languages: [],
  });

  const designInfo = reactive({
    heading_title_color: null as ResumeColor | null,
    entry_title_color: null as ResumeColor | null,
    text_color: null as ResumeColor | null,
    font: "Inter",
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

  const colorOptions: ResumeColor[] = [
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

  function handleChangeFont(font: string) {
    designInfo.font = font;
  }

  function handleChangeColor(color: ResumeColor | null) {
    designInfo.heading_title_color = color;
  }

  function handleChangeEntryTitleColor(color: ResumeColor | null) {
    designInfo.entry_title_color = color;
  }

  return {
    personalInfo,
    designInfo,
    fontOptions,
    colorOptions,
    handleChangeFont,
    handleChangeColor,
    handleChangeEntryTitleColor,
  };
});
