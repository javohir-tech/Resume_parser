<script setup lang="ts">
import { useDebounceFn } from '@vueuse/core';
import type { Resume } from '~/entities/resume/models/types';
import type { ResumeTemplateBlokcs } from '~/entities/resume/models/template-contract';
import { buildBlock } from '~/entities/resume/models/build-blocks';
import { useResumeStore } from '~/entities/resume/models/store';
import { PAGE_WIDTH_PX, PAGE_HEIGHT_PX, PAGE_CONTENT_WIDTH_PX } from '~/entities/resume/models/pagination';
import { isSidebarBlock, packSidebarColumn, SIDEBAR_WIDTH_PX, SIDEBAR_GAP_PX } from '~/entities/resume/models/sidebar-pagination';
import { useResumePageScale } from '~/entities/resume/lib/useResumePageScale';
import SidebarBlock from './SidebarBlock.vue';

const props = defineProps<{ resume: Resume; template: ResumeTemplateBlokcs }>()
const resumeStore = useResumeStore()
const { locale } = useI18n()
const blocks = computed(() => buildBlock(props.resume))
const sideBlocks = computed(() => blocks.value.filter(isSidebarBlock))
const mainBlocks = computed(() => blocks.value.filter(block => !isSidebarBlock(block)))
const measurementRef = ref<HTMLElement | null>(null)
const headerRef = ref<HTMLElement | null>(null)
const heights = shallowRef(new Map<string, number>())
const headerHeight = ref(0)
const sidePages = computed(() => packSidebarColumn(sideBlocks.value, heights.value, headerHeight.value))
const mainPages = computed(() => packSidebarColumn(mainBlocks.value, heights.value, headerHeight.value))
const pageCount = computed(() => Math.max(sidePages.value.length, mainPages.value.length))
const containerRef = ref<HTMLElement | null>(null)
const { scale } = useResumePageScale(containerRef)
const fontStyle = computed(() => ({ fontFamily: `${resumeStore.designInfo.font}, Arial, sans-serif` }))
const columnsStyle = {
  gridTemplateColumns: `${SIDEBAR_WIDTH_PX}px ${PAGE_CONTENT_WIDTH_PX - SIDEBAR_WIDTH_PX - SIDEBAR_GAP_PX}px`,
  columnGap: `${SIDEBAR_GAP_PX}px`,
}

const recalc = useDebounceFn(() => {
  const next = new Map<string, number>()
  measurementRef.value?.querySelectorAll<HTMLElement>('[data-block-id]').forEach(element => {
    next.set(element.dataset.blockId!, element.getBoundingClientRect().height)
  })
  heights.value = next
  headerHeight.value = headerRef.value?.getBoundingClientRect().height ?? 0
}, 100)
watch([blocks, () => resumeStore.designInfo.font, locale], async () => {
  await nextTick()
  recalc()
}, { deep: true, flush: 'post' })
let observer: ResizeObserver | undefined
onMounted(async () => {
  observer = new ResizeObserver(() => recalc())
  if (measurementRef.value) observer.observe(measurementRef.value)
  recalc()
  await document.fonts.ready
  recalc()
})
onBeforeUnmount(() => observer?.disconnect())
</script>

<template>
  <div ref="measurementRef" class="sidebar-measure" aria-hidden="true" inert :style="{ ...fontStyle, width: `${PAGE_CONTENT_WIDTH_PX}px` }">
    <div ref="headerRef"><component :is="template.header" :resume="resume" /></div>
    <div class="grid" :style="columnsStyle">
      <div class="min-w-0">
        <div v-for="block in sideBlocks" :key="block.id" :data-block-id="block.id">
          <SidebarBlock :block="block" :resume="resume" :template="template" />
        </div>
      </div>
      <div class="min-w-0">
        <div v-for="block in mainBlocks" :key="block.id" :data-block-id="block.id">
          <SidebarBlock :block="block" :resume="resume" :template="template" />
        </div>
      </div>
    </div>
  </div>

  <div ref="containerRef" class="sidebar-preview p-10 flex flex-col items-center gap-8">
    <div v-for="pageNumber in pageCount" :key="pageNumber" class="relative mb-5"
      :style="{ width: `${PAGE_WIDTH_PX * scale}px`, height: `${PAGE_HEIGHT_PX * scale}px` }">
      <div class="absolute top-0 left-0 shadow-xl" :style="{ width: `${PAGE_WIDTH_PX}px`, transform: `scale(${scale})`, transformOrigin: 'top left' }">
        <component :is="template.page">
          <component :is="template.header" v-if="pageNumber === 1" :resume="resume" />
          <div class="grid items-start" :style="columnsStyle">
            <div class="min-w-0">
              <SidebarBlock v-for="block in sidePages[pageNumber - 1]" :key="block.id" :block="block" :resume="resume" :template="template" />
            </div>
            <div class="min-w-0">
              <SidebarBlock v-for="block in mainPages[pageNumber - 1]" :key="block.id" :block="block" :resume="resume" :template="template" />
            </div>
          </div>
        </component>
      </div>
    </div>
  </div>

  <!-- Print in document order so PDF text extraction does not mix columns. -->
  <Teleport to="body">
    <div class="sidebar-print" :style="fontStyle">
      <component :is="template.page">
        <component :is="template.header" :resume="resume" />
        <SidebarBlock v-for="block in blocks" :key="block.id" :block="block" :resume="resume" :template="template" />
      </component>
    </div>
  </Teleport>
</template>

<style scoped>
.sidebar-measure {
  position: fixed;
  top: 0;
  left: 0;
  visibility: hidden;
  pointer-events: none;
  z-index: -1;
  font-size: 12px;
  line-height: 1.7;
  overflow-wrap: break-word;
  word-break: break-word;
}
.sidebar-print { display: none; }
@media print {
  :global(body:has(.sidebar-print) > :not(.sidebar-print)) { display: none !important; }
  .sidebar-print { display: block; color: #0f172a; background: white; }
}
</style>
