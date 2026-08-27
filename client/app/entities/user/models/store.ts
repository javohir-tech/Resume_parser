import { fetchGetMe } from "../api";
import type { IUser } from "./types";

export const useUserStore = defineStore("user", () => {
  const user = ref<IUser | null>(null);
  const loading = ref<boolean>(false);

  const setUser = (data: IUser) => {
    user.value = data;
  };

  const getMe = async () => {
    loading.value = true;
    try {
      const response = await fetchGetMe();
      user.value = response
    } catch (error) {
      console.log(error);
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
    setUser,
    getMe,
    logout,
  };
});
