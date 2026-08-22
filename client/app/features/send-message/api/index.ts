export const telegramSendMessage = (message: string) =>
  $fetch("api/telegram/send", { method: "POST", body: { message } });
