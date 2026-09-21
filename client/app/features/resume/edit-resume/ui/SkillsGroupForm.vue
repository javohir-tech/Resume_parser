<script setup lang="ts">
import { skillCategories, type SkillGroup } from '~/entities/resume';

import { useSkillItem } from '../models/useSkillItem';
import { useSkillsGroup } from '../models/useSkillGroup';

const { isUpdating, updateSkillGroup } = useSkillsGroup()
const { isCreating, createSkillItem, isDeleting, deleteSkillItem, } = useSkillItem()

const props = defineProps<{
    skillsGroup: SkillGroup
}>()

const skill = ref<string>()
const skillCategoriesItems = ref<string[]>([...skillCategories])
const categoryOpen = ref(false)
const categorySearch = ref('')

function handleAddSkill() {
    if (!skill.value?.trim()) return
    createSkillItem(props.skillsGroup.id, { skill: skill.value.trim() })
    skill.value = ""
}


async function selectSkillCategory(value: string) {
    const title = value.trim()

    if (!title || isUpdating.value) return

    if (title !== props.skillsGroup.title) {
        await updateSkillGroup(props.skillsGroup.id, { title })
    }


    if (skillCategoriesItems.value.includes(title)) {
        skillCategoriesItems.value.push(title)
    }

    props.skillsGroup.title = title
    categoryOpen.value = false;
    categorySearch.value = ""
}

async function createSkillCategory(value: string) {
    selectSkillCategory(value)
}
</script>

<template>
    <div class="flex flex-col gap-3">
        <UFormField label="Skill Category" description="Choose a category or type your own to add it.">
            <USelectMenu :model-value="skillsGroup.title" v-model:open="categoryOpen" v-model:search-term="categorySearch" :items="skillCategoriesItems" create-item class="w-full"
                placeholder="Select or create a category" @update:model-value="selectSkillCategory"
                @create="createSkillCategory" />
        </UFormField>
        <div v-if="skillsGroup.skills.length" class="flex flex-wrap gap-1.5">
            <UButton v-for="skill in skillsGroup.skills" :key="skill.id" type="button"
                @click="deleteSkillItem(skillsGroup.id, skill.id)" :loading="isDeleting(skill.id)"
                :disabled="isDeleting(skill.id)" trailing-icon="i-lucide-x" color="neutral" variant="subtle" size="xs"
                :aria-label="`Remove ${skill.skill}`" class="rounded-md">{{ skill.skill }}
            </UButton>
        </div>
        <UForm @submit="handleAddSkill">
            <UFormField label="Skill">
                <div class="flex gap-2">
                    <UInput v-model="skill" class="min-w-0 flex-1" placeholder="JavaScript, Python..." />
                    <UButton type="submit" color="neutral" variant="outline" icon="i-lucide-plus"
                        :disabled="!skill?.trim() || isCreating" :loading="isCreating" aria-label="Add skill"
                        title="Add skill" />
                </div>
            </UFormField>
        </UForm>
    </div>
</template>
