<script setup lang="ts">
import useFont from '../models/useFont'
import { fonts } from '../models/fonts'
const { t } = useI18n()

const { font, setFont } = useFont()
const isOpen = ref(false)

function selectFont(value: typeof fonts[number]) {
    setFont(value)  
    isOpen.value = false
}
</script>

<template>
    <div class="flex flex-wrap items-center justify-between gap-3 py-1.5">
        <h2 class="text-sm font-medium text-highlighted">{{ t('settings.appearance.font') }}</h2>

        <UPopover v-model:open="isOpen" :content="{ align: 'end', sideOffset: 6, collisionPadding: 16 }"
            :ui="{ content: 'w-52 max-w-[calc(100vw-2rem)] overflow-hidden rounded-lg bg-default text-default ring-1 ring-default' }">

            <UButton color="neutral" variant="ghost" size="sm" :aria-label="t('settings.appearance.chooseFont', { font })"
                class="shrink-0 justify-between gap-2 rounded-lg px-2 py-1.5">
                <span class="text-left text-xs font-medium">{{ font }}</span>
                <UIcon name="i-lucide-chevron-down" class="size-3.5 text-muted motion-safe:transition-transform"
                    :class="{ 'rotate-180': isOpen }" aria-hidden="true" />
            </UButton>

            <template #content>
                <div class="max-h-[min(30rem,var(--reka-popover-content-available-height))] overflow-y-auto p-1">
                    <div class="flex flex-col gap-0.5" role="group" :aria-label="t('settings.appearance.fonts')">
                        <button v-for="f in fonts" :key="f" type="button" :aria-pressed="font === f"
                            class="flex min-h-9 cursor-pointer items-center gap-3 rounded-md px-3 py-2 text-left motion-safe:transition-colors focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-primary"
                            :class="font === f
                                ? 'bg-elevated text-highlighted'
                                : 'text-default hover:bg-elevated hover:text-highlighted'"
                            @click="selectFont(f)">
                            <span class="flex-1 text-sm font-medium" :style="{ fontFamily: `'${f}'` }">{{ f }}</span>
                            <UIcon v-if="font === f" name="i-lucide-check"
                                class="size-4 shrink-0 text-highlighted" aria-hidden="true" />
                        </button>
                    </div>
                </div>
            </template>
        </UPopover>
    </div>
</template>
