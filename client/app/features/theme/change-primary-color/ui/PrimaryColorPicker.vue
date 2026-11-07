<script setup lang="ts">
import usePrimaryColor from '../models/usePrimaryColor';
import { colors } from '../models/colors';

const { primary, setPrimary } = usePrimaryColor()
const isOpen = ref(false)
const selectedColor = computed(() => primary.value || 'green')

const swatchClasses: Record<string, string> = {
    green: 'bg-green-500',
    indigo: 'bg-indigo-500',
    black: 'bg-black dark:bg-white',
    red: 'bg-red-500',
    orange: 'bg-orange-500',
    amber: 'bg-amber-500',
    yellow: 'bg-yellow-400',
    lime: 'bg-lime-500',
    emerald: 'bg-emerald-500',
    teal: 'bg-teal-500',
    cyan: 'bg-cyan-500',
    sky: 'bg-sky-500',
    blue: 'bg-blue-500',
    violet: 'bg-violet-500',
    purple: 'bg-purple-500',
    fuchsia: 'bg-fuchsia-500',
    pink: 'bg-pink-500',
    rose: 'bg-rose-500',
}

function selectColor(color: typeof colors[number]) {
    setPrimary(color)
    isOpen.value = false
}
</script>

<template>
    <div class="flex items-center justify-between gap-3 py-1.5">

        <h2 class="text-sm font-medium text-highlighted">Primary color</h2>

        <UPopover v-model:open="isOpen" :content="{ align: 'end', sideOffset: 6, collisionPadding: 16 }"
            :ui="{ content: 'w-44 max-w-[calc(100vw-2rem)] overflow-hidden rounded-lg ring-0' }">

            <UButton color="neutral" variant="ghost" size="sm"
                :aria-label="`Primary color: ${selectedColor}. Choose a color`"
                class="shrink-0 justify-between gap-2 rounded-lg px-2 py-1.5">
                <span class="size-3.5 shrink-0 rounded-full"
                    :class="swatchClasses[selectedColor] || 'bg-primary'" aria-hidden="true" />
                <span class="text-left text-xs font-medium capitalize">{{ selectedColor }}</span>
                <UIcon name="i-lucide-chevron-down" class="size-3.5 text-muted motion-safe:transition-transform"
                    :class="{ 'rotate-180': isOpen }" aria-hidden="true" />
            </UButton>

            <template #content>
                <div class="max-h-[min(30rem,var(--reka-popover-content-available-height))] overflow-y-auto p-1">
                    <div class="flex flex-col gap-0.5" role="group" aria-label="Primary colors">
                        <button v-for="color in colors" :key="color" type="button"
                            :aria-pressed="selectedColor === color"
                            class="flex min-h-9 cursor-pointer items-center gap-3 rounded-md px-3 py-2 text-left motion-safe:transition-colors focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-primary"
                            :class="selectedColor === color
                                ? 'bg-elevated text-highlighted'
                                : 'text-default hover:bg-elevated hover:text-highlighted'"
                            @click="selectColor(color)">
                            <span class="size-2.5 shrink-0 rounded-full"
                                :class="swatchClasses[color]" aria-hidden="true" />
                            <span class="flex-1 text-sm font-medium capitalize">{{ color }}</span>
                            <UIcon v-if="selectedColor === color" name="i-lucide-check"
                                class="size-4 shrink-0 text-highlighted" aria-hidden="true" />
                        </button>
                    </div>
                </div>
            </template>
        </UPopover>
    </div>
</template>
