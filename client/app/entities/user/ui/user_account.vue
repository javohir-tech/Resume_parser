<script setup lang="ts">
import { getMeRequest } from '../api';

const emit = defineEmits(["save-username", "save-fullname"])

const props = defineProps<{
    loading: boolean
}>()

const username_modal_open = ref(false)
const full_name_modal_open = ref(false)

const { data, status, pending, error } = useLazyAsyncData("my_account", () => getMeRequest())

const username = ref(data.value?.username ?? "")
const full_name = ref(data.value?.full_name ?? "")

const handleSaveUsername = () => {
    if (!username.value || username.value === data.value?.username) return
    emit("save-username", username.value)
}

const handleSaveFullname = () => {
    if (!full_name.value || full_name.value === data.value?.full_name) return
    emit("save-fullname", full_name.value)
}

</script>

<template>
    <div class="flex flex-col">
        <div class="flex justify-between">
            <p>Username</p>
            <div class="flex items-center gap-2">
                <p>{{ data?.username }}</p>
                <UModal v-model:open="username_modal_open">
                    <UButton icon="i-lucide-pencil-line" variant="ghost" color="neutral" />
                    <template #content>
                        <UForm @submit.prevent="handleSaveUsername">
                            <UInput v-model="username" />
                            <div class="flex items-cnter gap-2">
                                <UButton @click="username_modal_open = false" label="Cancel" color="secondary" />
                                <UButton :loading="loading" :disabled="loading" label="Save" color="primary"
                                    type="submit" />
                            </div>
                        </UForm>
                    </template>
                </UModal>
            </div>
        </div>
        <div class="flex justify-between">
            <p>fullname</p>
            <div class="flex items-center gap-2">
                <p>{{ data?.full_name }}</p>
                <UModal v-model:open="full_name_modal_open">
                    <UButton icon="i-lucide-pencil-line" variant="ghost" color="neutral" />
                    <template #content>
                        <UForm @submit.prevent="handleSaveFullname">
                            <UInput v-model="full_name" />
                            <div class="flex items-cnter gap-2">
                                <UButton @click="full_name_modal_open = false" label="Cancel" color="secondary" />
                                <UButton :loading="loading" :disabled="loading" label="Save" color="primary"
                                    type="submit" />
                            </div>
                        </UForm>
                    </template>
                </UModal>
            </div>
        </div>
        <div class="flex justify-between">
            <p>plan</p>
            <p>{{ data?.plan }}</p>
        </div>
        <div class="flex justify-between">
            <p>telegram id</p>
            <p>{{ data?.telegram_id }}</p>
        </div>
        <div class="flex justify-between">
            <p>registred</p>
            <p>{{ data?.registered_at }}</p>
        </div>
    </div>
</template>