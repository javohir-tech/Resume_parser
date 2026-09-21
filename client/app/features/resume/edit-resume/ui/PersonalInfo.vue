<script setup lang="ts">
const { t } = useI18n()
import { useResumeStore } from '~/entities/resume';

const resumeStore = useResumeStore()
</script>

<template>
    <div class="space-y-4 p-4">
                <UFormField :label="t('resumeEditor.fullName')">
                    <UInput v-model="resumeStore.resume.fullname" class="w-full" :placeholder="t('resumeEditor.namePlaceholder')" />
                </UFormField>
                <UFormField :label="t('resumeEditor.professionalTitle')">
                    <UInput v-model="resumeStore.resume.title" class="w-full"
                        :placeholder="t('resumeEditor.titlePlaceholder')" />
                </UFormField>
                <UFormField :label="t('resumeEditor.email')">
                    <UInput v-model="resumeStore.resume.email" class="w-full" :placeholder="t('resumeEditor.emailPlaceholder')" />
                </UFormField>
                <UFormField :label="t('resumeEditor.phone')">
                    <UInput v-model="resumeStore.resume.phone" class="w-full" :placeholder="t('resumeEditor.phonePlaceholder')" />
                </UFormField>
                <UFormField :label="t('resumeEditor.location')">
                    <UInput v-model="resumeStore.resume.location" class="w-full" :placeholder="t('resumeEditor.cityPlaceholder')" />
                </UFormField>
                <UFormField :label="t('resumeEditor.website')">
                    <UInput v-model="resumeStore.resume.website" class="w-full" :placeholder="t('resumeEditor.websitePlaceholder')" />
                </UFormField>
                <UFormField :label="t('resumeEditor.linkedin')">
                    <UInput v-model="resumeStore.resume.linkedin_link" class="w-full"
                        :placeholder="t('resumeEditor.linkedinPlaceholder')" />
                </UFormField>
                <UFormField :label="t('resumeEditor.github')">
                    <UInput v-model="resumeStore.resume.github_link" class="w-full"
                        :placeholder="t('resumeEditor.githubPlaceholder')" />
                </UFormField>
                <UFormField :label="t('resumeEditor.summary')">
                    <UTextarea v-model="resumeStore.resume.summary" :rows="4" class="w-full"
                        :placeholder="t('resumeEditor.summaryPlaceholder')" />
                </UFormField>
            </div>
</template>
