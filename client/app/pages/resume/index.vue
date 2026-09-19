<script setup lang="ts">
import { useResume } from '~/features/resume';
import { getMyResumes } from '~/entities/resume/api';

const { loading, createResume } = useResume()

const { data, pending, error, refresh } = useLazyAsyncData("my_resumes", () => getMyResumes())
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
        <div v-else v-for="resume in data" :key="resume.id">
            <p>{{ resume.fullname || "resume" }}</p>
            <p>{{ resume.title || "resume_title" }}</p>
            
        </div>
        <p>{{ data?.length }}</p>
    </UContainer>
</template>