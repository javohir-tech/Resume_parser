import { telegramSendMessage } from "../api";
import type { Schema } from "./types";
import type { FetchError } from "ofetch";

export default function useSendMessage() {
  const toast = useToast();
  const loading = ref(false);

  async function sendMessageTelegram(data: Schema) {
    loading.value = true;
    try {
      const text = `
        name : ${data.name}, 
        email : ${data.email}, 
        theme : ${data.subject},
        message : ${data.message}
      `;

      const response = await telegramSendMessage(text);
      if (response.ok) {
        toast.add({
          title: "Xabaringiz yuborildi",
          description: "Tez orada siz bilan aloqaga chiqamiz",
          color: "success",
          icon: "i-lucide-check-circle",
        });
      }
      // console.log(response);
    } catch (error) {
      const err = error as FetchError
      
      console.error("Telegram send error:", err.statusCode, err.data);

      toast.add({
        title: "Xabar yuborilmadi",
        description: "Xatolik yuz berdi, iltimos qaytadan urinib ko‘ring",
        color: "error",
        icon : "i-lucide-x-circle"
      });
    } finally {
      loading.value = false;
    }
  }

  return { loading, sendMessageTelegram };
}
