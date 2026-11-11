<script setup lang="ts">
import { getMeRequest } from '../api';
const { t } = useI18n()

const props = defineProps<{
    loading: boolean,
    username_success: (value: string) => Promise<boolean>,
    full_name_success: (value: string) => Promise<boolean>
}>()

const username_modal_open = ref(false)
const full_name_modal_open = ref(false)

const { data, status, pending, error } = useLazyAsyncData("my_account", () => getMeRequest())

const username = ref(data.value?.username ?? "")
const full_name = ref(data.value?.full_name ?? "")

const handleSaveUsername = async () => {
    if (!username.value || username.value === data.value?.username) return

    const success = await props.username_success(username.value)
    if (success) {
        username_modal_open.value = false
        if (data.value?.username) {
            data.value.username = username.value
        }
    }
}

const handleSaveFullname = async () => {
    if (!full_name.value || full_name.value === data.value?.full_name) return

    const success = await props.full_name_success(full_name.value)
    if (success) {
        full_name_modal_open.value = false
        if (data.value?.full_name) {
            data.value.full_name = full_name.value
        }
    }
}

</script>

<template>
    <div class="divide-y divide-default">
        <div class="flex min-h-15 items-center justify-between gap-4 px-5 py-3 text-sm text-muted max-sm:flex-wrap max-sm:items-start">
            <p class="m-0 w-[38%] shrink-0 font-semibold text-highlighted max-sm:w-full">{{ t('profile.username') }}</p>
            <div class="flex min-w-0 items-center justify-end gap-2 text-right max-sm:justify-start max-sm:text-left">
                <p>{{ data?.username }}</p>
                <UModal v-model:open="username_modal_open" :title="t('settings.account.editUsername')"
                    :description="t('settings.account.usernameDescription')"
                    :close="{ 'aria-label': t('settings.actions.close') }"
                    :ui="{ content: 'max-w-md rounded-2xl', header: 'p-5 sm:p-6', wrapper: 'pe-8', body: 'p-0 sm:p-0', title: 'text-lg font-semibold', description: 'mt-1 text-sm text-muted' }">
                    <UButton class="shrink-0 text-muted" icon="i-lucide-pencil-line" variant="ghost" color="neutral"
                        :aria-label="t('settings.account.editUsername')" />
                    <template #body>
                        <UForm class="text-left" @submit.prevent="handleSaveUsername">
                            <div class="p-5 sm:p-6">
                                <UFormField :label="t('profile.username')" :help="t('settings.account.characterLimit', { count: 64 })">
                                    <UInput v-model="username" :maxlength="64" :placeholder="t('settings.account.usernamePlaceholder')"
                                        icon="i-lucide-at-sign" size="lg" class="w-full" :ui="{ base: 'rounded-xl' }" />
                                </UFormField>
                            </div>
                            <div class="flex flex-col-reverse gap-3 border-t border-default bg-muted/30 p-5 sm:flex-row sm:items-center sm:justify-end sm:p-6">
                                <UButton @click="username_modal_open = false" :label="t('settings.actions.cancel')" color="neutral"
                                    variant="soft" type="button" size="lg"
                                    class="min-h-11 w-full justify-center rounded-xl sm:w-auto sm:min-w-24" />
                                <UButton :loading="loading" :disabled="loading" :label="t('settings.actions.save')" color="primary"
                                    type="submit" size="lg"
                                    class="min-h-11 w-full justify-center rounded-xl sm:w-auto sm:min-w-24" />
                            </div>
                        </UForm>
                    </template>
                </UModal>
            </div>
        </div>
        <div class="flex min-h-15 items-center justify-between gap-4 px-5 py-3 text-sm text-muted max-sm:flex-wrap max-sm:items-start">
            <p class="m-0 w-[38%] shrink-0 font-semibold text-highlighted max-sm:w-full">{{ t('settings.account.fullName') }}</p>
            <div class="flex min-w-0 items-center justify-end gap-2 text-right max-sm:justify-start max-sm:text-left">
                <p>{{ data?.full_name.split("").slice(0, 30).join("") }}{{ data?.full_name !== undefined &&
                    data?.full_name.length > 30 ? '...' : '' }}</p>
                <UModal v-model:open="full_name_modal_open" :title="t('settings.account.editFullName')"
                    :description="t('settings.account.fullNameDescription')"
                    :close="{ 'aria-label': t('settings.actions.close') }"
                    :ui="{ content: 'max-w-md rounded-2xl', header: 'p-5 sm:p-6', wrapper: 'pe-8', body: 'p-0 sm:p-0', title: 'text-lg font-semibold', description: 'mt-1 text-sm text-muted' }">
                    <UButton class="shrink-0 text-muted" icon="i-lucide-pencil-line" variant="ghost" color="neutral"
                        :aria-label="t('settings.account.editFullName')" />
                    <template #body>
                        <UForm class="text-left" @submit.prevent="handleSaveFullname">
                            <div class="p-5 sm:p-6">
                                <UFormField :label="t('settings.account.fullName')" :help="t('settings.account.characterLimit', { count: 255 })">
                                    <UInput v-model="full_name" :maxlength="255" :placeholder="t('settings.account.fullNamePlaceholder')"
                                        icon="i-lucide-user" size="lg" class="w-full" :ui="{ base: 'rounded-xl' }" />
                                </UFormField>
                            </div>
                            <div class="flex flex-col-reverse gap-3 border-t border-default bg-muted/30 p-5 sm:flex-row sm:items-center sm:justify-end sm:p-6">
                                <UButton @click="full_name_modal_open = false" :label="t('settings.actions.cancel')" color="neutral"
                                    variant="soft" type="button" size="lg"
                                    class="min-h-11 w-full justify-center rounded-xl sm:w-auto sm:min-w-24" />
                                <UButton :loading="loading" :disabled="loading" :label="t('settings.actions.save')" color="primary"
                                    type="submit" size="lg"
                                    class="min-h-11 w-full justify-center rounded-xl sm:w-auto sm:min-w-24" />
                            </div>
                        </UForm>
                    </template>
                </UModal>
            </div>
        </div>
        <div class="flex min-h-15 items-center justify-between gap-4 px-5 py-3 text-sm text-muted max-sm:flex-wrap max-sm:items-start">
            <p class="m-0 w-[38%] shrink-0 font-semibold text-highlighted max-sm:w-full">{{ t('settings.account.plan') }}</p>
            <p>{{ data?.plan }}</p>
        </div>
        <div class="flex min-h-15 items-center justify-between gap-4 px-5 py-3 text-sm text-muted max-sm:flex-wrap max-sm:items-start">
            <p class="m-0 w-[38%] shrink-0 font-semibold text-highlighted max-sm:w-full">{{ t('profile.telegramId') }}</p>
            <p>{{ data?.telegram_id }}</p>
        </div>
        <div class="flex min-h-15 items-center justify-between gap-4 px-5 py-3 text-sm text-muted max-sm:flex-wrap max-sm:items-start">
            <p class="m-0 w-[38%] shrink-0 font-semibold text-highlighted max-sm:w-full">{{ t('profile.registered') }}</p>
            <p>{{ data?.registered_at }}</p>
        </div>
    </div>
</template>
