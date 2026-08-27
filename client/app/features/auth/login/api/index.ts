import type { LoginResponse } from "../models/types";

export const handleLogin = (code: string) =>
  $fetch<LoginResponse>(
    `http://127.0.0.1:8000/api/auth/telegram/verify?code=${code}`,
    { method: "POST" },
  );
