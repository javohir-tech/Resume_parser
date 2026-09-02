<script setup lang="ts">
import { defineAsyncComponent } from 'vue'
import { useResumeStore } from '~/entities/resume'

const templates = {
    classic: defineAsyncComponent(() =>
        import("~/entities/resume/ui/components/Classic.vue")
    ),
    modern: defineAsyncComponent(() =>
        import("~/entities/resume/ui/components/Modern.vue")
    )
}
const selectedTemplate = ref<keyof typeof templates>("classic")
const resumeStore = useResumeStore()

definePageMeta({
    layout: "resume-editor"
})
</script>

<template>
    <div ref="containerRef" class="p-10 flex justify-center overflow-hidden">
        <component :is="templates[selectedTemplate]" :fullname="resumeStore.personalInfo.fullname"
            :email="resumeStore.personalInfo.email" :phone="resumeStore.personalInfo.phone"
            :title="resumeStore.personalInfo.title"
            :summary="resumeStore.personalInfo.summary"
            :website="resumeStore.personalInfo.website"
            />
    </div>
</template>