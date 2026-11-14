import { api } from "~/shared/api";
import { type ResponseGetJobTitles } from "../models/types";

export const getJobTitles = (
  params: { search?: string } = {},
  signal?: AbortSignal,
) =>
  api<ResponseGetJobTitles[]>("/api/job_titles/filter", {
    method: "GET",
    query: params,
    signal,
    timeout: 15000,
    retry: 0,
  });
