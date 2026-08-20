<script setup lang="ts">

// components
import { SectionHeader } from '~/shared/components';
import { StepperStepContent } from '~/shared/components/StepperStepContent';

// nuxt ui 
import type { StepperItem } from '@nuxt/ui';

const { t } = useI18n()

const items: StepperItem[] = [
    {
        slot: "resume" as const,
        title: t('howItWorks.resume.title'),
        description: t('howItWorks.resume.subtitle'),
        icon: "i-lucide-file-user",
    },
    {
        slot: "vakansiya" as const,
        title: t('howItWorks.vacancy.title'),
        description: t('howItWorks.vacancy.subtitle'),
        icon: 'i-lucide-sparkles',
    },
    {
        slot: "download" as const,
        title: t('howItWorks.download.title'),
        description: t('howItWorks.download.subtitle'),
        icon: 'i-lucide-download',
    }
]


const stepper = useTemplateRef("stepper")
</script>

<template>
    <section id="how_it_works" class="bg-default py-20">
        <UContainer>
            <SectionHeader :eyebrow="t('howItWorks.eyebrow')" :title="t('howItWorks.title')"
                :subtitle="t('howItWorks.subtitle')" />

            <div class="mt-10">
                <UStepper orientation="horizontal" ref="stepper" :items="items">
                    <template #resume>
                        <StepperStepContent icon="i-lucide-file-user"
                            :description="t('howItWorks.resume.description')" />
                    </template>

                    <template #vakansiya>
                        <StepperStepContent icon="i-lucide-sparkles"
                            :description="t('howItWorks.vacancy.description')" />
                    </template>

                    <template #download>
                        <StepperStepContent icon="i-lucide-download"
                            :description="t('howItWorks.download.description')" />
                    </template>
                </UStepper>
            </div>
            <div class="flex justify-between md:justify-center gap-2 mt-4">
                <UButton leading-icon="i-lucide-arrow-left" :disabled="!stepper?.hasPrev" @click="stepper?.prev()">
                    Prev
                </UButton>
                <UButton leading-icon="i-lucide-arrow-right" :disabled="!stepper?.hasNext" @click="stepper?.next()">
                    Next
                </UButton>
            </div>
        </UContainer>
    </section>
</template>
