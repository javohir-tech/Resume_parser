<script setup lang="ts">
import ResumePage from '../ResumePage.vue';

defineProps<{
    fullname: string
}>()
</script>

<template>
    <ResumePage>
        <p>
            {{ fullname }}
        </p>
        <p class="text-gray-950">
            classic resume
        </p>
    </ResumePage>
</template>