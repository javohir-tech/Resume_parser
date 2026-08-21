<script setup lang="ts">

const { t } = useI18n()

useSeoMeta({
    title: () => t('seo.home.title'),
    description: () => t('seo.home.description'),

    ogTitle: () => t('seo.home.title'),
    ogDescription: () => t('seo.home.description'),

    twitterTitle: () => t('seo.home.title'),
    twitterDescription: () => t('seo.home.description')
})

// Sections 
import { HomeHero } from '~/widgets/home-hero';

</script>

<template>
    <!-- Home Hero Section -->
    <HomeHero />
    <!-- How It Works Section -->
    <LazyUiHowItWorks hydrate-on-visible />
    <!-- Home Features -->
    <LazyUiHomeFeatures hydrate-on-visible />
    <!-- Home Pricing -->
    <LazyUiHomePricing hydrate-on-visible />
    <!-- Home Requests -->
    <LazyUiHomeRequest hydrate-on-visible />
    <!-- Home Start Section -->
    <LazyUiHomeStart hydrate-on-visible />
</template>