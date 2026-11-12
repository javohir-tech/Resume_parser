import { fetch_logout } from "../api";
import { apiError, useApiToasts, useClearCookie } from "~/shared/lib";

export default function useLogout() {
  const loading = ref(false);
  const localePath = useLocalePath();
  const { showError, showSuccess } = useApiToasts();
  const { clearCookie } = useClearCookie();

  async function handle_logout() {
    try {
      const refresh_token = useCookie("refresh_token");
      if (refresh_token.value) {
        await fetch_logout({
          refresh_token: refresh_token.value,
        });
      }

      localStorage.clear();
      clearCookie();
      
      showSuccess("see are soon");
      await navigateTo(`${localePath("/")}`);
    } catch (error) {
      const err = apiError(error);
      showError(err.message);
    }
  }

  return { loading, handle_logout };
}
