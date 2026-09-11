<script setup lang="ts">
import type { Resume, ResumeBlock } from '~/entities/resume/models/types';
import type { ResumeTemplateBlokcs } from '~/entities/resume/models/template-contract';
import SidebarContacts from './SidebarContacts.vue';
defineProps<{ block: ResumeBlock; resume: Resume; template: ResumeTemplateBlokcs }>()
</script>

<template>
  <div :class="block.type === 'section-title' ? 'break-after-avoid' : ''">
    <SidebarContacts v-if="block.type === 'header'" :resume="resume" />
    <component :is="template.summary" v-else-if="block.type === 'summary'" :text="resume.summary" />
    <component :is="template.sectionTitle" v-else-if="block.type === 'section-title'" :section="block.section" />
    <component :is="template.experienceItem" v-else-if="block.type === 'experience-item'" :item="block.item" />
    <component :is="template.educationItem" v-else-if="block.type === 'education-item'" :item="block.item" />
    <component :is="template.skillsGroup" v-else-if="block.type === 'skills-group'" :item="block.item" />
    <component :is="template.languages" v-else-if="block.type === 'languages-item'" :item="block.item" />
  </div>
</template>
