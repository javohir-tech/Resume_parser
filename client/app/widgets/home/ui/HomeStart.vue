<script setup lang="ts">
import { SectionHeader } from '~/shared/components';

const { t } = useI18n()

</script>

<template>
    <section id="home-start" class="bg-default py-16 sm:py-20 lg:py-24">
        <UContainer>
            <div class="border-t border-default pt-12 sm:pt-16">
                <div aria-hidden="true" class="mb-8 h-1 w-12 rounded-full bg-primary" />

                <div class="grid items-center gap-8 lg:grid-cols-[minmax(0,1fr)_auto] lg:gap-16">
                    <SectionHeader class="max-w-2xl" justify="start" :title="t('homeStart.title')"
                        :subtitle="t('homeStart.subtitle')" />

                    <div class="flex lg:justify-end">
                        <UButton size="xl" color="primary" trailing-icon="i-lucide-arrow-up-right"
                            class="w-full justify-center gap-4 rounded-full px-7 py-4 font-medium whitespace-normal sm:w-auto"
                            :ui="{ trailingIcon: 'size-5 shrink-0' }">
                            {{ t('homeStart.button') }}
                        </UButton>
                    </div>
                </div>
            </div>
        </UContainer>
    </section>
</template>
