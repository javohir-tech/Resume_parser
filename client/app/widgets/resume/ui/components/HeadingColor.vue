<script setup lang="ts">
import { useResumeStore } from '~/entities/resume';
import type { ResumeColor } from "~/entities/resume/models/store"

const resumeStore = useResumeStore()
const isColorPickerOpen = ref(false)

function selectColor(color: ResumeColor | null) {
    resumeStore.handleChangeColor(color)
    isColorPickerOpen.value = false
}

</script>

<template>
    <div class="section-header">
        <h1 id="title-color-label" class="text-sm font-medium mb-3">
            Section Heading Color
        </h1>
        <UPopover v-model:open="isColorPickerOpen" :content="{ align: 'start', side: 'left', sideOffset: 12 }">
            <UButton color="neutral" variant="outline" class="w-full">
                <span class="size-5 shrink-0 rounded-full bg-default ring-1 ring-inset ring-black/10 dark:ring-white/20"
                    :style="{ backgroundColor: resumeStore.designInfo.heading_title_color?.hex }">
                    <UIcon v-if="!resumeStore.designInfo.heading_title_color" name="i-lucide-palette"
                        class="m-1 size-3 text-muted" />
                </span>
                <span class="flex-1 text-left text-xs capitalize">
                    {{ resumeStore.designInfo.heading_title_color?.name || 'Default' }}
                </span>
                <UIcon name="i-lucide-chevron-down" class="size-3.5 text-muted transition-transform"
                    :class="{ 'rotate-180': isColorPickerOpen }" />
            </UButton>
            <template #content>
                <div class="p-4">
                    <p class="mb-3 text-xs font-medium text-muted">
                        Selected: <span class="capitalize">{{ resumeStore.designInfo.heading_title_color?.name ||
                            'Default'
                            }}</span>
                    </p>
                    <UButton color="neutral" variant="outline" size="sm" icon="i-lucide-rotate-ccw"
                        class="mb-3 w-full" :aria-pressed="resumeStore.designInfo.heading_title_color === null"
                        @click="selectColor(null)">
                        <span class="flex-1 text-left">Default</span>
                        <UIcon v-if="resumeStore.designInfo.heading_title_color === null" name="i-lucide-check" class="size-4" />
                    </UButton>
                    <div class="grid grid-cols-4 gap-2" role="group" aria-label="Title colors">
                        <button v-for="color in resumeStore.colorOptions" :key="color.hex" type="button"
                            :aria-label="`${color.name} (${color.hex})`" :title="color.name"
                            :aria-pressed="resumeStore.designInfo.heading_title_color?.hex === color.hex"
                            class="flex min-w-16 cursor-pointer flex-col items-center gap-1.5 rounded-lg px-2 py-2 transition-colors hover:bg-elevated focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary"
                            @click="selectColor(color)">
                            <span class="flex size-8 items-center justify-center rounded-full border border-black/10"
                                :class="{ 'ring-2 ring-primary ring-offset-2 ring-offset-default': resumeStore.designInfo.heading_title_color?.hex === color.hex }"
                                :style="{ backgroundColor: color.hex }">
                                <UIcon v-if="resumeStore.designInfo.heading_title_color?.hex === color.hex"
                                    name="i-lucide-check" class="size-4 text-white drop-shadow-md" />
                            </span>
                            <span class="text-xs capitalize">{{ color.name }}</span>
                        </button>
                    </div>
                </div>
            </template>
        </UPopover>
    </div>
</template>
