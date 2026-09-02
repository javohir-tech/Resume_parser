<script setup lang="ts">
import { LeftSidebar } from '~/widgets/resume/leftSidebar'
import { RigthSidebar } from '~/widgets/resume/rigthSidebar'
const open = ref(true)
const rigthOpen = ref(true)
</script>

<template>
    <div class="flex flex-1">
        <USidebar v-model:open="open" variant="sidebar" collapsible="offcanvas" :style="{ '--sidebar-width': '22rem' }"
            :ui="{
                container: 'h-full'
            }">
            <template #header>

            </template>
            <div class="flex flex-col gap-4">
                <LeftSidebar />
            </div>
        </USidebar>

        <div
            class="flex-1 flex flex-col overflow-hidden lg:peer-data-[variant=floating]:my-4 peer-data-[variant=inset]:m-4 lg:peer-data-[variant=inset]:not-peer-data-[collapsible=offcanvas]:ms-0 peer-data-[variant=inset]:rounded-xl peer-data-[variant=inset]:shadow-sm peer-data-[variant=inset]:ring peer-data-[variant=inset]:ring-default bg-default">
            <div class="h-(--ui-header-height) shrink-0 flex items-center justify-between px-4 border-b border-default">
                <UButton icon="i-lucide-panel-left" color="neutral" variant="ghost" aria-label="Toggle sidebar"
                    @click="open = !open" />
                <UColorModeButton />
                <UButton icon="i-lucide-panel-right" color="neutral" variant="ghost" aria-label="Toggle sidebar"
                    @click="rigthOpen = !rigthOpen" />
            </div>
            <div>
                <slot />
            </div>
        </div>

        <USidebar v-model:open="rigthOpen" variant="sidebar" side="right" collapsible="offcanvas"
            :style="{ '--sidebar-width': '22rem' }" :ui="{
                container: 'h-full'
            }">
            <template #header>

            </template>
            <div class="flex flex-col gap-4">
                <RigthSidebar />
            </div>
        </USidebar>
    </div>
</template>