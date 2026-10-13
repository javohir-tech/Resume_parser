<script setup lang="ts">
const { t } = useI18n()
import { SkillsGroupForm , useSkillsGroup } from '~/features/resume/edit-resume';
import { useResumeStore } from '~/entities/resume';
import ResumeEditorSection from '../components/ResumeEditorSection.vue';

const props = defineProps<{
    open : boolean
}>()

const emit = defineEmits<{
    open : [] , 
    close : []
}>()
const resumeStore = useResumeStore()
const { isCreating, createSkillsGroup, isDeleting, deleteSkillsGroup } = useSkillsGroup()

const last_item_id = ref<string | null>(null)

const handleAddSection = async () =>{
    const id = await createSkillsGroup(resumeStore.resume.id)
    if(id){
        last_item_id.value = id
    }
}

</script>

<template>
    <ResumeEditorSection
        :items="resumeStore.resume.skills ?? []"
        :items_count="resumeStore.resume.skills?.length ?? 0"
        :item_header="t('resumeEditor.skills')"

        :item_title="(item) => item.title"

        :section_header="t('resumeEditor.skills')"
        :section_icon="'i-lucide-list-checks'"
        :section_empty="t('resumeEditor.skillsEmpty')"

        @add="handleAddSection"
        :add_button_title="t('resumeEditor.skillsAdd')"
        :add_pending="isCreating"

        @delete="deleteSkillsGroup"
        :delete_button_title="t('resumeEditor.skillsRemove')"
        :delete_pending="isDeleting"

        :last_item_id="last_item_id"
        :open="props.open"
        @open="emit('open')"
        @close="emit('close')"
    >

    <template #default="{item}">
        <SkillsGroupForm :skills-group="item"/>
    </template>
        
    </ResumeEditorSection>
</template>