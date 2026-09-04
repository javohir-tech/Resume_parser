<script setup lang="ts">
import { ResumeRenderer, useResumeStore, ClassicTemplate } from '~/entities/resume';

const templates = { classic: ClassicTemplate }
const selectedTemplate = ref<keyof typeof templates>("classic")
const resumeStore = useResumeStore()
</script>

<template>
    <ResumeRenderer :template="templates[selectedTemplate]" :resume="resumeStore.personalInfo"/>
</template>