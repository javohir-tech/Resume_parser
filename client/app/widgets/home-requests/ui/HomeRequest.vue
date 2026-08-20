<script setup lang="ts">
import { SectionHeader } from '~/shared/components';
import type { AccordionItem } from '@nuxt/ui/runtime/components/Accordion.vue.js';

const { t, tm, rt } = useI18n()

console.log(tm("requests.requests"))

const items = computed<AccordionItem[]>(() => {
    return (tm('requests.items') as any[]).map((item) => {
        return {
            label: rt(item.label),
            content: rt(item.content)
        }
    })
})
</script>

<template>
    <section id="requests-section" class="py-20">
        <UContainer>
            <SectionHeader :eyebrow="t('requests.eyebrow')" :title="t('requests.title')"
                :subtitle="t('requests.subtitle')" />
            <UAccordion :items="items" class="mt-5" />
        </UContainer>
    </section>
</template>