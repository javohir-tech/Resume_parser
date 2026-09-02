<script setup lang="ts">
import { SectionHeader } from '~/shared/components';
import CardList from '~/shared/components/Card/ui/CardList.vue';
import type { ICard } from '~/shared/components';

const { t } = useI18n()

const FEATURES_META = [
    { icon: 'i-lucide-bot', delay: 0 },
    { icon: 'i-lucide-languages', delay: 200 },
    { icon: 'i-lucide-layout-template', delay: 400 },
    { icon: 'i-lucide-type', delay: 0 },
    { icon: 'i-lucide-file-text', delay: 200 },
    { icon: 'i-lucide-shield-check', delay: 400 },
] as const

const cards_info = computed<ICard[]>(() => {
    return FEATURES_META.map((meta, i) => ({
        icon: meta.icon,
        delay: meta.delay,
        title: t(`features.items.${i}.title`),
        subtitle: t(`features.items.${i}.subtitle`)
    }))
})
</script>

<template>
    <section id="features" class="py-20">
        <UContainer>
            <SectionHeader :eyebrow="t('features.eyebrow')" :title="t('features.title')"
                :subtitle="t('features.subtitle')" />
            <CardList :cards_info="cards_info" />
        </UContainer>
    </section>
</template>