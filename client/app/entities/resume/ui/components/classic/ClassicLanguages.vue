<script setup lang="ts">
import type { Languages } from '~/entities/resume/models/types';

defineProps<{
    item: Languages
}>()
</script>

<template>
    <div class="mb-2 last:mb-0">
        <span class="text-sm font-bold">{{ item.language }}</span> : 
        <span class="text-sm text-gray-800">{{ item.degree }}</span>
    </div>
</template>