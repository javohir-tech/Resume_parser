<script setup lang="ts">
import { useResumeStore } from '~/entities/resume/models/store';

const resumeStore = useResumeStore()
</script>

<template>
  <div class="resume-page text-slate-900" :style="{fontFamily : resumeStore.designInfo.font}">
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
  color: #111827;
  font-size: 12px;
  line-height: 1.7;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
  overflow-wrap: break-word;
  word-break: break-word;
}
</style>

