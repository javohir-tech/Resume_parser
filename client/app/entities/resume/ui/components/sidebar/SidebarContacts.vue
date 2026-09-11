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
  try {
    const url = new URL(/^[a-z][a-z\d+.-]*:/i.test(text) ? text : `https://${text}`)
    return ['https:', 'http:'].includes(url.protocol) ? [{ label, href: url.href }] : []
  } catch {
    return []
  }
}))
</script>

<template>
  <section v-if="contacts.length || links.length" class="pb-4 text-[12px] leading-[1.65] text-slate-700 break-inside-avoid">
    <h2 class="border-b border-slate-300 pb-1.5 mb-2.5 text-[14px] leading-5 font-bold"
      :style="{ color: resumeStore.designInfo.heading_title_color?.hex || '#1e3a5f' }">{{ t('resumeDocument.sections.contacts') }}</h2>
    <p v-for="(contact, index) in contacts" :key="index" class="pb-1.5">{{ contact }}</p>
    <p v-for="link in links" :key="link.label" class="pb-1.5">
      <a :href="link.href" target="_blank" rel="noopener noreferrer"
        class="font-medium underline decoration-slate-400 underline-offset-2">{{ link.label }}</a>
    </p>
  </section>
</template>
