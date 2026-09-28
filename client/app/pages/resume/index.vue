<script setup lang="ts">
import { ResumeCard, getMyResumes } from '~/entities/resume'
import { useDeleteResume } from '~/features/resume/delete-resume'
import { useCreateResume } from '~/features/resume/create-resume'
import { ParseResumeForm } from '~/features/resume/parse-resume'

const { t } = useI18n()
const method = ref<'upload' | 'manual'>('upload')
const { deleteResume, isDeleting } = useDeleteResume()
const { loading, createResume } = useCreateResume()
const { data, pending, error } = useLazyAsyncData('my_resumes', () => getMyResumes())

const removeResume = async (id: string) => {
    const success = await deleteResume(id)
    if(success){
        data.value = data.value?.filter(r => r.id !== id)
    }
}
</script>

<template>
    <UContainer class="py-6 sm:py-10 lg:py-12">

        <header class="mb-8 max-w-2xl">
            <p class="mb-3 text-xs font-semibold uppercase tracking-[0.18em] text-primary">{{
                t('resumeWorkspace.eyebrow') }}</p>
            <h1 class="text-3xl font-semibold tracking-tight text-highlighted sm:text-4xl">{{ t('resumeWorkspace.title')
                }}</h1>
            <p class="mt-3 text-base leading-relaxed text-muted">{{ t('resumeWorkspace.description') }}</p>
        </header>

        <section class="overflow-hidden rounded-3xl border border-default bg-default"
            :aria-label="t('resumeWorkspace.newResume')">
            <div class="grid lg:grid-cols-[0.85fr_1.15fr]">
                <div class="border-b border-default bg-muted/40 p-5 sm:p-8 lg:border-r lg:border-b-0">

                    <div class="mb-6 flex items-center gap-3">
                        <span
                            class="flex size-9 items-center justify-center rounded-full bg-primary/10 text-sm font-semibold text-primary">01</span>
                        <h2 class="font-semibold text-highlighted">{{ t('resumeWorkspace.chooseMethod') }}</h2>
                    </div>

                    <div class="space-y-3">
                        <button v-for="option in (['upload', 'manual'] as const)" :key="option" type="button"
                            :aria-pressed="method === option" :disabled="loading"
                            class="flex w-full items-start gap-4 rounded-2xl border p-4 text-left transition focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-primary disabled:cursor-wait sm:p-5"
                            :class="method === option ? 'border-primary bg-default shadow-sm ring-1 ring-primary' : 'border-default bg-default/60 hover:border-primary/40 hover:bg-default'"
                            @click="method = option">

                            <span class="flex size-11 shrink-0 items-center justify-center rounded-xl"
                                :class="method === option ? 'bg-primary/10 text-primary' : 'bg-muted text-muted'">
                                <UIcon :name="option === 'upload' ? 'i-lucide-file-up' : 'i-lucide-file-pen-line'"
                                    class="size-5" />
                            </span>
                            <span class="min-w-0 flex-1">
                                <span class="block font-semibold text-highlighted">{{
                                    t(`resumeWorkspace.${option}Title`) }}</span>
                                <span class="mt-1 block text-sm leading-relaxed text-muted">{{
                                    t(`resumeWorkspace.${option}Description`) }}</span>
                            </span>
                            <UIcon :name="method === option ? 'i-lucide-circle-check' : 'i-lucide-circle'"
                                class="mt-1 size-5 shrink-0"
                                :class="method === option ? 'text-primary' : 'text-dimmed'" />

                        </button>
                    </div>

                    <p class="mt-6 flex items-start gap-2 text-xs leading-relaxed text-muted">
                        <UIcon name="i-lucide-pencil-line" class="mt-0.5 size-4 shrink-0" />
                        {{ t('resumeWorkspace.editHint') }}
                    </p>

                </div>

                <div class="p-5 sm:p-8">
                    <div class="mb-6 flex items-center gap-3">
                        <span
                            class="flex size-9 items-center justify-center rounded-full bg-primary/10 text-sm font-semibold text-primary">02</span>
                        <h2 class="grid font-semibold text-highlighted">
                            <span class="col-start-1 row-start-1" :class="{ invisible: method !== 'upload' }"
                                :aria-hidden="method !== 'upload'">{{ t('resumeWorkspace.uploadStep') }}</span>
                            <span class="col-start-1 row-start-1" :class="{ invisible: method !== 'manual' }"
                                :aria-hidden="method !== 'manual'">{{ t('resumeWorkspace.manualStep') }}</span>
                        </h2>
                    </div>

                    <div class="grid">
                        <div class="col-start-1 row-start-1 min-w-0" :class="{ invisible: method !== 'upload' }"
                            :inert="method !== 'upload'" :aria-hidden="method !== 'upload'">
                            <ParseResumeForm />
                        </div>

                        <div v-if="method === 'manual'"
                            class="col-start-1 row-start-1 flex min-h-72 min-w-0 flex-col items-center justify-center rounded-2xl border border-dashed border-default bg-muted/30 px-5 py-8 text-center">
                            <span
                                class="mb-4 flex size-14 items-center justify-center rounded-2xl bg-default text-primary shadow-sm">
                                <UIcon name="i-lucide-file-plus-2" class="size-7" />
                            </span>
                            <h3 class="text-lg font-semibold text-highlighted">{{ t('resumeWorkspace.blankTitle') }}
                            </h3>
                            <p class="mt-2 max-w-sm text-sm leading-relaxed text-muted">{{
                                t('resumeWorkspace.blankDescription') }}</p>
                            <UButton class="mt-6" size="lg" icon="i-lucide-plus" :loading="loading" :disabled="loading"
                                @click="createResume">{{ t('resumeWorkspace.startBlank') }}</UButton>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="mt-12" aria-labelledby="resume-list-title">
            <div class="mb-5 flex items-center gap-3">
                <h2 id="resume-list-title" class="text-xl font-semibold tracking-tight text-highlighted">{{
                    t('resumeList.title') }}</h2>
                <UBadge v-if="!pending && !error" color="neutral" variant="subtle" class="rounded-full">{{ data?.length
                    ?? 0 }}</UBadge>
            </div>
            <div v-if="pending" class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3" role="status"
                :aria-label="t('resumeList.loading')">
                <div v-for="item in 3" :key="item" class="rounded-2xl border border-default p-6">
                    <USkeleton class="mb-4 size-10 rounded-xl" />
                    <USkeleton class="mb-2 h-5 w-2/3" />
                    <USkeleton class="h-4 w-1/2" />
                </div>
            </div>
            <div v-else-if="error" class="rounded-2xl border border-error/20 bg-error/5 p-8 text-center" role="alert">
                <p class="text-sm text-error">{{ t('resumeList.loadError') }}</p>
            </div>
            <div v-else-if="!data?.length"
                class="flex flex-col items-center rounded-2xl border border-dashed border-default px-6 py-10 text-center">
                <UIcon name="i-lucide-files" class="mb-3 size-8 text-dimmed" />
                <h3 class="font-medium text-highlighted">{{ t('resumeList.empty') }}</h3>
                <p class="mt-2 max-w-md text-sm text-muted">{{ t('resumeWorkspace.emptyHint') }}</p>
            </div>
            <div v-else class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
                <ResumeCard v-for="resume in data" :key="resume.id" :id="resume.id" :fullname="resume.fullname"
                    :title="resume.title" :loading="isDeleting(resume.id)" @delete="removeResume(resume.id)" />
            </div>
        </section>
    </UContainer>
</template>
