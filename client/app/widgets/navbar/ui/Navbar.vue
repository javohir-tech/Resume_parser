<script setup lang="ts">
import type { NavigationMenuItem } from '@nuxt/ui/runtime/components/NavigationMenu.vue.js'
import { useLogout } from '~/features/auth/logout';

const { t, setLocale } = useI18n()
const localePath = useLocalePath()
const { loading, handle_logout } = useLogout()
const access_token = useCookie("access_token")

const open = ref<boolean>(false)

</script>

<template>
    <UHeader title="Resume Parser" :toggle="false" :ui="{ title: 'text-primary' }">
        <!-- <UNavigationMenu :items="items" variant="link" /> -->
        <template #right>
            <UPopover>
                <UButton icon="i-lucide-languages" color="neutral" :aria-label="t('account.language')"
                    variant="ghost" />

                <template #content="{ close }">
                    <div class="flex flex-col gap-1 p-1 min-w-32">
                        <UButton icon="circle-flags:uz" label="Uzbek" color="neutral" @click="setLocale('uz'), close()"
                            variant="ghost" />
                        <UButton icon="circle-flags:gb" label="English" color="neutral"
                            @click="setLocale('en'), close()" variant="ghost" />
                        <UButton icon="circle-flags:ru" label="Russian" color="neutral"
                            @click="setLocale('ru'), close()" variant="ghost" />
                    </div>
                </template>
            </UPopover>
            <UColorModeButton />
            <UPopover v-if="access_token" :content="{ side: 'bottom', align: 'end', sideOffset: 8 }">
                <UButton icon="i-lucide-menu" variant="ghost" color="neutral" />
                <template #content="{ close }">
                    <div class="flex flex-col gap-1 p-1 min-w-32">
                        <UButton :to="localePath('/settings')" icon="i-lucide-settings" @click="close" color="neutral"
                            variant="ghost" active-color="primary">
                            {{ t('account.settings') }}
                        </UButton>
                        <UButton :to="localePath('/resume')" icon="i-lucide-files" @click="close" color="neutral"
                            variant="ghost" active-color="primary">
                            {{ t('account.resumes') }}
                        </UButton>
                        <UButton :to="localePath('/job-match')" icon="i-lucide-wand-sparkles" @click="close"
                            color="neutral" variant="ghost" active-color="primary">
                            <!-- {{ t('account.resumes') }} -->
                            moslashtirish
                        </UButton>
                        <UModal v-model:open="open" :title="t('account.logoutConfirmTitle')"
                            :description="t('account.logoutConfirmDescription')"
                            :ui="{ content: 'max-w-sm rounded-2xl', header: 'p-5 sm:p-6', title: 'text-lg font-semibold', description: 'mt-1 text-sm text-muted', footer: 'flex justify-end gap-2 border-t border-default bg-muted/30 p-5 sm:px-6' }">
                            <UButton icon="i-lucide-log-out" color="error" variant="ghost">{{ t('account.logout') }}
                            </UButton>
                            <template #footer>
                                <div class="flex w-full justify-end gap-2">
                                    <UButton @click="open = false" color="neutral" variant="soft"
                                        :label="t('settings.actions.cancel')" />
                                    <UButton @click="handle_logout" :disabled="loading" :loading="loading"
                                        color="error" icon="i-lucide-log-out" :label="t('account.logout')" />
                                </div>
                            </template>
                        </UModal>
                    </div>
                </template>
            </UPopover>
            <UButton :to="localePath('/login')" v-else>{{ t('account.login') }}</UButton>
        </template>
    </UHeader>
</template>

<style scoped></style>
