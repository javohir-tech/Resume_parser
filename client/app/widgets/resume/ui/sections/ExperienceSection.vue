<script setup lang="ts">
const { t } = useI18n()
import { ExperienceForm , useExperience } from '~/features/resume/edit-resume';
import { useResumeStore } from '~/entities/resume';
import ResumeEditorSection from '../components/ResumeEditorSection.vue';

const { isCreating, createExperience, isDeleting, deleteExperience } = useExperience()
const resumeStore = useResumeStore()
</script>

<template>
    <ResumeEditorSection
        :items="resumeStore.resume.experience ?? []" 
        :section_icon="'i-lucide-briefcase-business'"
        :section_header="t('resumeEditor.experience')" 
        :items_count="resumeStore.resume.experience?.length ?? 0" 
        :item_header="t('resumeEditor.experience')"
        :remove_button_aria_label="t('resumeEditor.experienceRemove')"
        :remove_button_title="t('resumeEditor.experienceRemove')"
        :section_empty=" t('resumeEditor.experienceEmpty')"
        :add_button_label="t('resumeEditor.experienceAdd')"
        :add_pending="isCreating"
        :delete_pending="isDeleting"
        @add="createExperience" 
        @remove="deleteExperience"
    >
        <template #default="{item}">
            <ExperienceForm :experience="item" />
        </template>
    </ResumeEditorSection>
</template>