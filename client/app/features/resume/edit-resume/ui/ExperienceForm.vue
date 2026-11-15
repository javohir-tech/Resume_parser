<script setup lang="ts">
import type { Experience } from '~/entities/resume';
import { getJobTitles } from '~/entities/job-title';
import { CalendarDate, DateFormatter, getLocalTimeZone } from '@internationalized/date'
import { useExperienceAvtoSave } from '../models/useExperienceAvtoSave';
import { INPUT_LIMITS } from '~/shared/constants';

const { start, flush } = useExperienceAvtoSave(800)

const { t } = useI18n()

const df = new DateFormatter('en-US', { month: 'long', year: 'numeric' })
const ready = ref(false)
const router = useRouter()

let removeGuard: (() => void) | undefined

const monthFormatter = new DateFormatter('en-US', {
    month: 'long'
})

const startDate = ref<CalendarDate>()
const endDate = ref<CalendarDate>()
const isPresent = ref<boolean>(false)
const positionOpenRequested = ref(false)

const props = defineProps<{
    experience: Experience
}>()

const positionSearch = computed(() => props.experience.position.trim())
const debouncedSearch = refDebounced(positionSearch, 300)
const filterKey = computed(() => `job_titles_${debouncedSearch.value}`)

const { data, status, error } = useLazyAsyncData(filterKey, async (_nuxtApp, { signal }) => {
    const search = debouncedSearch.value

    return {
        search,
        items: search ? await getJobTitles({ search }, signal) : [],
    }
}, {
    deep: false,
    default: () => ({ search: '', items: [] }),
    dedupe: "cancel"
})

const isLoading = computed(() => Boolean(positionSearch.value) && (
    positionSearch.value !== debouncedSearch.value || status.value === 'pending'
))

const positionItems = computed(() => {
    // Never offer results from an earlier query while the user continues typing.
    if (!positionSearch.value || isLoading.value || data.value.search !== positionSearch.value || error.value) return []

    return [...new Set(data.value.items
        .map(item => item.title.trim())
        .filter(title => title && title.length <= INPUT_LIMITS.experience.position))]
})

const positionOpen = computed({
    get: () => positionOpenRequested.value && (isLoading.value || positionItems.value.length > 0),
    set: (open: boolean) => { positionOpenRequested.value = open },
})

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

watch(isPresent, (value) => {
    if (!value) return

    props.experience.endDate = ""
    endDate.value = undefined
})

onMounted(() => {
    const experience_id = props.experience.id

    if (experience_id) {
        ready.value = start(experience_id)
    }

    removeGuard = router.beforeEach(async () => {
        if (!ready.value) return true

        const result = await flush()
        if (result) return true

        return import.meta.client && window.confirm(t('resumeEditor.leaveWithoutSavingConfirm'))
    })
})

onScopeDispose(() => {
    removeGuard?.()
})

</script>

<template>

    <div class="space-y-3 my-3">
        <UFormField :label="t('resumeEditor.position')">
            <UInputMenu v-model="props.experience.position" v-model:open="positionOpen" mode="autocomplete"
                :items="positionItems" ignore-filter :trailing="false"
                :maxlength="INPUT_LIMITS.experience.position" :reset-search-term-on-blur="false"
                open-on-focus open-on-click class="w-full" :placeholder="t('resumeEditor.positionPlaceholder')"
                @keydown.tab="positionOpen = false">
                <template #empty>
                    <div v-if="isLoading" class="flex items-center justify-center py-1" role="status" aria-live="polite">
                        <UIcon name="i-lucide-loader-circle" class="size-5 animate-spin" aria-hidden="true" />
                        <span class="sr-only">{{ t('resumeEditor.positionSearchLoading') }}</span>
                    </div>
                </template>
            </UInputMenu>
        </UFormField>
        <UFormField :label="t('resumeEditor.company')">
            <UInput :maxlength="INPUT_LIMITS.experience.company" v-model="props.experience.company" class="w-full"
                :placeholder="t('resumeEditor.companyPlaceholder')" />
        </UFormField>
    </div>

    <UFormField :label="t('resumeEditor.location')" class="mb-3">
        <UInput :maxlength="INPUT_LIMITS.experience.location" class="w-full"
            :placeholder="t('resumeEditor.locationPlaceholder')" v-model="props.experience.location" />
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

        <UCheckbox v-model="isPresent" label="Present" />

        <UFormField :label="t('resumeEditor.endDate')" class="w-full">
            <UPopover class="w-full">
                <UButton :disabled="isPresent" color="neutral" variant="outline" size="sm" icon="i-lucide-calendar"
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
        <UTextarea :maxlength="INPUT_LIMITS.experience.description" :rows="8" class="w-full"
            v-model="props.experience.description" :placeholder="t('resumeEditor.descriptionPlaceholder')" autoresize />
    </UFormField>

</template>
