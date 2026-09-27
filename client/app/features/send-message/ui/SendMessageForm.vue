<script setup lang="ts">
import type { FormSubmitEvent } from "@nuxt/ui";
import useSendMessage from "../models/sendMessage";
import { type Schema, schema } from "../models/types";

const { loading, sendMessageTelegram } = useSendMessage()

const { t } = useI18n()

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
    <UForm :schema="schema" :state="state" class="space-y-5" @submit="submitForm">
        <div class="grid gap-5 sm:grid-cols-2">
            <UFormField :label="t('contact.form.nameLabel')" name="name">
                <UInput v-model="state.name" class="w-full" :placeholder="t('contact.namePlaceholder')"
                    autocomplete="name" size="lg" :ui="{ base: 'rounded-xl bg-muted/30 py-3' }" />
            </UFormField>
            <UFormField :label="t('contact.form.emailLabel')" name="email">
                <UInput v-model="state.email" class="w-full" placeholder="you@example.com"
                    autocomplete="email" size="lg" :ui="{ base: 'rounded-xl bg-muted/30 py-3' }" />
            </UFormField>
        </div>
        <UFormField :label="t('contact.form.subjectLabel')" name="subject">
            <UInput v-model="state.subject" class="w-full" :placeholder="t('contact.form.subjectPlaceholder')"
                size="lg" :ui="{ base: 'rounded-xl bg-muted/30 py-3' }" />
        </UFormField>
        <UFormField :label="t('contact.form.messageLabel')" name="message">
            <UTextarea v-model="state.message" :placeholder="t('contact.form.messagePlaceholder')" :rows="5"
                class="w-full" size="lg" :ui="{ base: 'resize-y rounded-xl bg-muted/30 p-3' }" />
        </UFormField>
        <div class="border-t border-default pt-5">
            <UButton :loading="loading" :disabled="loading" trailing-icon="i-lucide-arrow-up-right" type="submit"
                size="lg" class="w-full justify-center rounded-xl py-3 font-medium">
                {{ t('contact.form.submitButton') }}
            </UButton>
        </div>
    </UForm>
</template>
