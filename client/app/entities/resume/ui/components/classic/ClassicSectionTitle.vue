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
  <div class="pt-2 pb-2.5 break-after-avoid">
    <h2 class="border-b border-gray-300 pb-1.5 text-[11px] leading-5 font-bold uppercase tracking-[0.16em] text-gray-900"
      :style="{ color: resumeStore.designInfo.heading_title_color?.hex, borderColor: resumeStore.designInfo.heading_title_color?.hex }">
      {{ labels[section] }}
    </h2>
  </div>
</template>
