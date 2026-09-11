import type { ResumeTemplateBlokcs } from "./template-contract";
import type { FontOption } from "./constants";

export interface Experience {
  id: string;
  position: string;
  company: string;
  location?: string;
  startDate: string;
  endDate?: string;
  description?: string;
}

export interface Education {
  id: string;
  degree: string;
  fieldOfStudy: string;
  institution: string;
  location?: string;
  startDate: string;
  endDate?: string;
}

export interface SkillGroup {
  id: string;
  title: string;
  skills: string[];
}

export interface Personal {
  fullname: string;
  title?: string;
  email?: string;
  phone?: string;
  location?: string;
  website?: string;
  github_link?: string;
  linkedin_link?: string;
  summary?: string;
}

export type LanguageDegree =
  | "Elementary proficiency"
  | "Limited working proficiency"
  | "Professional working proficiency"
  | "Full professional proficiency"
  | "Native or bilingual proficiency"
  | "";

export interface Languages {
  id: string;
  language: string;
  degree: LanguageDegree;
}

export interface Resume extends Personal {
  skills?: SkillGroup[];
  education?: Education[];
  experience?: Experience[];
  languages?: Languages[];
}
export type ResumeColor = { name: string; hex: string };

export interface DesignInfo {
  heading_title_color: null | ResumeColor;
  entry_title_color: null | ResumeColor;
  text_color: null | ResumeBlock;
  font: FontOption;
}

export type ResumeSection = "experience" | "education" | "skills" | "languages";

export type ResumeBlock =
  | { id: string; type: "header" }
  | { id: string; type: "summary" }
  | { id: string; type: "section-title"; section: ResumeSection }
  | { id: string; type: "experience-item"; item: Experience }
  | { id: string; type: "education-item"; item: Education }
  | { id: string; type: "skills-group"; item: SkillGroup }
  | { id: string; type: "languages-item"; item: Languages };

export interface Templates {
  classic: ResumeTemplateBlokcs;
  modern: ResumeTemplateBlokcs;
}

export type TemplateName = keyof Templates;
