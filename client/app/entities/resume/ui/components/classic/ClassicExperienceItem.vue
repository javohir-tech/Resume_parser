<script setup lang="ts">
import type { Experience } from '~/entities/resume/models/types';
defineProps<{ item: Experience }>()
</script>
<template>
    <div class="mb-4 last:mb-0 break-inside-avoid">
        <div class="flex justify-between items-baseline">
            <h3 class="font-bold text-sm">{{ item.position }}</h3>
            <span class="text-xs text-gray-500 whitespace-nowrap ml-2">{{ item.startDate }} — {{ item.endDate ||
                'Hozirgacha' }}</span>
        </div>
        <p class="text-sm text-gray-600 italic">{{ item.company }}<span v-if="item.location"> · {{ item.location
        }}</span></p>
        <p v-if="item.description" class="text-sm text-gray-800 whitespace-pre-line mt-1 leading-relaxed">{{
            item.description }}</p>
    </div>
</template>