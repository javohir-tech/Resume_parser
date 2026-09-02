<script setup lang="ts">
import { PricingCard, SectionHeader } from '~/shared/components';
import { type IPricingCard } from '~/shared/components';

const { t, tm, rt } = useI18n()

const freePlan = computed<IPricingCard>(() => {
    return {
        label: t('pricing.free.label'),
        plan: t('pricing.free.plan'),
        plan_price: t('pricing.free.plan_price'),
        plan_term: t('pricing.free.plan_term'),
        subtitle: t('pricing.free.subtitle'),
        features: (tm('pricing.free.features') as any[]).map((item) => rt(item)),
    }
})

const proPlan = computed<IPricingCard>(() => {
    return {
        label: t('pricing.pro.label'),
        plan: t('pricing.pro.plan'),
        plan_price: t('pricing.pro.plan_price'),
        discount_note : t('pricing.pro.discount_note'),
        badge : t('pricing.pro.badge'),
        plan_term: t('pricing.pro.plan_term'),
        subtitle: t('pricing.free.subtitle'),
        features: (tm('pricing.pro.features') as any[]).map((item) => rt(item))
    }
})

</script>

<template>

    <section id="pricing" class="py-20">
        <UContainer>
            <SectionHeader :eyebrow="t('pricing.eyebrow')" :title="t('pricing.title')"
                :subtitle="t('pricing.subtitle')" />
            <div class="grid md:w-[90%] mx-auto grid-cols-1 md:grid-cols-2 gap-4 mt-10">
                <PricingCard :pricing-card="freePlan">
                    <UButton block variant="outline">{{ t('pricing.free.button') }}</UButton>
                </PricingCard>
                <PricingCard :pricing-card="proPlan">
                    <UButton block variant="solid" >{{ t('pricing.pro.button') }}</UButton>
                </PricingCard>
            </div>
        </UContainer>
    </section>
</template>