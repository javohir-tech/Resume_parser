<script setup lang="ts">
import { useResumeStore, useCreateSection } from '~/entities/resume';
import ExperienceForm from './components/ExperienceForm.vue';
const resumeStore = useResumeStore()
const { addExperience } = useCreateSection()

import { CalendarDate, DateFormatter, getLocalTimeZone } from '@internationalized/date'


const df = new DateFormatter('en-US', {
    dateStyle: 'medium'
})

const modelValue = shallowRef(new CalendarDate(2022, 1, 10))

</script>

<template>
    <div class="flex flex-col gap-4">

        <UFormField label="Ismingiz">
            <UInput v-model="resumeStore.personalInfo.fullname" class="w-full" placeholder="full name" />
        </UFormField>
        <UFormField label="Title">
            <UInput v-model="resumeStore.personalInfo.title" class="w-full" placeholder="title" />
        </UFormField>
        <UFormField label="Email">
            <UInput v-model="resumeStore.personalInfo.email" placeholder="email" class="w-full" />
        </UFormField>
        <UFormField label="Phone">
            <UInput v-model="resumeStore.personalInfo.phone" class="w-full" placeholder="phone" />
        </UFormField>
        <UFormField label="Location">
            <UInput v-model="resumeStore.personalInfo.location" placeholder="location" class="w-full" />
        </UFormField>
        <UFormField label="Your website">
            <UInput v-model="resumeStore.personalInfo.website" placeholder="website" class="w-full" />
        </UFormField>
        <UFormField label="Summary">
            <UTextarea :rows="4" class="w-full" v-model="resumeStore.personalInfo.summary" />
        </UFormField>

        <div class="" v-for="experience in resumeStore.personalInfo.experience" :key="experience.id">
            <div class="flex gap-2 justify-between items-center mb-3">
                <UFormField label="Postion">
                    <UInput v-model="experience.position" />
                </UFormField>
                <UFormField label="Compony">
                    <UInput v-model="experience.company" />
                </UFormField>
            </div>
            <UFormField label="location" class="mb-3">
                <UInput class="w-full" placeholder="Location" v-model="experience.location" />
            </UFormField>
            <div class="flex gap-2 justify-beetween items-center mb-3">
                <UFormField label="Start Date" class="w-full">
                    <UPopover class="w-full">
                        <UButton color="neutral" variant="subtle" icon="i-lucide-calendar">
                            {{ modelValue ? df.format(modelValue.toDate(getLocalTimeZone())) : 'Select a date' }}
                        </UButton>

                        <template #content>
                            <UCalendar v-model="modelValue" />
                        </template>
                    </UPopover>
                </UFormField>
                <UFormField label="End Date" class="w-full">
                    <UPopover class="w-full">
                        <UButton color="neutral" variant="subtle" icon="i-lucide-calendar">
                            {{ modelValue ? df.format(modelValue.toDate(getLocalTimeZone())) : 'Select a date' }}
                        </UButton>

                        <template #content>
                            <UCalendar v-model="modelValue" />
                        </template>
                    </UPopover>
                </UFormField>
            </div>
            <UFormField label="Education">
                <UTextarea :rows="5" class="w-full" v-model="experience.description" />
            </UFormField>
        </div>

        <UButton @click="addExperience">Experience qoshish</UButton>
    </div>
</template>
