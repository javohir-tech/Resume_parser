<script setup lang="ts">
import { useResumeStore, useResumeSection } from '~/entities/resume';
import ExperienceForm from './components/ExperienceForm.vue';

const resumeStore = useResumeStore()
const { addExperience, removeExperince } = useResumeSection()


</script>

<template>
    <div class="flex flex-col gap-4">

        <UFormField label="Ismingiz">
            <UInput v-model="resumeStore.personalInfo.fullname" class="w-full" placeholder="full name" />
        </UFormField>
        <UFormField label="Title">
            <UInput v-model="resumeStore.personalInfo.title" class="w-full" placeholder="title" />
        </UFormField>
        <UFormField label="Email">
            <UInput v-model="resumeStore.personalInfo.email" placeholder="email" class="w-full" />
        </UFormField>
        <UFormField label="Phone">
            <UInput v-model="resumeStore.personalInfo.phone" class="w-full" placeholder="phone" />
        </UFormField>
        <UFormField label="Location">
            <UInput v-model="resumeStore.personalInfo.location" placeholder="location" class="w-full" />
        </UFormField>
        <UFormField label="Your website">
            <UInput v-model="resumeStore.personalInfo.website" placeholder="website" class="w-full" />
        </UFormField>
        <UFormField label="Summary">
            <UTextarea :rows="4" class="w-full" v-model="resumeStore.personalInfo.summary" />
        </UFormField>

        <!-- Expreries Form-->
        <div v-for="experience in resumeStore.personalInfo.experience" :key="experience.id">
            <ExperienceForm :experience="experience" />
            <div class="text-end">
                <UButton @click="removeExperince(experience.id)" icon="i-lucide-trash" class="mt-3" color="error"
                    variant="outline" />
            </div>
        </div>
        <UButton @click="addExperience">Experience qoshish</UButton>
        <!-- Education Form -->

    </div>
</template>
