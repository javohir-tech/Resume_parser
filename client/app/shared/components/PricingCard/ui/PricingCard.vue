<script setup lang="ts">
import type { IPricingCard } from '../models/types';
const props = defineProps<{
    pricingCard: IPricingCard
}>()

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
        class="py-5 flex flex-col opacity-0 justify-between px-6 border border-gray-200 dark:border-white/10 rounded-xl transition-all duration-200 ease-in-out hover:shadow-md dark:hover:border-primary"
        :class="{ 'animate-fade-up': isVisible }">
        <div class="flex items-baseline justify-between">
            <h3
                class="font-mono text-[0.8rem] tracking-[0.18em] text-muted-foreground text-gray-500 font-medium uppercase">
                {{ pricingCard.label }}
            </h3>
            <UBadge v-if="pricingCard.badge" :label="pricingCard.badge" color="warning" />
        </div>
        <p class="flex flex-wrap items-baseline gap-2 mt-5">
            <span class="text-4xl font-display font-semibold tracking-tigth">{{ pricingCard.plan }}</span>
            <span class="text-4xl font-display font-semibold tracking-tigth">{{ pricingCard.plan_price ?? "" }}</span>
            <span class="text-sm text-gray-500">{{ pricingCard.plan_term }}</span>
        </p>
        <p v-if="pricingCard.discount_note" class="mt-3 text-sm text-primary leading-relaxed">
            {{ pricingCard.discount_note }}
        </p>
        <p class="mt-3 text-sm text-gray-500 leading-relaxed">
            {{ pricingCard.subtitle }}
        </p>
        <ul class="flex flex-col gap-3 mt-6">
            <li class="flex flex-baseline gap-2" v-for="feuture in pricingCard.features" :key="feuture">
                <span>
                    <UIcon name="i-lucide-check" class="text-primary" />
                </span>
                <span class="text-sm text-gray-500">{{ feuture }}</span>
            </li>
        </ul>
        <div class="mt-10">
            <slot />
        </div>
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