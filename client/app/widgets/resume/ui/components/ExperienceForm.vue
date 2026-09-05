<script setup lang="ts">
import type { Experience } from '~/entities/resume';
import { CalendarDate, DateFormatter, getLocalTimeZone } from '@internationalized/date'


const df = new DateFormatter('en-US', {
    dateStyle: 'medium'
})

const modelValue = shallowRef(new CalendarDate(2022, 1, 10))

const experience = defineModel<Experience>({ required: true })

</script>

<template>
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
</template>