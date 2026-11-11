<script setup lang="ts">
import { PrimaryColorPicker } from '~/features/theme/change-primary-color';
import { NeutralColorPicker } from '~/features/theme/change-neutral-color';
import { FontPicker } from '~/features/theme/change-font';
import { RestartTheme } from '~/features/theme/restart';
const { t } = useI18n()

definePageMeta({
    middleware: "auth",
    layout: "settings"
})

</script>

<template>
    <div class="mx-auto flex w-full max-w-4xl flex-col gap-8">
        <header>
            <h1 class="m-0 text-3xl font-bold tracking-tight text-highlighted">{{ t('settings.appearance.title') }}</h1>
        </header>

        <section class="flex flex-col gap-3">
            <h2 class="m-0 text-base font-semibold text-highlighted">{{ t('settings.general') }}</h2>
            <div class="overflow-hidden rounded-2xl border border-default bg-default text-default">
                <div class="px-5 py-2.5"><PrimaryColorPicker /></div>
                <div class="border-t border-default px-5 py-2.5"><NeutralColorPicker /></div>
                <div class="border-t border-default px-5 py-2.5"><FontPicker /></div>
            </div>
        </section>

        <section class="flex items-center justify-between gap-6 rounded-2xl border border-default bg-default px-5 py-4 text-default max-sm:flex-col max-sm:items-start">
            <div>
                <h2 class="m-0 text-base font-semibold text-highlighted">{{ t('settings.appearance.resetTitle') }}</h2>
                <p class="mt-1 text-sm leading-6 text-muted">{{ t('settings.appearance.resetDescription') }}</p>
            </div>
            <RestartTheme />
        </section>
    </div>
</template>
