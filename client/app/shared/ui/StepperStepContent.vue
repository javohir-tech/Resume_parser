<script setup lang="ts">
defineProps<{
    icon: string;
    description: string
}>()
</script>

<template>
    <div class="group flex flex-col items-center h-55 gap-4 px-4 py-8 text-center">
        <div
            class="relative flex h-16 w-16 items-center justify-center rounded-full bg-primary/10 ring-1 ring-primary/20 transition-all duration-500 group-hover:scale-110 group-hover:bg-primary/15 group-hover:ring-primary/40">
            <UIcon :name="icon" class="h-7 w-7 text-primary transition-transform duration-500 group-hover:-rotate-6" />
        </div>
        <p class="max-w-xs text-sm leading-relaxed text-muted">
            {{ description }}
        </p>
    </div>
</template>