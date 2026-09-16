<script setup lang="ts">
import { useResumeStore } from '~/entities/resume';

const resumeStore = useResumeStore()
</script>

<template>
    <div class="space-y-4 p-4">
                <UFormField label="Full name">
                    <UInput v-model="resumeStore.resume.fullname" class="w-full" placeholder="Suvonov Javohir" />
                </UFormField>
                <UFormField label="Professional title">
                    <UInput v-model="resumeStore.resume.title" class="w-full"
                        placeholder="Full Stack Developer" />
                </UFormField>
                <UFormField label="Email">
                    <UInput v-model="resumeStore.resume.email" class="w-full" placeholder="example@gmail.com" />
                </UFormField>
                <UFormField label="Phone">
                    <UInput v-model="resumeStore.resume.phone" class="w-full" placeholder="+998..." />
                </UFormField>
                <UFormField label="Location">
                    <UInput v-model="resumeStore.resume.location" class="w-full" placeholder="Tashkent" />
                </UFormField>
                <UFormField label="Website">
                    <UInput v-model="resumeStore.resume.website" class="w-full" placeholder="myportfolio.com" />
                </UFormField>
                <UFormField label="LinkedIn">
                    <UInput v-model="resumeStore.resume.linkedin_link" class="w-full"
                        placeholder="https://www.linkedin.com/in/..." />
                </UFormField>
                <UFormField label="GitHub">
                    <UInput v-model="resumeStore.resume.github_link" class="w-full"
                        placeholder="https://github.com/..." />
                </UFormField>
                <UFormField label="Summary">
                    <UTextarea v-model="resumeStore.resume.summary" :rows="4" class="w-full"
                        placeholder="Write a brief professional summary..." />
                </UFormField>
            </div>
</template>