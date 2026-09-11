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
    <div class="flex flex-col gap-3">
        <UFormField label="Degree">
            <UInput v-model="props.education.degree" class="w-full" placeholder="Bachelor's degree..." />
        </UFormField>
        <UFormField label="Institution">
            <UInput class="w-full" v-model="props.education.institution"
                placeholder="Tashkent University of Information Technologies ..." />
        </UFormField>
        <UFormField label="Field of study">
            <UInput class="w-full" v-model="props.education.fieldOfStudy" placeholder=" Electrical power engineer..." />
        </UFormField>
        <div class="grid gap-3">
            <UFormField label="Start Date" class="w-full">
                <UPopover class="w-full">
                    <UButton color="neutral" variant="outline" size="sm" icon="i-lucide-calendar" class="w-full justify-start font-normal">
                        {{ startDate ? df.format(startDate.toDate(getLocalTimeZone())) : props.education.startDate || 'Select a date' }}
                    </UButton>

                    <template #content>
                        <UCalendar type="month" v-model="startDate" />
                    </template>
                </UPopover>
            </UFormField>
            <UFormField label="End Date" class="w-full">
                <UPopover class="w-full">
                    <UButton color="neutral" variant="outline" size="sm" icon="i-lucide-calendar" class="w-full justify-start font-normal">
                        {{ endDate ? df.format(endDate.toDate(getLocalTimeZone())) : props.education.endDate || 'Select a date' }}
                    </UButton>

                    <template #content>
                        <UCalendar type="month" v-model="endDate" />
                    </template>
                </UPopover>
            </UFormField>
        </div>
        <UFormField label="Location">
            <UInput class="w-full" v-model="props.education.location" placeholder="Tashkent..."/>
        </UFormField>
    </div>
</template>

