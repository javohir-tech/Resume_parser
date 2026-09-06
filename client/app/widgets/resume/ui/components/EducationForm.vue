<script setup lang="ts">
import type { Education } from '~/entities/resume'
import { CalendarDate, DateFormatter, getLocalTimeZone } from '@internationalized/date'

const df = new DateFormatter("us-US", {
    month: "long",
    year: "numeric"
})

const monthFormatter = new DateFormatter("us-Us", {
    month: "long"
})

const startDate = ref<CalendarDate>()
const endDate = ref<CalendarDate>()

const props = defineProps<{
    education: Education
}>()

watch(startDate, (newDate) => {
    if (!newDate) return
    const month = monthFormatter.format(newDate.toDate(getLocalTimeZone()))
    const newStartDate = `${month} ${newDate.year}`
    props.education.startDate = newStartDate
})

watch(endDate, (newDate) => {
    if (!newDate) return
    const month = monthFormatter.format(newDate.toDate(getLocalTimeZone()))
    const newEndDate = `${month} ${newDate.year}`
    props.education.endDate = newEndDate
})




</script>

<template>
    <div class="flex flex-col gap-4">
        <UFormField label="Field of study">
            <UInput class="w-full" v-model="props.education.fieldOfStudy" />
        </UFormField>
        <UFormField label="Institution">
            <UInput class="w-full" v-model="props.education.institution" />
        </UFormField>
        <div class="flex justify-between items-center gap-4">
            <UFormField label="Start Date" class="w-full">
                <UPopover class="w-full">
                    <UButton color="neutral" variant="subtle" icon="i-lucide-calendar">
                        {{ startDate ? df.format(startDate.toDate(getLocalTimeZone())) : 'Select a date' }}
                    </UButton>

                    <template #content>
                        <UCalendar type="month" v-model="startDate" />
                    </template>
                </UPopover>
            </UFormField>
            <UFormField label="End Date" class="w-full">
                <UPopover class="w-full">
                    <UButton color="neutral" variant="subtle" icon="i-lucide-calendar">
                        {{ endDate ? df.format(endDate.toDate(getLocalTimeZone())) : 'Select a date' }}
                    </UButton>

                    <template #content>
                        <UCalendar type="month" v-model="endDate" />
                    </template>
                </UPopover>
            </UFormField>
        </div>
        <UFormField label="Location">
            <UInput class="w-full" v-model="props.education.location" />
        </UFormField>
    </div>
</template>