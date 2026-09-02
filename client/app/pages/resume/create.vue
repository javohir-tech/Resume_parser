<script setup lang="ts">
import { ClassicResume, ModernResume, useResumeStore } from '~/entities/resume'

const templates = {
    classic: ClassicResume,
    modern: ModernResume
}
const selectedTemplate = ref<keyof typeof templates>("classic")
const resumeStore = useResumeStore()

definePageMeta({
    layout: "resume-editor"
})
</script>

<template>
    <div ref="containerRef" class="p-10 flex justify-center overflow-hidden">
            <component :is="templates[selectedTemplate]" :fullname="resumeStore.personalInfo.fullName" />
    </div>
</template>