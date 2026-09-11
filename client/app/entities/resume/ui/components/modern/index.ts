import type { ResumeTemplateBlokcs } from "~/entities/resume/models/template-contract";
import ModernPage from "./ModernPage.vue";
import ModernHeader from "./ModernHeader.vue";
import ModernSummary from "./ModernSummary.vue";
import ModernSectionTitle from "./ModernSectionTitle.vue";
import ModernExperienceItem from "./ModernExperienceItem.vue";
import ModernEducationItem from "./ModernEducationItem.vue";
import ModernSkillsGroup from "./ModernSkillsGroup.vue";
import ModernLanguages from "./ModernLanguages.vue";

export const ModernTemplate: ResumeTemplateBlokcs = {
  page: ModernPage,
  header: ModernHeader,
  summary: ModernSummary,
  sectionTitle: ModernSectionTitle,
  experienceItem: ModernExperienceItem,
  educationItem: ModernEducationItem,
  skillsGroup: ModernSkillsGroup,
  languages: ModernLanguages,
};

