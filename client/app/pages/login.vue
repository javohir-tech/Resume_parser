<script setup lang="ts">
definePageMeta({
    middleware: "guest"
})
import { LoginForm } from '~/features/auth/login';

const { t } = useI18n()
const route = useRoute()

const initialCode = computed<string | null>(() => {
    const code = route.query.code

    if (typeof code !== "string") {
        return null
    }

    return code.slice(0, 6)
})


</script>

<template>
    <div class="min-h-screen flex items-center justify-center px-4">
        <UContainer class="w-full">
            <div class="mx-auto w-full max-w-md">
                <!-- Card -->
                <div class="rounded-2xl border border-gray-200 p-8 text-center shadow-sm dark:border-gray-800">
                    <!-- Icon -->
                    <div class="mx-auto mb-6 flex size-14 items-center justify-center rounded-2xl bg-primary/10">
                        <UIcon name="i-lucide-send" class="size-7 text-primary" />
                    </div>

                    <!-- Title -->
                    <h1 class="text-2xl font-semibold tracking-tight">
                        {{ t('auth.login.title') }}
                    </h1>

                    <!-- Description -->
                    <p class="mt-3 text-sm leading-6 text-muted">
                        <a href="https://t.me/resume_parser_auth_bot" target="_blank"
                            class="font-medium text-primary transition-colors hover:text-primary/80">
                            @resume_parserbot
                        </a>
                        {{ t("auth.login.description") }}
                        <span class="font-medium text-white">
                            {{ t("auth.login.codeLabel") }}
                        </span>
                        {{ t("auth.login.descriptionEnd") }}
                    </p>

                    <!-- Code -->
                    <div class="mt-8 flex flex-col items-center justify-center">
                        <LoginForm :query_code="initialCode" />
                    </div>

                    <!-- Helper -->
                    <p class="mt-5 text-xs text-muted">
                        {{ t("auth.login.helper") }}
                    </p>
                </div>

                <!-- Footer text -->
                <p class="mt-6 text-center text-xs text-muted">
                    {{ t("auth.login.footer") }}
                </p>
            </div>
        </UContainer>
    </div>
</template>