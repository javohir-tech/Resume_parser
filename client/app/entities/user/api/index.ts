import type {
  IUser,
  ResponseSessions,
} from "../models/types";
import { api } from "~/shared/api";

export const getMeRequest = () => api<IUser>("/api/users/me", { method: "GET" });

export const GetSessionsRequest = () =>
  api<ResponseSessions>("/api/users/me/sessions", {
    method: "GET",
    credentials: "include",
  });
