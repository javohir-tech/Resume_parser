<script setup lang="ts">
import { UserProfile, UserSessions } from '~/entities/user';

definePageMeta({
  middleware: "auth"
})

</script>

<template>
  <UContainer>
    <UserProfile />
    <UserSessions />
  </UContainer>
</template>