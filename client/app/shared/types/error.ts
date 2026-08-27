export interface ApiErrorBody {
  detail: string;
}

export interface ToManyRequests {
  success: boolean;
  message: string;
  retry_after: string;
}
