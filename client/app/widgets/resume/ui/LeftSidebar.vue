<script setup lang="ts">
import { useResumeStore, useResumeSection } from '~/entities/resume';
import ExperienceForm from './components/ExperienceForm.vue';
import EducationForm from './components/EducationForm.vue';
import SkillsGroupForm from './components/SkillsGroupForm.vue';
import LanguagesForm from './components/LanguagesForm.vue';

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
        <section class="overflow-hidden rounded-xl border border-default bg-default">
            <div class="flex items-center gap-2.5 border-b border-default bg-elevated/50 px-4 py-3">
                <UIcon name="i-lucide-user-round" class="size-4 text-muted" />
                <h2 class="text-sm font-semibold">Personal details</h2>
            </div>
            <div class="space-y-4 p-4">
                <UFormField label="Full name">
                    <UInput v-model="resumeStore.personalInfo.fullname" class="w-full" placeholder="Suvonov Javohir" />
                </UFormField>
                <UFormField label="Professional title">
                    <UInput v-model="resumeStore.personalInfo.title" class="w-full"
                        placeholder="Full Stack Developer" />
                </UFormField>
                <UFormField label="Email">
                    <UInput v-model="resumeStore.personalInfo.email" class="w-full" placeholder="example@gmail.com" />
                </UFormField>
                <UFormField label="Phone">
                    <UInput v-model="resumeStore.personalInfo.phone" class="w-full" placeholder="+998..." />
                </UFormField>
                <UFormField label="Location">
                    <UInput v-model="resumeStore.personalInfo.location" class="w-full" placeholder="Tashkent" />
                </UFormField>
                <UFormField label="Website">
                    <UInput v-model="resumeStore.personalInfo.website" class="w-full" placeholder="myportfolio.com" />
                </UFormField>
                <UFormField label="LinkedIn">
                    <UInput v-model="resumeStore.personalInfo.linkedin_link" class="w-full"
                        placeholder="https://www.linkedin.com/in/..." />
                </UFormField>
                <UFormField label="GitHub">
                    <UInput v-model="resumeStore.personalInfo.github_link" class="w-full"
                        placeholder="https://github.com/..." />
                </UFormField>
                <UFormField label="Summary">
                    <UTextarea v-model="resumeStore.personalInfo.summary" :rows="4" class="w-full"
                        placeholder="Write a brief professional summary..." />
                </UFormField>
            </div>
        </section>

        <!-- ////////////////////////////////////////////////// -->
        <!-- Expreries Form-->
        <!-- ////////////////////////////////////////////////// -->
        <section class="overflow-hidden rounded-xl border border-default bg-default">
            <div class="flex items-center gap-2.5 border-b border-default bg-elevated/50 px-4 py-3">
                <UIcon name="i-lucide-briefcase-business" class="size-4 text-muted" />
                <h2 class="flex-1 text-sm font-semibold">Experience</h2>
                <span class="rounded-md bg-default px-2 py-0.5 text-xs font-medium tabular-nums text-muted">{{
                    resumeStore.personalInfo.experience?.length || 0 }}</span>
            </div>
            <div class="space-y-3 p-3">
                <div v-for="(experience, index) in resumeStore.personalInfo.experience" :key="experience.id"
                    class="rounded-lg border border-default p-3">
                    <div class="mb-3 flex items-center gap-2 border-b border-default pb-2">
                        <span class="min-w-0 flex-1 truncate text-xs font-semibold text-muted">{{ experience.position ||
                            'Experience ' + (index + 1) }}</span>
                        <UButton type="button" color="neutral" variant="ghost" size="xs" icon="i-lucide-trash-2"
                            class="shrink-0 hover:bg-error/10 hover:text-error" aria-label="Remove experience"
                            title="Remove experience" @click="removeExperince(experience.id)" />
                    </div>
                    <ExperienceForm :experience="experience" />
                </div>
                <p v-if="!resumeStore.personalInfo.experience?.length"
                    class="px-1 py-2 text-xs leading-relaxed text-muted">Add your first experience to get started.</p>
                <UButton type="button" color="neutral" variant="outline" size="sm" icon="i-lucide-plus"
                    class="w-full justify-center rounded-lg border-dashed py-2" @click="addExperience">Add experience
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
                    resumeStore.personalInfo.education?.length || 0 }}</span>
            </div>
            <div class="space-y-3 p-3">
                <div v-for="(education, index) in resumeStore.personalInfo.education" :key="education.id"
                    class="rounded-lg border border-default p-3">
                    <div class="mb-3 flex items-center gap-2 border-b border-default pb-2">
                        <span class="min-w-0 flex-1 truncate text-xs font-semibold text-muted">{{ education.degree ||
                            'Education ' + (index + 1) }}</span>
                        <UButton type="button" color="neutral" variant="ghost" size="xs" icon="i-lucide-trash-2"
                            class="shrink-0 hover:bg-error/10 hover:text-error" aria-label="Remove education"
                            title="Remove education" @click="removeEducation(education.id)" />
                    </div>
                    <EducationForm :education="education" />
                </div>
                <p v-if="!resumeStore.personalInfo.education?.length"
                    class="px-1 py-2 text-xs leading-relaxed text-muted">Add your first education to get started.</p>
                <UButton type="button" color="neutral" variant="outline" size="sm" icon="i-lucide-plus"
                    class="w-full justify-center rounded-lg border-dashed py-2" @click="addEducation">Add education
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
                    resumeStore.personalInfo.skills?.length || 0 }}</span>
            </div>
            <div class="space-y-3 p-3">
                <div v-for="(skillsGroup, index) in resumeStore.personalInfo.skills" :key="skillsGroup.id"
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
                <p v-if="!resumeStore.personalInfo.skills?.length" class="px-1 py-2 text-xs leading-relaxed text-muted">
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
                    resumeStore.personalInfo.languages?.length || 0 }}</span>
            </div>
            <div class="space-y-3 p-3">
                <div v-for="(language, index) in resumeStore.personalInfo.languages" :key="language.id"
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
                <p v-if="!resumeStore.personalInfo.languages?.length"
                    class="px-1 py-2 text-xs leading-relaxed text-muted">Add your first language to get started.</p>
                <UButton type="button" color="neutral" variant="outline" size="sm" icon="i-lucide-plus"
                    class="w-full justify-center rounded-lg border-dashed py-2" @click="addLanguage">Add language
                </UButton>
            </div>
        </section>


    </div>
</template>
