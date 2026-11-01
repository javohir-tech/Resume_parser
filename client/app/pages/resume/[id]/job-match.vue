<script setup lang="ts">
import { getMyResumes } from '~/entities/resume';

const route = useRoute()
const { t } = useI18n()
const localePath = useLocalePath()
const toast = useToast()
const resumeId = computed(() => typeof route.params.id === 'string' ? route.params.id : '')
const resumeKey = computed(() => `job_match_${resumeId.value}`)
const { data, status, error, refresh } = useLazyAsyncData(
    resumeKey,
    (_nuxtApp, { signal }) => resumeId.value
        ? getMyResumes({ resume_id: resumeId.value }, signal)
        : Promise.resolve([]),
    { server: false, default: () => [], dedupe: 'cancel' }
)
const resume = computed(() => data.value[0])
const isTailored = computed(() => resume.value?.parent_resume_id != null)
const pageTitle = computed(() => !resume.value
    ? t('jobMatchResult.detailsTitle')
    : t(isTailored.value ? 'jobMatchResult.title' : 'jobMatchResult.originalTitle'))
const isLoading = computed(() => status.value === 'pending' || status.value === 'idle')
const { copy, copied, text } = useClipboard({ legacy: true, copiedDuring: 2000 })
const copying = ref(false)
const letterCopied = computed(() => copied.value && text.value === resume.value?.cover_letter)

async function copyCoverLetter() {
    const letter = resume.value?.cover_letter
    if (!letter?.trim() || copying.value) return
    copying.value = true
    try {
        await copy(letter)
    } catch {
        toast.add({ title: t('resumeList.copyError'), color: 'error' })
    } finally {
        copying.value = false
    }
}
</script>

