import type { NitroFetchOptions, NitroFetchRequest } from "nitropack";
import { FetchError } from "ofetch";

const apiBaseUrl = "http://localhost:8000";

const apiFetch = $fetch.create({
  baseURL: apiBaseUrl,
  onRequest({ options }) {
    const accessToken = useCookie<string | null>("access_token");

    if (accessToken.value) {
      const headers = new Headers(options.headers);
      headers.set("Authorization", `Bearer ${accessToken.value}`);
      options.headers = headers;
    }
  },
});

let refreshPromise: Promise<string | null> | null = null;

async function requestNewAccessToken(): Promise<string | null> {
  const accessToken = useCookie<string | null>("access_token");
  const refreshToken = useCookie<string | null>("refresh_token");

  if (!refreshToken.value) {
    return null;
  }

  try {
    const response = await $fetch<{ access_token: string }>("/api/auth/refresh", {
      baseURL: apiBaseUrl,
      method: "POST",
      body: { refresh_token: refreshToken.value },
      credentials: "include",
    });

    accessToken.value = response.access_token;
    return response.access_token;
  } catch {
    accessToken.value = null;
    refreshToken.value = null;
    return null;
  }
}

function refreshAccessToken(): Promise<string | null> {
  if (import.meta.client && refreshPromise) {
    return refreshPromise;
  }

  const request = requestNewAccessToken();
  if (!import.meta.client) {
    return request;
  }

  refreshPromise = request.finally(() => {
    refreshPromise = null;
  });
  return refreshPromise;
}

export async function api<T>(
  request: NitroFetchRequest,
  options: NitroFetchOptions<NitroFetchRequest> = {},
): Promise<T> {
  try {
    return await apiFetch<T>(request, options) as T;
  } catch (error) {
    const requestPath = typeof request === "string" ? request.split("?")[0] : "";
    const isLoginRequest = requestPath === "/api/auth/telegram/verify";

    if (
      !(error instanceof FetchError) ||
      error.response?.status !== 401 ||
      isLoginRequest
    ) {
      throw error;
    }

    const newAccessToken = await refreshAccessToken();
    if (!newAccessToken) {
      await navigateTo("/login");
      throw error;
    }

    const headers = new Headers(options.headers);
    headers.set("Authorization", `Bearer ${newAccessToken}`);

    try {
      return await apiFetch<T>(request, {
        ...options,
        headers,
        retry: false,
      }) as T;
    } catch (retryError) {
      if (retryError instanceof FetchError && retryError.response?.status === 401) {
        useCookie<string | null>("access_token").value = null;
        useCookie<string | null>("refresh_token").value = null;
        await navigateTo("/login");
      }
      throw retryError;
    }
  }
}
