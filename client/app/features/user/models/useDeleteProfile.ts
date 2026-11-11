import { deleteProfileRequest } from "../api";
import { apiError, useApiToasts } from "~/shared/lib";
import { useUserStore } from "~/entities/user";

export const useDeleteProfile = () => {
  const loading = ref<boolean>(false);
  const { showError, showSuccess } = useApiToasts();
  const localPath = useLocalePath();
  const store = useUserStore();

  const deleteProfile = async () => {
    loading.value = true;
    try {
      const response = await deleteProfileRequest();
      showSuccess(response.message);
      if (response.success) {
        const access_token = useCookie("access_token");
        const refresh_token = useCookie("refresh_token");
        const device_id = useCookie("device_id");
        const i18n = useCookie("i18n_redirected");
        device_id.value = null;
        i18n.value = null;
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

        localStorage.clear();
        store.logout();
        await navigateTo(`${localPath("/login")}`);
      }
    } catch (error) {
      const err = apiError(error);
      showError(err.message);
    } finally {
      loading.value = false;
    }
  };

  return { loading, deleteProfile };
};
