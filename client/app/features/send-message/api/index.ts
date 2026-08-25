import { type TelegramResponse } from "../models/types";

export const telegramSendMessage = (message: string) =>
  $fetch<TelegramResponse>("/api/telegram/send", {
    method: "POST",
    body: { message },
  });
