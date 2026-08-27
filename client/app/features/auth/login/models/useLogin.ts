import { handleLogin } from "../api";
import { FetchError } from "ofetch";
import { useUserStore } from "~/entities/user";
import type { ApiErrorBody, ToManyRequests } from "~/shared/types";

export default function useLogin() {
  const loading = ref<boolean>(false);
  const err = ref<string | null>(null);
  const to_many_request = ref(false);
  const toast = useToast();
  const retry_after = ref<number>(0);
  const userStore = useUserStore();

  let countdownInterval: ReturnType<typeof setInterval> | null = null;

  function startCountdown(seconds: number) {
    retry_after.value = seconds;
    to_many_request.value = true;

    if (countdownInterval) clearInterval(countdownInterval);

    countdownInterval = setInterval(() => {
      retry_after.value -= 1;

      if (retry_after.value <= 0) {
        to_many_request.value = false;
        if (countdownInterval) clearInterval(countdownInterval);
      }
    }, 1000);
  }

  async function login(code: string) {
    loading.value = true;
    try {
      const response = await handleLogin(code);

      // console.log(response.data);

      const access_token = useCookie("access_token");
      const refresh_token = useCookie("refresh_token");

      access_token.value = response.data.tokens.access_token;
      refresh_token.value = response.data.tokens.refresh_token;

      userStore.setUser(response.data.user);

      if (response.success) {
        await navigateTo("/");

        toast.add({
          title: response.message,
          color: "success",
          icon: "i-lucide-check-circle",
        });
      }
    } catch (error) {
      const fetchError = error as FetchError;
      if (fetchError.status === 429) {
        err.value = fetchError.data?.message;
        const HeaderRetry = fetchError.response?.headers.get("Retry-After");
        startCountdown(Number(HeaderRetry) || 60);
      } else {
        err.value = fetchError.data?.detail ?? "Internal Server Error";
      }
      console.log(err.value, fetchError.status);
      if (err.value) {
        toast.add({
          title: err.value,
          color: "error",
          icon: "i-lucide-x-circle",
        });
      }
    } finally {
      loading.value = false;
    }
  }

  return { loading, err, countdownInterval, to_many_request, login };
}
