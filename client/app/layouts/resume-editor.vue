<script setup lang="ts">
import { LeftSidebar, RightSidebar } from '~/widgets/resume';

const open = ref(true)
const rightOpen = ref(true)
const localPath = useLocalePath()

type sidebarSide = "right" | "left"

const leftSide = ref<sidebarSide>("left")
const rightSide = ref<sidebarSide>("right")

const swapSidebars = () => {
    if (leftSide.value === "left" && rightSide.value === "right") {
        leftSide.value = "right"
        rightSide.value = "left"
    } else if (leftSide.value === "right" && rightSide.value === "left") {
        leftSide.value = "left"
        rightSide.value = "right"
    }
}

function toggleSidebars(): void {
    const shouldOpen = !(open.value || rightOpen.value)

    open.value = shouldOpen
    rightOpen.value = shouldOpen
}


</script>

<template>
    <div class="flex flex-1">
        <LeftSidebar v-model:open="open" :side="leftSide" :class="leftSide === 'left' ? 'order-1' : 'order-3'" />

        <div class="order-2 flex min-w-0 flex-1 h-screen overflow-hidden">
            <div
                class="flex-1 flex flex-col overflow-hidden lg:peer-data-[variant=floating]:my-4 peer-data-[variant=inset]:m-4 lg:peer-data-[variant=inset]:not-peer-data-[collapsible=offcanvas]:ms-0 peer-data-[variant=inset]:rounded-xl peer-data-[variant=inset]:shadow-sm peer-data-[variant=inset]:ring peer-data-[variant=inset]:ring-default bg-default">

                <div
                    class="h-(--ui-header-height) shrink-0 flex items-center justify-between px-4 border-b border-default">

                    <UButton icon="i-lucide-panel-left" color="neutral" variant="ghost" aria-label="Toggle sidebar"
                        @click="leftSide === 'left' ? open = !open : rightOpen = !rightOpen" />

                    <div class="flex items-center gap-2">
                        <UColorModeButton />
                        <UButton :to="localPath('/resume')" icon="i-lucide-house" variant="ghost" color="neutral" />
                        <UTooltip text="Sidebarlar o‘rnini almashtirish">
                            <UButton @click="swapSidebars" icon="i-lucide-arrow-left-right" variant="ghost"
                                color="neutral" />
                        </UTooltip>
                        <UButton class="hidden lg:inline-flex"
                            :icon="open || rightOpen ? 'i-lucide-minimize-2' : 'i-lucide-maximize-2'" color="neutral"
                            variant="ghost" aria-label="Sidebarlarni ochish yoki yopish" @click="toggleSidebars" />
                    </div>

                    <UButton icon="i-lucide-panel-right" color="neutral" variant="ghost" aria-label="Toggle sidebar"
                        @click="leftSide === 'right' ? open = !open : rightOpen = !rightOpen" />

                </div>
                <div class="flex-1 overflow-y-auto">
                    <slot />
                </div>
            </div>
        </div>

        <RightSidebar v-model:open="rightOpen" :side="rightSide"
            :class="rightSide === 'left' ? 'order-1' : 'order-3'" />


    </div>
</template>
