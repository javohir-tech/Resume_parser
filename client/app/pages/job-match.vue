<script setup lang="ts">
import { getMyResumes } from '~/entities/resume';
import { useJobMatch } from '~/features/resume/job-match';

const search = ref("")
const { t } = useI18n()
const { jobMatchResume, loading, error_message } = useJobMatch()
const page = ref(1)
const debouncedSearch = refDebounced(search, 300)

const resumesKey = computed(() => `my_resumes_orginal_${debouncedSearch.value.trim()}_${page.value}`)

const selectedResumeId = ref<string>("")
const vacancy_text = ref<string>("")

const { data, status, error, refresh } = useLazyAsyncData(resumesKey, (_nuxtApp, { signal }) =>
    getMyResumes({ page: page.value, resume_type: "orginal", search: debouncedSearch.value.trim() || undefined }, signal), {
    server: false,
    default: () => ({
        count: 0,
        next: null,
        previous: null,
        results: []
    }),
    dedupe: "cancel"
}
)

const isLoading = computed(() => status.value === "idle" || status.value === "pending")

const handleSelectResume = (resume_id: string) => {
    if (!resume_id) return

    if (resume_id === selectedResumeId.value) {
        selectedResumeId.value = ""
    } else {
        selectedResumeId.value = resume_id
    }
}

const handleJobMatch = async (selected_resume_id: string, vacancy_text: string) => {
    if (!selected_resume_id || vacancy_text.length < 10 || vacancy_text.length > 1500) return

    await jobMatchResume(selected_resume_id, vacancy_text)

}


</script>

