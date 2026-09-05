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
    experience: [
      // {
      //   id: "kadkakw",
      //   company: "limsa",
      //   position: "front end",
      //   endDate: "nima",
      //   startDate: "saom",
      //   location: "tashkenn",
      //   description: "",
      // },
    ],
  });

  return { personalInfo };
});
