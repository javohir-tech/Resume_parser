<script setup lang="ts">
import { fetchGetSessions } from '../api'
import User_session_card from './user_session_card.vue'
const { t } = useI18n()

const { data, pending, error, refresh } = useLazyAsyncData(
    'sessions',
    () => fetchGetSessions(),
    { server: false }
)

const deleteSession = (device_id: string) => {
    if (!data.value) return

    data.value = {
        ...data.value,
        sessions: data.value.sessions.filter(session => session.device_id !== device_id)
    }
}

</script>

<template>
    <div class="flex flex-col gap-8">
        <header>
            <h1 class="m-0 text-3xl font-bold tracking-tight text-highlighted">
                {{ t('profile.sessions.title') }}
            </h1>
        </header>

        <section class="flex flex-col gap-3">
            <h2 class="m-0 text-base font-semibold text-highlighted">
                {{ t('profile.sessions.description') }}
            </h2>
            <div class="overflow-hidden rounded-2xl border border-default bg-default text-default">
                <ClientOnly>
                    <div v-if="pending" class="space-y-3 p-5">
                        <USkeleton v-for="i in 3" :key="i" class="h-20 w-full rounded-xl" />
                    </div>

                    <UAlert v-else-if="error" class="m-5" color="error" variant="soft" :title="t('profile.sessions.loadError')" />

                    <div v-else class="divide-y divide-default">
                        <div v-for="session in data?.sessions ?? []" :key="session.id" class="px-5 py-4">
                            <User_session_card :session="session" @delete="deleteSession" />
                        </div>
                    </div>

                    <template #fallback>
                        <div class="space-y-3 p-5">
                            <USkeleton v-for="i in 3" :key="i" class="h-20 w-full rounded-xl" />
                        </div>
                    </template>
                </ClientOnly>
            </div>
        </section>
    </div>
</template>
