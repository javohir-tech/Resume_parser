import type { IUser } from "../models/types";
import { api } from "~/shared/api";

export const fetchGetMe = () => api<IUser>("/api/users/me", { method: "GET" });
