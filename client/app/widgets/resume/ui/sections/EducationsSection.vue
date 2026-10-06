<script setup lang="ts">
const { t } = useI18n()
import { EducationForm } from '~/features/resume/edit-resume';
import { useEducation } from '~/features/resume/edit-resume';
import { useResumeStore } from '~/entities/resume';
import ResumeEditorSection from '../components/ResumeEditorSection.vue';

const { isCreating, createEducation, isDeleting, deleteEducation } = useEducation()


const resumeStore = useResumeStore()
</script>

<template>
    <ResumeEditorSection 
    :items="resumeStore.resume.education ?? []" 
    :section_header="t('resumeEditor.education')"
    :items_count="resumeStore.resume.education?.length ?? 0" 
    :item_header="t('resumeEditor.education')"
    :remove_button_aria_label="t('resumeEditor.educationRemove')"
    :remove_button_title="t('resumeEditor.educationRemove')" 
    :section_empty="t('resumeEditor.educationEmpty')"
    :add_button_label="t('resumeEditor.educationAdd')" 
    :add_pending="isCreating" 
    :delete_pending="isDeleting"
    @add="createEducation"
    @remove="deleteEducation">

        <template #default="{ item }">
            <EducationForm :education="item" />
        </template>
        
    </ResumeEditorSection>
</template>