import { handleLogin } from "../api";
import { FetchError } from "ofetch";
import { useUserStore } from "~/entities/user";
import { useApiToasts, apiError } from "~/shared/lib";

export default function useLogin() {
  const loading = ref<boolean>(false);
  const to_many_request = ref(false);
  const retry_after = ref<number>(0);
  const userStore = useUserStore();
  const { showSuccess, showError } = useApiToasts();

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

        showSuccess(response.message);
      }
    } catch (error) {
      const fetchError = error as FetchError;
      if (fetchError.response?.status === 429) {
        showError(fetchError.data?.message);
          const HeaderRetry = fetchError.response?.headers.get("Retry-After");
          startCountdown(Number(HeaderRetry) || 60);
      } else {
        const err = apiError(fetchError);
        showError(err.message);
      }
    } finally {
      loading.value = false;
    }
  }

  return { loading, countdownInterval, to_many_request, login };
}
