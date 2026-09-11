<script setup lang="ts">
import type { Education } from '~/entities/resume/models/types';
import { useResumeStore } from '~/entities/resume/models/store';

defineProps<{ item: Education }>()
const resumeStore = useResumeStore()
const { t } = useI18n()
</script>

<template>
  <div class="pb-4 text-[13px] leading-[1.65] text-slate-900 break-inside-avoid">
    <h3 class="text-[14px] font-semibold" :style="{ color: resumeStore.designInfo.entry_title_color?.hex || '#0f172a' }">{{ item.degree }}</h3>
    <p v-if="item.institution || item.location" class="text-slate-700 font-medium">{{ item.institution }}<template v-if="item.institution && item.location">, </template>{{ item.location }}</p>
    <p v-if="item.startDate || item.endDate" class="text-[12px] text-slate-600">{{ item.startDate }}<template v-if="item.startDate"> – </template>{{ item.endDate || t('resumeDocument.present') }}</p>
    <p v-if="item.fieldOfStudy" class="pt-1.5">{{ item.fieldOfStudy }}</p>
  </div>
</template>
