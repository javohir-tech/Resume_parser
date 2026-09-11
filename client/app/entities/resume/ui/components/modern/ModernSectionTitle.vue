<script setup lang="ts">
import type { ResumeSection } from '~/entities/resume/models/types';
import { useResumeStore } from '~/entities/resume/models/store';
defineProps<{ section: ResumeSection }>()
const resumeStore = useResumeStore()
const { t } = useI18n()
</script>
<template>
  <div class="pt-3 pb-2 break-after-avoid">
    <h2 class="text-[14px] leading-5 font-bold text-slate-900" :style="{ color: resumeStore.designInfo.heading_title_color?.hex }">{{ t(`resumeDocument.sections.${section}`) }}</h2>
  </div>
</template>

