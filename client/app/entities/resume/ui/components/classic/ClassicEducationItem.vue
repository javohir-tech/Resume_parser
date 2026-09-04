<script setup lang="ts">
import type { Education } from '~/entities/resume/models/types';
defineProps<{ item: Education }>()
</script>
<template>
    <div class="mb-3 last:mb-0 break-inside-avoid">
        <div class="flex justify-between items-baseline">
            <h3 class="font-bold text-sm">{{ item.degree }}</h3>
            <span class="text-xs text-gray-500 whitespace-nowrap ml-2">{{ item.startDate }} — {{ item.endDate ||
                'Hozirgacha' }}</span>
        </div>
        <p class="text-sm text-gray-600 italic">{{ item.institution }}<span v-if="item.location"> · {{ item.location
                }}</span></p>
    </div>
</template>