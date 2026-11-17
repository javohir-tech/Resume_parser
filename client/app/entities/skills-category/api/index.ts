import { api } from "~/shared/api";

export const getSkillCategoriesRequest = (
  params: { search?: string } = {},
  signal?: AbortSignal,
) =>
  api<{ title: string }[]>("/api/skills_category/filter", {
    method: "GET",
    query: params,
    signal,
    timeout: 15000,
    retry: 0,
  });
