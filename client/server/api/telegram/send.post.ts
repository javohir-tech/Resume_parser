export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig();
  const { message } = await readBody(event);

  return await $fetch(
    `https://api.telegram.org/bot${config.botToken}/sendMessage`,
    {
      method: "POST",
      body: {
        chat_id: config.chatId,
        text: message,
      },
    },
  );
});
