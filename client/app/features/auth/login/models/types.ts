import type { IUser } from "~/entities/user";

export interface LoginResponse {
  success: boolean;
  message: string;
  data: {
    tokens: {
      access_token: string;
      refresh_token: string;
    };
    user: IUser;
  };
}
