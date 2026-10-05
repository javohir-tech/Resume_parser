import { api } from "~/shared/api";
import type { Languages } from "~/entities/resume";

export const createLanguageRequest = (resume_id: string) =>
  api<{ language_id: string }>(`/api/resume/language/create/${resume_id}`, {
    method: "POST", 
  });

export const editLanguageRequest = (
  language_id: string,
  language_info: Partial<Omit<Languages, "id">>,
) =>
  api<null>(`/api/resume/language/edit/${language_id}`, {
    method: "PATCH",
    body: language_info,
  });

export const deleteLanguageRequest = (language_id: string) =>
  api<{ success : boolean ,  detail: string }>(`/api/resume/language/delete/${language_id}`, {
    method: "DELETE",
  });