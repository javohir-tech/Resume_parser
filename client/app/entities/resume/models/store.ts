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
    title_color : "" , 
    name_font : "" , 
  })

  return { personalInfo };
});
