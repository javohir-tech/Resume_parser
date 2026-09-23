<script setup lang="ts">
const { t } = useI18n()
import type { Languages } from '~/entities/resume';
import { languages } from '~/entities/resume';
import { useLanguage } from '../models/useLanguage';

const props = defineProps<{
    language: Languages
}>()

const { editLanguage } = useLanguage()

const langaugeOpen = ref(false)
const langaugeSearch = ref("")

const degrees = ref<string[]>([
    'Elementary proficiency',
    'Full professional proficiency',
    'Limited working proficiency',
    'Native or bilingual proficiency',
    'Professional working proficiency',
])

const languageItems = ref<string[]>([...languages])
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

function createLanguage(language: string) {
    languageItems.value.push(language)
    selectLanguage(language)
}

function selectLanguage(value: string) {
    const language = value.trim()

    if (!value.trim()) return

    if (value !== props.language.language) {
        void editLanguage(props.language.id, { language: language })
    }

    props.language.language = language
    langaugeOpen.value = false
    langaugeSearch.value = ""
}

function handleSelectDegree(value: string) {
    editLanguage(props.language.id, { degree: value })
}


</script>
<template>
    <div class="flex flex-col gap-3">
        <UFormField :label="t('resumeEditor.language')">
            <USelectMenu create-item :model-value="language.language" v-model:open="langaugeOpen"
                v-model:search-term="langaugeSearch" :items="languageItems" class="w-full"
                :placeholder="t('resumeEditor.languagePlaceholder')" @create="createLanguage" @update:model-value="selectLanguage" />
        </UFormField>
        <UFormField :label="t('resumeEditor.proficiency')">
            <USelect v-model="language.degree" class="w-full" :placeholder="t('resumeEditor.proficiencyPlaceholder')"
                :items="localizedDegrees" value-key="value" @change="handleSelectDegree(language.degree)" />
        </UFormField>
    </div>
</template>
