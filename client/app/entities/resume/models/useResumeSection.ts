import { useResumeStore } from "./store";

export const useResumeSection = () => {
  const resumeStore = useResumeStore();

  function addExperience() {
    resumeStore.personalInfo.experience?.push({
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
    resumeStore.personalInfo.experience =
      resumeStore.personalInfo.experience?.filter((exp) => exp.id !== id);
  }

  function addEducation() {
    resumeStore.personalInfo.education?.push({
      id: crypto.randomUUID(),
      fieldOfStudy: "",
      institution: "",
      location: "",
      startDate: "",
      endDate: "",
    });
  }

  function removeEducation(id: string) {
    resumeStore.personalInfo.education =
      resumeStore.personalInfo.education?.filter((edc) => edc.id !== id);
  }

  return { addExperience, removeExperince , addEducation , removeEducation };
};
