<script setup lang="ts">
import { ResumeRenderer, useResumeStore, ClassicTemplate, ModernTemplate, MinimalTemplate } from '~/entities/resume';
import type { Templates } from '~/entities/resume';

const templates: Templates = { classic: ClassicTemplate, modern: ModernTemplate, minimal: MinimalTemplate }
const resumeStore = useResumeStore()

definePageMeta({
    layout: "resume-editor"
})

</script>

<template>
    <ResumeRenderer :template="templates[resumeStore.template]" :resume="resumeStore.personalInfo" />
</template>
