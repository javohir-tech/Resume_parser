<script setup lang="ts">
import { useResumeStore } from '~/entities/resume/models/store';

defineProps<{ text?: string }>()
const resumeStore = useResumeStore()
const { t } = useI18n()
</script>
<template>
  <section v-if="text" class="pb-3">
    <h2 class="text-[14px] leading-5 font-bold text-slate-900" :style="{ color: resumeStore.designInfo.heading_title_color?.hex }">{{ t('resumeDocument.sections.summary') }}</h2>
    <p class="pt-2 text-[13px] leading-[1.65] whitespace-pre-line text-slate-800">{{ text }}</p>
  </section>
</template>

