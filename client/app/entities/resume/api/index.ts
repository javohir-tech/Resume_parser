import type { Resume, Personal , DesignInfo } from "../models/types";
import { api } from "~/shared/api";
import { colorOptions } from "../models/constants";

export const getResumeFetch = (resume_id: string) =>
  api<Resume>(`/api/resume/${resume_id}`, { method: "GET" });

export const getMyResumes = () =>
  api<Pick<Personal, "id" | "fullname" | "title">[]>("/api/resume/my/resumes", {
    method: "GET",
  });

type DesignResponse = Omit<DesignInfo, "heading_title_color" | "entry_title_color"> & {
  heading_title_color: string | null;
  entry_title_color: string | null;
};

function restoreColor(hex: string | null): DesignInfo["heading_title_color"] {
  if (!hex) return null;
  const color = colorOptions.find((option) => option.hex.toLowerCase() === hex.toLowerCase());
  return color ? { ...color } : { name: hex, hex };
}

export const getResumeDesignRequest = async (resume_id: string): Promise<DesignInfo> => {
  const design = await api<DesignResponse>(`/api/resume/${resume_id}/design`);
  return {
    template: design.template ?? "classic",
    font: design.font ?? "Inter",
    heading_title_color: restoreColor(design.heading_title_color),
    entry_title_color: restoreColor(design.entry_title_color),
  };
};
