import { api } from "~/shared/api";

export const deleteResumeRequest = (resume_id: string) =>
  api<{success : boolean, message: string }>(`/api/resume/delete/${resume_id}`, {
    method: "DELETE",
  });