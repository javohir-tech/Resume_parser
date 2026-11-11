<script setup lang="ts">
import { UserSessions } from '~/entities/user';

definePageMeta({
    layout: "settings"
})
</script>

<template>
    <div class="mx-auto flex w-full max-w-4xl flex-col">
        <UserSessions />
    </div>
</template>
