import type { ResumeTemplateBlokcs } from "../../../models/template-contract";
import MinimalPage from "./MinimalPage.vue";
import MinimalHeader from "./MinimalHeader.vue";
import MinimalSummary from "./MinimalSummary.vue";
import MinimalSectionTitle from "./MinimalSectionTitle.vue";
import MinimalExperienceItem from "./MinimalExperienceItem.vue";
import MinimalEducationItem from "./MinimalEducationItem.vue";
import MinimalSkillsGroup from "./MinimalSkillsGroup.vue";
import MinimalLanguages from "./MinimalLanguages.vue";

export const MinimalTemplate: ResumeTemplateBlokcs = {
  page: MinimalPage,
  header: MinimalHeader,
  summary: MinimalSummary,
  sectionTitle: MinimalSectionTitle,
  experienceItem: MinimalExperienceItem,
  educationItem: MinimalEducationItem,
  skillsGroup: MinimalSkillsGroup,
  languages: MinimalLanguages,
};
