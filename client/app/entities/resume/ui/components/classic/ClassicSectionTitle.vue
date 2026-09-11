<script setup lang="ts">
import type { ResumeSection } from '~/entities/resume/models/types';
import { useResumeStore } from '~/entities/resume/models/store';
defineProps<{ section: ResumeSection }>()
const resumeStore = useResumeStore()
const labels: Record<ResumeSection, string> = {
  experience: 'Ish tajribasi', education: "Ta'lim", skills: "Ko'nikmalar", languages: "Tillar"
}
</script>
<template>
  <h2 class="text-sm font-bold uppercase tracking-wider border-b border-gray-400 mb-3 pb-1"
    :style="section === 'experience' ? { color: resumeStore.designInfo.heading_title_color?.hex, borderColor: resumeStore.designInfo.heading_title_color?.hex } : undefined">
    {{ labels[section] }}
  </h2>
</template>
