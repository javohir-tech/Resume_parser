<script setup lang="ts">
// import { UserProfile } from '~/entities/user';
import { DeleteProfile } from '~/features/user';

definePageMeta({
    middleware: "auth",
    layout: "profile"
})

</script>

<template>
    <DeleteProfile />
</template>
