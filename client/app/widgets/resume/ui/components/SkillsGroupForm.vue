<script setup lang="ts">
import type { SkillGroup } from '~/entities/resume';
import { useResumeSection, skillCategories  } from '~/entities/resume';

const { addSkill, removeSkill } = useResumeSection()
const props = defineProps<{
    skillsGroup: SkillGroup
}>()

const skill = ref<string>()
const skillCategoriesItems = ref<string[]>([...skillCategories])

function handleAddSkill() {
    if (!skill.value?.trim()) return
    addSkill(props.skillsGroup.id, skill.value.trim())
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
        <div class="flex flex-wrap gap-1">
            <UBadge v-for="(skill, index) in skillsGroup.skills" :key="index"
                @click="removeSkill(skillsGroup.id, index)" icon="i-lucide-x" color="error" variant="outline"
                class="cursor-pointer">{{ skill }}</UBadge>
        </div>
        <UForm @submit="handleAddSkill">
            <UFormField label="Skill">
                <UInput v-model="skill" class="w-full" placeholder="JavaSacript , Python , Nuxt ..." />
            </UFormField>
        </UForm>
    </div>
</template>