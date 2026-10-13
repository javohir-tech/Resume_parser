<script setup lang="ts">
const { t } = useI18n()
import { ExperienceForm , useExperience } from '~/features/resume/edit-resume';
import { useResumeStore } from '~/entities/resume';
import ResumeEditorSection from '../components/ResumeEditorSection.vue';

const { isCreating, createExperience, isDeleting, deleteExperience } = useExperience()
const resumeStore = useResumeStore()

const last_item_id = ref<string | null>(null)

const handleAddSection = async () =>{
    const id = await createExperience(resumeStore.resume.id)
    if(id){
        last_item_id.value = id
    }
}

</script>

<template>
    <ResumeEditorSection
        :items="resumeStore.resume.experience ?? []" 
        :items_count="resumeStore.resume.experience?.length ?? 0"

        :item_header="t('resumeEditor.experience')"
        :item_title="(item) => item.position"

        :section_icon="'i-lucide-briefcase-business'" 
        :section_header="t('resumeEditor.experience')" 
        :section_empty=" t('resumeEditor.experienceEmpty')"

        @add="handleAddSection" 
        :add_button_title="t('resumeEditor.experienceAdd')"
        :add_pending="isCreating"

        @delete="deleteExperience"
        :delete_button_title="t('resumeEditor.experienceRemove')"
        :delete_pending="isDeleting"
        
        :last_item_id="last_item_id"
    >
        <template #default="{item}">
            <ExperienceForm :experience="item" />
        </template>
    </ResumeEditorSection>
</template>
