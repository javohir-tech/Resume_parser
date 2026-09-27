import type {
  Personal,
  Experience,
  Education,
  Languages,
  Skill,
} from "~/entities/resume";

export interface ParseResumeResponse extends Omit<Personal, "id"> {
  experience: Omit<Experience, "id">;
  education: Omit<Education, "id">;
  languages: Omit<Languages, "id">;
  skills: { title: string; skills: Omit<Skill, "id"> };
}

export interface ImportResumeResponse {
    success : boolean ;
    resume_id : string;
}
