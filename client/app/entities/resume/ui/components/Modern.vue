<script setup lang="ts">
defineProps<{
    fullname : string
}>()
</script>

<template>
    <p>
        {{ fullname }}
    </p>
    <p class="text-black-500">
        modern resume
    </p>
</template>