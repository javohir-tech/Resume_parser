<script setup lang="ts">
import Classic from '~/components/resume/Classic.vue';
import Modern from '~/components/resume/Modern.vue';


const templates = {
    classic: Classic,
    modern: Modern
}
const selectedTemplate = ref<keyof typeof templates>("classic")

const resumeStore = useResumeStore()

definePageMeta({
    layout: "resume-editor"
})
</script>

<template>
    <div class="p-10">
        <component :is="templates[selectedTemplate]" :fullname="resumeStore.personalInfo.fullName" />
    </div>
</template>