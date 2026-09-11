<script setup lang="ts">
import { ResumeRenderer, useResumeStore, ClassicTemplate, ModernTemplate, MinimalTemplate, ProfessionalTemplate, SidebarTemplate } from '~/entities/resume';
import type { Templates } from '~/entities/resume';

const templates: Templates = { classic: ClassicTemplate, modern: ModernTemplate, minimal: MinimalTemplate, professional: ProfessionalTemplate, sidebar: SidebarTemplate }
const resumeStore = useResumeStore()
const selectedTemplate = computed(() => templates[resumeStore.template])

definePageMeta({
    layout: "resume-editor"
})

</script>

<template>
    <component :is="selectedTemplate.renderer || ResumeRenderer" :template="selectedTemplate" :resume="resumeStore.personalInfo" />
</template>
