<script setup lang="ts">
import { UserSessions } from '~/entities/user';

definePageMeta({
    layout: "profile"
})
</script>

<template>
    <div>
        <UserSessions />
    </div>
</template>