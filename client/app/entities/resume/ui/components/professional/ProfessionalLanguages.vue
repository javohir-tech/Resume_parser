<script setup lang="ts">
import type { Languages, LanguageDegree } from '~/entities/resume/models/types';
import { useResumeStore } from '~/entities/resume/models/store';

defineProps<{ item: Languages }>()
const resumeStore = useResumeStore()
const { t } = useI18n()
const proficiencyKeys: Record<Exclude<LanguageDegree, ''>, string> = {
  'Elementary proficiency': 'elementary',
  'Limited working proficiency': 'limited',
  'Professional working proficiency': 'professional',
  'Full professional proficiency': 'full',
  'Native or bilingual proficiency': 'native',
}
</script>

<template>
  <p class="pb-1.5 text-[13px] leading-[1.65] text-slate-900 break-inside-avoid">
    <strong class="font-semibold" :style="{ color: resumeStore.designInfo.entry_title_color?.hex }">{{ item.language }}</strong><span v-if="item.degree">: {{ t(`resumeDocument.proficiency.${proficiencyKeys[item.degree]}`) }}</span>
  </p>
</template>
