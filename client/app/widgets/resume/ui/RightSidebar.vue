<script setup lang="ts">
import { useResumeStore } from '~/entities/resume';

const resumeStore = useResumeStore()

</script>

<template>
    <UPopover mode="hover" enable-touch :content="{ align: 'start', side: 'left' }">
        <UButton label="color" />

        <template #content>
            <div v-for="color in resumeStore.colorOptions" :key="color.name"  @click="resumeStore.handleChangeColor(color.hex)">
                {{ color.name }}
            </div>
        </template>
    </UPopover>
    <UPopover mode="hover" enable-touch :content="{ align: 'start', side: 'left' }">
        <UButton label="font" />
        <template #content>
            <div>
                <div v-for="font in resumeStore.fontOptions">
                    <UButton @click="resumeStore.handleChangeFont(font)" :label="font" />
                </div>
            </div>
        </template>
    </UPopover>
</template>
