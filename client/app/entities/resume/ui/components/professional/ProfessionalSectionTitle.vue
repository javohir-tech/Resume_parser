<script setup lang="ts">
import type { ResumeSection } from '~/entities/resume/models/types';
import { useResumeStore } from '~/entities/resume/models/store';

defineProps<{ section: ResumeSection }>()
const resumeStore = useResumeStore()
const { t } = useI18n()
</script>

<template>
  <div class="pt-2 pb-2.5 break-after-avoid">
    <h2 class="border-b border-slate-300 pb-1.5 text-[14px] leading-5 font-bold"
      :style="{ color: resumeStore.designInfo.heading_title_color?.hex || '#1e3a5f' }">{{ t(`resumeDocument.sections.${section}`) }}</h2>
  </div>
</template>
