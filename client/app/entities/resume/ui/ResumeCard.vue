<script setup lang="ts">
const { t } = useI18n()

defineProps<{
    id: string,
    fullname?: string,
    title?: string,
    parent_resume_id ?: string ,
    job_company?: string,
    job_title?: string,
    loading: boolean
}>()

const emit = defineEmits<{
    delete: []
}>()

const localPath = useLocalePath()
const open = ref(false)

</script>

<template>
    <NuxtLink :to="localPath(`/resume/${id}`)" class="block min-w-0 max-w-full">
        <UCard
            class="group min-w-0 cursor-pointer transition duration-200 hover:-translate-y-1 hover:shadow-lg hover:ring-primary/40">
            <div class="flex min-w-0 items-center gap-2 sm:gap-4">
                <p v-if="parent_resume_id">Ai Moslashgan</p>
                <div class="min-w-0 flex-1">
                    <p class="truncate font-semibold">
                        {{ fullname || t('resumeList.untitled') }}
                    </p>
                    <p class="truncate text-sm text-muted">
                        {{ title || t('resumeList.noTitle') }}
                    </p>
                </div>

                <UPopover v-model:open="open">
                    <UButton class="shrink-0" icon="i-lucide-trash-2" color="error" variant="ghost" size="sm"
                        :aria-label="t('resumeList.delete')" @click.stop.prevent />
                    <template #content>
                        <div class="min-h-24 min-w-46 m-4 flex flex-col py-2">
                            <p class="mb-3">
                                {{ t('resumeEditor.deleteConfirmation') }}
                            </p>
                            <div class="flex justify-between items-center gap-2">

                                <UButton class="flex-1 justify-center" color="neutral" variant="outline" size="xs"
                                    icon="i-lucide-x" :label="t('resumeEditor.cancel')" @click="open = false" />

                                <UButton class="flex-1 justify-center" type="button" color="error" variant="outline"
                                    size="xs" icon="i-lucide-trash-2" :label="t('resumeEditor.delete')"
                                    :loading="loading" :disabled="loading" @click="emit('delete')" />
                            </div>
                        </div>
                    </template>
                </UPopover>

                <UIcon name="i-lucide-chevron-right"
                    class="size-5 shrink-0 text-muted transition group-hover:translate-x-1 group-hover:text-primary" />
            </div>
        </UCard>
    </NuxtLink>
</template>
