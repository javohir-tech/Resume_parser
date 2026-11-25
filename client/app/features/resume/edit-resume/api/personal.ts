import { api } from "~/shared/api";
import type { Personal } from "~/entities/resume";

export const editResumeRequest = (
  resume_id: string,
  personal_info: Partial<Omit<Personal, "id">>,
) =>
  api<null>(`/api/resume/${resume_id}`, {
    method: "PATCH",
    body: personal_info,
  });
