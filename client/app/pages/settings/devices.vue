<script setup lang="ts">
import { UserSessions } from '~/entities/user';

definePageMeta({
    layout: "settings"
})
</script>

<template>
    <div>
        <UserSessions />
    </div>
</template>