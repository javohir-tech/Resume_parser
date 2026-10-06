<script setup lang="ts">
const { t } = useI18n()
import { LanguagesForm , useLanguage } from '~/features/resume/edit-resume';
import { useResumeStore } from '~/entities/resume';
import ResumeEditorSection from '../components/ResumeEditorSection.vue';

const { isCreating, createLanguage, isDeleting, deleteLanguage } = useLanguage()
const resumeStore = useResumeStore()

</script>

<template>
    <ResumeEditorSection
        :items="resumeStore.resume.languages ?? []"
        :section_header="t('resumeEditor.languages')"
        :section_icon="'i-lucide-languages'"
        :items_count="resumeStore.resume.languages?.length ?? 0"
        :item_header="t('resumeEditor.languages')"
        :remove_button_aria_label="t('resumeEditor.languagesRemove')"
        :remove_button_title="t('resumeEditor.languagesRemove')"
        :section_empty="t('resumeEditor.languagesEmpty')"
        :add_button_label="t('resumeEditor.languagesAdd')"
        :add_pending="isCreating"
        :delete_pending="isDeleting"
        @add="createLanguage"
        @remove="deleteLanguage"
    >
    <template #default="{item}">
        <LanguagesForm :language="item"/>
    </template>

    </ResumeEditorSection>
</template>