<script setup lang="ts">
import type { Resume } from '../models/types';
import type { ResumeTemplateBlokcs } from '../models/template-contract';
import { buildBlock } from '../models/build-blocks';
import { useResumePagination } from '../lib/useResumePagination';
import { useResumePageScale } from '../lib/useResumePageScale';
import { PAGE_WIDTH_PX, PAGE_HEIGHT_PX, PAGE_CONTENT_WIDTH_PX } from '../models/pagination';

const props = defineProps<{
    resume: Resume,
    template: ResumeTemplateBlokcs
}>()

const blocks = computed(() => buildBlock(props.resume))
const { setMeasureRef, pageContents } = useResumePagination(blocks)

const containerRef = ref<HTMLElement | null>(null)
const { scale } = useResumePageScale(containerRef)
</script>

<template>
  <!-- Ko'rinmas o'lchov qatlami: har bir blok haqiqiy kontent kengligida render qilinadi -->
  <div class="fixed opacity-0 pointer-events-none -z-10 top-0 left-0" :style="{ width: `${PAGE_CONTENT_WIDTH_PX}px` }">
    <template v-for="block in blocks" :key="block.id">
      <component :is="template.header" v-if="block.type === 'header'" :ref="setMeasureRef(block.id)" :resume="resume" />
      <component :is="template.summary" v-else-if="block.type === 'summary'" :ref="setMeasureRef(block.id)" :text="resume.summary" />
      <component :is="template.sectionTitle" v-else-if="block.type === 'section-title'" :ref="setMeasureRef(block.id)" :section="block.section" />
      <component :is="template.experienceItem" v-else-if="block.type === 'experience-item'" :ref="setMeasureRef(block.id)" :item="block.item" />
      <component :is="template.educationItem" v-else-if="block.type === 'education-item'" :ref="setMeasureRef(block.id)" :item="block.item" />
      <component :is="template.skillsGroup" v-else-if="block.type === 'skills-group'" :ref="setMeasureRef(block.id)" :item="block.item" />
    </template>
  </div>

  <!-- Ko'rinadigan, sahifalangan render -->
  <div ref="containerRef" class="p-10 flex flex-col items-center gap-8 overflow-x-auto">
    <div
      v-for="(page, i) in pageContents"
      :key="i"
      class="relative"
      :style="{ width: `${PAGE_WIDTH_PX * scale}px`, height: `${PAGE_HEIGHT_PX * scale}px` }"
    >
      <div class="absolute top-0 left-0" :style="{ width: `${PAGE_WIDTH_PX}px`, transform: `scale(${scale})`, transformOrigin: 'top left' }">
        <component :is="template.page">
          <component :is="template.header" v-if="page.showHeader" :resume="resume" />
          <component :is="template.summary" v-if="page.showSummary" :text="resume.summary" />

          <template v-if="page.experience.items.length">
            <component :is="template.sectionTitle" v-if="page.experience.showTitle" section="experience" />
            <component :is="template.experienceItem" v-for="item in page.experience.items" :key="item.id" :item="item" />
          </template>

          <template v-if="page.education.items.length">
            <component :is="template.sectionTitle" v-if="page.education.showTitle" section="education" />
            <component :is="template.educationItem" v-for="item in page.education.items" :key="item.id" :item="item" />
          </template>

          <template v-if="page.skills.items.length">
            <component :is="template.sectionTitle" v-if="page.skills.showTitle" section="skills" />
            <component :is="template.skillsGroup" v-for="item in page.skills.items" :key="item.id" :item="item" />
          </template>
        </component>
      </div>
    </div>
  </div>
</template>y