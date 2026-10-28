<script setup lang="ts">
import { UserProfile, UserSessions } from '~/entities/user';
import { DeleteProfile } from '~/features/user';

definePageMeta({
  middleware: "auth"
})

</script>

<template>
  <UContainer class="max-w-5xl">
    <UserProfile />
    <UserSessions />
    <DeleteProfile />
  </UContainer>
</template>
