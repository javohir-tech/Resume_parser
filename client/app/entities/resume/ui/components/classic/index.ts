import type { ResumeTemplateBlokcs } from "~/entities/resume/models/template-contract";
import ClassicPage from "./ClassicPage.vue";
import ClassicHeader from "./ClassicHeader.vue";
import ClassicSummary from "./ClassicSummary.vue";
import ClassicSectionTitle from "./ClassicSectionTitle.vue";
import ClassicExperienceItem from "./ClassicExperienceItem.vue";
import ClassicEducationItem from "./ClassicEducationItem.vue";
import ClassicSkillsGroup from "./ClassicSkillsGroup.vue";

export const ClassicTemplate: ResumeTemplateBlokcs = {
  page: ClassicPage,
  header: ClassicHeader,
  summary: ClassicSummary,
  sectionTitle: ClassicSectionTitle,
  experienceItem: ClassicExperienceItem,
  educationItem: ClassicEducationItem,
  skillsGroup: ClassicSkillsGroup,
};
