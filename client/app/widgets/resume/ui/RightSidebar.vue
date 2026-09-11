<script setup lang="ts">
import HeadingColor from './components/HeadingColor.vue';
import EntryTitleColor from './components/EntryTitleColor.vue';
import FontChoose from './components/FontChoose.vue';

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
        <UFormField :label="t('resumeDocument.language')">
            <USelect :model-value="locale" :items="languageOptions" value-key="value"
                icon="i-lucide-languages" class="w-full" @update:model-value="changeLanguage" />
        </UFormField>

        <!-- Section Header -->
        <HeadingColor />

        <!-- Entry Title-->
        <EntryTitleColor />

        <!-- Font choose -->
        <FontChoose />
    </div>
</template>
