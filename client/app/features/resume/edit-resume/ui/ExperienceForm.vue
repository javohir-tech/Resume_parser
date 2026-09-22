<script setup lang="ts">
const { t } = useI18n()
import type { Experience } from '~/entities/resume';
import { CalendarDate, DateFormatter, getLocalTimeZone } from '@internationalized/date'
import { useExperienceAvtoSave } from '../models/useExperienceAvtoSave';

const { start, flush } = useExperienceAvtoSave(800)


const df = new DateFormatter('en-US', { month: 'long', year: 'numeric' })
const ready = ref(false)
const router = useRouter()

let removeGuard : (()=> void) | undefined

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

watch(endDate, (newDate) => {
    if (!newDate) return
    const month = monthFormatter.format(
        newDate?.toDate(getLocalTimeZone())
    )
    const newEndDate = `${month} ${newDate.year}`
    props.experience.endDate = newEndDate
})

onMounted(() => {
    const experience_id = props.experience.id

    if (experience_id) {
        ready.value = start(experience_id)
    }

    removeGuard = router.beforeEach(async ()=>{
        if(!ready.value) return true

        return await flush()
    })
})

onScopeDispose(()=>{
    removeGuard?.()
})

</script>

<template>
    <div class="space-y-3 mb-3">
        <UFormField :label="t('resumeEditor.position')">
            <UInput v-model="props.experience.position" class="w-full"
                :placeholder="t('resumeEditor.positionPlaceholder')" />
        </UFormField>
        <UFormField :label="t('resumeEditor.company')">
            <UInput v-model="props.experience.company" class="w-full"
                :placeholder="t('resumeEditor.companyPlaceholder')" />
        </UFormField>
    </div>
    <UFormField :label="t('resumeEditor.location')" class="mb-3">
        <UInput class="w-full" :placeholder="t('resumeEditor.locationPlaceholder')"
            v-model="props.experience.location" />
    </UFormField>
    <div class="grid gap-3 mb-3">
        <UFormField :label="t('resumeEditor.startDate')" class="w-full">
            <UPopover class="w-full">
                <UButton color="neutral" variant="outline" size="sm" icon="i-lucide-calendar"
                    class="w-full justify-start font-normal">
                    {{ startDate ? df.format(startDate.toDate(getLocalTimeZone())) : props.experience.startDate ||
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
                    {{ endDate ? df.format(endDate.toDate(getLocalTimeZone())) : props.experience.endDate ||
                        'Select a date' }}
                </UButton>

                <template #content>
                    <UCalendar locale="en-US" type="month" v-model="endDate" />
                </template>
            </UPopover>
        </UFormField>
    </div>
    <UFormField :label="t('resumeEditor.description')">
        <UTextarea :rows="5" class="w-full" v-model="props.experience.description"
            :placeholder="t('resumeEditor.descriptionPlaceholder')" />
    </UFormField>
</template>
