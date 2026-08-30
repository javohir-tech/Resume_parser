export const api = $fetch.create({
    baseURL : "http://localhost:8000" , 
    onRequest({options}){
        const access_token = useCookie("access_token")
        if(access_token){
            options.headers = new Headers(options.headers)
            options.headers.set("Authorization" , `Bearer ${access_token.value}`)
        }
    } , 

    async onResponseError({response}){
        if(response.status === 401){
            await navigateTo("/login")
        }
    }
})