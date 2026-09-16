import type {
  Resume,
  Templates,
  TemplateName,
  ResumeColor,
  DesignInfo,
} from "./types";

export const useResumeStore = defineStore("resume", () => {

  const template = ref<TemplateName>("classic");

  const personalInfo = ref<Resume>({
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

  const designInfo = ref<DesignInfo>({
    heading_title_color: null,
    entry_title_color: null,
    text_color: null,
    font: "Inter",
  });

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
    template,
    personalInfo,
    designInfo,
    restartDesign,
    handleChangeFont,
    handleChangeColor,
    handleChangeEntryTitleColor,
  };
});
