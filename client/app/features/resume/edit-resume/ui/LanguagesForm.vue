<script setup lang="ts">
import type { Languages, LanguageDegree } from '~/entities/resume';
import { languages } from '~/entities/resume';

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

const languageItems = ref<string[]>([...languages])

function createLanguage(language: string) {
    languageItems.value.push(language)
    props.language.language = language
}


</script>
<template>
    <div class="flex flex-col gap-3">
        <UFormField label="Language">
            <USelectMenu create-item v-model="language.language" :items="languageItems" class="w-full"
                placeholder="English, Chinese ..." @create="createLanguage" />
        </UFormField>
        <UFormField label="Proficiency">
            <USelect v-model="language.degree" class="w-full" placeholder="Elementary proficiency..."
                :items="degrees" />
        </UFormField>
    </div>
</template>
