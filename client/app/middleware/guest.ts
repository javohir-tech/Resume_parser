export default defineNuxtRouteMiddleware((to , from)=>{
    const access_token = useCookie("access_token")

    if(access_token.value && to.path === "/login"){
        return navigateTo("/")
    }
})