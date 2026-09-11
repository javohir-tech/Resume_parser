<script setup lang="ts">
import type { Education } from '~/entities/resume/models/types';
import { useResumeStore } from '~/entities/resume/models/store';
defineProps<{ item: Education }>()
const resumeStore = useResumeStore()
const { t } = useI18n()
</script>
<template>
  <div class="pb-4 text-[13px] leading-[1.65] text-slate-800 break-inside-avoid">
    <div class="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-0.5">
      <h3 class="min-w-0 font-semibold" :style="{ color: resumeStore.designInfo.entry_title_color?.hex }">{{ item.degree }}</h3>
      <p v-if="item.startDate || item.endDate" class="shrink-0 text-[12px] text-slate-600">{{ item.startDate }}<template v-if="item.startDate"> – </template>{{ item.endDate || t('resumeDocument.present') }}</p>
    </div>
    <p v-if="item.institution || item.location">{{ item.institution }}<template v-if="item.institution && item.location">, </template>{{ item.location }}</p>
    <p v-if="item.fieldOfStudy" class="mt-1">{{ item.fieldOfStudy }}</p>
  </div>
</template>



