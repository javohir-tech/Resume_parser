import { resumeParseRequest, resumeImportRequest } from "../api";
import type { ImportResumeResponse, ParseResumeResponse } from "./types";
import { useApiToasts, apiError } from "~/shared/lib";

export function useResumeParse() {
  const { showError } = useApiToasts();

  let disposed = false

  async function resumeParse(file: File): Promise<ParseResumeResponse | null> {
    if(disposed) return null

    try {
      const response = await resumeParseRequest(file);
      if(disposed) return null
      return response;
    } catch (error) {
      if(!disposed){  
        const err = apiError(error);
        showError(err.message);
      }
      return null;
    }
  }

  async function resumeImport(
    parse_resume: ParseResumeResponse,
  ): Promise<ImportResumeResponse | null> {
    if(disposed) return null
    try {
      const response = await resumeImportRequest(parse_resume);
      if(disposed) return null
      return response;
    } catch (error) {
      if(!disposed){
        const err = apiError(error);
        showError(err.message);
      }
      return null;
    }
  }

  onScopeDispose(()=>{
    disposed = true
  })

  return { resumeParse , resumeImport };
}
