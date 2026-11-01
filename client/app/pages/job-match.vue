<script setup lang="ts">
import { getMyResumes } from '~/entities/resume';

const search = ref("")
const { t } = useI18n()

const debouncedSearch = refDebounced(search, 300)
const route = useRoute()

const resumesKey = computed(() => `my_resumes_orginal_${debouncedSearch.value.trim()}`)

const { data, status, error, refresh } = useLazyAsyncData(resumesKey, (_nuxtApp, { signal }) =>
    getMyResumes({ resume_type: "orginal", search: debouncedSearch.value.trim() || undefined }, signal), {
    server: false,
    default: () => [],
    dedupe: "cancel"
}
)

const isLoading = computed(() => status.value === "idle" || status.value === "pending")

</script>

<template>
    <UContainer class="flex min-h-[calc(100vh-4rem)] min-w-0 flex-col py-6 sm:py-10 lg:py-12">

        <header class="mb-8 max-w-2xl">
            <p class="font-semibold text-xs text-primary mb-3 uppercase tracking-[0.18em]">Yakuniy qadam shu yerda
            </p>
            <h1 class="font-semibold text-3xl sm:text-4xl mb-3 tracking-tight text-highlighted">Resumeni moslashtirish
            </h1>
            <p class="text-base text-muted">
                rezyumeingizni tanlang va vakansiyani kiriting AI rezyumeingizni vakansiyaga moslashtirip beradi
            </p>
        </header>

        <div class="mb-3 grid flex-1 grid-cols-1 lg:grid-cols-8 gap-4 ">
            <div class="flex flex-col bg-muted/40 lg:col-span-3 p-5 rounded-lg border-1 border-default">
                <h2 class="mb-3 font-semibold text-highlighted">
                    Resumelar
                </h2>
                <div class="mb-3">
                    <UInput v-model="search" icon="i-lucide-search" placeholder="Search..." class="block" />
                </div>

                <div v-if="data.length > 0" class="flex flex-col gap-2">
                    <div v-for="resume in data"
                        class="p-3 border rounded-md border-default border-2 duration-200 hover:ring-2 hover:ring-primary/40 hover:shadow-lg">
                        <p>{{ resume.fullname || t('resumeList.untitled') }}</p>
                        <p>{{ resume.title || t('resumeList.noTitle') }}</p>
                    </div>
                </div>

                <div v-else-if="isLoading" class="grid grid-cols-1 gap-4" role="status"
                    :aria-label="t('resumeList.loading')">
                    <div v-for="item in 3" :key="item" class="rounded-2xl border border-default p-3">
                        <USkeleton class="mb-2 size-6 rounded-xl" />
                        <USkeleton class="mb-2 h-3 w-2/3" />
                        <USkeleton class="h-2 w-1/2" />
                    </div>
                </div>

                <div v-else-if="error" class="rounded-2xl border border-error/20 bg-error/5 p-8 text-center">
                    <UIcon name="i-lucide-cloud-off" class="mb-3 size-8 text-error" />
                    <p class="text-sm text-error">{{ t('resumeList.loadError') }}</p>
                    <UButton class="mt-4" icon="i-lucide-refresh-cw" color="neutral" variant="outline"
                        @click="refresh()">{{
                            t('resumeList.retry') }}</UButton>
                </div>

                <div v-else
                    class="flex flex-col items-center rounded-2xl border border-dashed border-default px-6 py-10 text-center">
                    <UIcon name="i-lucide-files" class="mb-3 size-8 text-dimmed" />
                    <h3 class="font-medium text-highlighted">{{ t('resumeList.empty') }}</h3>
                </div>

            </div>
            <div class="flex flex-col bg-muted/40 lg:col-span-5 p-5 rounded-lg border-1 border-default">
                <h1 class="mb-3 font-semibold text-highlighted">Vakansiya tekstini shu joyga joylashtiring</h1>
                <UTextarea class="w-full flex-1"
                    :ui="{ root: 'flex flex-1 w-full', base: 'h-full w-full resize-none' }" />
            </div>
        </div>

        <div class="text-end">
            <UButton>Moslashtirish</UButton>
        </div>

    </UContainer>
</template>