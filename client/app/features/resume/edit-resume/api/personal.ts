import { api } from "~/shared/api";
import type { Personal } from "~/entities/resume";

export const editResumeFetch = (
  resume_id: string,
  personal_info: Partial<Omit<Personal, "id">>,
) =>
  api<null>(`/api/resume/edit/${resume_id}`, {
    method: "PATCH",
    body: personal_info,
  });
