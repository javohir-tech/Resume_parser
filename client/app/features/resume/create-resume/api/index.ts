import { api } from "~/shared/api";

export const createResumeFetch = () =>
  api<{ success: boolean; resume_id: string }>("/api/resume/create", {
    method: "POST",
  });
