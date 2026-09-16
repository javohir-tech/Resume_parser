import type {
  Resume,
  Personal,
  Experience,
  Education,
  Languages,
  SkillGroup,
} from "../models/types";
import { api } from "~/shared/api";

///////////////////////////////////////////////
// Resume
///////////////////////////////////////////////
export const createResume = () =>
  api<{ resume_id: string }>("/api/resume/create", { method: "POST" });

export const getResume = (resume_id: string) =>
  api<Resume>(`/api/resume/${resume_id}`, { method: "GET" });

export const editResume = (
  resume_id: string,
  personal_info: Partial<Omit<Personal , "id">>,
) =>
  api<null>(`/api/resume/edit/${resume_id}`, {
    method: "PATCH",
    body: personal_info,
  });

export const deleteResume = (resume_id: string) =>
  api<{ message: string }>(`/api/resume/delete/${resume_id}`, {
    method: "DELETE",
  });

///////////////////////////////////////////////
// Experience
///////////////////////////////////////////////
export const createExperience = (resume_id: string) =>
  api<{ experience_id: string }>(`/api/resume/experience/create/${resume_id}`, {
    method: "POST",
  });

export const editExperience = (
  experience_id: string,
  experience_info: Partial<Omit<Experience, "id">>,
) =>
  api<null>(`/api/resume/experience/edit/${experience_id}`, {
    method: "PATCH",
    body: experience_info,
  });

export const deleteExperience = (experience_id: string) =>
  api<void>(`/api/resume/experience/delete/${experience_id}`, {
    method: "DELETE",
  });

///////////////////////////////////////////////
// Education
///////////////////////////////////////////////
export const createEducation = (resume_id: string) =>
  api<{ education_id: string }>(`/api/resume/education/create/${resume_id}`, {
    method: "POST",
  });

export const editEducation = (
  education_id: string,
  education_info: Partial<Omit<Education, "id">>,
) =>
  api<null>(`/api/resume/education/edit/${education_id}`, {
    method: "PATCH",
    body: education_info,
  });

export const deleteEducation = (education_id: string) =>
  api<{ message: string }>(`/api/resume/education/delete/${education_id}`, {
    method: "DELETE",
  });

///////////////////////////////////////////////
// Languages
///////////////////////////////////////////////
export const createLanguage = (resume_id: string) =>
  api<{ language_id: string }>(`/api/resume/language/create/${resume_id}`, {
    method: "POST",
  });

export const editLanguage = (
  language_id: string,
  language_info: Partial<Omit<Languages, "id">>,
) =>
  api<null>(`/api/resume/language/edit/${language_id}`, {
    method: "PATCH",
    body: language_info,
  });

export const deleteLanguage = (language_id: string) =>
  api<{ detail: string }>(`/api/resume/language/delete/${language_id}`, {
    method: "DELETE",
  });

///////////////////////////////////////////////
// Skill groups
///////////////////////////////////////////////
export const createSkillGroup = (resume_id: string) =>
  api<{ skills_id: string }>(`/api/resume/skills/create/${resume_id}`, {
    method: "POST",
  });

export const editSkillGroup = (
  skills_id: string,
  skills_info: Pick<SkillGroup, "title">,
) =>
  api<null>(`/api/resume/skills/edit/${skills_id}`, {
    method: "PATCH",
    body: skills_info,
  });

export const deleteSkillGroup = (skills_id: string) =>
  api<{ detail: string }>(`/api/resume/skills/delete/${skills_id}`, {
    method: "DELETE",
  });

///////////////////////////////////////////////
// Skill items
///////////////////////////////////////////////
export const createSkillItem = (
  skills_group_id: string,
  skill_info: { skill: string },
) =>
  api<{ skill_item_id: string }>(`/api/resume/skill_item/create/${skills_group_id}`, {
    method: "POST",
    body: skill_info,
  });

export const deleteSkillItem = (skill_item_id: string) =>
  api<{ detail: string }>(`/api/resume/skill_item/delete/${skill_item_id}`, {
    method: "DELETE",
  });
