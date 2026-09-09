<script setup lang="ts">
import type { Languages, LanguageDegree } from '~/entities/resume';

const props = defineProps<{
    language: Languages
}>()

const degrees = ref<LanguageDegree[]>([
    'Elementary proficiency',
    'Full professional proficiency',
    'Limited working proficiency',
    'Native or bilingual proficiency',
    'Professional working proficiency',
])

const languages = ref(["Uzbek",
    "English",
    "Russian",
    "Chinese",
    "Spanish",
    "French",
    "German",
    "Italian",
    "Portuguese",
    "Arabic",
    "Japanese",
    "Korean",
    "Turkish",
    "Hindi",
    "Persian",
    "Kazakh",
    "Kyrgyz",
    "Tajik",
    "Turkmen",
    "Ukrainian",
    "Polish",
    "Dutch",
    "Swedish",
    "Norwegian",
    "Danish",
    "Finnish",
    "Czech",
    "Greek",
    "Hebrew",
])


</script>
<template>
    <div class="flex flex-col gap-4">
        <h1 class="font-medium">{{ language.language }}</h1>
        <UFormField>
            <USelectMenu v-model="language.language" :items="languages" class="w-full"
                placeholder="English, Chinese ..." />
        </UFormField>
        <UFormField>
            <USelect v-model="language.degree" class="w-full" placeholder="Elementary proficiency..."
                :items="degrees" />
        </UFormField>
    </div>
</template>