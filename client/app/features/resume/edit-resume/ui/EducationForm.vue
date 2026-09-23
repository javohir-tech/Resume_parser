<script setup lang="ts">
const { t } = useI18n()
import type { Education } from '~/entities/resume'
import { CalendarDate, DateFormatter, getLocalTimeZone } from '@internationalized/date'
import { useEducationSaveAvto } from '../models/useEducationAvtoSave'

const { start, flush } = useEducationSaveAvto()


const ready = ref(false)
const router = useRouter()
let removeGuard: (() => void) | null

const df = new DateFormatter('en-US', { month: 'long', year: 'numeric' })

const monthFormatter = new DateFormatter('en-US', {
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

onMounted(() => {
    if (props.education.id) {
        ready.value = start(props.education.id)
    }

    removeGuard = router.beforeEach(async () => {
        if (!ready.value) return true

        return await flush()
    })
})

onScopeDispose(() => {
    removeGuard?.()
})




</script>

<template>
    <div class="flex flex-col gap-3">
        <UFormField :label="t('resumeEditor.degree')">
            <UInput v-model="props.education.degree" class="w-full"
                :placeholder="t('resumeEditor.degreePlaceholder')" />
        </UFormField>
        <UFormField :label="t('resumeEditor.institution')">
            <UInput class="w-full" v-model="props.education.institution"
                :placeholder="t('resumeEditor.institutionPlaceholder')" />
        </UFormField>
        <UFormField :label="t('resumeEditor.fieldOfStudy')">
            <UInput class="w-full" v-model="props.education.fieldOfStudy"
                :placeholder="t('resumeEditor.fieldPlaceholder')" />
        </UFormField>
        <div class="grid gap-3">
            <UFormField :label="t('resumeEditor.startDate')" class="w-full">
                <UPopover class="w-full">
                    <UButton color="neutral" variant="outline" size="sm" icon="i-lucide-calendar"
                        class="w-full justify-start font-normal">
                        {{ startDate ? df.format(startDate.toDate(getLocalTimeZone())) : props.education.startDate ||
                            'Select a date' }}
                    </UButton>

                    <template #content>
                        <UCalendar locale="en-US" type="month" v-model="startDate" />
                    </template>
                </UPopover>
            </UFormField>
            <UFormField :label="t('resumeEditor.endDate')" class="w-full">
                <UPopover class="w-full">
                    <UButton color="neutral" variant="outline" size="sm" icon="i-lucide-calendar"
                        class="w-full justify-start font-normal">
                        {{ endDate
                            ?
                            df.format(endDate.toDate(getLocalTimeZone()))
                            : props.education.endDate || 'Selecta date' }}
                    </UButton>

                    <template #content>
                        <UCalendar locale="en-US" type="month" v-model="endDate" />
                    </template>
                </UPopover>
            </UFormField>
        </div>
        <UFormField :label="t('resumeEditor.location')">
            <UInput class="w-full" v-model="props.education.location"
                :placeholder="t('resumeEditor.locationPlaceholder')" />
        </UFormField>
    </div>
</template>
