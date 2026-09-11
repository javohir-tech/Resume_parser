<script setup lang="ts">
import type { Experience } from '~/entities/resume/models/types';
import { useResumeStore } from '~/entities/resume/models/store';
defineProps<{ item: Experience }>()
const resumeStore = useResumeStore()
const { t } = useI18n()
</script>
<template>
  <div class="pb-4 text-[13px] leading-[1.65] text-slate-800 break-inside-avoid">
    <div class="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-0.5">
      <h3 class="min-w-0 font-semibold" :style="{ color: resumeStore.designInfo.entry_title_color?.hex }">{{ item.position }}</h3>
      <p v-if="item.startDate || item.endDate" class="shrink-0 text-[12px] text-slate-600">{{ item.startDate }}<template v-if="item.startDate"> – </template>{{ item.endDate || t('resumeDocument.present') }}</p>
    </div>
    <p v-if="item.company || item.location">{{ item.company }}<template v-if="item.company && item.location">, </template>{{ item.location }}</p>
    <p v-if="item.description" class="mt-1.5 whitespace-pre-line">{{ item.description }}</p>
  </div>
</template>




