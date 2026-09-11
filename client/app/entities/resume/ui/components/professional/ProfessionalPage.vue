<script setup lang="ts">
import { useResumeStore } from '~/entities/resume/models/store';

const resumeStore = useResumeStore()
</script>

<template>
  <div class="resume-page" :style="{ fontFamily: `${resumeStore.designInfo.font}, Arial, sans-serif` }">
    <slot />
  </div>
</template>

<style scoped>
.resume-page {
  box-sizing: border-box;
  width: 210mm;
  min-height: 297mm;
  padding: 15mm;
  background: white;
  color: #0f172a;
  font-size: 12px;
  line-height: 1.7;
  overflow-wrap: break-word;
  word-break: break-word;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
</style>
