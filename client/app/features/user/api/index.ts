import { api } from "~/shared/api";
import type {
  ResponseRemoveSession,
  PayloadEditAccount,
} from "../models/types";

export const EditAccountRequest = (payload: PayloadEditAccount) =>
  api<{ success: boolean }>("/api/users/account/edit", {
    method: "PATCH",
    body: payload,
  });

export const fetchRemoveSession = (device_id: string) =>
  api<ResponseRemoveSession>(`/api/users/sessions/${device_id}`, {
    method: "DELETE",
  });

export const deleteProfileRequest = () =>
  api<{ success: boolean; message: string }>("/api/users/profile/delete", {
    method: "DELETE",
  });
