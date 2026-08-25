export default defineEventHandler(async (event) =>{
    const config = useRuntimeConfig()
    const body = await readBody(event)
    console.log(body)


    return await $fetch(`https://api.telegram.org/bot${config.botToken}/sendMessage` , {
        method : "POST" , 
        body:{
            chat_id : config.chatId , 
            text : body.message
        }
    })
})