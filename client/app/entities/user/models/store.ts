import { fetchGetMe } from "../api";
import type { IUser } from "./types";
import { apiError, useApiToasts } from "~/shared/lib";

export const useUserStore = defineStore("user", () => {
  const user = ref<IUser | null>(null);
  const loading = ref<boolean>(false);
  const error = ref<string | null>(null);
  const { showError } = useApiToasts();

  const setUser = (data: IUser) => {
    user.value = data;
  };

  const getMe = async () => {
    loading.value = true;
    try {
      const response = await fetchGetMe();
      user.value = response;
    } catch (error) {
      const err = apiError(error)
      showError(err.message)
      // console.log(error);
    } finally {
      loading.value = false;
    }
  };

  const logout = () => {
    user.value = null;
  };

  return {
    user,
    loading,
    error,
    setUser,
    getMe,
    logout,
  };
});
