import { api } from "~/shared/api";
import type {
  ParseResumeResponse,
  ImportResumeResponse,
} from "../models/types";

export const resumeParseRequest = (file : File) => {
    const formData = new FormData()
    formData.append("file" , file)

    return api<ParseResumeResponse>("/api/resume/parse" , {
        method : "POST" , body : formData
    })
}

export const resumeImportRequest = (resume_ai_response: ParseResumeResponse) =>
  api<ImportResumeResponse>("/api/resume/import", {
    method: "POST",
    body: { resume: resume_ai_response },
  });
