<script setup lang="ts">
const { t } = useI18n()
import { ExperienceForm } from '~/features/resume/edit-resume';
import { useExperience } from '~/features/resume/edit-resume';
import { useResumeStore } from '~/entities/resume';

const { isCreating, createExperience, isDeleting, deleteExperience } = useExperience()
const resumeStore = useResumeStore()
</script>

<template>
    <section class="overflow-hidden rounded-xl border border-default bg-default">
        <div class="flex items-center gap-2.5 border-b border-default bg-elevated/50 px-4 py-3">
            <UIcon name="i-lucide-briefcase-business" class="size-4 text-muted" />
            <h2 class="flex-1 text-sm font-semibold">{{ t('resumeEditor.experience') }}</h2>
            <span class="rounded-md bg-default px-2 py-0.5 text-xs font-medium tabular-nums text-muted">{{
                resumeStore.resume.experience?.length || 0 }}</span>
        </div>
        <div class="space-y-3 p-3">
            <div v-for="(experience, index) in resumeStore.resume.experience" :key="experience.id"
                class="rounded-lg border border-default p-3">
                <div class="mb-3 flex items-center gap-2 border-b border-default pb-2">
                    <span class="min-w-0 flex-1 truncate text-xs font-semibold text-muted">{{ experience.position ||
                        t('resumeEditor.experienceFallback', { number: index + 1 }) }}</span>
                    <UButton type="button" color="neutral" variant="ghost" size="xs" icon="i-lucide-trash-2"
                        class="shrink-0 hover:bg-error/10 hover:text-error" :aria-label="t('resumeEditor.experienceRemove')"
                        :title="t('resumeEditor.experienceRemove')" :loading="isDeleting(experience.id)"
                        :disabled="isDeleting(experience.id)" @click="deleteExperience(experience.id)" />
                </div>
                <ExperienceForm :experience="experience" />
            </div>
            <p v-if="!resumeStore.resume.experience?.length" class="px-1 py-2 text-xs leading-relaxed text-muted">
                {{ t('resumeEditor.experienceEmpty') }}</p>
            <UButton type="button" color="neutral" variant="outline" size="sm" icon="i-lucide-plus"
                class="w-full justify-center rounded-lg border-dashed py-2" :loading="isCreating" :disabled="isCreating"
                @click="createExperience()">{{ t('resumeEditor.experienceAdd') }}
            </UButton>
        </div>
    </section>
</template>