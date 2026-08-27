import { useUserStore } from "~/entities/user";

export default function useLogout() {
  const loading = ref(false);
  const userStore = useUserStore();
  const toast = useToast();

  async function handle_logout() {
    const access_token = useCookie("access_token");
    const refresh_token = useCookie("refresh_token");
    access_token.value = null;
    refresh_token.value = null;
    userStore.logout();
    toast.add({ title: "see are soon", color: "success" });
  }

  return { loading, handle_logout };
}
