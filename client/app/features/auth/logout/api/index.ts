import { api } from "~/shared/api";
import type { RequestLogout, Responselogout } from "../models/types";

export const fetch_logout = (payload: RequestLogout) =>
  api<Responselogout>("/api/auth/logout", { method: "POST", body: payload });
