<script setup lang="ts">
import type { Resume } from '~/entities/resume/models/types';
import { useResumeStore } from '~/entities/resume/models/store';

const props = defineProps<{ resume: Resume }>()
const resumeStore = useResumeStore()
const { t } = useI18n()
const contacts = computed(() => [props.resume.email, props.resume.phone, props.resume.location]
  .map(value => value?.trim()).filter(Boolean))

const links = computed(() => [
  { label: t('resumeDocument.website'), value: props.resume.website },
  { label: 'LinkedIn', value: props.resume.linkedin_link },
  { label: 'GitHub', value: props.resume.github_link },
].flatMap(({ label, value }) => {
    const text = value?.trim()
    if (!text) return []
    let href: string | undefined
    try {
      const url = new URL(/^[a-z][a-z\d+.-]*:/i.test(text) ? text : `https://${text}`)
      if (url.protocol === 'https:' || url.protocol === 'http:') href = url.href
    } catch {
      // Omit invalid addresses instead of creating a broken link.
    }
    return href ? [{ label, href }] : []
  }))
</script>

<template>
  <header class="pb-5 text-left text-slate-900 break-inside-avoid">
    <h1 class="text-[30px] leading-tight font-bold" :style="{ color: resumeStore.designInfo.heading_title_color?.hex || '#1e3a5f' }">{{ resume.fullname }}</h1>
    <p v-if="resume.title" class="pt-1.5 text-[15px] leading-relaxed font-medium"
      :style="{ color: resumeStore.designInfo.entry_title_color?.hex || '#334155' }">{{ resume.title }}</p>
    <div v-if="contacts.length || links.length" class="flex flex-wrap gap-x-3 gap-y-1 pt-2 text-[12px] leading-[1.65] text-slate-700">
      <span v-for="(contact, index) in contacts" :key="index" class="max-w-full">
        <span v-if="index" aria-hidden="true" class="mr-3 text-slate-400">·</span>{{ contact }}
      </span>
      <span v-for="(link, index) in links" :key="link.label" class="max-w-full">
        <span v-if="contacts.length || index" aria-hidden="true" class="mr-3 text-slate-400">·</span>
        <a :href="link.href" target="_blank" rel="noopener noreferrer"
          class="font-medium underline decoration-slate-300 underline-offset-2">{{ link.label }}</a>
      </span>
    </div>
    <div class="mt-4 border-b-2" :style="{ borderColor: resumeStore.designInfo.heading_title_color?.hex || '#1e3a5f' }" aria-hidden="true" />
  </header>
</template>
