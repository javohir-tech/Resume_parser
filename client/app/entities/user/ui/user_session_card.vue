<script setup lang="ts">
import type { ISessions } from '../models/types';
const { t, locale } = useI18n()

const formatDate = (date: string) => {
    return new Intl.DateTimeFormat(locale.value, {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        timeZone: 'Asia/Tashkent',
    }).format(new Date(date))
}

const emit = defineEmits<{
    delete: [device_id: string]
}>()

const deleteSession = (device_id: string) => {
    emit("delete", device_id)
}

const props = defineProps<{
    session: ISessions,
    is_deleting: (device_id: string) => boolean
}>()

</script>

<template>
    <div class="flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between sm:gap-4">
        <!-- Device -->
        <div class="flex min-w-0 items-start gap-3">
            <div class="flex size-9 shrink-0 items-center justify-center rounded-lg bg-muted">
                <!-- <UIcon :name="session.device_type === 'mobile'
                    ? 'i-lucide-smartphone'
                    : 'i-lucide-monitor'
                    " class="size-5 text-muted" /> -->
                <UIcon name="i-lucide-monitor" class="size-5 text-muted" />
            </div>

            <div class="min-w-0">
                <div class="flex items-center gap-2 flex-wrap">
                    <p class="break-words text-sm font-semibold text-highlighted">
                        {{ session.os_name || t('profile.sessions.unknownOs') }}
                    </p>

                    <UBadge v-if="session.is_current" color="primary" variant="soft" size="sm">
                        {{ t('profile.sessions.currentDevice') }}
                    </UBadge>
                </div>

                <p class="mt-1 break-words text-sm text-muted">
                    {{ session.browser_name || t('profile.sessions.unknownBrowser') }}
                    <span v-if="session.browser_version">
                        {{ session.browser_version }}
                    </span>
                </p>
            </div>
        </div>

        <!-- Date + Action -->
        <div
            class="flex min-w-0 flex-col items-start gap-2 pl-12 text-left sm:shrink-0 sm:items-end sm:pl-0 sm:text-right">
            <p class="text-sm text-muted">
                {{ formatDate(session.last_seen_at) }}
            </p>
            <p class="break-all text-xs text-muted">
                {{ session.ip_address || t('profile.sessions.noIp') }}
            </p>

            <UButton :loading="props.is_deleting(session.device_id)" :disabled="props.is_deleting(session.device_id)"
                v-if="!session.is_current" @click="deleteSession(session.device_id)" color="error" variant="soft"
                size="sm" icon="i-lucide-log-out" class="shrink-0 rounded-xl">
                {{ t('profile.sessions.revoke') }}
            </UButton>
        </div>
    </div>

    <!-- Details -->
    <div class="mt-3 flex flex-wrap gap-x-4 gap-y-2 pl-12 text-xs text-muted">
        <div v-if="session.os_version" class="flex items-center gap-1.5">
            <UIcon name="i-lucide-layers-2" class="size-3.5" />
            <span>{{ t('profile.sessions.osVersion', { version: session.os_version }) }}</span>
        </div>

        <div class="flex items-center gap-1.5">
            <UIcon name="i-lucide-globe" class="size-3.5" />
            <span>{{ session.ip_address || '—' }}</span>
        </div>

        <div class="flex items-center gap-1.5">
            <UIcon name="i-lucide-calendar" class="size-3.5" />
            <span>{{ formatDate(session.created_at) }}</span>
        </div>
    </div>
</template>
