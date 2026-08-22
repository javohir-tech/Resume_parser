<script setup lang="ts">
import * as v from "valibot"
import type { FormSubmitEvent } from "@nuxt/ui";

const schema = v.object({
    name: v.pipe(
        v.string(),
        v.minLength(1, "Ism kiritilishi shart"),
        v.minLength(2, "Ism juda qisqa"),
        v.maxLength(50, "Ism juda uzun")
    ),
    email: v.pipe(
        v.string(),
        v.minLength(1, "Email kiritilishi shart"),
        v.email("Email formati noto'g'ri"),
        v.maxLength(75, "email juda uzun")
    ),
    subject: v.pipe(
        v.string(),
        v.minLength(1, "Mavzu kiritilishi shart"),
        v.maxLength(100, "mavzu juda uzun")
    ),
    message: v.pipe(
        v.string(),
        v.minLength(1, "Xabar kiritilishi shart"),
        v.minLength(10, "Xabar juda qisqa, kamida 10 belgi"),
        v.maxLength(300, "xabar juda uzun , 300 tadan oshmasin")
    )
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
            <UButton icon="lucide:send" type="submit">Yuborish</UButton>
        </div>
    </UForm>
</template>