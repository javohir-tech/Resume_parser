<script setup lang="ts">
import { type Resume } from '~/entities/resume/models/types';
const props = defineProps<{ resume: Resume }>()
const contacts = computed(() => [props.resume.email, props.resume.phone, props.resume.location].filter(Boolean))
const websiteUrl = computed(() => {
    const website = props.resume.website?.trim()
    if (!website) return undefined
    try {
        const url = new URL(/^[a-z][a-z\d+.-]*:/i.test(website) ? website : `https://${website}`)
        return ['http:', 'https:'].includes(url.protocol) ? url.href : undefined
    } catch {
        return undefined
    }
})
</script>
<template>
    <header class="pb-5 text-center text-gray-900">
        <h1 class="text-[30px] leading-tight font-bold tracking-[0.06em] uppercase">{{ resume.fullname }}</h1>
        <p v-if="resume.title" class="mt-2 text-[15px] leading-snug tracking-wide text-gray-600">{{ resume.title }}</p>
        <div class="mt-3 flex flex-wrap justify-center gap-x-3 gap-y-1 text-[11px] leading-relaxed text-gray-600">
            <span v-for="(contact, index) in contacts" :key="index" class="max-w-full">
                <span v-if="index" aria-hidden="true" class="mr-3 text-gray-400">·</span>{{ contact }}
            </span>
            <span v-if="websiteUrl" class="max-w-full">
                <span v-if="contacts.length" aria-hidden="true" class="mr-3 text-gray-400">·</span>
                <a :href="websiteUrl" target="_blank" rel="noopener noreferrer"
                    class="font-medium text-gray-700 underline decoration-gray-400 underline-offset-2">
                    Website
                </a>
            </span>
            <span class="max-w-full" v-if="props.resume.linkedin_link">
                <span v-if="contacts.length || websiteUrl" aria-hidden="true" class="mr-3 text-gray-400">·</span>
                <span class="font-medium text-gray-700 underline decoration-gray-400 underline-offset-2">
                    <a :href="props.resume.linkedin_link" target="_blank" rel="noopener noreferrer">
                        LinkedIn
                    </a>
                </span>
            </span>
            <span class="max-w-full" v-if="props.resume.github_link">
                <span v-if="contacts.length || websiteUrl || props.resume.linkedin_link" aria-hidden="true" class="mr-3 text-gray-400">·</span>
                <span class="font-medium text-gray-700 underline decoration-gray-400 underline-offset-2">
                    <a :href="props.resume.github_link" target="_blank" rel="noopener noreferrer">
                        GitHub
                    </a>
                </span>
            </span>
        </div>
        <div class="mt-4 border-b-2 border-gray-800" />
    </header>
</template>
