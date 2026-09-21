<script setup lang="ts">
import type { SkillGroup } from '~/entities/resume';
import {  skillCategories  } from '~/entities/resume';
import { useResumeSection } from '../models/useResumeSection';

import { useSkillItem } from '../models/useSkillItem';

const {isCreating , createSkillItem} = useSkillItem()

const { addSkill, removeSkill } = useResumeSection()
const props = defineProps<{
    skillsGroup: SkillGroup
}>()

const skill = ref<string>()
const skillCategoriesItems = ref<string[]>([...skillCategories])

function handleAddSkill() {
    if (!skill.value?.trim()) return
    createSkillItem(props.skillsGroup.id , {skill : skill.value.trim()})
    skill.value = ""
}

function createSkillCategory(skillCategory: string) {
    skillCategoriesItems.value.push(skillCategory)
    props.skillsGroup.title = skillCategory
}
</script>

<template>
    <div class="flex flex-col gap-3">
        <UFormField label="Skill Category">
            <USelectMenu v-model="skillsGroup.title" :items="skillCategoriesItems" create-item class="w-full"
                placeholder="Front End , Backend ..." @create="createSkillCategory" />
        </UFormField>
        <div v-if="skillsGroup.skills.length" class="flex flex-wrap gap-1.5">
            <UButton v-for="skill in skillsGroup.skills" :key="skill.id" type="button"
                @click="removeSkill(skillsGroup.id, skill.id)" trailing-icon="i-lucide-x" color="neutral" variant="subtle"
                size="xs" :aria-label="`Remove ${skill.skill}`" class="rounded-md">{{ skill.skill }}</UButton>
        </div>
        <UForm @submit="handleAddSkill">
            <UFormField label="Skill">
                <div class="flex gap-2">
                    <UInput v-model="skill" class="min-w-0 flex-1" placeholder="JavaScript, Python..." />
                    <UButton type="submit" color="neutral" variant="outline" icon="i-lucide-plus"
                        :disabled="!skill?.trim() || isCreating" :loading="isCreating" aria-label="Add skill" title="Add skill" />
                </div>
            </UFormField>
        </UForm>
    </div>
</template>
