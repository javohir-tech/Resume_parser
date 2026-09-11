<script setup lang="ts">
import { useResumeStore , type ResumeColor , colorOptions } from '~/entities/resume';
import { useMediaQuery } from '@vueuse/core';

const resumeStore = useResumeStore()
const isColorPickerOpen = ref(false)
const isDesktop = useMediaQuery('(min-width: 1024px)')

function selectColor(color: ResumeColor | null) {
    resumeStore.handleChangeEntryTitleColor(color)
    isColorPickerOpen.value = false
}

</script>

<template>
    <div class="entry-title-color">
        <h1 id="entry-title-color-label" class="text-sm font-medium mb-3">
            Entry Title Color
        </h1>
        <UPopover v-model:open="isColorPickerOpen"
            :content="{ align: 'start', side: isDesktop ? 'left' : 'bottom', sideOffset: 8, collisionPadding: 12 }"
            :ui="{ content: 'w-80 max-w-[calc(100vw-1.5rem)] max-h-(--reka-popover-content-available-height) overflow-y-auto' }">
            <UButton color="neutral" variant="outline" aria-labelledby="entry-title-color-label" class="w-full">
                <span class="size-5 shrink-0 rounded-full bg-default ring-1 ring-inset ring-black/10 dark:ring-white/20"
                    :style="{ backgroundColor: resumeStore.designInfo.entry_title_color?.hex }">
                    <UIcon v-if="!resumeStore.designInfo.entry_title_color" name="i-lucide-palette"
                        class="m-1 size-3 text-muted" />
                </span>
                <span class="flex-1 text-left text-xs capitalize">
                    {{ resumeStore.designInfo.entry_title_color?.name || 'Default' }}
                </span>
                <UIcon name="i-lucide-chevron-down" class="size-3.5 text-muted transition-transform"
                    :class="{ 'rotate-180': isColorPickerOpen }" />
            </UButton>
            <template #content>
                <div class="p-4">
                    <p class="mb-3 text-xs font-medium text-muted">
                        Selected: <span class="capitalize">{{ resumeStore.designInfo.entry_title_color?.name ||
                            'Default'
                            }}</span>
                    </p>
                    <UButton color="neutral" variant="outline" size="sm" icon="i-lucide-rotate-ccw"
                        class="mb-3 w-full" :aria-pressed="resumeStore.designInfo.entry_title_color === null"
                        @click="selectColor(null)">
                        <span class="flex-1 text-left">Default</span>
                        <UIcon v-if="resumeStore.designInfo.entry_title_color === null" name="i-lucide-check" class="size-4" />
                    </UButton>
                    <div class="grid grid-cols-4 gap-2" role="group" aria-label="Entry title colors">
                        <button v-for="color in colorOptions" :key="color.hex" type="button"
                            :aria-label="`${color.name} (${color.hex})`" :title="color.name"
                            :aria-pressed="resumeStore.designInfo.entry_title_color?.hex === color.hex"
                            class="flex min-w-0 cursor-pointer flex-col items-center gap-1.5 rounded-lg px-1 py-2 transition-colors hover:bg-elevated focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary"
                            @click="selectColor(color)">
                            <span class="flex size-8 items-center justify-center rounded-full border border-black/10"
                                :class="{ 'ring-2 ring-primary ring-offset-2 ring-offset-default': resumeStore.designInfo.entry_title_color?.hex === color.hex }"
                                :style="{ backgroundColor: color.hex }">
                                <UIcon v-if="resumeStore.designInfo.entry_title_color?.hex === color.hex"
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
