<script setup lang="ts">
import type { FormSubmitEvent } from "@nuxt/ui";
import useSendMessage from "../models/sendMessage";
import { type Schema, schema } from "../models/types";

const { loading, sendMessageTelegram } = useSendMessage()

const state = reactive<Schema>({
    name: "",
    email: "",
    subject: "",
    message: "",
})


async function submitForm(event: FormSubmitEvent<Schema>) {
    await sendMessageTelegram(event.data)
    state.email = ""
    state.name = ""
    state.subject = ""
    state.message = ""
}

</script>

<template>
    <UForm :schema="schema" :state="state" @submit="submitForm">
        <div class="flex flex-col md:flex-row md:justify-between gap-3">
            <UFormField label="Ismingiz" class="flex-1 font-mono" name="name">
                <UInput v-model="state.name" class="w-full" placeholder="Suvonov Javohir" size="xl" />
            </UFormField>
            <UFormField label="Email" class="flex-1 font-mono" name="email">
                <UInput v-model="state.email" class="w-full" placeholder="example@gmail.com" size="xl" />
            </UFormField>
        </div>
        <UFormField label="Mavzu" class="font-mono mt-4" name="subject">
            <UInput v-model="state.subject" class="w-full font-mono" placeholder="Nima haqida yozmoqchisiz" size="xl" />
        </UFormField>
        <UFormField label="Xabar" class="font-mono mt-4" name="message">
            <UTextarea v-model="state.message" placeholder="Savolingiz yoki taklifingizni batafsil yozing..." :rows="4"
                class="w-full" />
        </UFormField>
        <div class="text-end mt-5">
            <UButton :loading="loading" :disabled="loading" icon="lucide:send" type="submit">Yuborish</UButton>
        </div>
    </UForm>
</template>