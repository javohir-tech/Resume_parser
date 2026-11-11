export interface ResponseRemoveSession {
  success: boolean;
  message: string;
}

export interface PayloadEditAccount {
  username ?: string;
  full_name ?: string;
}
