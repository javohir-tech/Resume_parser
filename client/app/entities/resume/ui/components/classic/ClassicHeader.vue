<script setup lang="ts">
import { type Resume } from '~/entities/resume/models/types';
const props = defineProps<{ resume: Resume }>()
const contacts = computed(() => [props.resume.email, props.resume.phone, props.resume.location, props.resume.website].filter(Boolean))
</script>
<template>
    <header class="pb-5 text-center text-gray-900">
        <h1 class="text-[30px] leading-tight font-bold tracking-[0.06em] uppercase">{{ resume.fullname }}</h1>
        <p v-if="resume.title" class="mt-2 text-[15px] leading-snug tracking-wide text-gray-600">{{ resume.title }}</p>
        <div v-if="contacts.length" class="mt-3 flex flex-wrap justify-center gap-x-3 gap-y-1 text-[11px] leading-relaxed text-gray-600">
            <span v-for="(contact, index) in contacts" :key="index" class="max-w-full">
                <span v-if="index" aria-hidden="true" class="mr-3 text-gray-400">·</span>{{ contact }}
            </span>
        </div>
        <div class="mt-4 border-b-2 border-gray-800" />
    </header>
</template>