<template>
    <UContainer class="job-match py-8 sm:py-12 lg:py-14">
        <header class="mb-8 max-w-2xl sm:mb-10">
            <div
                class="mb-4 inline-flex items-center gap-2 rounded-full bg-primary/10 px-3 py-1.5 text-xs font-medium text-primary">
                <UIcon name="i-lucide-sparkles" class="size-3.5" aria-hidden="true" />
                {{ t('jobMatch.eyebrow') }}
            </div>
            <h1 class="text-3xl font-semibold tracking-tight text-highlighted sm:text-4xl">
                {{ t('jobMatch.title') }}
            </h1>
            <p class="mt-3 text-base leading-7 text-muted">
                {{ t('jobMatch.description') }}
            </p>
        </header>

        <div class="grid items-stretch gap-5 lg:grid-cols-5 lg:gap-6">
            <section class="match-panel min-w-0 lg:col-span-2" aria-labelledby="resume-heading">
                <div class="flex items-start gap-3">
                    <span class="step-number" aria-hidden="true">1</span>
                    <div>
                        <h2 id="resume-heading" class="text-lg font-semibold text-highlighted">{{
                            t('jobMatch.resumeHeading') }}</h2>
                        <p class="mt-1 text-sm leading-6 text-muted">{{ t('jobMatch.resumeHint') }}</p>
                    </div>
                </div>

                <label for="resume-search" class="sr-only">{{ t('jobMatch.searchLabel') }}</label>
                <UInput id="resume-search" v-model="search" :maxlength="255" icon="i-lucide-search"
                    :placeholder="t('jobMatch.searchPlaceholder')" size="lg" class="mt-6 w-full" />

                <div class="mt-4 min-h-64 lg:min-h-80" :aria-busy="isLoading">
                    <div v-if="isLoading" class="space-y-3" role="status" :aria-label="t('jobMatch.loading')">
                        <span class="sr-only">{{ t('jobMatch.loading') }}</span>
                        <div v-for="item in 3" :key="item"
                            class="flex items-center gap-3 rounded-xl border border-default p-4">
                            <USkeleton class="size-11 shrink-0 rounded-lg" />
                            <div class="flex-1 space-y-2.5">
                                <USkeleton class="h-3 w-3/4" />
                                <USkeleton class="h-3 w-1/2" />
                            </div>
                        </div>
                    </div>

                    <div v-else-if="error" class="empty-state rounded-xl bg-error/5" role="alert">
                        <UIcon name="i-lucide-cloud-off" class="mb-3 size-7 text-error" aria-hidden="true" />
                        <h3 class="font-medium text-highlighted">{{ t('jobMatch.loadError') }}</h3>
                        <p class="mt-2 text-sm leading-6 text-muted">{{ t('jobMatch.loadErrorHint') }}</p>
                        <UButton class="mt-4" icon="i-lucide-refresh-cw" color="neutral" variant="outline"
                            @click="refresh()">{{ t('jobMatch.retry') }}</UButton>
                    </div>

                    <div v-else-if="data.results?.length > 0" class="resume-list space-y-3" role="group"
                        aria-labelledby="resume-heading">
                        <button v-for="resume in data.results" :key="resume.id" type="button"
                            class="resume-option group flex w-full items-center gap-3 rounded-xl border p-4 text-left"
                            :class="selectedResumeId === resume.id ? 'border-primary bg-primary/5 ring-1 ring-primary' : 'border-default bg-default hover:border-primary/50 hover:bg-elevated/50'"
                            :aria-pressed="selectedResumeId === resume.id" @click="handleSelectResume(resume.id)">
                            <span class="flex size-11 shrink-0 items-center justify-center rounded-lg"
                                :class="selectedResumeId === resume.id ? 'bg-primary/10 text-primary' : 'bg-elevated text-muted'">
                                <UIcon name="i-lucide-file-user" class="size-5" aria-hidden="true" />
                            </span>
                            <span class="min-w-0 flex-1">
                                <span class="block break-words text-sm font-semibold text-highlighted">{{
                                    resume.fullname || t('jobMatch.untitled') }}</span>
                                <span class="resume-title mt-1 h-10 break-words text-sm leading-5 text-muted">{{
                                    resume.title ||
                                    t('jobMatch.noTitle') }}</span>
                            </span>
                            <span class="flex size-5 shrink-0 items-center justify-center rounded-full border"
                                :class="selectedResumeId === resume.id ? 'border-primary bg-primary text-inverted' : 'border-accented'">
                                <UIcon v-if="selectedResumeId === resume.id" name="i-lucide-check" class="size-3.5"
                                    aria-hidden="true" />
                            </span>
                        </button>
                    </div>


                    <div v-else class="empty-state rounded-xl border border-dashed border-default">
                        <span class="mb-4 flex size-12 items-center justify-center rounded-full bg-elevated">
                            <UIcon :name="search.trim() ? 'i-lucide-search-x' : 'i-lucide-files'"
                                class="size-6 text-muted" aria-hidden="true" />
                        </span>
                        <h3 class="font-medium text-highlighted">{{ search.trim() ? t('jobMatch.noResults') :
                            t('jobMatch.empty') }}</h3>
                        <p class="mt-2 max-w-64 text-sm leading-6 text-muted">
                            {{ search.trim() ? t('jobMatch.noResultsHint') : t('jobMatch.emptyHint') }}
                        </p>
                    </div>
                </div>

                <div v-if="data.results?.length > 0" class="mt-3 flex justify-center">
                    <UPagination v-model:page="page" :total="data.count" />
                </div>
            </section>

            <section class="match-panel flex min-w-0 flex-col lg:col-span-3" aria-labelledby="vacancy-heading">
                <div class="flex items-start gap-3">
                    <span class="step-number" aria-hidden="true">2</span>
                    <div>
                        <h2 id="vacancy-heading" class="text-lg font-semibold text-highlighted">
                            <label for="vacancy-text">{{ t('jobMatch.vacancyHeading') }}</label>
                        </h2>
                        <p id="vacancy-hint" class="mt-1 text-sm leading-6 text-muted">{{ t('jobMatch.vacancyHint') }}
                        </p>
                    </div>
                </div>

                <UTextarea id="vacancy-text" v-model="vacancy_text" class="mt-6 flex w-full flex-1" :minlength="10"
                    :maxlength="1500" :rows="12" size="lg" aria-describedby="vacancy-hint vacancy-length"
                    :placeholder="t('jobMatch.vacancyPlaceholder')"
                    :ui="{ root: 'flex flex-1 w-full', base: 'h-full min-h-72 w-full resize-y rounded-xl leading-7 lg:min-h-80' }" />

                <div id="vacancy-length"
                    class="mt-3 flex flex-wrap items-center justify-between gap-2 text-xs text-muted">
                    <span>{{ t('jobMatch.minimumLength', { min: 10 }) }}</span>
                    <span class="tabular-nums" :class="vacancy_text.length === 1500 ? 'font-medium text-warning' : ''">
                        {{ t('jobMatch.characterCount', { count: vacancy_text.length, max: '1 500' }) }}
                    </span>
                </div>
            </section>
        </div>

        <div class="my-5">
            <UAlert color="error" variant="soft" v-if="error_message" :description="error_message"
                icon="i-lucide-terminal" />
        </div>

        <footer
            class="mt-6 flex flex-col gap-4 rounded-2xl border border-default bg-muted/30 p-5 sm:flex-row sm:items-center sm:justify-between sm:px-6">
            <p class="flex items-start gap-2.5 text-sm leading-6 text-muted">
                <UIcon name="i-lucide-info" class="mt-0.5 size-5 shrink-0" aria-hidden="true" />
                {{ t('jobMatch.submitHint') }}
            </p>
            <UButton size="lg" icon="i-lucide-sparkles" class="w-full shrink-0 justify-center sm:w-auto"
                :disabled="!selectedResumeId || vacancy_text.length < 10 || vacancy_text.length > 1500 || loading"
                @click="handleJobMatch(selectedResumeId, vacancy_text)" :loading="loading">
                {{ t('jobMatch.submit') }}
            </UButton>
        </footer>
    </UContainer>
</template>

<style scoped>
.match-panel {
    padding: 1.5rem;
    border: 1px solid var(--ui-border);
    border-radius: 1rem;
    background: var(--ui-bg);
}

.step-number {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    width: 2rem;
    height: 2rem;
    border: 1px solid var(--ui-border-accented);
    border-radius: 0.625rem;
    background: var(--ui-bg-muted);
    color: var(--ui-text-highlighted);
    font-size: 0.875rem;
    font-weight: 600;
}

.resume-list {
    max-height: 20rem;
    overflow-y: auto;
    padding: 2px;
    scrollbar-width: thin;
}

.resume-option {
    cursor: pointer;
    transition: background-color 150ms, border-color 150ms, box-shadow 150ms;
}

.resume-title {
    display: -webkit-box;
    overflow: hidden;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
}

.resume-option:focus-visible {
    outline: 2px solid var(--ui-primary);
    outline-offset: 3px;
}

.empty-state {
    display: flex;
    min-height: 16rem;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 2rem 1rem;
    text-align: center;
}

@media (max-width: 639px) {
    .match-panel {
        padding: 1.25rem;
    }
}

@media (prefers-reduced-motion: reduce) {
    .resume-option {
        transition: none;
    }
}
</style>
