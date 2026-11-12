import { deleteProfileRequest } from "../api";
import { apiError, useApiToasts, useClearCookie } from "~/shared/lib";

export const useDeleteProfile = () => {
  const loading = ref<boolean>(false);
  const { showError, showSuccess } = useApiToasts();
  const { clearCookie } = useClearCookie();
  const localPath = useLocalePath();

  const deleteProfile = async () => {
    loading.value = true;
    try {
      const response = await deleteProfileRequest();
      showSuccess(response.message);
      if (response.success) {
        const device_id = useCookie("device_id");
        const i18n = useCookie("i18n_redirected");
        device_id.value = null;
        i18n.value = null;
        clearCookie();
        localStorage.clear();
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
