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

import { useGetResume } from '~/entities/resume';

import { usePersonalAvtoSave } from '~/features/resume/edit-resume';

const { error, start,  flush } = usePersonalAvtoSave(800)

const ready = ref(false)

const {  getResume } = useGetResume()


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
const resumeId = computed(() => route.params.id)


definePageMeta({
    layout: "resume-editor" , 

    key : (route) => String(route.params.id)
})

onMounted(async () => {
    const success = await getResume(String(resumeId.value))

    if(success){
        ready.value = start()
    }
})

async function saveBeforeNavigation(){
    if(!ready.value) return true ;

    return await flush()
}

onBeforeRouteLeave(saveBeforeNavigation)

onBeforeRouteUpdate(async (to , from)=>{
    if(to.params.id !== from.params.id){
        return await saveBeforeNavigation()
    }
})

onUnmounted(() => {
    resumeStore.restartInfo()
    resumeStore.restartDesign()
})

</script>

<template>
    <component :is="selectedTemplate.renderer || ResumeRenderer" :template="selectedTemplate"
        :resume="resumeStore.resume" />
</template>
