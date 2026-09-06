<script setup lang="ts">
import type { Languages } from '~/entities/resume';

const props = defineProps < {
    language: Languages
} > ()
</script>
<template>
    <div class="flex flex-col">
        <UFormField>
            <UInput v-model="language.language" />
        </UFormField>
        <UFormField>
            <UInput v-model="language.degree" />
        </UFormField>
    </div>
</template>