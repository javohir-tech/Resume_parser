<script setup lang="ts">
import { useResumeStore, templates } from '~/entities/resume/index.ts';
import { EntryTitleColor, HeadingColor, FontChoose } from '~/features/resume/design-edit';

const resumeStore = useResumeStore()
const open = defineModel<boolean>("open", { default: false })

const { t, locale, setLocale } = useI18n()
const languageOptions = [
    { label: 'O‘zbekcha', value: 'uz' },
    { label: 'Русский', value: 'ru' },
    { label: 'English', value: 'en' },
]

function changeLanguage(value: string) {
    if (value === 'uz' || value === 'ru' || value === 'en') return setLocale(value)
}

</script>

<template>
    <USidebar v-model:open="open" variant="sidebar" side="right" collapsible="offcanvas"
        :style="{ '--sidebar-width': '22rem' }" :ui="{
            container: 'h-full'
        }">
        <template #header>

        </template>
        <div class="flex flex-col gap-4">
            <UFormField label="Templates">
                <USelect v-model.nullable="resumeStore.designInfo.template" :items="templates"
                    icon="i-lucide-layout-template" class="w-full" />
            </UFormField>

            <UFormField :label="t('resumeDocument.language')">
                <USelect :model-value="locale" :items="languageOptions" value-key="value" icon="i-lucide-languages"
                    class="w-full" @update:model-value="changeLanguage" />
            </UFormField>

            <!-- Section Header -->
            <HeadingColor />

            <!-- Entry Title-->
            <EntryTitleColor />

            <!-- Font choose -->
            <FontChoose />

            <!-- Restart Button -->
            <div>
                <h1 class="text-sm font-medium mb-3">
                    Default Desing
                </h1>
                <UButton @click="resumeStore.restartDesign" label="Restart" color="neutral" variant="outline"
                    icon="i-lucide-rotate-ccw" class="w-full" />
            </div>

            <div>
                <h1 class="text-sm font-medium mb-3">Resume</h1>
                <div class="flex justify-between item-center gap-x-3">
                    <UButton :disabled="!resumeStore.resume.id"
                        :to="resumeStore.resume.id ? `/resume/${resumeStore.resume.id}/view` : ''" block label="View"
                        icon="i-lucide-eye" variant="outline" color="neutral" />
                    <UButton block label="Download" icon="i-lucide-download" variant="outline" color="neutral" />
                </div>
            </div>
        </div>
    </USidebar>
</template>
