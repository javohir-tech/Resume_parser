<script setup lang="ts">
const { t } = useI18n()
import {  type SkillGroup } from '~/entities/resume';

import { useSkillItem } from '../models/useSkillItem';

import { INPUT_LIMITS } from '~/shared/constants';

import { useSkillsGroupAvtoSave } from '../models/useSkillsGroupAvtoSave';

import { getSkillCategoriesRequest } from '~/entities/skills-category';

const { isCreating, createSkillItem, isDeleting, deleteSkillItem, } = useSkillItem()
const { start, flush } = useSkillsGroupAvtoSave()

const props = defineProps<{
    skillsGroup: SkillGroup
}>()

const skill = ref<string>()
const ready = ref(false)
const router = useRouter()
let removeGuard: (() => void) | undefined

const categorySearch = computed(() => props.skillsGroup.title.trim())
const debouncedSearch = refDebounced(categorySearch, 800)
const categoryOpenRequest = ref(false)

const searchedKeys = computed(() => `skills_category_${debouncedSearch.value}`)

const { data, status, error } = useLazyAsyncData(searchedKeys, async (_nuxtApp, { signal }) => {
    const search = debouncedSearch.value

    return {
        search,
        items: search ? await getSkillCategoriesRequest({ search }, signal) : []
    }
}, {
    deep: false,
    default: () => ({ search: "", items: [] }),
    dedupe: "cancel"
})

function handleAddSkill() {
    if (!skill.value?.trim()) return
    createSkillItem(props.skillsGroup.id, { skill: skill.value.trim() })
    skill.value = ""
}

const isLoading = computed(() => Boolean(categorySearch.value) && (categorySearch.value !== debouncedSearch.value || status.value === "pending"))

const categoriesItems = computed(() => {
    if (!categorySearch.value || isLoading.value || data.value.search !== categorySearch.value || error.value) return []

    return [...new Set(data.value.items
        .map(item => item.title.trim())
        .filter(title => title && title.length <= INPUT_LIMITS.skills_group.title))]
})

const categoryOpen = computed({
    get: () => categoryOpenRequest.value && (isLoading.value || categoriesItems.value.length > 0),
    set: (open: boolean) => { categoryOpenRequest.value = open }
})


onMounted(() => {
    const skills_group_id = props.skillsGroup.id

    if (skills_group_id) {
        ready.value = start(skills_group_id)
    }

    removeGuard = router.beforeEach(async () => {
        if (!ready.value) return true

        const result = await flush()
        if (result) return true

        return import.meta.client && window.confirm("resumeEditor.leaveWithoutSavingConfirm")
    })
})

onScopeDispose(() => {
    removeGuard?.()
})

</script>

<template>
    <div class="flex flex-col gap-3 mt-3">
        <UFormField :label="t('resumeEditor.skillCategory')" :description="t('resumeEditor.categoryHint')">
            <UInputMenu v-model="props.skillsGroup.title" v-model:open="categoryOpen" mode="autocomplete"
                :items="categoriesItems" ignore-filter :trailing="false"
                :maxlength="INPUT_LIMITS.experience.position" :reset-search-term-on-blur="false"
                open-on-focus open-on-click class="w-full" :placeholder="t('resumeEditor.positionPlaceholder')"
                @keydown.tab="categoryOpen = false">
                <template #empty>
                    <div v-if="isLoading" class="flex items-center justify-center py-1" role="status" aria-live="polite">
                        <UIcon name="i-lucide-loader-circle" class="size-5 animate-spin" aria-hidden="true" />
                        <span class="sr-only">{{ t('resumeEditor.positionSearchLoading') }}</span>
                    </div>
                </template>
            </UInputMenu>
        </UFormField>
        <div v-if="skillsGroup.skills.length" class="flex flex-wrap gap-1.5">
            <UButton v-for="skill in skillsGroup.skills" :key="skill.id" type="button"
                @click="deleteSkillItem(skillsGroup.id, skill.id)" :loading="isDeleting(skill.id)"
                :disabled="isDeleting(skill.id)" trailing-icon="i-lucide-x" color="neutral" variant="subtle" size="xs"
                :aria-label="t('resumeEditor.removeSkill', { skill: skill.skill })" class="rounded-md">{{ skill.skill }}
            </UButton>
        </div>
        <UForm @submit="handleAddSkill">
            <UFormField :label="t('resumeEditor.skill')">
                <div class="flex gap-2">
                    <UInput :maxlength="INPUT_LIMITS.skill_item.skill" v-model="skill" class="min-w-0 flex-1"
                        :placeholder="t('resumeEditor.skillPlaceholder')" />
                    <UButton type="submit" color="neutral" variant="outline" icon="i-lucide-plus"
                        :disabled="!skill?.trim() || isCreating" :loading="isCreating"
                        :aria-label="t('resumeEditor.addSkill')" :title="t('resumeEditor.addSkill')" />
                </div>
            </UFormField>
        </UForm>
    </div>
</template>
