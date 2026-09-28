import { useUserStore } from "~/entities/user";
import { fetch_logout } from "../api";
import { apiError, useApiToasts } from "~/shared/lib";

export default function useLogout() {
  const loading = ref(false);
  const userStore = useUserStore();
  const localePath = useLocalePath()
  const { showError  , showSuccess } = useApiToasts();

  async function handle_logout() {
    try {
      const refresh_token = useCookie("refresh_token");
      if (refresh_token.value) {
        await fetch_logout({
          refresh_token: refresh_token.value,
        });
      }
      const access_token = useCookie("access_token");
      access_token.value = null;
      refresh_token.value = null;
      userStore.logout();
      showSuccess("see are soon")
      await navigateTo(`${localePath('/')}`)
    } catch (error) {
      const err = apiError(error)
      showError(err.message)
    }
  }

  return { loading, handle_logout };
}
