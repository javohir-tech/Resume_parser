<script setup lang="ts">
import { useResumeStore } from '~/entities/resume/models/store';

defineProps<{ text?: string }>()
const resumeStore = useResumeStore()
const { t } = useI18n()
</script>
<template>
  <section v-if="text" class="pb-4">
    <h2 class="border-b border-gray-300 pb-1.5 text-[11px] leading-5 font-bold uppercase tracking-[0.16em] text-gray-900"
      :style="{ color: resumeStore.designInfo.heading_title_color?.hex, borderColor: resumeStore.designInfo.heading_title_color?.hex }">
      {{ t('resumeDocument.sections.summary') }}
    </h2>
    <p class="pt-2.5 text-[12px] leading-[1.7] whitespace-pre-line text-gray-700">{{ text }}</p>
  </section>
</template>
