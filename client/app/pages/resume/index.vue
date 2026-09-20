<script setup lang="ts">
import { useResume , useCreateResume } from '~/features/resume';
import { getMyResumes } from '~/entities/resume/api';
import { ResumeCard } from '~/entities/resume';

const { t } = useI18n()
const selectedFileName = ref('')
const onFileChange = (event: Event) => {
    selectedFileName.value = (event.target as HTMLInputElement).files?.[0]?.name ?? ''
}

const {  deleteResume, isDeleting } = useResume()
const {loading , createResume} = useCreateResume()
const { data, pending, error, refresh } = useLazyAsyncData("my_resumes", () => getMyResumes())

const removeResume = async (id: string) => {
    await deleteResume(id)
    data.value = data.value?.filter(r => r.id !== id)
}

</script>

<template>
    <UContainer class="space-y-8 py-10">

        <div class="flex flex-wrap items-end gap-4">
            <UButton @click="createResume" icon="i-lucide-plus" size="lg" :loading="loading" :disabled="loading">
                {{ t('resumeList.create') }}
            </UButton>
            <div class="space-y-2">
                <label for="resume-upload" class="block text-sm font-medium">{{ t('resumeList.upload') }}</label>
                <div class="relative flex items-center gap-3 rounded-lg border border-default p-2 text-sm focus-within:ring-2 focus-within:ring-primary">
                    <input id="resume-upload" type="file" class="absolute inset-0 h-full w-full cursor-pointer opacity-0"
                        :aria-label="t('resumeList.upload')" @change="onFileChange" />
                    <span class="rounded-md bg-elevated px-3 py-1">{{ t('resumeList.chooseFile') }}</span>
                    <span aria-live="polite">{{ selectedFileName || t('resumeList.noFile') }}</span>
                </div>
            </div>
        </div>

        <h1 class="text-2xl font-semibold">{{ t('resumeList.title') }}</h1>

        <div v-if="pending">{{ t('resumeList.loading') }}</div>
        <div v-else-if="error">{{ t('resumeList.loadError') }}</div>
        <div v-else-if="!data?.length">{{ t('resumeList.empty') }}</div>
        <div v-else class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            <ResumeCard v-for="resume in data" :key="resume.id" :id="resume.id" :fullname="resume.fullname" :title="resume.title"
                :loading="isDeleting(resume.id)" @delete="removeResume(resume.id)" />
        </div>

    </UContainer>
</template>
