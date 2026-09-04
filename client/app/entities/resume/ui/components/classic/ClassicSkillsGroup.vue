<script setup lang="ts">
import type { SkillGroup } from '~/entities/resume/models/types';
defineProps<{ item: SkillGroup }>()
</script>
<template>
    <div class="mb-2 last:mb-0">
        <span class="text-sm font-bold">{{ item.title }}: </span>
        <span class="text-sm text-gray-800">{{ item.skills.join(', ') }}</span>
    </div>
</template>