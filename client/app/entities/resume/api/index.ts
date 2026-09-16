import type {
  Resume,
  Personal
} from "../models/types";
import { api } from "~/shared/api";

export const getResume = (resume_id: string) =>
  api<Resume>(`/api/resume/${resume_id}`, { method: "GET" });

export const getMyResumes = () =>
  api<Pick<Personal, "id" | "fullname" | "title">[]>("/api/resume/my/resumes", {
    method: "GET",
  });
