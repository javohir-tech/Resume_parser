<script setup lang="ts">
import { useResumeStore ,FONT_OPTIONS } from '~/entities/resume';

const resumeStore = useResumeStore()

const items = ref(FONT_OPTIONS.map(item => {
    return {
        label: item,
        value: item,
        style: { fontFamily: item }
    }
}))

</script>

<template>
    <div>
        <h1 class="text-sm font-medium mb-3">
            Fonts
        </h1>
        <USelectMenu v-model="resumeStore.designInfo.font" icon="i-lucide-type" :items="items" value-key="value"
            class="w-full">
            <template #item-label="{ item }">
                <span :style="{ fontFamily: item.value }">{{ item.label }}</span>
            </template>
        </USelectMenu>
    </div>
</template>