<script setup lang="ts">
const { t } = useI18n()
const open = ref(true)
import { PersonalInfoForm } from '~/features/resume/edit-resume';
</script>

<template>
    <section class="overflow-hidden rounded-xl border border-default bg-default">
        <UCollapsible v-model:open="open" class="flex flex-col">

            <div class="flex items-center gap-2.5 border-b border-default bg-elevated/50 px-4 py-3">
                <UIcon name="i-lucide-user-round" class="size-4 text-muted" />
                <h2 class="text-sm flex-1 font-semibold">{{ t('resumeEditor.personal') }}</h2>
                <UIcon :name="open ? 'i-lucide-chevron-up' : 'i-lucide-chevron-down'" />
                <span class="rounded-md px-2 py-0.5 text-xs invisible font-medium tabular-nums text-muted">
                    0
                </span>
            </div>

            <template #content>
                <PersonalInfoForm />
            </template>
        </UCollapsible>
    </section>
</template>