<script setup lang="ts">
const { t } = useI18n()
import { useResumeStore } from '~/entities/resume';
import { INPUT_LIMITS } from '~/shared/constants';

const resumeStore = useResumeStore()
</script>

<template>
    <div class="space-y-4 p-4">
        <UFormField :label="t('resumeEditor.fullName')">
            <UInput :maxlength="INPUT_LIMITS.personal.fullName" v-model="resumeStore.resume.fullname" class="w-full"
                :placeholder="t('resumeEditor.namePlaceholder')" />
        </UFormField>
        <UFormField :label="t('resumeEditor.professionalTitle')">
            <UInput :maxlength="INPUT_LIMITS.personal.professionalTitle" v-model="resumeStore.resume.title"
                class="w-full" :placeholder="t('resumeEditor.titlePlaceholder')" />
        </UFormField>
        <UFormField :label="t('resumeEditor.email')">
            <UInput v-model="resumeStore.resume.email" class="w-full" :placeholder="t('resumeEditor.emailPlaceholder')"
                :maxlength="INPUT_LIMITS.personal.email" />
        </UFormField>
        <UFormField :label="t('resumeEditor.phone')">
            <UInput v-model="resumeStore.resume.phone" class="w-full" :placeholder="t('resumeEditor.phonePlaceholder')"
                :maxlength="INPUT_LIMITS.personal.phone" />
        </UFormField>
        <UFormField :label="t('resumeEditor.location')">
            <UInput v-model="resumeStore.resume.location" class="w-full"
                :placeholder="t('resumeEditor.cityPlaceholder')" :maxlength="INPUT_LIMITS.personal.location" />
        </UFormField>
        <UFormField :label="t('resumeEditor.website')">
            <UInput v-model="resumeStore.resume.website" class="w-full"
                :placeholder="t('resumeEditor.websitePlaceholder')" :maxlength="INPUT_LIMITS.personal.website" />
        </UFormField>
        <UFormField :label="t('resumeEditor.linkedin')">
            <UInput v-model="resumeStore.resume.linkedin_link" class="w-full"
                :placeholder="t('resumeEditor.linkedinPlaceholder')" :maxlength="INPUT_LIMITS.personal.linkedin_link" />
        </UFormField>
        <UFormField :label="t('resumeEditor.github')">
            <UInput v-model="resumeStore.resume.github_link" class="w-full"
                :placeholder="t('resumeEditor.githubPlaceholder')" :maxlength="INPUT_LIMITS.personal.github_link" />
        </UFormField>
        <UFormField :label="t('resumeEditor.summary')">
            <UTextarea v-model="resumeStore.resume.summary" :maxlength="INPUT_LIMITS.personal.summary " :rows="8"
                class="w-full" :placeholder="t('resumeEditor.summaryPlaceholder')" autoresize />
        </UFormField>
    </div>
</template>
