import { useResumeStore } from "./store";

export const useCreateSection = () => {
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
