<script setup lang="ts">
const { t } = useI18n()
import { PersonalInfoForm } from '~/features/resume/edit-resume';
</script>

<template>
    <section class="overflow-hidden rounded-xl border border-default bg-default">
        <div class="flex items-center gap-2.5 border-b border-default bg-elevated/50 px-4 py-3">
            <UIcon name="i-lucide-user-round" class="size-4 text-muted" />
            <h2 class="text-sm font-semibold">{{ t('resumeEditor.personal') }}</h2>
        </div>
        <PersonalInfoForm />
    </section>
</template>