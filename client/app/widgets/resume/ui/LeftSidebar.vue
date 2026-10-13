<script setup lang="ts">
import { type SectionType } from '~/entities/resume/index.ts';

import PersonalSection from './sections/PersonalSection.vue';
import ExperienceSection from './sections/ExperienceSection.vue';
import EducationsSection from './sections/EducationsSection.vue';
import LanguageSection from './sections/LanguageSection.vue';
import SkillSection from './sections/SkillSection.vue';

import type { SidebarProps } from '@nuxt/ui';

const openedSections = ref<Set<SectionType>>(new Set<SectionType>())

const { t } = useI18n()

defineProps<Pick<SidebarProps, "side"> & {
    open: boolean;
}>()

const handleOpenSection = (section: SectionType) => {
    openedSections.value.clear()
    openedSections.value.add(section)
}

onMounted(() => {
    handleOpenSection("personal")
})

</script>

<template>
    <USidebar :open="open" :side="side" rail variant="sidebar" collapsible="offcanvas"
        :style="{ '--sidebar-width': '26rem' }" :ui="{
            container: 'h-full'
        }">
        <template #header>
            <h2 class="text-base font-semibold">{{ t('resumeSidebar.details') }}</h2>
        </template>
        <div class="flex flex-col gap-6 pb-6">

            <PersonalSection :open="openedSections.has('personal')" @open="handleOpenSection('personal')"
                @close="openedSections.delete('personal')" />

            <ExperienceSection :open="openedSections.has('experience')" @open="handleOpenSection('experience')"
                @close="openedSections.delete('experience')" />

            <EducationsSection :open="openedSections.has('education')" @open="handleOpenSection('education')"
                @close="openedSections.delete('education')" />

            <SkillSection :open="openedSections.has('skill')" @open="handleOpenSection('skill')"
                @close="openedSections.delete('skill')" />

            <LanguageSection :open="openedSections.has('language')" @open="handleOpenSection('language')"
                @close="openedSections.delete('language')" />
                
        </div>
    </USidebar>
</template>
