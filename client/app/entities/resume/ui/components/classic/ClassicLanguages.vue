<script setup lang="ts">
import type { Languages } from '~/entities/resume/models/types';
import { useResumeStore } from '~/entities/resume/models/store';

const resumeStore = useResumeStore()
const { t } = useI18n()
const proficiencyKeys: Record<string, string> = {
    'Elementary proficiency': 'elementary',
    'Limited working proficiency': 'limited',
    'Professional working proficiency': 'professional',
    'Full professional proficiency': 'full',
    'Native or bilingual proficiency': 'native',
}

defineProps<{
    item: Languages
}>()
</script>

<template>
    <div class="flex items-baseline justify-between gap-4 pb-2 text-[12px] leading-[1.7] break-inside-avoid">
        <span class="font-semibold text-gray-900" :style="{ color: resumeStore.designInfo.entry_title_color?.hex }">{{
            item.language }}</span>
        <span v-if="item.degree" class="text-right text-[11px] text-gray-600">
            {{ proficiencyKeys[item.degree] ? t(`resumeDocument.proficiency.${proficiencyKeys[item.degree]}`) :
                item.degree }}</span>
    </div>
</template>
