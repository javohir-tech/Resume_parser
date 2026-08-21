<script setup lang="ts">
const toaster = { position: 'bottom-right', duration: 4000, max: 3 } as const
</script>

<template>
  <UApp :toaster="toaster">
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </UApp>
</template>
