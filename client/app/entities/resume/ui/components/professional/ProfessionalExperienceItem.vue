<script setup lang="ts">
import type { Experience } from '~/entities/resume/models/types';
import { useResumeStore } from '~/entities/resume/models/store';

defineProps<{ item: Experience }>()
const resumeStore = useResumeStore()
const { t } = useI18n()
</script>

<template>
  <div class="pb-4 text-[13px] leading-[1.65] text-slate-900 break-inside-avoid">
    <h3 class="text-[14px] font-semibold" :style="{ color: resumeStore.designInfo.entry_title_color?.hex || '#0f172a' }">{{ item.position }}</h3>
    <p v-if="item.company || item.location" class="text-slate-700 font-medium">{{ item.company }}<template v-if="item.company && item.location">, </template>{{ item.location }}</p>
    <p v-if="item.startDate || item.endDate" class="text-[12px] text-slate-600">{{ item.startDate }}<template v-if="item.startDate"> – </template>{{ item.endDate || t('resumeDocument.present') }}</p>
    <p v-if="item.description" class="pt-1.5 whitespace-pre-line">{{ item.description }}</p>
  </div>
</template>
