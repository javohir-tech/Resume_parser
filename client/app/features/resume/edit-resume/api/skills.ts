import { api } from "~/shared/api";
import type {  SkillGroup } from "~/entities/resume";

///////////////////////////////////////////////
// Skill groups
///////////////////////////////////////////////
export const createSkillGroupRequest = (resume_id: string) =>
  api<{ skills_id: string }>(`/api/resume/skills/${resume_id}`, {
    method: "POST",
  });

export const editSkillGroupRequest = (
  skills_group_id: string,
  skills_info: Partial<Omit<SkillGroup , "id" | "skills">>,
) =>
  api<null>(`/api/resume/skills/${skills_group_id}`, {
    method: "PATCH",
    body: skills_info,
  });

export const deleteSkillGroupRequest = (skills_id: string) =>
  api<{ detail: string }>(`/api/resume/skills/${skills_id}`, {
    method: "DELETE",
  });

///////////////////////////////////////////////
// Skill items
///////////////////////////////////////////////
export const createSkillItemRequest = (
  skills_group_id: string,
  skill_info: { skill: string },
) =>
  api<{ skill_item_id: string }>(
    `/api/resume/skills_item/${skills_group_id}`,
    {
      method: "POST",
      body: skill_info,
    },
  );

export const deleteSkillItemRequest = (skill_item_id: string) =>
  api<{ detail: string }>(`/api/resume/skills_item/${skill_item_id}`, {
    method: "DELETE",
  });
