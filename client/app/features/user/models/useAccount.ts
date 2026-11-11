import { apiError, useApiToasts } from "~/shared/lib";
import { EditAccountRequest } from "../api";
import { type PayloadEditAccount } from "./types";

export const useAccount = () => {
  const loading = ref<boolean>(false);
  const { showError, showSuccess } = useApiToasts();

  const editAccount = async (params: PayloadEditAccount): Promise<boolean> => {
    loading.value = true;
    try {
      const response = await EditAccountRequest(params);
      if (response.success) {
        return true;
      }
      return false;
    } catch (error) {
      const err = apiError(error);
      showError(err.message);
      return false;
    } finally {
      loading.value = false;
    }
  };

  return { loading, editAccount };
};
