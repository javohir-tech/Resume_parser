<script setup lang="ts">
import type { Experience } from '~/entities/resume';
import { CalendarDate, DateFormatter, getLocalTimeZone } from '@internationalized/date'


const df = new DateFormatter('en-US', {
    month: "long",
    year: "numeric"
})

const monthFormatter = new DateFormatter('en-US', {
    month: 'long'
})

const startDate = ref<CalendarDate>()
const endDate = ref<CalendarDate>()

const props = defineProps<{
    experience: Experience
}>()
watch(startDate, (newDate) => {
    if (!newDate) return
    const month = monthFormatter.format(
        newDate?.toDate(getLocalTimeZone())
    )
    const newStartDate = `${month} ${newDate.year}`
    console.log(newStartDate)
    props.experience.startDate = newStartDate
})

watch(endDate , (newDate)=>{
    if (!newDate) return
    const month = monthFormatter.format(
        newDate?.toDate(getLocalTimeZone())
    )
    const newEndDate = `${month} ${newDate.year}`
    props.experience.endDate = newEndDate
})

</script>

<template>
    <div class="flex gap-2 just ify-between items-center mb-3">
        <UFormField label="Postion">
            <UInput v-model="props.experience.position" />
        </UFormField>
        <UFormField label="Compony">
            <UInput v-model="props.experience.company" />
        </UFormField>
    </div>
    <UFormField label="location" class="mb-3">
        <UInput class="w-full" placeholder="Location" v-model="props.experience.location" />
    </UFormField>
    <div class="flex gap-2 justify-beetween items-center mb-3">
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
    <UFormField label="Education">
        <UTextarea :rows="5" class="w-full" v-model="props.experience.description" />
    </UFormField>
</template>