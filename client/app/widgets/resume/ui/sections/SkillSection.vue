<script setup lang="ts">
import { SkillsGroupForm } from '~/features/resume/edit-resume';
import { useResumeStore } from '~/entities/resume';
import { useSkillsGroup } from '~/features/resume/edit-resume';

const resumeStore = useResumeStore()
const { isCreating, createSkillsGroup, isDeleting, deleteSkillsGroup } = useSkillsGroup()

</script>

<template>
    <section class="overflow-hidden rounded-xl border border-default bg-default">
        <div class="flex items-center gap-2.5 border-b border-default bg-elevated/50 px-4 py-3">
            <UIcon name="i-lucide-list-checks" class="size-4 text-muted" />
            <h2 class="flex-1 text-sm font-semibold">Skills</h2>
            <span class="rounded-md bg-default px-2 py-0.5 text-xs font-medium tabular-nums text-muted">{{
                resumeStore.resume.skills?.length || 0 }}</span>
        </div>
        <div class="space-y-3 p-3">
            <div v-for="(skillsGroup, index) in resumeStore.resume.skills" :key="skillsGroup.id"
                class="rounded-lg border border-default p-3">
                <div class="mb-3 flex items-center gap-2 border-b border-default pb-2">
                    <span class="min-w-0 flex-1 truncate text-xs font-semibold text-muted">{{ skillsGroup.title ||
                        'Skills ' + (index + 1) }}</span>
                    <UButton type="button" color="neutral" variant="ghost" size="xs" icon="i-lucide-trash-2"
                        class="shrink-0 hover:bg-error/10 hover:text-error" aria-label="Remove skill group"
                        title="Remove skill group" :loading="isDeleting(skillsGroup.id)"
                        :disabled="isDeleting(skillsGroup.id)" @click="deleteSkillsGroup(skillsGroup.id)" />
                </div>
                <SkillsGroupForm :skills-group="skillsGroup" />
            </div>
            <p v-if="!resumeStore.resume.skills?.length" class="px-1 py-2 text-xs leading-relaxed text-muted">
                Add your first skill group to get started.</p>
            <UButton type="button" color="neutral" variant="outline" size="sm" icon="i-lucide-plus"
                class="w-full justify-center rounded-lg border-dashed py-2" :loading="isCreating" :disabled="isCreating"
                @click="createSkillsGroup()">Add skill group
            </UButton>
        </div>
    </section>
</template>