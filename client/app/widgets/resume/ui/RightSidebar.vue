<script setup lang="ts">
import { useResumeStore } from '~/entities/resume';
import HeadingColor from './components/HeadingColor.vue';
import EntryTitleColor from './components/EntryTitleColor.vue';
import FontChoose from './components/FontChoose.vue';

const resumeStore = useResumeStore()

</script>

<template>
    <div class="flex flex-col gap-4">

        <!-- Section Header -->
        <HeadingColor />

        <!-- Entry Title-->
        <EntryTitleColor />

        <!-- Font choose -->
        <FontChoose />
    </div>
</template>
