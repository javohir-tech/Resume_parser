<script setup lang="ts">
const { t, locale } = useI18n()
import type { Experience } from '~/entities/resume';
import { CalendarDate, DateFormatter, getLocalTimeZone } from '@internationalized/date'


const df = computed(() => new DateFormatter(locale.value, { month: 'long', year: 'numeric' }))

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
    // console.log(newStartDate)
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
        <UFormField :label="t('resumeEditor.position')">
            <UInput v-model="props.experience.position" class="w-full" :placeholder="t('resumeEditor.positionPlaceholder')"/>
        </UFormField>
        <UFormField :label="t('resumeEditor.company')">
            <UInput v-model="props.experience.company" class="w-full" :placeholder="t('resumeEditor.companyPlaceholder')"/>
        </UFormField>
    </div>
    <UFormField :label="t('resumeEditor.location')" class="mb-3">
        <UInput class="w-full" :placeholder="t('resumeEditor.locationPlaceholder')" v-model="props.experience.location" />
    </UFormField>
    <div class="grid gap-3 mb-3">
        <UFormField :label="t('resumeEditor.startDate')" class="w-full">
            <UPopover class="w-full">
                <UButton color="neutral" variant="outline" size="sm" icon="i-lucide-calendar" class="w-full justify-start font-normal">
                    {{ startDate ? df.format(startDate.toDate(getLocalTimeZone())) : props.experience.startDate || t('resumeEditor.selectDate') }}
                </UButton>

                <template #content>
                    <UCalendar :locale="locale" type="month" v-model="startDate" />
                </template>
            </UPopover>
        </UFormField>
        <UFormField :label="t('resumeEditor.endDate')" class="w-full">
            <UPopover class="w-full">
                <UButton color="neutral" variant="outline" size="sm" icon="i-lucide-calendar" class="w-full justify-start font-normal">
                    {{ endDate ? df.format(endDate.toDate(getLocalTimeZone())) : props.experience.endDate || t('resumeEditor.selectDate') }}
                </UButton>

                <template #content>
                    <UCalendar :locale="locale" type="month" v-model="endDate" />
                </template>
            </UPopover>
        </UFormField>
    </div>
    <UFormField :label="t('resumeEditor.description')">
        <UTextarea :rows="5" class="w-full" v-model="props.experience.description" :placeholder="t('resumeEditor.descriptionPlaceholder')"/>
    </UFormField>
</template>

