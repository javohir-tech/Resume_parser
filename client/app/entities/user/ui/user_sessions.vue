<script setup lang="ts">
import { fetchGetSessions } from '../api'
import User_session_card from './user_session_card.vue'

const { data, pending, error, refresh } = useLazyAsyncData(
    'sessions',
    () => fetchGetSessions(),
    { server: false }
)
</script>

<template>
    <section class="py-10">
        <UCard>
            <template #header>
                <div>
                    <h2 class="text-lg font-semibold">
                        Qurilmalar
                    </h2>
                    <p class="text-sm text-muted mt-1">
                        Hisobingizga kirilgan qurilmalar
                    </p>
                </div>
            </template>

            <ClientOnly>
                <div v-if="pending" class="space-y-3">
                    <USkeleton v-for="i in 3" :key="i" class="h-20 w-full" />
                </div>

                <UAlert v-else-if="error" color="error" variant="soft"
                    title="Qurilmalarni yuklashda xatolik yuz berdi" />

                <div v-else class="divide-y divide-default">
                    <div v-for="session in data?.sessions ?? []" :key="session.id" class="py-4 first:pt-0 last:pb-0">
                        <User_session_card :session="session" />
                    </div>
                </div>

                <template #fallback>
                    <div class="space-y-3">
                        <USkeleton v-for="i in 3" :key="i" class="h-20 w-full" />
                    </div>
                </template>
            </ClientOnly>
        </UCard>
    </section>
</template>