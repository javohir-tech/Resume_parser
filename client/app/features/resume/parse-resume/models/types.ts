import type {
  Personal,
  Experience,
  Education,
  Languages,
  Skill,
} from "~/entities/resume";

type ParseFields<T> = {
  [K in keyof T as Exclude<K, "id">]-?: T[K] | null;
};

export interface ParsedResume extends Omit<Personal, "id"> {
  experience: ParseFields<Experience>[];
  education: ParseFields<Education>[];
  languages: ParseFields<Languages>[];
  skills: {
    title: string | null;
    skills: ParseFields<Skill>[];
  }[];
}

export interface ParseResumeResponse {
  resume: ParsedResume;
}

export interface ImportResumeResponse {
  success: boolean;
  resume_id: string;
}
