<script setup lang="ts">
import { useResumeStore, useResumeSection } from '~/entities/resume';
import ExperienceForm from './components/ExperienceForm.vue';
import EducationForm from './components/EducationForm.vue';
import SkillsGroupForm from './components/SkillsGroupForm.vue';

const resumeStore = useResumeStore()
const { addExperience, removeExperince, addEducation, removeEducation, addSkillsGroup, removeSkillsGroup,
} = useResumeSection()


</script>

<template>
    <div class="flex flex-col gap-4">
        <UFormField label="Ismingiz">
            <UInput v-model="resumeStore.personalInfo.fullname" class="w-full" placeholder="Suvonov Javohir" />
        </UFormField>
        <UFormField label="Title">
            <UInput v-model="resumeStore.personalInfo.title" class="w-full" placeholder="Full Stack developer" />
        </UFormField>
        <UFormField label="Email">
            <UInput v-model="resumeStore.personalInfo.email" placeholder="example@gmail.com" class="w-full" />
        </UFormField>
        <UFormField label="Phone">
            <UInput v-model="resumeStore.personalInfo.phone" class="w-full" placeholder="+998..." />
        </UFormField>
        <UFormField label="Location">
            <UInput v-model="resumeStore.personalInfo.location" placeholder="Tashkent" class="w-full" />
        </UFormField>
        <UFormField label="Your website">
            <UInput v-model="resumeStore.personalInfo.website" placeholder="https//:..." class="w-full" />
        </UFormField>
        <UFormField label="Summary">
            <UTextarea :rows="4" class="w-full" v-model="resumeStore.personalInfo.summary"
                placeholder="Write a brief professional summary about yourself..." />
        </UFormField>

        <!-- ////////////////////////////////////////////////// -->
        <!-- Expreries Form-->
        <!-- ////////////////////////////////////////////////// -->
        <h1 class="font-medium">Experience</h1>
        <div v-for="experience in resumeStore.personalInfo.experience" :key="experience.id">
            <ExperienceForm :experience="experience" />
            <div class="text-end">
                <UButton @click="removeExperince(experience.id)" icon="i-lucide-trash" class="mt-3" color="error"
                    variant="outline" />
            </div>
        </div>
        <UButton trailing-icon="i-lucide-plus" @click="addExperience">Experience qoshish</UButton>
        <!-- ////////////////////////////////////////////////// -->
        <!-- Education Form -->
        <!-- ////////////////////////////////////////////////// -->
        <h1 class="font-medium">Educations</h1>
        <div v-for="education in resumeStore.personalInfo.education" :key="education.id">
            <EducationForm :education="education" />
            <div class="text-end">
                <UButton @click="removeEducation(education.id)" icon="i-lucide-trash" class="mt-3" color="error"
                    variant="outline" />
            </div>
        </div>
        <UButton trailing-icon="i-lucide-plus" @click="addEducation">Education qoshish</UButton>
    </div>
    <!-- ////////////////////////////////////////////////// -->
    <!-- Skills Group Form -->
    <!-- ////////////////////////////////////////////////// -->
    <h1 class="font-medium">Skills Group</h1>
    <div v-for="skillsGroup in resumeStore.personalInfo.skills" :key="skillsGroup.id">
        <SkillsGroupForm :skills-group="skillsGroup" />
        <div class="text-end">
            <UButton @click="removeSkillsGroup(skillsGroup.id)" icon="i-lucide-trash" class="mt-3" color="error"
                variant="outline" />
        </div>
    </div>
    <UButton trailing-icon="i-lucide-plus" @click="addSkillsGroup">Skill qoshish</UButton>

</template>
