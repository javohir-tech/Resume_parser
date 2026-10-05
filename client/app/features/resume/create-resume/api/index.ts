import { api } from "~/shared/api";

export const createResumeRequest = () =>
  api<{ success: boolean; resume_id: string }>("/api/resume/create", {
    method: "POST",
  });
