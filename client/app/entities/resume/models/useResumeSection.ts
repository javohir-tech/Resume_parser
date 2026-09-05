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

  function removeExperince(id: string) {
    resume.personalInfo.experience = resume.personalInfo.experience?.filter(
      (exp) => exp.id !== id,
    );
  }

  return { addExperience , removeExperince };
};
