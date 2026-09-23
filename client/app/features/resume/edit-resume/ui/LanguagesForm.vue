<script setup lang="ts">
const { t } = useI18n()
import type { Languages } from '~/entities/resume';
import { languages } from '~/entities/resume';
import { useLanguage } from '../models/useLanguage';

const props = defineProps<{
    language: Languages
}>()

const { editLanguage } = useLanguage()

const languageOpen = ref(false)
const languageSearch = ref("")

const degrees = ref<string[]>([
    'Elementary proficiency',
    'Full professional proficiency',
    'Limited working proficiency',
    'Native or bilingual proficiency',
    'Professional working proficiency',
])

const languageItems = ref<string[]>([
    ...new Set([...languages, props.language.language].filter(Boolean)),
])
const proficiencyKeys: Record<string, string> = {
    'Elementary proficiency': 'elementary',
    'Full professional proficiency': 'full',
    'Limited working proficiency': 'limited',
    'Native or bilingual proficiency': 'native',
    'Professional working proficiency': 'professional',
}
const localizedDegrees = computed(() => degrees.value.map(value => ({
    value,
    label: t(`resumeDocument.proficiency.${proficiencyKeys[value]}`),
})))

function selectLanguage(value: string) {
    const language = value.trim()

    if (!language) return

    if (!languageItems.value.includes(language)) {
        languageItems.value.push(language)
    }

    if (language !== props.language.language) {
        props.language.language = language
        void editLanguage(props.language.id, { language })
    }

    languageOpen.value = false
    languageSearch.value = ""
}

function handleSelectDegree(value: string) {
    editLanguage(props.language.id, { degree: value })
}


</script>
<template>
    <div class="flex flex-col gap-3">
        <UFormField :label="t('resumeEditor.language')" :description="t('resumeEditor.languageHint')">
            <USelectMenu create-item :model-value="language.language" v-model:open="languageOpen"
                v-model:search-term="languageSearch" :items="languageItems" class="w-full"
                :placeholder="t('resumeEditor.languagePlaceholder')" @create="selectLanguage" @update:model-value="selectLanguage" />
        </UFormField>
        <UFormField :label="t('resumeEditor.proficiency')">
            <USelect v-model="language.degree" class="w-full" :placeholder="t('resumeEditor.proficiencyPlaceholder')"
                :items="localizedDegrees" value-key="value" @change="handleSelectDegree(language.degree)" />
        </UFormField>
    </div>
</template>
