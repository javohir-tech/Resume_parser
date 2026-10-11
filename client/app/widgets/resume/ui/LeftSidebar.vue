<script setup lang="ts">
import PersonalSection from './sections/PersonalSection.vue';
import ExperienceSection from './sections/ExperienceSection.vue';
import EducationsSection from './sections/EducationsSection.vue';
import LanguageSection from './sections/LanguageSection.vue';
import SkillSection from './sections/SkillSection.vue';

defineProps<{
    open: boolean;
    side: "right" | "left"
}>()
</script>

<template>
    <USidebar :open="open" :side="side" variant="sidebar" collapsible="offcanvas"
        :style="{ '--sidebar-width': '26rem' }" :ui="{
            container: 'h-full'
        }">
        <template #header>

        </template>
        <div class="flex flex-col gap-6 pb-6">
            <PersonalSection />
            <ExperienceSection />
            <EducationsSection />
            <SkillSection />
            <LanguageSection />
        </div>
    </USidebar>
</template>
