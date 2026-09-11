<script setup lang="ts">
import { type Resume } from '~/entities/resume/models/types';
import { useResumeStore } from '~/entities/resume/models/store';
const resumeStore = useResumeStore()
const props = defineProps<{ resume: Resume }>()
const { t } = useI18n()
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
    <header class="pb-6 text-left text-slate-900">
        <h1 class="text-[28px] leading-tight font-bold">{{ resume.fullname }}</h1>
        <p v-if="resume.title" class="mt-2 text-[16px] leading-snug font-medium"
            :style="{ color: resumeStore.designInfo.entry_title_color?.hex }">{{ resume.title }}</p>
        <div class="mt-3 text-[12px] leading-relaxed text-slate-800">
            <p v-if="contacts.length">{{ contacts.join(' | ') }}</p>
            <span v-if="websiteUrl" class="max-w-full">
                <span v-if="contacts.length" aria-hidden="true" class="mr-3 text-slate-400">·</span>
                <a :href="websiteUrl" target="_blank" rel="noopener noreferrer"
                    class="font-medium text-slate-700 underline decoration-slate-400 underline-offset-2">
                    {{ t('resumeDocument.website') }}
                </a>
            </span>
            <span class="max-w-full" v-if="props.resume.linkedin_link">
                <span v-if="contacts.length || websiteUrl" aria-hidden="true" class="mr-3 text-slate-400">·</span>
                <span class="font-medium text-slate-700 underline decoration-slate-400 underline-offset-2">
                    <a :href="props.resume.linkedin_link" target="_blank" rel="noopener noreferrer">
                        LinkedIn
                    </a>
                </span>
            </span>
            <span class="max-w-full" v-if="props.resume.github_link">
                <span v-if="contacts.length || websiteUrl || props.resume.linkedin_link" aria-hidden="true" class="mr-3 text-slate-400">·</span>
                <span class="font-medium text-slate-700 underline decoration-slate-400 underline-offset-2">
                    <a :href="props.resume.github_link" target="_blank" rel="noopener noreferrer">
                        GitHub
                    </a>
                </span>
            </span>
        </div>
    </header>
</template>

