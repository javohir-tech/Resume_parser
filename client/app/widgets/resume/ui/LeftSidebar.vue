<script setup lang="ts">
import { useResumeStore } from '~/entities/resume';
import {
    useResumeSection,
    PersonalInfoForm,
    ExperienceForm,
    EducationForm,
    LanguagesForm,
    SkillsGroupForm
} from '~/features/resume/edit-resume';

import { useExperience, useEducation } from '~/features/resume/edit-resume';

const { isCreating, createExperience, isDeleting, deleteExperience } = useExperience()
const { isCreating: educationCreating, createEducation, isDeleting: educationIsDeleting, deleteEducation } = useEducation()


const resumeStore = useResumeStore()
const {
    addExperience,
    removeExperince,
    addEducation,
    removeEducation,
    addSkillsGroup,
    removeSkillsGroup,
    addLanguage,
    removeLanguage
} = useResumeSection()


</script>

<template>
    <div class="flex flex-col gap-6 pb-6">
        <!-- ////////////////////////////////////////////////// -->
        <!-- Personal Info Form-->
        <!-- ////////////////////////////////////////////////// -->
        <section class="overflow-hidden rounded-xl border border-default bg-default">
            <div class="flex items-center gap-2.5 border-b border-default bg-elevated/50 px-4 py-3">
                <UIcon name="i-lucide-user-round" class="size-4 text-muted" />
                <h2 class="text-sm font-semibold">Personal details</h2>
            </div>
            <PersonalInfoForm />
        </section>

        <!-- ////////////////////////////////////////////////// -->
        <!-- Expreries Form-->
        <!-- ////////////////////////////////////////////////// -->
        <section class="overflow-hidden rounded-xl border border-default bg-default">
            <div class="flex items-center gap-2.5 border-b border-default bg-elevated/50 px-4 py-3">
                <UIcon name="i-lucide-briefcase-business" class="size-4 text-muted" />
                <h2 class="flex-1 text-sm font-semibold">Experience</h2>
                <span class="rounded-md bg-default px-2 py-0.5 text-xs font-medium tabular-nums text-muted">{{
                    resumeStore.resume.experience?.length || 0 }}</span>
            </div>
            <div class="space-y-3 p-3">
                <div v-for="(experience, index) in resumeStore.resume.experience" :key="experience.id"
                    class="rounded-lg border border-default p-3">
                    <div class="mb-3 flex items-center gap-2 border-b border-default pb-2">
                        <span class="min-w-0 flex-1 truncate text-xs font-semibold text-muted">{{ experience.position ||
                            'Experience ' + (index + 1) }}</span>
                        <UButton type="button" color="neutral" variant="ghost" size="xs" icon="i-lucide-trash-2"
                            class="shrink-0 hover:bg-error/10 hover:text-error" aria-label="Remove experience"
                            title="Remove experience" :loading="isDeleting(experience.id)"
                            :disabled="isDeleting(experience.id)" @click="deleteExperience(experience.id)" />
                    </div>
                    <ExperienceForm :experience="experience" />
                </div>
                <p v-if="!resumeStore.resume.experience?.length" class="px-1 py-2 text-xs leading-relaxed text-muted">
                    Add your first experience to get started.</p>
                <UButton type="button" color="neutral" variant="outline" size="sm" icon="i-lucide-plus"
                    class="w-full justify-center rounded-lg border-dashed py-2" :loading="isCreating"
                    :disabled="isCreating" @click="createExperience()">Add experience
                </UButton>
            </div>
        </section>

        <!-- ////////////////////////////////////////////////// -->
        <!-- Education Form -->
        <!-- ////////////////////////////////////////////////// -->
        <section class="overflow-hidden rounded-xl border border-default bg-default">
            <div class="flex items-center gap-2.5 border-b border-default bg-elevated/50 px-4 py-3">
                <UIcon name="i-lucide-graduation-cap" class="size-4 text-muted" />
                <h2 class="flex-1 text-sm font-semibold">Education</h2>
                <span class="rounded-md bg-default px-2 py-0.5 text-xs font-medium tabular-nums text-muted">{{
                    resumeStore.resume.education?.length || 0 }}</span>
            </div>
            <div class="space-y-3 p-3">
                <div v-for="(education, index) in resumeStore.resume.education" :key="education.id"
                    class="rounded-lg border border-default p-3">
                    <div class="mb-3 flex items-center gap-2 border-b border-default pb-2">
                        <span class="min-w-0 flex-1 truncate text-xs font-semibold text-muted">{{ education.degree ||
                            'Education ' + (index + 1) }}</span>
                        <UButton type="button" color="neutral" variant="ghost" size="xs" icon="i-lucide-trash-2"
                            class="shrink-0 hover:bg-error/10 hover:text-error" aria-label="Remove education"
                            title="Remove education" :loading="educationIsDeleting(education.id)"
                            :disabled="educationIsDeleting(education.id)" @click="deleteEducation(education.id)" />
                    </div>
                    <EducationForm :education="education" />
                </div>
                <p v-if="!resumeStore.resume.education?.length" class="px-1 py-2 text-xs leading-relaxed text-muted">Add
                    your first education to get started.</p>
                <UButton type="button" color="neutral" variant="outline" size="sm" icon="i-lucide-plus"
                    class="w-full justify-center rounded-lg border-dashed py-2" :loading="educationCreating"
                    :disabled="educationCreating" @click="createEducation()">Add education
                </UButton>
            </div>
        </section>

        <!-- ////////////////////////////////////////////////// -->
        <!-- Skills Group Form -->
        <!-- ////////////////////////////////////////////////// -->

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
                            title="Remove skill group" @click="removeSkillsGroup(skillsGroup.id)" />
                    </div>
                    <SkillsGroupForm :skills-group="skillsGroup" />
                </div>
                <p v-if="!resumeStore.resume.skills?.length" class="px-1 py-2 text-xs leading-relaxed text-muted">
                    Add your first skill group to get started.</p>
                <UButton type="button" color="neutral" variant="outline" size="sm" icon="i-lucide-plus"
                    class="w-full justify-center rounded-lg border-dashed py-2" @click="addSkillsGroup">Add skill group
                </UButton>
            </div>
        </section>

        <!-- ////////////////////////////////////////////////// -->
        <!-- Languages Group Form -->
        <!-- ////////////////////////////////////////////////// -->
        <section class="overflow-hidden rounded-xl border border-default bg-default">
            <div class="flex items-center gap-2.5 border-b border-default bg-elevated/50 px-4 py-3">
                <UIcon name="i-lucide-languages" class="size-4 text-muted" />
                <h2 class="flex-1 text-sm font-semibold">Languages</h2>
                <span class="rounded-md bg-default px-2 py-0.5 text-xs font-medium tabular-nums text-muted">{{
                    resumeStore.resume.languages?.length || 0 }}</span>
            </div>
            <div class="space-y-3 p-3">
                <div v-for="(language, index) in resumeStore.resume.languages" :key="language.id"
                    class="rounded-lg border border-default p-3">
                    <div class="mb-3 flex items-center gap-2 border-b border-default pb-2">
                        <span class="min-w-0 flex-1 truncate text-xs font-semibold text-muted">{{ language.language ||
                            'Languages ' + (index + 1) }}</span>
                        <UButton type="button" color="neutral" variant="ghost" size="xs" icon="i-lucide-trash-2"
                            class="shrink-0 hover:bg-error/10 hover:text-error" aria-label="Remove language"
                            title="Remove language" @click="removeLanguage(language.id)" />
                    </div>
                    <LanguagesForm :language="language" />
                </div>
                <p v-if="!resumeStore.resume.languages?.length" class="px-1 py-2 text-xs leading-relaxed text-muted">Add
                    your first language to get started.</p>
                <UButton type="button" color="neutral" variant="outline" size="sm" icon="i-lucide-plus"
                    class="w-full justify-center rounded-lg border-dashed py-2" @click="addLanguage">Add language
                </UButton>
            </div>
        </section>


    </div>
</template>
