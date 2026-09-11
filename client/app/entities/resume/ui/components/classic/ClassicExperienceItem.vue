<script setup lang="ts">
import type { Experience } from '~/entities/resume/models/types';
import { useResumeStore } from '~/entities/resume/models/store';
defineProps<{ item: Experience }>()
const resumeStore = useResumeStore()
const { t } = useI18n()
</script>
<template>
    <div class="pb-3.5 break-inside-avoid">
        <div class="flex justify-between items-baseline gap-4">
            <h3 class="min-w-0 text-[13px] leading-snug font-semibold text-gray-900" :style="{ color: resumeStore.designInfo.entry_title_color?.hex }">{{ item.position }}</h3>
            <span v-if="item.startDate || item.endDate" class="shrink-0 text-[10px] leading-5 tabular-nums text-gray-500">{{ item.startDate }}<template v-if="item.startDate"> — </template>{{ item.endDate || t('resumeDocument.present') }}</span>
        </div>
        <p v-if="item.company || item.location" class="mt-0.5 text-[12px] leading-relaxed text-gray-600">{{ item.company }}<span v-if="item.location"><template v-if="item.company"> · </template>{{ item.location
        }}</span></p>
        <p v-if="item.description" class="mt-1.5 text-[12px] leading-[1.7] whitespace-pre-line text-gray-700">{{
            item.description }}</p>
    </div>
</template>

