import type {
  Resume,
  Templates,
  TemplateName,
  ResumeColor,
  DesignInfo,
  Personal
} from "./types";

export const useResumeStore = defineStore("resume", () => {

  const template = ref<TemplateName>("classic");

  const resume = ref<Resume>({
    id : "",
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

  function restartInfo(){
    resume.value.id  = ""  , 
    resume.value.fullname =  "",
    resume.value.title =  "",
    resume.value.email =  "",
    resume.value.phone =  "",
    resume.value.location =  "",
    resume.value.website =  "",
    resume.value.github_link =  "",
    resume.value.linkedin_link =  "",
    resume.value.summary =  "",
    resume.value.skills =  [],
    resume.value.education =  [],
    resume.value.experience =  [],
    resume.value.languages =  []
  }

  function restartDesign() {
    designInfo.value.entry_title_color = null;
    designInfo.value.heading_title_color = null;
    designInfo.value.text_color = null;
    designInfo.value.font = "Inter";
  }

  return {
    template,
    resume,
    designInfo,
    restartInfo,
    restartDesign,
    handleChangeFont,
    handleChangeColor,
    handleChangeEntryTitleColor,
  };
});
