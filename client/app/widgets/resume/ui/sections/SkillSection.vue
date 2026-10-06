<script setup lang="ts">
const { t } = useI18n()
import { SkillsGroupForm , useSkillsGroup } from '~/features/resume/edit-resume';
import { useResumeStore } from '~/entities/resume';
import ResumeEditorSection from '../components/ResumeEditorSection.vue';

const resumeStore = useResumeStore()
const { isCreating, createSkillsGroup, isDeleting, deleteSkillsGroup } = useSkillsGroup()

</script>

<template>
    <ResumeEditorSection
        :items="resumeStore.resume.skills ?? []"
        :items_count="resumeStore.resume.skills?.length ?? 0"
        :item_header="t('resumeEditor.skills')"

        :section_header="t('resumeEditor.skills')"
        :section_icon="'i-lucide-list-checks'"
        :section_empty="t('resumeEditor.skillsEmpty')"

        @add="createSkillsGroup"
        :add_button_title="t('resumeEditor.skillsAdd')"
        :add_pending="isCreating"

        @delete="deleteSkillsGroup"
        :delete_button_title="t('resumeEditor.skillsRemove')"
        :delete_pending="isDeleting"
    >

    <template #default="{item}">
        <SkillsGroupForm :skills-group="item"/>
    </template>
        
    </ResumeEditorSection>
</template>