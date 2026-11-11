<script setup lang="ts">
import { useDeleteProfile } from '../models/useDeleteProfile';

const { t } = useI18n()
const delete_check = ref<string>("")
const { deleteProfile , loading } = useDeleteProfile()

const handleDeleteProfile = async () => {
    if (delete_check.value.trim() !== "delete") return

    await deleteProfile()
}

</script>

<template>
    <div>
        <UModal :title="t('profile.delete.title')" :description="t('profile.delete.description')"
            :close="{ 'aria-label': t('profile.delete.close') }"
            :ui="{ content: 'max-w-md rounded-2xl', header: 'p-5 sm:p-6', body: 'p-5 sm:p-6', footer: 'p-5 sm:p-6' }">
            <div class="flex items-center justify-between gap-4 max-sm:flex-col max-sm:items-start">
                <div>
                    <p class="m-0 text-base font-semibold text-highlighted">{{ t('settings.account.deleteTitle') }}</p>
                    <p class="mt-1 text-sm leading-6 text-muted">{{ t('settings.account.deleteDescription') }}</p>
                </div>
                <UButton class="shrink-0 rounded-xl max-sm:self-end" :label="t('profile.delete.action')" color="error" variant="soft" size="sm" />
            </div>

            <template #body>
                <div class="space-y-6">
                    <div class="flex items-start gap-3 rounded-xl border border-error/20 bg-error/5 p-4">
                        <span class="flex size-9 shrink-0 items-center justify-center rounded-lg bg-error/10 text-error"
                            aria-hidden="true">
                            <UIcon name="i-lucide-triangle-alert" class="size-5" />
                        </span>
                        <div class="min-w-0">
                            <p class="text-sm font-semibold text-highlighted">{{ t('profile.delete.warningTitle') }}</p>
                            <p class="mt-1 text-sm leading-relaxed text-muted">{{ t('profile.delete.warning') }}</p>
                        </div>
                    </div>

                    <UFormField :label="t('profile.delete.confirmLabel')" :help="t('profile.delete.confirmHelp')">
                        <UInput v-model="delete_check" placeholder="delete" size="lg" class="w-full"
                            :ui="{ base: 'rounded-xl' }" autocomplete="off" autocapitalize="none" :spellcheck="false" />
                    </UFormField>
                </div>
            </template>

            <template #footer>
                <UButton :loading="loading" :disabled="delete_check.trim() !== 'delete' || loading" @click="handleDeleteProfile" type="button" :label="t('profile.delete.action')"
                    icon="i-lucide-trash-2" color="error" size="lg" block class="min-h-11 cursor-pointer rounded-xl" />
            </template>
        </UModal>
    </div>
</template>
