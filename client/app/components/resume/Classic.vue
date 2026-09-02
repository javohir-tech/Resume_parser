<script setup  lang="ts">
defineProps<{
    fullname : string
}>()
</script>

<template>
    classic template
    <p>{{ fullname }}</p>   
</template>