<script setup lang="ts">
import type { NavigationMenuItem } from '@nuxt/ui/runtime/components/NavigationMenu.vue.js'

const { t, setLocale } = useI18n()

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
        label : "Aloqa" , 
        to : "/contact"
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
        </template>

        <template #body>
            <UNavigationMenu :items="items" orientation="vertical" />
        </template>
    </UHeader>
</template>

<style scoped></style>