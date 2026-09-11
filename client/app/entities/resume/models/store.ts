import type {
  Resume,
  Templates,
  TemplateName,
  ResumeColor,
  DesignInfo,
} from "./types";
import { useStorage } from "@vueuse/core";
import { skipHydrate } from "pinia";

export const useResumeStore = defineStore("resume", () => {
  const storageOptions = { mergeDefaults: true, initOnMounted: true };

  const fontOptions = [
    "Inter",
    "Roboto",
    "Merriweather",
    "Playfair Display",
    "Lato",
    "Poppins",
    "Nunito",
  ];

  type FontOption = (typeof fontOptions)[number];

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

  const templates: TemplateName[] = ["classic", "modern"];

  const template = useStorage<TemplateName>(
    "resume-parser:template:v1",
    "classic",
    undefined,
    storageOptions,
  );

  const personalInfo = useStorage<Resume>(
    "resume-parser:personal-info:v1",
    {
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
    },
    undefined,
    storageOptions,
  );

  const designInfo = useStorage<DesignInfo>(
    "resume-parser:design-info:v1",
    {
      heading_title_color: null,
      entry_title_color: null,
      text_color: null,
      font: "Inter",
    },
    undefined,
    storageOptions,
  );

  function handleChangeFont(font: string) {
    designInfo.value.font = font;
  }

  function handleChangeColor(color: ResumeColor | null) {
    designInfo.value.heading_title_color = color;
  }

  function handleChangeEntryTitleColor(color: ResumeColor | null) {
    designInfo.value.entry_title_color = color;
  }

  function restartDesign() {
    designInfo.value.entry_title_color = null;
    designInfo.value.heading_title_color = null;
    designInfo.value.text_color = null;
    designInfo.value.font = "Inter";
  }

  return {
    template: skipHydrate(template),
    personalInfo: skipHydrate(personalInfo),
    designInfo: skipHydrate(designInfo),
    restartDesign,
    handleChangeFont,
    handleChangeColor,
    handleChangeEntryTitleColor,
  };
});
