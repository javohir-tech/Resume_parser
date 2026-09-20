import { api } from "~/shared/api";
import type { Languages } from "~/entities/resume";

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