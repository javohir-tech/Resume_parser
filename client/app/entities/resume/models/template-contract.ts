import type { Component } from "vue";

export interface ResumeTemplateBlokcs {
  renderer?: Component;
  page: Component;
  header: Component;
  summary: Component;
  sectionTitle: Component;
  experienceItem: Component;
  educationItem: Component;
  skillsGroup: Component;
  languages : Component;
}
