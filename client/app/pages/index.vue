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
    <LazyHowItWorks hydrate-on-visible />
    <!-- Home Features -->
    <LazyHomeFeatures hydrate-on-visible />
    <!-- Home Pricing -->
    <LazyHomePricing hydrate-on-visible />
    <!-- Home Requests -->
    <LazyHomeRequest hydrate-on-visible />
    <!-- Home Start Section -->
    <LazyHomeStart hydrate-on-visible />
</template>