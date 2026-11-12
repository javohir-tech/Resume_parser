<script setup lang="ts">
// import { UserSessions } from '~/entities/user';
import { UserSessions } from '~/widgets/user/user-sessions';

const { t } = useI18n()

definePageMeta({
    layout: "settings"
})
</script>

<template>
    <div class="mx-auto flex w-full max-w-4xl flex-col gap-8">
        <header>
            <h1 class="m-0 text-3xl font-bold tracking-tight text-highlighted">
                {{ t('profile.sessions.title') }}
            </h1>
        </header>
        <UserSessions />
    </div>
</template>
