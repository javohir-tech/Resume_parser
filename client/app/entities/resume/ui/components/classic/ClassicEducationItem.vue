<script setup lang="ts">
import type { Education } from '~/entities/resume/models/types';
import { useResumeStore } from '~/entities/resume/models/store';
defineProps<{ item: Education }>()
const resumeStore = useResumeStore()
</script>
<template>
    <div class="pb-3.5 break-inside-avoid">
        <div class="flex justify-between items-baseline gap-4">
            <h3 class="min-w-0 text-[13px] leading-snug font-semibold text-gray-900" :style="{ color: resumeStore.designInfo.entry_title_color?.hex }">{{ item.degree }}</h3>
            <span v-if="item.startDate || item.endDate" class="shrink-0 text-[10px] leading-5 tabular-nums text-gray-500">{{ item.startDate }}<template v-if="item.startDate"> — </template>{{ item.endDate || 'Hozirgacha' }}</span>
        </div>
        <p v-if="item.institution || item.location" class="mt-0.5 text-[12px] leading-relaxed text-gray-600">{{ item.institution }}<span v-if="item.location"><template v-if="item.institution"> · </template>{{ item.location
        }}</span></p>
        <p v-if="item.fieldOfStudy" class="mt-1 text-[11px] leading-relaxed italic text-gray-500">{{ item.fieldOfStudy }}</p>
    </div>
</template>
