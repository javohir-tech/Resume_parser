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
import { HomeFeatures } from '~/widgets/home-features';
import { HomeHero } from '~/widgets/home-hero';
import { HomePricing } from '~/widgets/home-pricing';
import { HomeRequests } from '~/widgets/home-requests';
import { HomeStart } from '~/widgets/home-start';
import { HowItWorks } from '~/widgets/how-it-works';
</script>

<template>
    <!-- Home Hero Section -->
    <HomeHero />
    <!-- How It Works Section -->
    <HowItWorks />
    <!-- Home Features -->
    <HomeFeatures />
    <!-- Home Pricing -->
    <HomePricing />
    <!-- Home Requests -->
    <HomeRequests />
    <!-- Home Start Section -->
    <HomeStart />
</template>