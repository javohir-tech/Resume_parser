<script setup lang="ts">
const localPath = useLocalePath()
const { t } = useI18n()

</script>

<template>
    <NuxtLayout name="default">
        <div class="min-h-[calc(100vh-8rem)] py-6 sm:py-8">
            <UContainer class="mx-auto w-full max-w-7xl px-4 sm:px-6">
                <div class="grid min-h-[calc(100vh-11rem)] grid-cols-1 overflow-hidden rounded-2xl border border-default bg-default text-default shadow-sm lg:grid-cols-[260px_minmax(0,1fr)]">
                    <aside class="border-b border-default bg-muted/40 p-4 lg:border-b-0 lg:border-r lg:p-6">
                        <h1 class="mb-4 px-2 text-xl font-bold tracking-tight text-highlighted">{{ t('settings.title')
                            }}</h1>
                        <nav class="flex w-full gap-1 lg:flex-col" :aria-label="t('settings.navigation')">
                            <UButton
                                class="min-w-0 flex-1 flex-col justify-center gap-1 rounded-xl px-1 py-2 text-center text-[10px] leading-tight hover:bg-elevated [&.router-link-exact-active]:bg-elevated [&.router-link-exact-active]:font-semibold lg:w-full lg:flex-row lg:justify-start lg:gap-2 lg:px-3 lg:py-2.5 lg:text-left lg:text-sm"
                                :to="localPath('/settings/account')" icon="i-lucide-user" color="neutral"
                                variant="ghost" active-color="primary" active-variant="soft">
                                {{ t('settings.account.title') }}
                            </UButton>
                            <UButton
                                class="min-w-0 flex-1 flex-col justify-center gap-1 rounded-xl px-1 py-2 text-center text-[10px] leading-tight hover:bg-elevated [&.router-link-exact-active]:bg-elevated [&.router-link-exact-active]:font-semibold lg:w-full lg:flex-row lg:justify-start lg:gap-2 lg:px-3 lg:py-2.5 lg:text-left lg:text-sm"
                                :to="localPath('/settings/appearance')" icon="i-lucide-palette" color="neutral"
                                variant="ghost" active-color="primary" active-variant="soft">
                                {{ t('settings.appearance.title') }}
                            </UButton>
                            <UButton
                                class="min-w-0 flex-1 flex-col justify-center gap-1 rounded-xl px-1 py-2 text-center text-[10px] leading-tight hover:bg-elevated [&.router-link-exact-active]:bg-elevated [&.router-link-exact-active]:font-semibold lg:w-full lg:flex-row lg:justify-start lg:gap-2 lg:px-3 lg:py-2.5 lg:text-left lg:text-sm"
                                :to="localPath('/settings/billing')" icon="i-lucide-credit-card" color="neutral"
                                variant="ghost" active-color="primary" active-variant="soft">
                                {{ t('settings.billing.title') }}
                            </UButton>
                            <UButton
                                class="min-w-0 flex-1 flex-col justify-center gap-1 rounded-xl px-1 py-2 text-center text-[10px] leading-tight hover:bg-elevated [&.router-link-exact-active]:bg-elevated [&.router-link-exact-active]:font-semibold lg:w-full lg:flex-row lg:justify-start lg:gap-2 lg:px-3 lg:py-2.5 lg:text-left lg:text-sm"
                                :to="localPath('/settings/devices')" icon="i-lucide-monitor-smartphone" color="neutral"
                                variant="ghost" active-color="primary" active-variant="soft">
                                {{ t('profile.sessions.title') }}
                            </UButton>
                        </nav>
                    </aside>
                    <main class="min-w-0 px-5 py-7 sm:px-8 sm:py-10 lg:px-16 xl:px-20">
                        <slot />
                    </main>
                </div>
            </UContainer>
        </div>
    </NuxtLayout>
</template>
