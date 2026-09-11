<script setup lang="ts">
import type { Resume } from '~/entities/resume/models/types';
import { useResumeStore } from '~/entities/resume/models/store';

const props = defineProps<{ resume: Resume }>()
const resumeStore = useResumeStore()
const contacts = computed(() => [props.resume.email, props.resume.phone, props.resume.location]
  .map(value => value?.trim()).filter(Boolean))

// Preserve visible addresses for text extraction; only HTTP(S) links are clickable.
const links = computed(() => [props.resume.website, props.resume.linkedin_link, props.resume.github_link]
  .map(value => value?.trim()).filter((value): value is string => Boolean(value))
  .map(text => {
    let href: string | undefined
    try {
      const url = new URL(/^[a-z][a-z\d+.-]*:/i.test(text) ? text : `https://${text}`)
      if (url.protocol === 'https:' || url.protocol === 'http:') href = url.href
    } catch {
      // Keep invalid addresses readable without creating a broken link.
    }
    return { text, href }
  }))
</script>

<template>
  <header class="pb-5 text-left text-neutral-900 break-inside-avoid">
    <h1 class="text-[26px] leading-tight font-semibold">{{ resume.fullname }}</h1>
    <p v-if="resume.title" class="pt-1 text-[14px] leading-relaxed"
      :style="{ color: resumeStore.designInfo.entry_title_color?.hex }">{{ resume.title }}</p>
    <div v-if="contacts.length || links.length" class="pt-2 text-[12px] leading-[1.65] text-neutral-700">
      <p v-if="contacts.length">{{ contacts.join(' | ') }}</p>
      <p v-for="(link, index) in links" :key="index">
        <a v-if="link.href" :href="link.href" target="_blank" rel="noopener noreferrer"
          class="underline decoration-neutral-300 underline-offset-2">{{ link.text }}</a>
        <span v-else>{{ link.text }}</span>
      </p>
    </div>
  </header>
</template>
