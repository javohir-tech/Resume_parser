<script setup lang="ts">

const props = defineProps<{
    eyebrow?: string
    title?: string
    subtitle?: string
}>()

</script>
<template>
    <div>
        <div class="mb-5 flex items-center gap-2 justify-center">
            <span v-if="eyebrow" class="h-1.5 w-1.5 rounded-full bg-primary-500 dark:bg-primary-400" />
            <span class="text-[13px] text-gray-500 dark:text-white/50">
                {{ eyebrow }}
            </span>
        </div>

        <h2 class="text-[28px] text-center md:text-[34px] font-semibold tracking-tight ">
            {{ title }}
        </h2>

        <p class="mt-3 text-center text-[15px] text-gray-500 dark:text-white/45">
            {{ subtitle }}
        </p>
    </div>
</template>
