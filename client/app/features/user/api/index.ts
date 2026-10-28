import { api } from "~/shared/api";
import type { ResponseRemoveSession } from "../models/types";

export const fetchRemoveSession = (device_id: string) =>
  api<ResponseRemoveSession>(`/api/users/sessions/${device_id}`, {
    method: "DELETE",
  });

export const deleteProfileRequest = () =>
  api<{ success: boolean; message: string }>("/api/users/profile/delete", {
    method: "DELETE",
  });
