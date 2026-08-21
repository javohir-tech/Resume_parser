<script setup lang="ts">
import type { IContactLink } from '../models/types';

const props = defineProps<{
    contact: IContactLink
}>()
</script>

<template>
    <a :href="contact.link" target="_blanck" class="flex items-center gap-3 transtion-colors hover:text-primary py-2 ">
        <UIcon :name="contact.icon" />
        <p class="font-medium text-sm">{{ contact.title }}</p>
    </a>
</template>