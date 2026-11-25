import { api } from "~/shared/api";
import type { Experience } from "~/entities/resume";

export const createExperienceRequest = (resume_id: string) =>
  api<{ experience_id: string }>(`/api/resume/experience/${resume_id}`, {
    method: "POST",
  });

export const editExperienceRequest = (
  experience_id: string,
  experience_info: Partial<Omit<Experience, "id">>,
) =>
  api<null>(`/api/resume/experience/${experience_id}`, {
    method: "PATCH",
    body: experience_info,
  });

export const deleteExperienceRequest = (experience_id: string) =>
  api<void>(`/api/resume/experience/${experience_id}`, {
    method: "DELETE",
  });