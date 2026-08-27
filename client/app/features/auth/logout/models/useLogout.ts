import { useUserStore } from "~/entities/user";
import { fetch_logout } from "../api";

export default function useLogout() {
  const loading = ref(false);
  const userStore = useUserStore();
  const toast = useToast();

  async function handle_logout() {
    try {
      const refresh_token = useCookie("refresh_token");
      if (refresh_token.value) {
        const response = await fetch_logout({
          refresh_token: refresh_token.value,
        });

      }
      const access_token = useCookie("access_token");
      access_token.value = null;
      refresh_token.value = null;
      userStore.logout();
      toast.add({ title: "see are soon", color: "success" });
    } catch (error) {}
  }

  return { loading, handle_logout };
}
