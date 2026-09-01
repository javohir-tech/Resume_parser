<script setup lang="ts">
import { storeToRefs } from 'pinia'
import { useUserStore } from '../models/store'
import { UserAvatar } from '..';

const { loading, user, error } = storeToRefs(useUserStore())

const formatDate = (date: string) => {
    return new Intl.DateTimeFormat("uz-Uz", {
        year: "numeric",
        month: "long",
        day: "numeric",
        hour: "2-digit",
        minute: "2-digit",
    }).format(new Date(date))
}

</script>

<template>
    <section class="py-10">
        <UCard>
            <div v-if="loading" class="space-y-4">
                <div class="flex items-center gap-4">
                    <USkeleton class="size-14 rounded-full" />

                    <div class="space-y-2">
                        <USkeleton class="h-4 w-32" />
                        <USkeleton class="h-3 w-24" />
                    </div>
                </div>

                <USkeleton class="h-10 w-full" />
                <USkeleton class="h-10 w-full" />
            </div>

            <div v-else-if="user" class="space-y-6">
                <!-- Header -->
                <div class="flex items-center gap-4">
                    <UserAvatar class="size-14 text-xl" />
                    <div>
                        <h2 class="font-semibold text-lg">
                            {{ user.full_name }}
                        </h2>

                        <p v-if="user.username" class="text-sm text-muted">
                            @{{ user.username }}
                        </p>
                    </div>
                </div>

                <!-- Information -->
                <div class="divide-y divide-default border-y border-default">
                    <div class="flex justify-between py-3">
                        <span class="text-sm text-muted">Telegram ID</span>
                        <span class="text-sm font-medium">{{ user.telegram_id }}</span>
                    </div>

                    <div class="flex justify-between py-3">
                        <span class="text-sm text-muted">Username</span>
                        <span class="text-sm font-medium">
                            {{ user.username ? `@${user.username}` : '—' }}
                        </span>
                    </div>

                    <div class="flex justify-between py-3">
                        <span class="text-sm text-muted">Registered</span>
                        <ClientOnly>
                            <span class="text-sm font-medium">
                                {{ formatDate(user.registered_at) }}
                            </span>
                            <template #fallback>
                                <USkeleton class="h-5 w-32"/>
                            </template>
                        </ClientOnly>
                    </div>
                </div>
            </div>

            <UAlert v-else-if="error" color="error" variant="soft" title="Failed to load profile" />
        </UCard>
    </section>
</template>