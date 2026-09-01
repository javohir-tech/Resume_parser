import { fetchGetMe } from "../api";
import type { IUser } from "./types";
import { FetchError } from "ofetch";
import type { ApiErrorBody } from "~/shared/types";

export const useUserStore = defineStore("user", () => {
  const user = ref<IUser | null>(null);
  const loading = ref<boolean>(false);
  const error = ref<string | null>(null);

  const setUser = (data: IUser) => {
    user.value = data;
  };

  const getMe = async () => {
    loading.value = true;
    try {
      const response = await fetchGetMe();
      user.value = response;
    } catch (err) {
      const fetchError = err as FetchError<ApiErrorBody>;
      error.value = fetchError.data?.detail ?? "Internal server error";
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
