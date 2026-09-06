<script setup lang="ts">
import type { SkillGroup } from '~/entities/resume';
import { useResumeSection } from '~/entities/resume';

const { addSkill, removeSkill } = useResumeSection()
const props = defineProps<{
    skillsGroup: SkillGroup
}>()

const skill = ref<string>()

function handleAddSkill() {
    if (!skill.value?.trim()) return
    addSkill(props.skillsGroup.id, skill.value.trim())
    skill.value = ""
}
</script>

<template>
    <div class="flex flex-col gap-3">
        <UFormField label="Skill Group">
            <UInput v-model="skillsGroup.title" class="w-full" placeholder="Front End , Backend ..." />
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