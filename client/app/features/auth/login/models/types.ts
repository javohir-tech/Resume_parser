export interface LoginResponse {
  success: boolean;
  message: string;
  data: {
    tokens: {
      access_token: string;
      refresh_token: string;
    };
    user: {
      id: string;
      full_name: string;
      username: string  | null;
      telegram_id: number;
      registered_at: string;
    };
  };
}
