<script setup lang="ts">

// components
import { CardList, SectionHeader } from '~/shared/components';
import type { ICard } from '~/shared/components';

const { t } = useI18n()

const STEP_META = [
    { icon: 'i-lucide-file-user', delay: 0 },
    { icon: 'i-lucide-sparkles', delay: 200 },
    { icon: 'i-lucide-download', delay: 400 },
] as const

const cards_info = computed<ICard[]>(() =>
    STEP_META.map((meta, i) => ({
        icon: meta.icon,
        delay: meta.delay,
        title: t(`howItWorks.steps.${i}.title`),
        subtitle: t(`howItWorks.steps.${i}.subtitle`),
    }))
)
</script>

<template>
    <section id="how_it_works" class="bg-default py-20">
        <UContainer>
            <SectionHeader :eyebrow="t('howItWorks. eyebrow')" :title="t('howItWorks.title')"
                :subtitle="t('howItWorks.subtitle')" />
            <CardList :cards_info="cards_info" />
        </UContainer>
    </section>
</template>