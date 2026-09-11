<script setup lang="ts">
import type { Resume } from '~/entities/resume/models/types';
import { useResumeStore } from '~/entities/resume/models/store';
defineProps<{ resume: Resume }>()
const resumeStore = useResumeStore()
</script>

<template>
  <header class="pb-6 break-inside-avoid">
    <h1 class="text-[30px] leading-tight font-bold" :style="{ color: resumeStore.designInfo.heading_title_color?.hex || '#1e3a5f' }">{{ resume.fullname }}</h1>
    <p v-if="resume.title" class="pt-2 text-[15px] leading-relaxed font-medium"
      :style="{ color: resumeStore.designInfo.entry_title_color?.hex || '#334155' }">{{ resume.title }}</p>
    <div class="mt-4 border-b-2" :style="{ borderColor: resumeStore.designInfo.heading_title_color?.hex || '#1e3a5f' }" aria-hidden="true" />
  </header>
</template>
