import { api } from "~/shared/api";
import type { Education } from "~/entities/resume";

export const createEducationFetch = (resume_id: string) =>
  api<{ education_id: string }>(`/api/resume/education/create/${resume_id}`, {
    method: "POST",
  });

export const editEducationFetch = (
  education_id: string,
  education_info: Partial<Omit<Education, "id">>,
) =>
  api<null>(`/api/resume/education/edit/${education_id}`, {
    method: "PATCH",
    body: education_info,
  });

export const deleteEducationFetch = (education_id: string) =>
  api<{ message: string }>(`/api/resume/education/delete/${education_id}`, {
    method: "DELETE",
  });