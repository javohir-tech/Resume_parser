import { api } from "~/shared/api";
import type { Experience } from "~/entities/resume";

export const createExperienceFetch = (resume_id: string) =>
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

export const deleteExperienceFetch = (experience_id: string) =>
  api<void>(`/api/resume/experience/delete/${experience_id}`, {
    method: "DELETE",
  });