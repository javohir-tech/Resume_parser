import { fetchRemoveSession } from "../api";
import { apiError, useApiToasts } from "~/shared/lib";

export const useSessionRevoke = () => {
  const loading = ref(false);
  const { showError, showSuccess } = useApiToasts();

  const revokeSession = async (device_id: string) => {
    if (!device_id) return;

    loading.value = true;
    try {
      const response = await fetchRemoveSession(device_id);
      // console.log(response);
      if (response.success) {
        showSuccess(response.message);
      }
    } catch (error) {
      const err = apiError(error);
      showError(err.message);
    } finally {
      loading.value = false;
    }
  };

  return {
    loading,
    revokeSession,
  };
};
