import { api } from "~/shared/api";

export const downloadResumeRequest = (resume_id: string, html: string) =>
  api<Blob>(`/api/resume/${resume_id}/download`, {
    method: "POST",
    body: { html },
    responseType: "blob",
  });


