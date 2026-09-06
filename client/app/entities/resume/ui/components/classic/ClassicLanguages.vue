<script setup lang="ts">
import type { Languages } from '~/entities/resume/models/types';

defineProps<{
    item: Languages
}>()
</script>

<template>
    <div class="flex gap-1">
        salom 
        <p class="text-gray-500">{{ item.language }}</p>
        <p>{{ item.degree }}</p>
    </div>
</template>