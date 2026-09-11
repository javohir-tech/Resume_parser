<script setup lang="ts">
import type { SkillGroup } from '~/entities/resume/models/types';
import { useResumeStore } from '~/entities/resume/models/store';

defineProps<{ item: SkillGroup }>()
const resumeStore = useResumeStore()
</script>

<template>
  <p class="pb-1.5 text-[13px] leading-[1.65] text-neutral-900 break-inside-avoid">
    <strong v-if="item.title" class="font-semibold" :style="{ color: resumeStore.designInfo.entry_title_color?.hex }">{{ item.title }}<template v-if="item.skills.length">: </template></strong>
    <span>{{ item.skills.join(', ') }}</span>
  </p>
</template>
