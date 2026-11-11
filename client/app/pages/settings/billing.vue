<script setup lang="ts">
const { t } = useI18n()

definePageMeta({
    layout: "settings"
})
</script>

<template>
    <div class="mx-auto flex w-full max-w-4xl flex-col gap-8">
        <header>
            <h1 class="m-0 text-3xl font-bold tracking-tight text-highlighted">{{ t('settings.billing.title') }}</h1>
        </header>
        <section class="min-h-18 rounded-2xl border border-default bg-default p-5 text-default">
            {{ t('settings.billing.title') }}
        </section>
    </div>
</template>
