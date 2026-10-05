<script setup lang="ts">

import {
    PaginatedResume,
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
import { useEditDesign } from '~/features/resume/design-edit';

definePageMeta({
    middleware: "auth",
    layout: "resume-editor",

    key: (route) => String(route.params.id)
})

const { start, flush } = usePersonalAvtoSave(800)
const { start: startDesign, flush: flushDesign } = useEditDesign(800)

const ready = ref(false)

const { getResume } = useGetResume()


const templates: Templates = {
    classic: ClassicTemplate,
    modern: ModernTemplate,
    minimal: MinimalTemplate,
    professional: ProfessionalTemplate,
    sidebar: SidebarTemplate
}

const resumeStore = useResumeStore()
const selectedTemplate = computed(() => templates[resumeStore.designInfo.template ?? 'classic'])
const route = useRoute()
const resumeId = computed(() => route.params.id)

onMounted(async () => {
    const success = await getResume(String(resumeId.value))

    if (success) {
        const personalReady = start()
        const designReady = startDesign()
        ready.value = personalReady && designReady
    }
})

async function saveBeforeNavigation() {
    if (!ready.value) return true;

    const results = await Promise.all([flush(), flushDesign()])
    return results.every(Boolean)
}

onBeforeRouteLeave(saveBeforeNavigation)

onBeforeRouteUpdate(async (to, from) => {
    if (to.params.id !== from.params.id) {
        return await saveBeforeNavigation()
    }
})

onUnmounted(() => {
    resumeStore.restartInfo()
    resumeStore.restartDesign()
})

</script>

<template>
    <component :is="selectedTemplate.renderer || PaginatedResume" :template="selectedTemplate"
        :resume="resumeStore.resume" />
</template>
