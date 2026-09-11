<script setup lang="ts">
import { useResumeStore } from '~/entities/resume/index.ts';

import HeadingColor from './components/HeadingColor.vue';
import EntryTitleColor from './components/EntryTitleColor.vue';
import FontChoose from './components/FontChoose.vue';

const resumeStore = useResumeStore()

const { t, locale, setLocale } = useI18n()
const languageOptions = [
    { label: 'O‘zbekcha', value: 'uz' },
    { label: 'Русский', value: 'ru' },
    { label: 'English', value: 'en' },
]

function changeLanguage(value: string) {
    if (value === 'uz' || value === 'ru' || value === 'en') return setLocale(value)
}

</script>

<template>
    <div class="flex flex-col gap-4">
        <UFormField label="Templates">
            <USelect v-model="resumeStore.template" :items="resumeStore.templates" icon="i-lucide-layout-template"
                class="w-full" />
        </UFormField>

        <UFormField :label="t('resumeDocument.language')">
            <USelect :model-value="locale" :items="languageOptions" value-key="value" icon="i-lucide-languages"
                class="w-full" @update:model-value="changeLanguage" />
        </UFormField>

        <!-- Section Header -->
        <HeadingColor />

        <!-- Entry Title-->
        <EntryTitleColor />

        <!-- Font choose -->
        <FontChoose />

        <!-- Restart Button -->
        <div>
            <h1 class="text-sm font-medium mb-3">
                Default Desing
            </h1>
            <UButton label="Restart" color="neutral" variant="outline" icon="i-lucide-rotate-ccw" class="w-full"  />
        </div>
    </div>
</template>
