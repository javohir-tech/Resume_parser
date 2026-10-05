<script setup lang="ts">

const open = defineModel<boolean>("open", { default: false })

import PersonalSection from './sections/PersonalSection.vue';
import ExperienceSection from './sections/ExperienceSection.vue';
import EducationsSection from './sections/EducationsSection.vue';
import LanguageSection from './sections/LanguageSection.vue';
import SkillSection from './sections/SkillSection.vue';

</script>

<template>
    <USidebar v-model:open="open" variant="sidebar" collapsible="offcanvas" :style="{ '--sidebar-width': '22rem' }" :ui="{
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
