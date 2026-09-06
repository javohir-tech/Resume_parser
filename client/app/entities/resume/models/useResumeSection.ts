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
      degree : "",
      location: "",
      startDate: "",
      endDate: "",
    });
  }

  function removeEducation(id: string) {
    resumeStore.personalInfo.education =
      resumeStore.personalInfo.education?.filter((edc) => edc.id !== id);
  }

  function addSkillsGroup() {
    resumeStore.personalInfo.skills?.push({
      id: crypto.randomUUID(),
      title: "",
      skills: [],
    });
  }

  function removeSkillsGroup(id: string) {
    resumeStore.personalInfo.skills = resumeStore.personalInfo.skills?.filter(
      (sk) => sk.id !== id,
    );
  }

  function addSkill(id: string, skill: string) {
    const skillGroup = resumeStore.personalInfo.skills?.find(
      (sk) => sk.id === id,
    );
    if (skillGroup) {
      skillGroup.skills.push(skill);
    }
  }

  function removeSkill(id: string, index: number) {
    const skillGroup = resumeStore.personalInfo.skills?.find(
      (sk) => sk.id === id,
    );

    if (skillGroup && index !== -1) {
      skillGroup.skills.splice(index, 1);
    }
  }

  return {
    addExperience,
    removeExperince,
    addEducation,
    removeEducation,
    addSkillsGroup,
    removeSkillsGroup,
    addSkill,
    removeSkill,
  };
};
