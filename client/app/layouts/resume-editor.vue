<script setup lang="ts">
import { LeftSidebar, RightSidebar } from '~/widgets/resume';

const open = ref(true)
const rightOpen = ref(true)
const localPath = useLocalePath()

type sidebarSide = "right" | "left"

const leftSide = ref<sidebarSide>("left")
const rightSide = ref<sidebarSide>("right")

const swapSidebars = () => {
    if(leftSide.value === "left" && rightSide.value === "right"){
        leftSide.value = "right"
        rightSide.value = "left"
    }else if(leftSide.value === "right" && rightSide.value ==="left"){
        leftSide.value = "left"
        rightSide.value = "right"
    }
}

</script>

<template>
    <div class="flex flex-1">
        <LeftSidebar :open="open" :side="leftSide" :class="leftSide === 'left' ? 'order-1' : 'order-3'" />

        <div class="order-2 flex min-w-0 flex-1 h-screen overflow-hidden">
            <div
                class="flex-1 flex flex-col overflow-hidden lg:peer-data-[variant=floating]:my-4 peer-data-[variant=inset]:m-4 lg:peer-data-[variant=inset]:not-peer-data-[collapsible=offcanvas]:ms-0 peer-data-[variant=inset]:rounded-xl peer-data-[variant=inset]:shadow-sm peer-data-[variant=inset]:ring peer-data-[variant=inset]:ring-default bg-default">

                <div
                    class="h-(--ui-header-height) shrink-0 flex items-center justify-between px-4 border-b border-default">

                    <UButton icon="i-lucide-panel-left" color="neutral" variant="ghost" aria-label="Toggle sidebar"
                        @click="leftSide === 'left' ? open = !open : rightOpen = !rightOpen" />

                    <div class="flex items-center gap-2">
                        <UColorModeButton />
                        <UButton :to="localPath('/resume')" icon="i-lucide-house" variant="ghost" color="neutral"/>
                        <UButton @click="swapSidebars" aria-label="Sidebarlar o‘rnini almashtirish" icon="i-lucide-arrow-left-right" variant="ghost" color="neutral" />
                    </div>

                    <UButton icon="i-lucide-panel-right" color="neutral" variant="ghost" aria-label="Toggle sidebar"
                        @click="leftSide === 'right' ? open = !open : rightOpen = !rightOpen" />

                </div>
                <div class="flex-1 overflow-y-auto">
                    <slot />
                </div>
            </div>
        </div>


        <RightSidebar :open="rightOpen" :side="rightSide" :class="rightSide === 'left' ? 'order-1' : 'order-3'" />


    </div>
</template>
