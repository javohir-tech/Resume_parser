import { resumeParseRequest, resumeImportRequest } from "../api";
import type { ImportResumeResponse, ParseResumeResponse } from "./types";
import { useApiToast, apiError } from "~/shared/lib";

export function useResumeParse() {
  const { showError } = useApiToast();

  async function resumeParse(file: File): Promise<ParseResumeResponse | null> {
    try {
      const response = await resumeParseRequest(file);
      return response;
    } catch (error) {
      const err = apiError(error);
      showError(null, err.message);
      return null;
    }
  }

  async function resumeImport(
    parse_resume: ParseResumeResponse,
  ): Promise<ImportResumeResponse | null> {
    try {
      const response = await resumeImportRequest(parse_resume);
      return response;
    } catch (error) {
      const err = apiError(error);
      showError(null, err.message);
      return null;
    }
  }

  return { resumeParse , resumeImport };
}
