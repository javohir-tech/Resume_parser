import { api } from "~/shared/api";
import type { DesignInfo } from "~/entities/resume";

export const editDesignRequest = (resume_id: string, payload: Partial<DesignInfo>) =>
  api(`/api/resume/edit/${resume_id}/design`, {
    method: "PATCH",
    body: {
      ...payload,
      ...(payload.heading_title_color !== undefined
        ? { heading_title_color: payload.heading_title_color?.hex ?? null }
        : {}),
      ...(payload.entry_title_color !== undefined
        ? { entry_title_color: payload.entry_title_color?.hex ?? null }
        : {}),
    },
  });
