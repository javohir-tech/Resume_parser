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
    <section class="pb-6 pt-8 sm:pb-8 sm:pt-12" :aria-label="t('account.profile')" :aria-busy="loading">
        <div class="mb-6 flex items-center gap-3">
            <span class="flex size-10 items-center justify-center rounded-2xl bg-primary/10 text-primary">
                <UIcon name="i-lucide-user-round" class="size-5" />
            </span>
            <h1 class="text-2xl font-semibold tracking-tight text-highlighted">{{ t('account.profile') }}</h1>
        </div>

        <div v-if="loading" class="overflow-hidden rounded-2xl border border-default bg-default p-6 sm:p-10">
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

        <div v-else-if="user" class="overflow-hidden rounded-2xl border border-default bg-default shadow-sm">
            <div class="profile-cover relative h-28 overflow-hidden sm:h-36" aria-hidden="true">
                <div class="profile-grid absolute inset-0 opacity-20" />
                <div class="absolute -right-8 -top-28 size-80 rounded-full border border-white/20" />
                <div class="absolute -right-24 -top-12 size-80 rounded-full border border-white/15" />
                <div class="absolute right-20 top-14 size-36 rounded-full border border-white/15" />
                <UIcon name="i-lucide-sparkles" class="absolute right-8 top-8 size-6 text-white/70 sm:right-12" />
            </div>

            <div class="px-5 pb-6 sm:px-9 sm:pb-9">
                <div
                    class="relative -mt-12 flex flex-col items-start gap-6 sm:flex-row sm:items-end sm:justify-between">
                    <div class="min-w-0 max-w-full">
                        <div class="inline-flex rounded-full bg-default p-1.5 shadow-lg ring-1 ring-black/5">
                            <UserAvatar size="lg" />
                        </div>
                        <div class="mt-4 flex flex-wrap items-center gap-3">
                            <h2
                                class="min-w-0 break-words text-2xl font-semibold tracking-tight text-highlighted sm:text-3xl">
                                {{ user.full_name }}
                            </h2>
                            <UBadge :color="user.plan === 'pro' ? 'primary' : 'neutral'" variant="soft"
                                :icon="user.plan === 'pro' ? 'i-lucide-sparkles' : 'i-lucide-leaf'"
                                class="shrink-0 rounded-full px-3 py-1">
                                {{ user.plan === 'pro' ? 'Pro' : 'Free' }}
                            </UBadge>
                        </div>
                        <p v-if="user.username" class="mt-1 break-all text-sm text-muted">@{{ user.username }}</p>
                    </div>
                    <div class="flex w-full flex-wrap items-center gap-3 sm:w-auto sm:justify-end">
                        <UButton :to="localePath('/resume')" trailing-icon="i-lucide-arrow-up-right" size="lg"
                            color="primary" variant="solid"
                            class="min-h-11 flex-1 justify-center rounded-xl px-5 sm:flex-none">
                            {{ t('account.resumes') }}
                        </UButton>
                    </div>
                </div>

                <dl class="mt-7 grid gap-3 border-t border-default pt-6 sm:mt-8 sm:grid-cols-3">
                    <div class="min-w-0 rounded-2xl bg-elevated/50 p-4 sm:p-5">
                        <dt class="flex items-center gap-2 text-sm text-muted">
                            <UIcon name="i-lucide-send" class="size-4 shrink-0 text-primary" />
                            {{ t('profile.telegramId') }}
                        </dt>
                        <dd class="mt-3 break-all font-mono text-base font-medium text-highlighted">{{ user.telegram_id
                        }}</dd>
                    </div>
                    <div class="min-w-0 rounded-2xl bg-elevated/50 p-4 sm:p-5">
                        <dt class="flex items-center gap-2 text-sm text-muted">
                            <UIcon name="i-lucide-at-sign" class="size-4 shrink-0 text-primary" />
                            {{ t('profile.username') }}
                        </dt>
                        <dd class="mt-3 break-all text-base font-medium text-highlighted">{{ user.username ?
                            `@${user.username}` : '—' }}</dd>
                    </div>
                    <div class="min-w-0 rounded-2xl bg-elevated/50 p-4 sm:p-5">
                        <dt class="flex items-center gap-2 text-sm text-muted">
                            <UIcon name="i-lucide-calendar-days" class="size-4 shrink-0 text-primary" />
                            {{ t('profile.registered') }}
                        </dt>
                        <dd class="mt-3 text-base font-medium text-highlighted">
                            <ClientOnly>
                                <time :datetime="user.registered_at">{{ registeredDate }}</time>
                                <template #fallback>
                                    <USkeleton class="h-6 w-32" />
                                </template>
                            </ClientOnly>
                        </dd>
                    </div>
                </dl>
            </div>
        </div>

        <UAlert v-else color="error" variant="soft" icon="i-lucide-circle-alert" :title="t('profile.loadError')" />

        <div v-if="!loading && user"
            class="mt-6 flex flex-col gap-5 rounded-2xl border border-primary/20 bg-primary/5 p-5 sm:flex-row sm:items-center sm:justify-between sm:p-7">
            <div class="flex items-center gap-4">
                <span class="flex size-12 shrink-0 items-center justify-center rounded-2xl bg-primary/10 text-primary"
                    aria-hidden="true">
                    <UIcon :name="user.plan === 'pro' ? 'i-lucide-badge-check' : 'i-lucide-sparkles'" class="size-6" />
                </span>
                <div class="min-w-0">
                    <p class="text-sm text-muted">{{ t('profile.plan.current') }}</p>
                    <h2 class="mt-1 text-lg font-semibold text-highlighted">
                        {{ user.plan === 'pro' ? t('profile.plan.proActive') : t('profile.plan.freeActive') }}
                    </h2>
                </div>
            </div>
            <UButton :to="localePath('/settings')" v-if="user.plan !== 'pro'" size="lg" color="primary"
                trailing-icon="i-lucide-arrow-up-right"
                class="min-h-11 cursor-pointer justify-center rounded-xl px-5 sm:shrink-0">
                {{ t('profile.plan.upgrade') }}
            </UButton>
        </div>
    </section>
</template>

<style scoped>
.profile-grid {
    background-image:
        linear-gradient(to right, #ffffff30 1px, transparent 1px),
        linear-gradient(to bottom, #ffffff30 1px, transparent 1px);
    background-size: 32px 32px;
    mask-image: linear-gradient(to right, transparent, black);
}

.profile-cover {
    background-color: #064e3b;
    background-image:
        radial-gradient(ellipse at 15% 120%, #34d39980, transparent 55%),
        radial-gradient(ellipse at 85% 0%, #14b8a650, transparent 60%),
        linear-gradient(115deg, #022c22, #065f46);
}
</style>
