<script setup lang="ts">
const colorMode = useColorMode()
const { t, locale, setLocale } = useI18n()

const isDark = computed({
    get() {
        return colorMode.value === "dark"
    },
    set(_isDark) {
        colorMode.preference = _isDark ? 'dark' : "light"
    }
})

function onLocaleChange(event: Event) {
    const target = event.target as HTMLSelectElement
    setLocale(target.value as "uz" | "en" | "en")
}
</script>

<template>
    <nav>
        <span>{{ t('navbar.home') }}</span>
        <span>{{ t('navbar.resume') }}</span>
        <span>{{ t('navbar.about') }}</span>
        <span>{{ t('navbar.contact') }}</span>
    </nav>
    <select :value="locale" @change="onLocaleChange">
         <option value="uz" :selected="locale === 'uz'">O'zbek</option>
        <option value="ru" :selected="locale === 'ru'">Русский</option>
        <option value="en" :selected="locale === 'en'">English</option>
    </select>
    <ClientOnly>
        <UButton :icon="isDark ? 'i-lucide-moon' : 'i-lucide-sun'" color="neutral" variant="ghost"
            :aria-label="`Switch to ${isDark ? 'light' : 'dark'} mode`" @click="isDark = !isDark" />

        <template #fallback>
            <span class="size-8" />
        </template>
    </ClientOnly>
</template>