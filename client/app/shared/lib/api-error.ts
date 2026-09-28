import type { FetchError } from "ofetch";

export interface ApiError {
  status: number | null;
  code: string;
  message: string;
}

interface ValidationItem {
  loc: (string | number)[];
  msg: string;
  type: string;
}

export function apiError(error: unknown) {
  const fallback: ApiError = {
    status: null,
    code: "UNKNOWN_ERROR",
    message: "Kutilmagan xatolik yuz berdi.",
  };

  const err = error as FetchError | undefined;
  if (!err) return fallback;

  if (!err.response) {
    return {
      ...fallback,
      code: "NETWORK_ERROR",
      message: "Serverga ulanib bo'lmadi.",
    };
  }

  const status = err.response.status;
  const detail = err.data?.detail;

  if (detail && typeof detail === "object" && !Array.isArray(detail)) {
    return {
      status,
      code: detail.code ?? "API_ERROR",
      message: detail?.message ?? fallback.message,
    };
  }

  if (Array.isArray(detail)) {
    const first = detail[0] as ValidationItem | undefined;
    return {
      status,
      code: "VALIDATION_ERROR",
      message: first
        ? `${first.loc.slice(1).join(".")} : ${first.msg}`
        : "Ma'lumotlar noto'g'ri.",
    };
  }

  if (typeof detail === "string") {
    return { status, code: "API_ERROR", message: detail };
  }

  return { ...fallback, status };
}
