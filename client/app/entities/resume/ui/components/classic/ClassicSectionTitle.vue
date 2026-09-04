<script setup lang="ts">
import type { ResumeSection } from '~/entities/resume/models/types';
defineProps<{ section: ResumeSection }>()
const labels: Record<ResumeSection, string> = {
  experience: 'Ish tajribasi', education: "Ta'lim", skills: "Ko'nikmalar",
}
</script>
<template>
  <h2 class="text-sm font-bold uppercase tracking-wider border-b border-gray-400 mb-3 pb-1">
    {{ labels[section] }}
  </h2>
</template>