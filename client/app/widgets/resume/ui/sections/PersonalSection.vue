<script setup lang="ts">
import { PersonalInfoForm } from '~/features/resume/edit-resume';

const { t } = useI18n()

const props = defineProps<{
    open: boolean
}>()

const emit = defineEmits<{
    open: [],
    close: []
}>()

</script>

<template>
    <section class="overflow-hidden rounded-xl border border-default bg-default">
        <UCollapsible :open="props.open" class="flex flex-col">

            <div class="flex items-center gap-2.5 border-b border-default bg-elevated/50 px-4 py-3 cursor-pointer"
                @click="props.open ? emit('close') : emit('open')">
                <UIcon name="i-lucide-user-round" class="size-4 text-muted" />
                <h2 class="text-sm flex-1 font-semibold">{{ t('resumeEditor.personal') }}</h2>
                <UIcon :name="props.open ? 'i-lucide-chevron-up' : 'i-lucide-chevron-down'" />
            </div>

            <template #content>
                <PersonalInfoForm />
            </template>
        </UCollapsible>
    </section>
</template>