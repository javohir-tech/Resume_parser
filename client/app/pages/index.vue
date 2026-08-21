<script setup lang="ts">
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