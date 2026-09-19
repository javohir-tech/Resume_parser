<script setup lang="ts">
import { useResume } from '~/features/resume';
import { getMyResumes } from '~/entities/resume/api';
import { ResumeCard } from '~/entities/resume';

const { loading, createResume, deleteResume, isDeleting } = useResume()

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
                Resume yaratish
            </UButton>
            <div class="space-y-2">
                <label for="resume-upload" class="block text-sm font-medium">Resume yuklash</label>
                <input id="resume-upload" type="file"
                    class="block w-full rounded-lg border border-default p-2 text-sm file:mr-3 file:rounded-md file:border-0 file:bg-elevated file:px-3 file:py-1 file:text-default" />
            </div>
        </div>

        <h1 class="text-2xl font-semibold">Resumelarim</h1>

        <div v-if="pending">Yuklanmoqda...</div>
        <div v-else-if="error">Resumelarni yuklashda xatolik yuz berdi</div>
        <div v-else-if="!data?.length">Hozircha resume yo'q</div>
        <div v-else class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            <ResumeCard v-for="resume in data" :key="resume.id" :fullname="resume.fullname" :title="resume.title"
                :loading="isDeleting(resume.id)" @delete="removeResume(resume.id)" />
        </div>

    </UContainer>
</template>