<template>
    <UContainer class="max-w-5xl py-6 sm:py-8">
        <header class="mb-8 max-w-2xl">
            <span v-if="resume && !isLoading && !error" class="mb-4 inline-flex items-center gap-2 rounded-full bg-primary/10 px-3 py-1.5 text-xs font-medium text-primary">
                <UIcon :name="isTailored ? 'i-lucide-sparkles' : 'i-lucide-file-text'" class="size-3.5" aria-hidden="true" />
                {{ t(isTailored ? 'jobMatch.eyebrow' : 'resumeList.filterOriginal') }}
            </span>
            <h1 class="text-3xl font-semibold tracking-tight text-highlighted sm:text-4xl">{{ pageTitle }}</h1>
            <p v-if="resume && !isLoading && !error" class="mt-3 leading-7 text-muted">{{ t(isTailored ? 'jobMatchResult.description' : 'jobMatchResult.originalDescription') }}</p>
        </header>

        <div v-if="isLoading" class="grid gap-4 lg:grid-cols-3" role="status" :aria-label="t('jobMatch.loading')">
            <span class="sr-only">{{ t('jobMatch.loading') }}</span>
            <div class="space-y-4 rounded-xl border border-default p-4">
                <USkeleton class="size-10 rounded-xl" />
                <USkeleton class="h-6 w-3/4" />
                <USkeleton class="h-4 w-1/2" />
                <USkeleton class="h-24 w-full" />
            </div>
            <div class="space-y-4 rounded-xl border border-default p-4 lg:col-span-2">
                <USkeleton class="h-6 w-1/3" />
                <USkeleton v-for="line in 6" :key="line" class="h-4" :class="line === 6 ? 'w-2/3' : 'w-full'" />
            </div>
        </div>

        <div v-else-if="error" class="rounded-xl border border-error/20 bg-error/5 p-8 text-center" role="alert">
            <UIcon name="i-lucide-cloud-off" class="mb-3 size-6 text-error" aria-hidden="true" />
            <h2 class="font-semibold text-highlighted">{{ t('jobMatch.loadError') }}</h2>
            <p class="mt-2 text-sm text-muted">{{ t('jobMatch.loadErrorHint') }}</p>
            <UButton class="mt-5" icon="i-lucide-refresh-cw" :label="t('jobMatch.retry')" @click="refresh()" />
        </div>

        <div v-else-if="resume" class="grid items-start gap-4" :class="isTailored ? 'lg:grid-cols-3' : 'max-w-md'">
            <section class="min-w-0 overflow-hidden rounded-xl border border-default bg-default" aria-labelledby="resume-heading">
                <div class="border-b border-default bg-primary/5 p-4">
                    <span class="mb-3 flex size-10 items-center justify-center rounded-xl bg-primary/10 text-primary">
                        <UIcon name="i-lucide-file-user" class="size-5" aria-hidden="true" />
                    </span>
                    <h2 id="resume-heading" class="break-words text-lg font-semibold text-highlighted">{{ resume.fullname || t('jobMatch.untitled') }}</h2>
                    <p class="mt-2 break-words text-sm leading-6 text-muted">{{ resume.title || t('jobMatch.noTitle') }}</p>
                </div>
                <div class="p-4">
                    <dl v-if="isTailored" class="space-y-4">
                        <div>
                            <dt class="flex items-center gap-2 text-xs font-medium text-muted">
                                <UIcon name="i-lucide-building-2" class="size-3.5" aria-hidden="true" />
                                {{ t('resumeEditor.company') }}
                            </dt>
                            <dd class="mt-2 break-words text-sm font-medium text-highlighted">{{ resume.job_company || t('jobMatchResult.unspecified') }}</dd>
                        </div>
                        <div>
                            <dt class="flex items-center gap-2 text-xs font-medium text-muted">
                                <UIcon name="i-lucide-briefcase-business" class="size-3.5" aria-hidden="true" />
                                {{ t('resumeEditor.position') }}
                            </dt>
                            <dd class="mt-2 break-words text-sm font-medium text-highlighted">{{ resume.job_title || t('jobMatch.noTitle') }}</dd>
                        </div>
                    </dl>
                    <div class="space-y-2" :class="{ 'mt-4 border-t border-default pt-4': isTailored }">
                        <UButton :to="localePath(`/resume/${resume.id}`)" icon="i-lucide-pencil" size="sm" block :label="t('jobMatchResult.edit')" />
                        <UButton :to="localePath(`/resume/${resume.id}/view`)" icon="i-lucide-eye" color="neutral" variant="outline" size="sm" block :label="t('resumeList.view')" />
                    </div>
                </div>
            </section>

            <section v-if="isTailored" class="min-w-0 overflow-hidden rounded-xl border border-default bg-default lg:col-span-2" aria-labelledby="letter-heading">
                <div class="flex flex-wrap items-center justify-between gap-3 border-b border-default p-4">
                    <div class="flex items-center gap-3">
                        <span class="flex size-8 items-center justify-center rounded-lg bg-elevated text-primary">
                            <UIcon name="i-lucide-mail" class="size-4" aria-hidden="true" />
                        </span>
                        <h2 id="letter-heading" class="text-base font-semibold text-highlighted">{{ t('jobMatchResult.coverLetter') }}</h2>
                    </div>
                    <span aria-live="polite">
                        <UButton :icon="letterCopied ? 'i-lucide-check' : 'i-lucide-copy'" color="neutral" variant="outline" size="sm"
                            :label="letterCopied ? t('resumeList.copied') : t('jobMatchResult.copy')"
                            :loading="copying" :disabled="!resume.cover_letter?.trim() || copying" @click="copyCoverLetter" />
                    </span>
                </div>
                <div v-if="resume.cover_letter?.trim()" class="whitespace-pre-wrap break-words p-4 text-sm leading-7 text-default sm:p-5">{{ resume.cover_letter }}</div>
                <div v-else class="px-4 py-10 text-center">
                    <UIcon name="i-lucide-mail-open" class="mb-3 size-6 text-muted" aria-hidden="true" />
                    <p class="text-sm text-muted">{{ t('jobMatchResult.noLetter') }}</p>
                </div>
                <p v-if="resume.cover_letter?.trim()" class="flex items-start gap-2 border-t border-default bg-primary/5 px-4 py-3 text-xs leading-5 text-muted sm:px-5">
                    <UIcon name="i-lucide-info" class="mt-0.5 size-3.5 shrink-0 text-primary" aria-hidden="true" />
                    {{ t('jobMatchResult.sendHint') }}
                </p>
            </section>
        </div>

        <div v-else class="rounded-xl border border-dashed border-default px-4 py-10 text-center">
            <UIcon name="i-lucide-file-search" class="mb-4 size-7 text-muted" aria-hidden="true" />
            <h2 class="text-lg font-semibold text-highlighted">{{ t('jobMatch.noResults') }}</h2>
            <p class="mt-2 text-sm text-muted">{{ t('jobMatchResult.notFoundHint') }}</p>
        </div>
    </UContainer>
</template>
