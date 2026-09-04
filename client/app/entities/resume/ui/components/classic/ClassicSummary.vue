<script setup lang="ts">
defineProps<{ text?: string }>()
</script>
<template>
  <section v-if="text" class="mb-6">
    <h2 class="text-sm font-bold uppercase tracking-wider border-b border-gray-400 mb-2 pb-1">Malumot</h2>
    <p class="text-sm leading-relaxed text-gray-800">{{ text }}</p>
  </section>
</template>