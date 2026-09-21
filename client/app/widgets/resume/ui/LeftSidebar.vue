<script setup lang="ts">

import PersonalSection from './sections/PersonalSection.vue';
import ExperienceSection from './sections/ExperienceSection.vue';
import EducationsSection from './sections/EducationsSection.vue';
import LanguageSection from './sections/LanguageSection.vue';
import SkillSection from './sections/SkillSection.vue';

</script>

<template>
    <div class="flex flex-col gap-6 pb-6">
        <PersonalSection />
        <ExperienceSection />
        <EducationsSection />
        <SkillSection />
        <LanguageSection />
    </div>
</template>
