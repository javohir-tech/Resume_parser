<script setup lang="ts">
import type { ICard } from '../models/types';
defineProps<ICard>()

const el = ref<HTMLElement | null>(null)
const isVisible = ref(false)

const { stop } = useIntersectionObserver(
    el,
    ([entry]) => {
        if (entry?.isIntersecting) {
            isVisible.value = true
            stop()
        }
    },
    {
        threshold: 0,
        rootMargin: "0px 0px -200px 0px"
    }
)
</script>

<template>
    <div ref="el"
        class="rounded-xl border border-gray-200 cursor-pointer p-6 opacity-0 dark:border-white/10 transition-shadow ease-in-out duration-300 hover:shadow-md dark:hover:ring ring-primary-500"
        :class="{ 'animate-fade-up': isVisible }" :style="{ animationDelay: `${delay ?? 0}ms` }">
        <div class="mb-5 flex h-10 w-10 items-center justify-center rounded-full bg-gray-100 dark:bg-white/10">
            <Icon :name="icon" class="h-5 w-5 text-gray-600 dark:text-white/70" />
        </div>

        <h3 class="text-[16px] font-semibold text-gray-900 dark:text-white">
            {{ title }}
        </h3>

        <p class="mt-2 text-[14px] leading-relaxed text-gray-500 dark:text-white/50">
            {{ subtitle }}
        </p>
    </div>
</template>

<style scoped>
@keyframes fade-up {
    from {
        opacity: 0;
        transform: translateY(8px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.animate-fade-up {
    animation: fade-up 0.2s ease-in forwards;
}
</style>