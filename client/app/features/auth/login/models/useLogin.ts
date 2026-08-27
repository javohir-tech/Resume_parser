import { handleLogin } from "../api";

export default function useLogin() {
  const loading = ref<boolean>(false);
  const err = ref<string | null>(null);

  async function login(code: string) {
    loading.value = true;
    try {
      const { data } = await handleLogin(code);

      const access_token = useCookie("access_token");
      const refresh_token = useCookie("refresh_token");

      access_token.value = data.tokens.access_token;
      refresh_token.value = data.tokens.refresh_token;
      
    } catch (error) {
      console.log(error);
    } finally {
      loading.value = false;
    }
  }

  return { loading, err, login };
}
