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
