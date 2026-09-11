<script setup lang="ts">
import { ResumeRenderer, useResumeStore, ClassicTemplate, ModernTemplate } from '~/entities/resume';

const templates = { classic: ClassicTemplate, modern: ModernTemplate }
const selectedTemplate = ref<keyof typeof templates>("modern")
const resumeStore = useResumeStore()

definePageMeta({
    layout : "resume-editor"
})

</script>

<template>
    <div class="flex justify-center gap-1 pt-5" role="group" aria-label="Resume template">
        <UButton v-for="name in (['classic', 'modern'] as const)" :key="name" color="neutral"
            :variant="selectedTemplate === name ? 'solid' : 'ghost'" size="sm" class="capitalize"
            :aria-pressed="selectedTemplate === name" @click="selectedTemplate = name">{{ name }}</UButton>
    </div>
    <ResumeRenderer :template="templates[selectedTemplate]" :resume="resumeStore.personalInfo"/>
</template> 
