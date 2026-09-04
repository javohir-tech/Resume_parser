<template>
  <div class="resume-page font-serif text-gray-900">
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
  overflow-wrap: break-word;
  word-break: break-word;
}
</style>