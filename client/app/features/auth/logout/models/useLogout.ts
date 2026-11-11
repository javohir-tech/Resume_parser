import { useUserStore } from "~/entities/user";
import { fetch_logout } from "../api";
import { apiError, useApiToasts } from "~/shared/lib";

export default function useLogout() {
  const loading = ref(false);
  const userStore = useUserStore();
  const localePath = useLocalePath();
  const { showError, showSuccess } = useApiToasts();

  async function handle_logout() {
    try {
      const refresh_token = useCookie("refresh_token");
      if (refresh_token.value) {
        await fetch_logout({
          refresh_token: refresh_token.value,
        });
      }
      const access_token = useCookie("access_token");
      localStorage.clear();
      access_token.value = null;
      refresh_token.value = null;

      const primary_color = useCookie("primary-color");
      const neutral_color = useCookie("neutral_color");
      const font_cookie = useCookie("app-font");
      const appConfig = useAppConfig();

      const font = useState("app-font", () => font_cookie.value);

      primary_color.value = "green";
      neutral_color.value = "slate";
      font_cookie.value = "Inter";
      font.value = "Inter";
      appConfig.ui.colors.primary = primary_color.value;
      appConfig.ui.colors.neutral = neutral_color.value;

      userStore.logout();
      showSuccess("see are soon");
      await navigateTo(`${localePath("/")}`);
    } catch (error) {
      const err = apiError(error);
      showError(err.message);
    }
  }

  return { loading, handle_logout };
}
