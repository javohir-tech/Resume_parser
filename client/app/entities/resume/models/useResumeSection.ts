import { useResumeStore } from "./store";

export const useResumeSection = () => {
  const resumeStore = useResumeStore();

  function addExperience() {
    resumeStore.resume.experience?.push({
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
    resumeStore.resume.experience =
      resumeStore.resume.experience?.filter((exp) => exp.id !== id);
  }

  function addEducation() {
    resumeStore.resume.education?.push({
      id: crypto.randomUUID(),
      fieldOfStudy: "",
      institution: "",
      degree: "",
      location: "",
      startDate: "",
      endDate: "",
    });
  }

  function removeEducation(id: string) {
    resumeStore.resume.education =
      resumeStore.resume.education?.filter((edc) => edc.id !== id);
  }

  function addSkillsGroup() {
    resumeStore.resume.skills?.push({
      id: crypto.randomUUID(),
      title: "",
      skills: [],
    });
  }

  function removeSkillsGroup(id: string) {
    resumeStore.resume.skills = resumeStore.resume.skills?.filter(
      (sk) => sk.id !== id,
    );
  }

  function addSkill(id: string, skill: string) {
    const skillGroup = resumeStore.resume.skills?.find(
      (sk) => sk.id === id,
    );
    if (skillGroup) {
      skillGroup.skills.push({ id: crypto.randomUUID(), skill });
    }
  }

  function removeSkill(id: string, skillId: string) {
    const skillGroup = resumeStore.resume.skills?.find(
      (sk) => sk.id === id,
    );

    if (skillGroup) {
      skillGroup.skills = skillGroup.skills.filter((skill) => skill.id !== skillId);
    }
  }

  function addLanguage() {
    resumeStore.resume.languages?.push({
      id: crypto.randomUUID(),
      language: "",
      degree: "",
    });
  }

  function removeLanguage(id: string) {
    resumeStore.resume.languages =
      resumeStore.resume.languages?.filter((l) => l.id !== id);
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
    addLanguage,
    removeLanguage
  };
};
