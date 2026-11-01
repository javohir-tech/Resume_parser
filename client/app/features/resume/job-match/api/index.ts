import { api } from "~/shared/api";
import type { ResponseJobMatch, PayloadJobMatch } from "../models/types";

export const JobMatchRequest = (data: PayloadJobMatch) =>
  api<ResponseJobMatch>("/api/resume/job-match", {
    method: "POST",
    body: { ...data },
  });
  