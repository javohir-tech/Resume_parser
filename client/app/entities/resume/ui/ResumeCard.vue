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
const confirmingDelete = ref(false)
watch(open, () => { confirmingDelete.value = false })
const cardTitle = computed(() =>
    (props.parent_resume_id ? props.job_title || props.title : props.title) || t('resumeList.noTitle')
)
const toast = useToast()
const { copy, copied } = useClipboard({ legacy: true, copiedDuring: 2000 })
const copying = ref(false)

async function copyCoverLetter() {
    if (!props.cover_letter?.trim() || copying.value) return

    copying.value = true
    try {
        await copy(props.cover_letter)
    } catch {
        toast.add({ title: t('resumeList.copyError'), color: 'error' })
    } finally {
        copying.value = false
    }
}

</script>

<template>
    <article
        class="group flex h-full min-w-0 flex-col overflow-hidden rounded-2xl border border-default bg-default transition duration-200 hover:-translate-y-1 hover:shadow-lg hover:ring-1 hover:ring-primary/40 motion-reduce:transform-none motion-reduce:transition-none">
        <div class="flex-1 p-4">

            <div class="mb-3 flex items-center gap-2.5">
                <span class="flex size-9 shrink-0 items-center justify-center rounded-lg"
                    :class="parent_resume_id ? 'bg-primary/10 text-primary' : 'bg-muted text-muted'">
                    <UIcon name="i-lucide-file-text" class="size-5" aria-hidden="true" />
                </span>

                <span class="inline-flex min-w-0 items-center gap-1.5 rounded-full px-2.5 py-1 text-xs font-medium"
                    :class="parent_resume_id ? 'bg-primary/10 text-primary' : 'bg-muted text-muted'">
                    <UIcon v-if="parent_resume_id" name="i-lucide-sparkles" class="size-3.5 shrink-0"
                        aria-hidden="true" />
                    {{ parent_resume_id ? t('resumeList.filterAi') : t('resumeList.filterOriginal') }}
                </span>

                <UPopover v-model:open="open" :content="{ align: 'end' }">
                    <UButton class="ml-auto shrink-0" icon="i-lucide-ellipsis" color="neutral" variant="ghost"
                        :aria-label="t('resumeList.actions')" :disabled="loading" />
                    <template #content>
                        <div v-if="!confirmingDelete" class="w-52 p-1.5">
                            <UButton block class="justify-start" icon="i-lucide-eye" color="neutral" variant="ghost"
                                label="View" />
                            <UButton block class="justify-start" icon="i-lucide-copy" color="neutral" variant="ghost"
                                label="Copy Link" />
                            <UButton block class="justify-start" icon="i-lucide-download" color="neutral"
                                variant="ghost" label="Download" />
                            <UButton block class="justify-start" icon="i-lucide-copy" color="neutral" variant="ghost"
                                label="Copy Cover Letter" />
                            <UButton block class="justify-start" icon="i-lucide-trash-2" color="error" variant="ghost"
                                :label="t('resumeList.delete')" @click="confirmingDelete = true" />
                        </div>
                        <div v-else class="w-64 max-w-[calc(100vw-2rem)] p-4">
                            <p class="mb-4 text-sm font-medium text-highlighted">{{ t('resumeEditor.deleteConfirmation')
                            }}</p>
                            <div class="flex gap-2">
                                <UButton class="flex-1 justify-center" color="neutral" variant="outline" size="sm"
                                    :label="t('resumeEditor.cancel')" :disabled="loading"
                                    @click="confirmingDelete = false" />
                                <UButton class="flex-1 justify-center" color="error" size="sm"
                                    :label="t('resumeEditor.delete')" :loading="loading" :disabled="loading"
                                    @click="emit('delete')" />
                            </div>
                        </div>
                    </template>
                </UPopover>
                
            </div>

            <h3 class="text-lg font-semibold leading-6 tracking-tight text-highlighted">
                <NuxtLink :to="localPath(`/resume/${id}`)"
                    class="line-clamp-2 rounded-sm break-words transition-colors hover:text-primary focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-primary"
                    :title="cardTitle">{{ cardTitle }}</NuxtLink>
            </h3>

            <div class="mt-2 space-y-1 text-sm text-muted">
                <p class="flex min-w-0 items-center gap-2">
                    <UIcon name="i-lucide-user-round" class="size-4 shrink-0 text-dimmed" aria-hidden="true" />
                    <span class="truncate" :title="fullname">{{ fullname || t('resumeList.untitled') }}</span>
                </p>
                <p v-if="parent_resume_id && job_company" class="flex min-w-0 items-center gap-2">
                    <UIcon name="i-lucide-building-2" class="size-4 shrink-0 text-dimmed" aria-hidden="true" />
                    <span class="truncate" :title="job_company">{{ job_company }}</span>
                </p>
            </div>

        </div>

        <div class="flex flex-wrap items-center justify-between gap-2 border-t border-default bg-muted/20 px-4 py-2">
            <UButton :to="localPath(`/resume/${id}`)" color="primary" variant="ghost" size="sm"
                trailing-icon="i-lucide-arrow-up-right" :label="t('resumeList.open')" />
            <UButton v-if="parent_resume_id" type="button" color="neutral" variant="ghost" size="sm"
                :icon="copied ? 'i-lucide-check' : 'i-lucide-copy'"
                :label="copied ? t('resumeList.copied') : t('resumeList.coverLetter')"
                :aria-label="copied ? t('resumeList.copied') : t('resumeList.copyCoverLetter')"
                :title="cover_letter?.trim() ? t('resumeList.copyCoverLetter') : t('resumeList.noCoverLetter')"
                :disabled="!cover_letter?.trim()" :loading="copying" @click="copyCoverLetter" />
        </div>

    </article>
</template>
