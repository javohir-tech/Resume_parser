<script setup lang="ts">

const props = withDefaults(defineProps<{
    eyebrow?: string,
    title?: string,
    subtitle?: string,
    justify?: "start" | "center" | "end"
}>(), {
    justify: "center"
})

</script>
<template>
    <div>
        <div class="mb-5 flex gap-2 items-center" :class="`justify-${justify}`">
            <span v-if="eyebrow" class="h-1.5 w-1.5 rounded-full bg-primary-500 dark:bg-primary-400" />
            <span class="text-[13px] text-gray-500 dark:text-white/50">
                {{ eyebrow }}
            </span>
        </div>

        <h2 class="text-[28px] md:text-[34px] font-semibold tracking-tight" :class="`text-${justify}`">
            {{ title }}
        </h2>

        <p class="mt-3 text-[15px] text-gray-500 dark:text-white/45" :class="`text-${justify}`">
            {{ subtitle }}
        </p>
    </div>
</template>
