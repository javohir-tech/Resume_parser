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
    <div class="space-y-3 mb-3">
        <UFormField label="Position">
            <UInput v-model="props.experience.position" class="w-full" placeholder="Frontend Developer"/>
        </UFormField>
        <UFormField label="Company">
            <UInput v-model="props.experience.company" class="w-full" placeholder="Google, Meta, Amazon..."/>
        </UFormField>
    </div>
    <UFormField label="Location" class="mb-3">
        <UInput class="w-full" placeholder="Tashkent..." v-model="props.experience.location" />
    </UFormField>
    <div class="grid gap-3 mb-3">
        <UFormField label="Start Date" class="w-full">
            <UPopover class="w-full">
                <UButton color="neutral" variant="outline" size="sm" icon="i-lucide-calendar" class="w-full justify-start font-normal">
                    {{ startDate ? df.format(startDate.toDate(getLocalTimeZone())) : props.experience.startDate || 'Select a date' }}
                </UButton>

                <template #content>
                    <UCalendar type="month" v-model="startDate" />
                </template>
            </UPopover>
        </UFormField>
        <UFormField label="End Date" class="w-full">
            <UPopover class="w-full">
                <UButton color="neutral" variant="outline" size="sm" icon="i-lucide-calendar" class="w-full justify-start font-normal">
                    {{ endDate ? df.format(endDate.toDate(getLocalTimeZone())) : props.experience.endDate || 'Select a date' }}
                </UButton>

                <template #content>
                    <UCalendar type="month" v-model="endDate" />
                </template>
            </UPopover>
        </UFormField>
    </div>
    <UFormField label="Description">
        <UTextarea :rows="5" class="w-full" v-model="props.experience.description" placeholder="Describe your role, responsibilities, and key achievements..."/>
    </UFormField>
</template>

