<script setup lang="ts">
import type { IContactLink } from '../models/types'

defineProps<{ contact: IContactLink }>()
</script>

<template>
    <a :href="contact.link" :target="contact.link.startsWith('https:') ? '_blank' : undefined" rel="noopener noreferrer"
        class="group flex min-w-0 items-center gap-3 rounded-xl border border-transparent px-3 py-3 transition-colors hover:border-default hover:bg-elevated focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary">
        <span
            class="flex size-10 shrink-0 items-center justify-center rounded-xl border border-default bg-default text-muted transition-colors group-hover:border-primary/30 group-hover:text-primary">
            <UIcon :name="contact.icon" class="size-4" aria-hidden="true" />
        </span>
        <span class="min-w-0 flex-1 break-words text-sm font-medium text-highlighted">{{ contact.title }}</span>
        <UIcon name="i-lucide-arrow-up-right"
            class="size-4 shrink-0 text-dimmed transition-colors group-hover:text-primary" aria-hidden="true" />
    </a>
</template>
