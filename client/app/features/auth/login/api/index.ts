import type { LoginResponse } from "../models/types";
import { api } from "~/shared/api";

export const handleLogin = (code: string) =>
  api<LoginResponse>(`/api/auth/telegram/verify?code=${code}`, {
    method: "POST",
  });
