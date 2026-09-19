<script setup lang="ts">
import type { NavigationMenuItem } from '@nuxt/ui/runtime/components/NavigationMenu.vue.js'
import { UserAvatar } from '~/entities/user';
import { useLogout } from '~/features/auth/logout';

const { t, setLocale } = useI18n()
const localePath = useLocalePath()
const { loading, handle_logout } = useLogout()
const access_token = useCookie("access_token")

const items = computed<NavigationMenuItem[]>(() => [
    {
        label: t('navbar.home'),
        to: localePath("/"),
    },
    {
        label: t('navbar.about'),
        to: localePath("/about"),
    },
    {
        label: t('navbar.contact'),
        to: localePath("/contact")
    }
])
</script>

<template>
    <UHeader title="Resume Parser" :ui="{ title: 'text-primary' }">
        <UNavigationMenu :items="items" variant="link" />
        <template #right>
            <UPopover>
                <UButton icon="i-lucide-languages" color="neutral" :aria-label="t('account.language')" variant="ghost" />

                <template #content="{ close }">
                    <div class="flex flex-col gap-1 p-1 min-w-32">
                        <UButton icon="circle-flags:uz" label="Uzbek" color="neutral" @click="setLocale('uz') , close()"
                            variant="ghost" />
                        <UButton icon="circle-flags:gb" label="English" color="neutral" @click="setLocale('en') , close()"
                            variant="ghost" />
                        <UButton icon="circle-flags:ru" label="Russian" color="neutral" @click="setLocale('ru') , close()"
                            variant="ghost" />
                    </div>
                </template>
            </UPopover>
            <UColorModeButton />
            <UPopover v-if="access_token">
                <UserAvatar />
                <template #content="{close}">
                    <div class="flex flex-col gap-1 p-1 min-w-32">
                        <UButton :to="localePath('/settings')" @click="close" color="neutral" variant="ghost">
                            {{ t('account.dashboard') }}
                        </UButton>
                        <UButton :to="localePath('/profile')" @click="close" color="neutral" variant="ghost">
                            {{ t('account.profile') }}
                        </UButton>
                        <UButton :to="localePath('/resume')" @click="close" color="neutral" variant="ghost">
                            {{ t('account.resumes') }}
                        </UButton>
                        <UButton @click="handle_logout" trailing-icon="i-lucide-log-out" :disabled="loading"
                            :loading="loading" color="error" variant="ghost">{{ t('account.logout') }}</UButton>
                    </div>
                </template>
            </UPopover>
            <UButton :to="localePath('/login')" v-else>{{ t('account.login') }}</UButton>
        </template>

        <template #body>
            <UNavigationMenu :items="items" orientation="vertical" />
        </template>
    </UHeader>
</template>

<style scoped></style>