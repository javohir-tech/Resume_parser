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

const containerRef = ref<HTMLElement | null>(null)
const scale = ref(1)

const PAGE_WIDTH_PX = 210 * 3.7795275591 // ~794px

function updateScale() {
    if (!containerRef.value) return
    const available = containerRef.value.clientWidth - 40 // padding hisobga olinadi
    scale.value = available < PAGE_WIDTH_PX
        ? Math.max(available / PAGE_WIDTH_PX, 0.3)
        : 1
}

onMounted(() => {
    updateScale()
    window.addEventListener('resize', updateScale)
})
onUnmounted(() => window.removeEventListener('resize', updateScale))

definePageMeta({
    layout: "resume-editor"
})
</script>

<template>
    <div ref="containerRef" class="p-10 flex justify-center overflow-x-auto border border-red-500">
        <div :style="{
            transform: `scale(${scale})`,
            transformOrigin: 'top center',
            marginBottom: `calc((1 - ${scale}) * -297mm)`
        }">
            <component :is="templates[selectedTemplate]" :fullname="resumeStore.personalInfo.fullname"
                :email="resumeStore.personalInfo.email" :phone="resumeStore.personalInfo.phone"
                :title="resumeStore.personalInfo.title" :summary="resumeStore.personalInfo.summary"
                :website="resumeStore.personalInfo.website" />
        </div>
    </div>
</template>