<script setup lang="ts">
const { t } = useI18n()
import type { Languages, LanguageDegree } from '~/entities/resume';
import { languages } from '~/entities/resume';

const props = defineProps<{
    language: Languages
}>()

const degrees = ref<Exclude<LanguageDegree, ''>[]>([
    'Elementary proficiency',
    'Full professional proficiency',
    'Limited working proficiency',
    'Native or bilingual proficiency',
    'Professional working proficiency',
])

const languageItems = ref<string[]>([...languages])
const localizedLanguages = computed(() => languageItems.value.map(value => ({
    value,
    label: languages.includes(value) ? t(`resumeEditor.language${value}`) : value,
})))
const proficiencyKeys: Record<Exclude<LanguageDegree, ''>, string> = {
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
    props.language.language = language
}


</script>
<template>
    <div class="flex flex-col gap-3">
        <UFormField :label="t('resumeEditor.language')">
            <USelectMenu create-item v-model="language.language" :items="localizedLanguages" value-key="value" class="w-full"
                :placeholder="t('resumeEditor.languagePlaceholder')" @create="createLanguage" />
        </UFormField>
        <UFormField :label="t('resumeEditor.proficiency')">
            <USelect v-model="language.degree" class="w-full" :placeholder="t('resumeEditor.proficiencyPlaceholder')"
                :items="localizedDegrees" value-key="value" />
        </UFormField>
    </div>
</template>
