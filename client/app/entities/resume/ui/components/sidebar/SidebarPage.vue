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
  background: linear-gradient(to right, #f1f5f9 0, #f1f5f9 74mm, white 74mm, white 100%);
  color: #0f172a;
  font-size: 12px;
  line-height: 1.7;
  overflow-wrap: break-word;
  word-break: break-word;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
@media print {
  .resume-page { width: auto; min-height: 0; padding: 0; background: white; }
}
</style>
