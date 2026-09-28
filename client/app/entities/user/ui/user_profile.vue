<script setup lang="ts">
import { storeToRefs } from 'pinia'
import { useUserStore } from '../models/store'
import UserAvatar from './userAvatar.vue'

const { loading, user } = storeToRefs(useUserStore())
const { t, locale } = useI18n()
const localePath = useLocalePath()

const registeredDate = computed(() => {
    if (!user.value?.registered_at) return '—'
    const date = new Date(user.value.registered_at)
    if (Number.isNaN(date.getTime())) return '—'
    return new Intl.DateTimeFormat(locale.value, {
        year: 'numeric', month: 'long', day: 'numeric',
    }).format(date)
})
</script>

<template>
    <section class="py-8 sm:py-12" :aria-label="t('account.profile')" :aria-busy="loading">
        <div class="mb-6 flex items-center gap-3">
            <span class="flex size-10 items-center justify-center rounded-2xl bg-primary/10 text-primary">
                <UIcon name="i-lucide-user-round" class="size-5" />
            </span>
            <h1 class="text-2xl font-semibold tracking-tight text-highlighted">{{ t('account.profile') }}</h1>
        </div>

        <div v-if="loading" class="overflow-hidden rounded-3xl border border-default bg-default p-6 sm:p-10">
            <USkeleton class="mb-8 h-24 w-full rounded-2xl" />
            <div class="flex items-center gap-5">
                <USkeleton class="size-24 shrink-0 rounded-full" />
                <div class="flex-1 space-y-3">
                    <USkeleton class="h-7 w-2/3 max-w-64" />
                    <USkeleton class="h-4 w-1/2 max-w-40" />
                </div>
            </div>
            <div class="mt-8 grid gap-4 sm:grid-cols-3">
                <USkeleton v-for="item in 3" :key="item" class="h-28 rounded-2xl" />
            </div>
        </div>

        <div v-else-if="user" class="overflow-hidden rounded-3xl border border-default bg-default shadow-sm">
            <div class="profile-cover relative h-32 overflow-hidden sm:h-40" aria-hidden="true">
                <div class="absolute -right-8 -top-28 size-80 rounded-full border border-white/20" />
                <div class="absolute -right-24 -top-12 size-80 rounded-full border border-white/15" />
                <div class="absolute right-20 top-14 size-36 rounded-full border border-white/15" />
                <UIcon name="i-lucide-sparkles" class="absolute right-8 top-8 size-6 text-white/70 sm:right-12" />
            </div>

            <div class="px-5 pb-6 sm:px-9 sm:pb-9">
                <div class="relative -mt-12 flex flex-col items-start gap-5 sm:flex-row sm:items-end sm:justify-between">
                    <div class="min-w-0 max-w-full">
                        <div class="inline-flex rounded-full bg-default p-1.5 shadow-sm">
                            <UserAvatar size="lg" />
                        </div>
                        <h2 class="mt-4 break-words text-2xl font-semibold tracking-tight text-highlighted sm:text-3xl">
                            {{ user.full_name }}
                        </h2>
                        <p v-if="user.username" class="mt-1 break-all text-sm text-muted">@{{ user.username }}</p>
                    </div>
                    <UButton :to="localePath('/resume')" trailing-icon="i-lucide-arrow-up-right" size="lg"
                        color="neutral" variant="outline" class="shrink-0 rounded-xl">
                        {{ t('account.resumes') }}
                    </UButton>
                </div>

                <dl class="mt-8 grid gap-3 sm:grid-cols-3">
                    <div class="min-w-0 rounded-2xl border border-default bg-elevated/40 p-5">
                        <dt class="flex items-center gap-2 text-sm text-muted">
                            <UIcon name="i-lucide-send" class="size-4 shrink-0 text-primary" />
                            {{ t('profile.telegramId') }}
                        </dt>
                        <dd class="mt-3 break-all font-mono text-base font-medium text-highlighted">{{ user.telegram_id }}</dd>
                    </div>
                    <div class="min-w-0 rounded-2xl border border-default bg-elevated/40 p-5">
                        <dt class="flex items-center gap-2 text-sm text-muted">
                            <UIcon name="i-lucide-at-sign" class="size-4 shrink-0 text-primary" />
                            {{ t('profile.username') }}
                        </dt>
                        <dd class="mt-3 break-all text-base font-medium text-highlighted">{{ user.username ? `@${user.username}` : '—' }}</dd>
                    </div>
                    <div class="min-w-0 rounded-2xl border border-default bg-elevated/40 p-5">
                        <dt class="flex items-center gap-2 text-sm text-muted">
                            <UIcon name="i-lucide-calendar-days" class="size-4 shrink-0 text-primary" />
                            {{ t('profile.registered') }}
                        </dt>
                        <dd class="mt-3 text-base font-medium text-highlighted">
                            <ClientOnly>
                                <time :datetime="user.registered_at">{{ registeredDate }}</time>
                                <template #fallback><USkeleton class="h-6 w-32" /></template>
                            </ClientOnly>
                        </dd>
                    </div>
                </dl>
            </div>
        </div>

        <UAlert v-else color="error" variant="soft" icon="i-lucide-circle-alert"
            :title="t('profile.loadError')" />
    </section>
</template>

<style scoped>
.profile-cover {
    background-color: #064e3b;
    background-image:
        radial-gradient(ellipse at 15% 120%, #34d39980, transparent 55%),
        radial-gradient(ellipse at 85% 0%, #14b8a650, transparent 60%),
        linear-gradient(115deg, #022c22, #065f46);
}
</style>
