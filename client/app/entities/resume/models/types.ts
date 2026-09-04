import { string } from "valibot";

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
  summary?: string;
}

export interface Resume extends Personal {
  skills?: SkillGroup[];
  education?: Education[];
  experience?: Experience[];
}

export type  ResumeSection = "experience" | "education" | "skills"

export type ResumeBlock  = 
  | {id : string ; type : "header"} 
  | {id : string ; type : "summary"}
  | {id : string ; type : "section-title" ; section : ResumeSection}
  | {id : string ; type : "experience-item" ; item : Experience}
  | {id : string ; type : "education-item";  item : Education}
  | {id : string ; type : "skills-group" ; item : SkillGroup}
