<script setup lang="ts">
import { useResumeStore } from '~/entities/resume';

const resumeStore = useResumeStore()
</script>

<template>
        <div>
            <UInput v-model="resumeStore.personalInfo.fullname" placeholder="full name"/>
            <UInput v-model="resumeStore.personalInfo.email" placeholder="email"/>
            <UInput v-model="resumeStore.personalInfo.phone" placeholder="phone"/>
            <UInput v-model="resumeStore.personalInfo.summary" placeholder="summary"/>
            <UInput v-model="resumeStore.personalInfo.location" placeholder="location"/>
            <UInput v-model="resumeStore.personalInfo.title" placeholder="title"/>
            <UInput v-model="resumeStore.personalInfo.website" placeholder="website"/>
        </div>
</template>
