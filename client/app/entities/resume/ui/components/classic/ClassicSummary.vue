<script setup lang="ts">
import { useResumeStore } from '~/entities/resume/models/store';

defineProps<{ text?: string }>()
const resumeStore = useResumeStore()
</script>
<template>
  <section v-if="text" class="mb-6" :style="{ fontFamily: resumeStore.designInfo.heading_font}">
    <h2 class="text-sm font-bold uppercase tracking-wider border-b mb-2 pb-1"
      :style="{ color: resumeStore.designInfo.title_color, borderColor: resumeStore.designInfo.title_color }">
      Malumot
    </h2>
    <p class="text-sm leading-relaxed text-gray-800">{{ text }}</p>
  </section>
</template>
