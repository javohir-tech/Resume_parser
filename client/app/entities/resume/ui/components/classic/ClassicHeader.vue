<script setup lang="ts">
import { type Resume } from '~/entities/resume/models/types';
defineProps<{ resume: Resume }>()
</script>
<template>
    <header class="text-center border-b-2 border-gray-900 pb-4 mb-6">
        <h1 class="text-3xl font-bold tracking-wide uppercase">{{ resume.fullname }}</h1>
        <p v-if="resume.title" class="text-lg text-gray-600 mt-1">{{ resume.title }}</p>
        <div class="flex justify-center flex-wrap gap-x-3 gap-y-1 text-sm text-gray-600 mt-3">
            <span v-if="resume.email">{{ resume.email }}</span>
            <span v-if="resume.phone">·</span><span v-if="resume.phone">{{ resume.phone }}</span>
            <span v-if="resume.location">·</span><span v-if="resume.location">{{ resume.location }}</span>
            <span v-if="resume.website">·</span><span v-if="resume.website">{{ resume.website }}</span>
        </div>
    </header>
</template>