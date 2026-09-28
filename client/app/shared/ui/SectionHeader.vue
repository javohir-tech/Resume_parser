<script setup lang="ts">

withDefaults(defineProps<{
    eyebrow?: string,
    title?: string,
    subtitle?: string,
    justify?: "start" | "center" | "end"
}>(), {
    justify: "center"
})

const alignmentClasses = {
    start: 'items-start text-start',
    center: 'items-center text-center',
    end: 'items-end text-end',
} as const

</script>
<template>
    <div class="flex flex-col gap-4 sm:gap-5" :class="alignmentClasses[justify]">
        <div v-if="eyebrow"
            class="inline-flex max-w-full items-center gap-2.5 rounded-full border border-primary-200/70 bg-primary-50/80 px-3.5 py-1.5 text-primary-700 dark:border-primary-400/20 dark:bg-primary-400/10 dark:text-primary-300">
            <span aria-hidden="true" class="size-1.5 shrink-0 rounded-full bg-primary-500 dark:bg-primary-400" />
            <span class="min-w-0 text-xs font-semibold leading-5 tracking-wide break-words sm:text-[13px]">
                {{ eyebrow }}
            </span>
        </div>

        <h2 v-if="title"
            class="max-w-3xl text-3xl font-semibold leading-tight tracking-tight text-highlighted text-balance break-words sm:text-4xl lg:text-[42px]">
            {{ title }}
        </h2>

        <p v-if="subtitle" class="max-w-2xl text-[15px] leading-7 text-muted text-pretty break-words sm:text-base">
            {{ subtitle }}
        </p>
    </div>
</template>
