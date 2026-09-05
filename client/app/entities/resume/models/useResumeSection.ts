import { useResumeStore } from "./store";

export const useResumeSection = () => {
  const resume = useResumeStore();

  function addExperience() {
    resume.personalInfo.experience?.push({
      id: crypto.randomUUID(),
      position: "",
      company: "",
      startDate: "",
      endDate: "",
      description: "",
      location: "",
    });
  }

  return { addExperience };
};
