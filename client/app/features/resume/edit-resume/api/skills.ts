import { api } from "~/shared/api";
import type { Skill, SkillGroup } from "~/entities/resume";

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
  api<{ skill_item_id: string }>(
    `/api/resume/skill_item/create/${skills_group_id}`,
    {
      method: "POST",
      body: skill_info,
    },
  );

export const deleteSkillItem = (skill_item_id: string) =>
  api<{ detail: string }>(`/api/resume/skill_item/delete/${skill_item_id}`, {
    method: "DELETE",
  });
