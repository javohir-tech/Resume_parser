<script setup lang="ts">
import {
    ResumeRenderer,
    useResumeStore,
    ClassicTemplate,
    ModernTemplate,
    MinimalTemplate,
    ProfessionalTemplate,
    SidebarTemplate, 
    type Templates
} from '~/entities/resume';

import { useGetResume } from '~/features/resume';

const {loading , getResume} = useGetResume()


const templates: Templates = {
    classic: ClassicTemplate,
    modern: ModernTemplate,
    minimal: MinimalTemplate,
    professional: ProfessionalTemplate,
    sidebar: SidebarTemplate
}

const resumeStore = useResumeStore()
const selectedTemplate = computed(() => templates[resumeStore.template])
const route = useRoute()
const resumeId = computed(()=>route.params.id)


definePageMeta({
    layout: "resume-editor"
})

onMounted(()=>{
    getResume(String(resumeId.value))
})

onUnmounted(()=>{
    resumeStore.restartInfo()
    resumeStore.restartDesign()
})

</script>

<template>
    <component :is="selectedTemplate.renderer || ResumeRenderer" :template="selectedTemplate"
        :resume="resumeStore.resume" />
</template>
