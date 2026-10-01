<script setup lang="ts">
definePageMeta({
    layout: "resume-view" 
})

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

import { useGetResume } from '~/entities/resume';


const templates : Templates = {
    classic: ClassicTemplate,
    modern: ModernTemplate,
    minimal: MinimalTemplate,
    professional: ProfessionalTemplate,
    sidebar: SidebarTemplate
}

const resumeStore = useResumeStore()
const route = useRoute()
const resumeId = computed(() => route.params.id)
const selectedTemplate = computed(()=>templates[resumeStore.designInfo.template])
const {getResume} = useGetResume()

onMounted(async()=>{
    await getResume(String(resumeId.value))
})

onUnmounted(() => {
    resumeStore.restartInfo()
    resumeStore.restartDesign()
})
</script>

<template>
    <component :is="selectedTemplate.renderer || ResumeRenderer" :template="selectedTemplate" :resume="resumeStore.resume"/>
</template>
