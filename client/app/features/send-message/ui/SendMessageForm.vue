<script setup lang="ts">
import * as v from "valibot"
import type { FormSubmitEvent } from "@nuxt/ui";

const schema = v.object({
    name: v.pipe(v.string()),
    email: v.pipe(v.string(), v.email("Invalid Email")),
    subject: v.pipe(v.string()),
    message: v.pipe(v.string())
})

type Schema = v.InferOutput<typeof schema>

const state = reactive<Schema>({
    name: "",
    email: "",
    subject: "",
    message: "",
})

const toast = useToast()

async function submitForm(event: FormSubmitEvent<Schema>) {
    toast.add({ title: "Success", description: "oxshadi", color: "success" })
    console.log(event.data)
}

</script>

<template>
    <UForm :schema="schema" :state="state" @submit="submitForm">
        <div class="flex justify-between gap-3">
            <UFormField label="Ismingiz" class="flex-1 font-mono">
                <UInput v-model="state.name" name="name" class="w-full" placeholder="Suvonov Javohir" size="xl" />
            </UFormField>
            <UFormField label="Email" class="flex-1 font-mono">
                <UInput v-model="state.email" name="email" class="w-full" placeholder="example@gmail.com" size="xl" />
            </UFormField>
        </div>
        <UFormField label="Mavzu" class="font-mono mt-4">
            <UInput v-model="state.subject" name="subject" class="w-full font-mono" placeholder="Nima haqida yozmoqchisiz" size="xl" />
        </UFormField>
        <UFormField label="Xabar" class="font-mono mt-4">
            <UTextarea name="message" v-model="state.message" placeholder="Savolingiz yoki taklifingizni batafsil yozing..." :rows="4"
                class="w-full" />
        </UFormField>
        <div class="text-end mt-5">
            <UButton icon="lucide:send" type="submit">Yuborish</UButton>
        </div>
    </UForm>
</template>