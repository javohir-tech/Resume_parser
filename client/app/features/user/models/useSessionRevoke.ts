import { fetchRemoveSession } from "../api";
import { apiError, useApiToasts } from "~/shared/lib";

export const useSessionRevoke = () => {
  const loading = ref(false);
  const { showError, showSuccess } = useApiToasts();
  const deletingSessions = ref<Set<string>>(new Set());

  const revokeSession = async (device_id: string): Promise<boolean> => {
    if (!device_id) return false;

    loading.value = true;
    deletingSessions.value.add(device_id);
    try {
      const response = await fetchRemoveSession(device_id);
      // console.log(response);
      if (response.success) {
        showSuccess(response.message);
        return true;
      }
      return false;
    } catch (error) {
      const err = apiError(error);
      showError(err.message);
      return false;
    } finally {
      deletingSessions.value.delete(device_id);
      loading.value = false;
    }
  };

  const isDeleting = (device_id: string) =>
    deletingSessions.value.has(device_id);

  return {
    loading,
    isDeleting,
    revokeSession,
  };
};
