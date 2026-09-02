<!-- components/resume/ResumePage.vue -->
<script setup lang="ts">
</script>

<template>
    <div class="resume-page">
        <slot />
    </div>
</template>

<style scoped>
.resume-page {
    width: 210mm;
    min-height: 297mm;
    padding: 15mm;
    margin: 0 auto;
    background: white;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

@media print {
    .resume-page {
        box-shadow: none;
        margin: 0;
    }
}
</style>