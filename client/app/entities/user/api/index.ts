import type {
  IUser,
  ResponseSessions,
  ResponseRemoveSession,
} from "../models/types";
import { api } from "~/shared/api";

export const fetchGetMe = () => api<IUser>("/api/users/me", { method: "GET" });

export const fetchGetSessions = () =>
  api<ResponseSessions>("/api/users/me/sessions", {
    method: "GET",
    credentials: "include",
  });

export const fetchRemoveSession = (device_id: string) =>
  api<ResponseRemoveSession>(`/api/users/sessions/${device_id}`, {
    method: "DELETE",
  });
