<script setup lang="ts">
const { t } = useI18n()

const props = defineProps<{
    id: string,
    fullname?: string,
    title?: string,
    parent_resume_id?: string | null,
    job_company?: string,
    job_title?: string,
    cover_letter?: string | null,
    loading: boolean
}>()

const emit = defineEmits<{
    delete: []
}>()

const localPath = useLocalePath()
const open = ref(false)
const toast = useToast()
const { copy, copied } = useClipboard({ legacy: true, copiedDuring: 2000 })
const copying = ref(false)

async function copyCoverLetter() {
    if (!props.cover_letter?.trim() || copying.value) return

    copying.value = true
    try {
        await copy(props.cover_letter)
    } catch {
        toast.add({ title: 'Nusxalab bo‘lmadi. Qayta urinib ko‘ring.', color: 'error' })
    } finally {
        copying.value = false
    }
}

</script>

<template>
    <NuxtLink :to="localPath(`/resume/${id}`)" class="block h-full min-w-0 max-w-full">
        <UCard
            class="group h-full min-w-0 cursor-pointer transition duration-200 hover:-translate-y-1 hover:shadow-lg hover:ring-primary/40">
            <div class="mb-4">
                <span
                    class="inline-flex items-center gap-1.5 rounded border border-default px-2 py-0.5 text-xs text-muted">
                    <UIcon :name="parent_resume_id ? 'i-lucide-sparkles' : 'i-lucide-file-text'"
                        class="size-3.5 shrink-0" aria-hidden="true" />
                    {{ parent_resume_id ? 'AI versiya' : 'Asl nusxa' }}
                </span>
            </div>
            <div class="flex min-w-0 items-center gap-2 sm:gap-4">
                <div class="min-w-0 flex-1">
                    <p class="truncate text-lg font-semibold text-highlighted"
                        :title="parent_resume_id ? (job_title || title) : fullname">
                        {{ parent_resume_id
                            ? (job_title || title || t('resumeList.noTitle'))
                            : (fullname || t('resumeList.untitled')) }}
                    </p>
                    <p class="min-h-5 truncate text-sm text-muted"
                        :title="parent_resume_id ? job_company : title">
                        {{ parent_resume_id ? job_company : (title || t('resumeList.noTitle')) }}
                    </p>
                </div>

                <UPopover v-model:open="open">
                    <UButton class="shrink-0" icon="i-lucide-trash-2" color="error" variant="ghost" size="sm"
                        :aria-label="t('resumeList.delete')" @click.stop.prevent />
                    <template #content>
                        <div class="min-h-24 min-w-46 m-4 flex flex-col py-2">
                            <p class="mb-3">
                                {{ t('resumeEditor.deleteConfirmation') }}
                            </p>
                            <div class="flex justify-between items-center gap-2">

                                <UButton class="flex-1 justify-center" color="neutral" variant="outline" size="xs"
                                    icon="i-lucide-x" :label="t('resumeEditor.cancel')" @click="open = false" />

                                <UButton class="flex-1 justify-center" type="button" color="error" variant="outline"
                                    size="xs" icon="i-lucide-trash-2" :label="t('resumeEditor.delete')"
                                    :loading="loading" :disabled="loading" @click="emit('delete')" />
                            </div>
                        </div>
                    </template>
                </UPopover>

                <UIcon name="i-lucide-chevron-right"
                    class="size-4 shrink-0 text-dimmed transition duration-200 group-hover:translate-x-1 group-hover:text-primary" />
            </div>
            <div :class="{ invisible: !parent_resume_id }"
                :aria-hidden="!parent_resume_id"
                class="mt-4 flex h-12 min-w-0 items-center gap-2 border-t border-default pt-3 text-sm text-muted">
                <UIcon name="i-lucide-user-round" class="size-4 shrink-0"
                    aria-hidden="true" />
                <p class="min-w-0 flex-1 truncate" :title="fullname">{{ fullname || t('resumeList.untitled') }}</p>
                <UButton v-if="parent_resume_id" type="button" color="neutral" variant="outline" size="xs"
                    class="shrink-0" :icon="copied ? 'i-lucide-check' : 'i-lucide-copy'"
                    :label="copied ? 'Nusxalandi' : 'Cover letter'"
                    :aria-label="copied ? 'Cover letter nusxalandi' : 'Cover letterni nusxalash'"
                    :title="cover_letter?.trim() ? 'Cover letterni nusxalash' : 'Cover letter mavjud emas'"
                    :disabled="!cover_letter?.trim()" :loading="copying"
                    @click.stop.prevent="copyCoverLetter" />
            </div>
        </UCard>
    </NuxtLink>
</template>
