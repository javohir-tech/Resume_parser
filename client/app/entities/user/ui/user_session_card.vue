<script setup lang="ts">
import type { ISessions } from '../models/types';

const formatDate = (date: string) => {
    return new Intl.DateTimeFormat('uz-UZ', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        timeZone: 'Asia/Tashkent',
    }).format(new Date(date))
}

defineProps<{
    session: ISessions
}>()
</script>

<template>
    <div class="flex items-start justify-between gap-4">
        <!-- Device -->
        <div class="flex items-start gap-3 min-w-0">
            <div class="size-10 shrink-0 rounded-lg bg-elevated flex items-center justify-center">
                <UIcon :name="session.device_type === 'mobile'
                    ? 'i-lucide-smartphone'
                    : 'i-lucide-monitor'
                    " class="size-5 text-muted" />
            </div>

            <div class="min-w-0">
                <div class="flex items-center gap-2 flex-wrap">
                    <p class="font-medium">
                        {{ session.os_name || 'Unknown OS' }}
                    </p>

                    <UBadge v-if="session.is_current" color="primary" variant="soft" size="sm">
                        Joriy qurilma
                    </UBadge>
                </div>

                <p class="text-sm text-muted mt-1">
                    {{ session.browser_name || 'Unknown browser' }}
                    <span v-if="session.browser_version">
                        {{ session.browser_version }}
                    </span>
                </p>
            </div>
        </div>

        <!-- Date + Action -->
        <div class="text-right shrink-0 flex flex-col items-end gap-2">
            <p class="text-sm">
                {{ formatDate(session.last_seen_at) }}
            </p>
            <p class="text-xs text-muted">
                {{ session.ip_address || 'IP mavjud emas' }}
            </p>

            <UButton v-if="!session.is_current" color="error" variant="soft" size="xs" icon="i-lucide-log-out">
                Chiqarib yuborish
            </UButton>
        </div>
    </div>

    <!-- Details -->
    <div class="mt-4 ml-13 flex flex-wrap gap-x-6 gap-y-2 text-xs text-muted">
        <div v-if="session.os_version" class="flex items-center gap-1.5">
            <UIcon name="i-lucide-layers-2" class="size-3.5" />
            <span>OS {{ session.os_version }}</span>
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