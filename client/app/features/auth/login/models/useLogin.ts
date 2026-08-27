import { handleLogin } from "../api";
import { FetchError } from "ofetch";
import { useUserStore } from "~/entities/user";
import type { ApiErrorBody } from "~/shared/types";

export default function useLogin() {
  const loading = ref<boolean>(false);
  const toast = useToast();
  const userStore = useUserStore();

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
      const fetchError = error as FetchError<ApiErrorBody>;
      const message = fetchError.data?.detail ?? "Internal Server Error";
      console.log(message, fetchError.status);
      toast.add({
        title: message,
        color: "error",
        icon: "i-lucide-x-circle",
      });
    } finally {
      loading.value = false;
    }
  }

  return { loading, login };
}
