<script setup lang="ts">
import type { NavigationMenuItem } from '@nuxt/ui/runtime/components/NavigationMenu.vue.js'
import { UserAvatar } from '~/entities/user';
import { useLogout } from '~/features/auth/logout';

const { t, setLocale } = useI18n()
const { loading, handle_logout } = useLogout()
const access_token = useCookie("access_token")

const items = computed<NavigationMenuItem[]>(() => [
    {
        label: t('navbar.home'),
        to: "/",
    },
    {
        label: t('navbar.about'),
        to: "/about",
    },
    {
        label: t('navbar.contact'),
        to: "/contact"
    }
])
</script>

<template>
    <UHeader title="Resume Parser" :ui="{ title: 'text-primary' }">
        <UNavigationMenu :items="items" variant="link" />
        <template #right>
            <UPopover>
                <UButton icon="i-lucide-languages" color="neutral" variant="ghost" />

                <template #content>
                    <div class="flex flex-col gap-1 p-1 min-w-32">
                        <UButton icon="circle-flags:uz" label="Uzbek" color="neutral" @click="setLocale('uz')"
                            variant="ghost" />
                        <UButton icon="circle-flags:gb" label="English" color="neutral" @click="setLocale('en')"
                            variant="ghost" />
                        <UButton icon="circle-flags:ru" label="Russian" color="neutral" @click="setLocale('ru')"
                            variant="ghost" />
                    </div>
                </template>
            </UPopover>
            <UColorModeButton />
            <UPopover v-if="access_token">
                <UserAvatar />
                <template #content>
                    <div class="flex flex-col gap-1 p-1 min-w-32">
                        <UButton to="/settings" color="neutral" variant="ghost">
                            dashboard
                        </UButton>
                        <UButton @click="handle_logout" trailing-icon="i-lucide-log-out" :disabled="loading" :loading="loading" color="error"
                            variant="ghost">Logout</UButton>
                    </div>
                </template>
            </UPopover>
            <UButton to="/login" v-else>Kirish</UButton>
        </template>

        <template #body>
            <UNavigationMenu :items="items" orientation="vertical" />
        </template>
    </UHeader>
</template>

<style scoped>

</style>