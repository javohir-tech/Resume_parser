import type { ResumeTemplateBlokcs } from "../../../models/template-contract";
import ProfessionalPage from "./ProfessionalPage.vue";
import ProfessionalHeader from "./ProfessionalHeader.vue";
import ProfessionalSummary from "./ProfessionalSummary.vue";
import ProfessionalSectionTitle from "./ProfessionalSectionTitle.vue";
import ProfessionalExperienceItem from "./ProfessionalExperienceItem.vue";
import ProfessionalEducationItem from "./ProfessionalEducationItem.vue";
import ProfessionalSkillsGroup from "./ProfessionalSkillsGroup.vue";
import ProfessionalLanguages from "./ProfessionalLanguages.vue";

export const ProfessionalTemplate: ResumeTemplateBlokcs = {
  page: ProfessionalPage,
  header: ProfessionalHeader,
  summary: ProfessionalSummary,
  sectionTitle: ProfessionalSectionTitle,
  experienceItem: ProfessionalExperienceItem,
  educationItem: ProfessionalEducationItem,
  skillsGroup: ProfessionalSkillsGroup,
  languages: ProfessionalLanguages,
};
