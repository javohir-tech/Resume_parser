<script setup lang="ts">
const { t } = useI18n()

defineProps<{
    fullname?: string,
    title?: string , 
    loading : boolean
}>()

const emit = defineEmits<{
    delete: []
}>()

</script>

<template>
    <UCard
        class="group cursor-pointer transition duration-200 hover:-translate-y-1 hover:shadow-lg hover:ring-primary/40">
        <div class="flex items-center gap-4">

            <div class="min-w-0 flex-1">
                <p class="truncate font-semibold">
                    {{ fullname || t('resumeList.untitled') }}
                </p>
                <p class="truncate text-sm text-muted">
                    {{ title || t('resumeList.noTitle') }}
                </p>
            </div>

            <UButton icon="i-lucide-trash-2" color="error" variant="ghost" size="sm" :aria-label="t('resumeList.delete')"
                @click.stop="emit('delete')" :loading="loading" :disabled="loading" />

            <UIcon name="i-lucide-chevron-right"
                class="size-5 shrink-0 text-muted transition group-hover:translate-x-1 group-hover:text-primary" />
        </div>
    </UCard>
</template>
