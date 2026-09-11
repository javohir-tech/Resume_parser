<script setup lang="ts">
import { useResumeStore } from '~/entities/resume/models/store';

defineProps<{ text?: string }>()
const resumeStore = useResumeStore()
const { t } = useI18n()
</script>

<template>
  <section v-if="text" class="pb-3 text-neutral-900">
    <h2 class="border-b border-neutral-300 pb-1 text-[13px] leading-5 font-semibold"
      :style="{ color: resumeStore.designInfo.heading_title_color?.hex }">{{ t('resumeDocument.sections.summary') }}</h2>
    <p class="pt-2 text-[13px] leading-[1.65] whitespace-pre-line">{{ text }}</p>
  </section>
</template>
