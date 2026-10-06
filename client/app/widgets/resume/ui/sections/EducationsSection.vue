<script setup lang="ts">
const { t } = useI18n()
import { EducationForm , useEducation } from '~/features/resume/edit-resume';
import { useResumeStore } from '~/entities/resume';
import ResumeEditorSection from '../components/ResumeEditorSection.vue';

const { isCreating, createEducation, isDeleting, deleteEducation } = useEducation()


const resumeStore = useResumeStore()
</script>

<template>
    <ResumeEditorSection 
    :items="resumeStore.resume.education ?? []" 
    :items_count="resumeStore.resume.education?.length ?? 0" 
    :item_header="t('resumeEditor.education')"

    :section_header="t('resumeEditor.education')"
    :section_icon="'i-lucide-graduation-cap'"
    :section_empty="t('resumeEditor.educationEmpty')"

    @add="createEducation"
    :add_button_title="t('resumeEditor.educationAdd')" 
    :add_pending="isCreating" 

    @delete="deleteEducation"
    :delete_button_title="t('resumeEditor.educationRemove')" 
    :delete_pending="isDeleting"
    >

        <template #default="{ item }">
            <EducationForm :education="item" />
        </template>
        
    </ResumeEditorSection>
</template>