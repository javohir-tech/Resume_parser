import { api } from "~/shared/api";

export const getSkillsRequest = (
  params: { search?: string } = {},
  signal: AbortSignal,
) =>
  api<{title : string}[]>("/api/skills_title/filter", {
    method: "GET",
    query: params,
    signal,
    timeout: 15000,
    retry: 0,
  });
