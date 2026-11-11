<script setup lang="ts">
import useNeutralColor from '../models/useNeutralColor';
import { colors } from '../models/colors';
const { t } = useI18n()

const { neutral, setNeutralColor } = useNeutralColor()
const isOpen = ref(false)
const selectedColor = computed(() => neutral.value || 'slate')

const swatchClasses: Record<string, string> = {
    slate: 'bg-slate-500',
    gray: 'bg-gray-500',
    zinc: 'bg-zinc-500',
    neutral: 'bg-neutral-500',
    stone: 'bg-stone-500',
    taupe: "bg-taupe-500",
    mauve: "bg-mauve-500",
    mist: "bg-mist-500",
    olive: "bg-olive-500"
}

function selectColor(color: typeof colors[number]) {
    setNeutralColor(color)
    isOpen.value = false
}
</script>

<template>
    <div class="flex flex-wrap items-center justify-between gap-3 py-1.5">

        <h2 class="text-sm font-medium text-highlighted">{{ t('settings.appearance.neutralColor') }}</h2>

        <UPopover v-model:open="isOpen" :content="{ align: 'end', sideOffset: 6, collisionPadding: 16 }"
            :ui="{ content: 'w-52 max-w-[calc(100vw-2rem)] overflow-hidden rounded-lg bg-default text-default ring-1 ring-default' }">

            <UButton color="neutral" variant="ghost" size="sm"
                :aria-label="t('settings.appearance.chooseNeutralColor', { color: selectedColor })"
                class="shrink-0 justify-between gap-2 rounded-lg px-2 py-1.5">
                <span class="size-3.5 shrink-0 rounded-full" :class="swatchClasses[selectedColor] || 'bg-neutral-500'"
                    aria-hidden="true" />
                <span class="text-left text-xs font-medium capitalize">{{ selectedColor }}</span>
                <UIcon name="i-lucide-chevron-down" class="size-3.5 text-muted motion-safe:transition-transform"
                    :class="{ 'rotate-180': isOpen }" aria-hidden="true" />
            </UButton>

            <template #content>
                <div class="max-h-[min(30rem,var(--reka-popover-content-available-height))] overflow-y-auto p-1">
                    <div class="flex flex-col gap-0.5" role="group" :aria-label="t('settings.appearance.neutralColors')">
                        <button v-for="color in colors" :key="color" type="button"
                            :aria-pressed="selectedColor === color"
                            class="flex min-h-9 cursor-pointer items-center gap-3 rounded-md px-3 py-2 text-left motion-safe:transition-colors focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-primary"
                            :class="selectedColor === color
                                ? 'bg-elevated text-highlighted'
                                : 'text-default hover:bg-elevated hover:text-highlighted'" @click="selectColor(color)">
                            <span class="size-2.5 shrink-0 rounded-full" :class="swatchClasses[color]"
                                aria-hidden="true" />
                            <span class="min-w-0 flex-1 break-words text-sm font-medium capitalize">{{ color }}</span>
                            <UIcon v-if="selectedColor === color" name="i-lucide-check"
                                class="size-4 shrink-0 text-highlighted" aria-hidden="true" />
                        </button>
                    </div>
                </div>
            </template>
        </UPopover>
    </div>
</template>
