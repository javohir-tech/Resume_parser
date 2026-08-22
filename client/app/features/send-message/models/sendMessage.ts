import { telegramSendMessage } from "../api";
import type { Schema } from "./types";

export default function useSendMessage() {
  const config = useRuntimeConfig();

  async function sendMessageTelegram(data: Schema) {
    try {
      const response = await telegramSendMessage("salom");
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }

  return { sendMessageTelegram };
}
