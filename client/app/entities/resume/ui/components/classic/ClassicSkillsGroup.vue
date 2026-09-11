<script setup lang="ts">
import type { SkillGroup } from '~/entities/resume/models/types';
import { useResumeStore } from '~/entities/resume/models/store';
defineProps<{ item: SkillGroup }>()
const resumeStore = useResumeStore()
</script>
<template>
    <div class="pb-2 text-[12px] leading-[1.7] break-inside-avoid">
        <span v-if="item.title" class="font-semibold text-gray-900" :style="{ color: resumeStore.designInfo.entry_title_color?.hex }">{{ item.title }}<template v-if="item.skills.length">: </template></span>
        <span class="text-gray-700">{{ item.skills.join(', ') }}</span>
    </div>
</template>
