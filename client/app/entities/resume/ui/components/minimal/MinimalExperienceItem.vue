<script setup lang="ts">
import type { Experience } from '~/entities/resume/models/types';
import { useResumeStore } from '~/entities/resume/models/store';

defineProps<{ item: Experience }>()
const resumeStore = useResumeStore()
const { t } = useI18n()
</script>

<template>
  <div class="pb-3 text-[13px] leading-[1.65] text-neutral-900 break-inside-avoid">
    <div class="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-0.5">
      <h3 class="min-w-0 font-semibold" :style="{ color: resumeStore.designInfo.entry_title_color?.hex }">{{ item.position }}</h3>
      <p v-if="item.startDate || item.endDate" class="shrink-0 text-[12px] text-neutral-600">{{ item.startDate }}<template v-if="item.startDate"> – </template>{{ item.endDate || t('resumeDocument.present') }}</p>
    </div>
    <p v-if="item.company || item.location" class="text-neutral-700">{{ item.company }}<template v-if="item.company && item.location">, </template>{{ item.location }}</p>
    <p v-if="item.description" class="pt-1 whitespace-pre-line">{{ item.description }}</p>
  </div>
</template>
