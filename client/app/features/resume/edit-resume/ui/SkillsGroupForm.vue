<script setup lang="ts">
const { t } = useI18n()
import { skillCategories, skills, type SkillGroup } from '~/entities/resume';

import { useSkillItem } from '../models/useSkillItem';
import { useSkillsGroup } from '../models/useSkillGroup';

import { INPUT_LIMITS } from '~/shared/constants';

import { useSkillsGroupAvtoSave } from '../models/useSkillsGroupAvtoSave';

const { isUpdating, updateSkillGroup } = useSkillsGroup()
const { isCreating, createSkillItem, isDeleting, deleteSkillItem, } = useSkillItem()
const { start, flush } = useSkillsGroupAvtoSave()

const props = defineProps<{
    skillsGroup: SkillGroup
}>()

const skill = ref<string>()
const skillCategoriesItems = ref<string[]>([...skillCategories])
const categoryOpen = ref(false)
const categorySearch = ref('')
const ready = ref(false)
const router = useRouter()

let removeGuard: (() => void) | undefined

function handleAddSkill() {
    if (!skill.value?.trim()) return
    createSkillItem(props.skillsGroup.id, { skill: skill.value.trim() })
    skill.value = ""
}


async function selectSkillCategory(value: string) {
    const title = value.trim()

    if (!title || isUpdating.value || title.length > INPUT_LIMITS.skills_group.title) return

    if (title !== props.skillsGroup.title) {
        await updateSkillGroup(props.skillsGroup.id, { title })
    }


    if (!skillCategoriesItems.value.includes(title)) {
        skillCategoriesItems.value.push(title)
    }

    props.skillsGroup.title = title
    categoryOpen.value = false;
    categorySearch.value = ""
}

async function createSkillCategory(value: string) {
    selectSkillCategory(value)
}

onMounted(() => {
    const skills_group_id = props.skillsGroup.id

    if (skills_group_id) {
        ready.value = start(skills_group_id)
    }

    removeGuard = router.beforeEach(async () => {
        if (!ready.value) return true

        const result = await flush()
        if (result) return true

        return import.meta.client && window.confirm("resumeEditor.leaveWithoutSavingConfirm")
    })
})

onScopeDispose(() => {
    removeGuard?.()
})

</script>

<template>
    <div class="flex flex-col gap-3 mt-3">
        <UFormField :label="t('resumeEditor.skillCategory')" :description="t('resumeEditor.categoryHint')">
            <UInput v-model="props.skillsGroup.title" />
        </UFormField>
        <div v-if="skillsGroup.skills.length" class="flex flex-wrap gap-1.5">
            <UButton v-for="skill in skillsGroup.skills" :key="skill.id" type="button"
                @click="deleteSkillItem(skillsGroup.id, skill.id)" :loading="isDeleting(skill.id)"
                :disabled="isDeleting(skill.id)" trailing-icon="i-lucide-x" color="neutral" variant="subtle" size="xs"
                :aria-label="t('resumeEditor.removeSkill', { skill: skill.skill })" class="rounded-md">{{ skill.skill }}
            </UButton>
        </div>
        <UForm @submit="handleAddSkill">
            <UFormField :label="t('resumeEditor.skill')">
                <div class="flex gap-2">
                    <UInput :maxlength="INPUT_LIMITS.skill_item.skill" v-model="skill" class="min-w-0 flex-1"
                        :placeholder="t('resumeEditor.skillPlaceholder')" />
                    <UButton type="submit" color="neutral" variant="outline" icon="i-lucide-plus"
                        :disabled="!skill?.trim() || isCreating" :loading="isCreating"
                        :aria-label="t('resumeEditor.addSkill')" :title="t('resumeEditor.addSkill')" />
                </div>
            </UFormField>
        </UForm>
    </div>
</template>
