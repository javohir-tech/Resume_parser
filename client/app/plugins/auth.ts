import { useUserStore } from "~/entities/user";

export default defineNuxtPlugin(async () => {
    const userStore = useUserStore()
    const access_token = useCookie("access_token")

    if(access_token.value){
        await userStore.getMe()
    }
});
