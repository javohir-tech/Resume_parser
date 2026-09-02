import { FetchError } from "ofetch";
import type { ApiErrorBody } from "~/shared/types";
import { fetchRemoveSession } from "../api";

export const useSessionRevoke = () => {
  const loading = ref(false);

  const toast = useToast();

  const revokeSession = async (device_id: string) => {
    if (!device_id) return;

    loading.value = true;
    try {
      const response = await fetchRemoveSession(device_id);
      // console.log(response);
      if (response.success) {
        toast.add({ title: response.message, color: "primary" });
      }
    } catch (error) {
      const err = error as FetchError<ApiErrorBody>;
      const message = err.data?.detail ?? "Internal Server Error";
      toast.add({ title: message, color: "error" });
      throw new Error(message);
    } finally {
      loading.value = false;
    }
  };

  return {
    loading,
    revokeSession,
  };
};
