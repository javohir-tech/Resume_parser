<script setup lang="ts">
import { LoginForm } from '~/features/auth/login';

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
                        Telegram orqali kirish
                    </h1>

                    <!-- Description -->
                    <p class="mt-3 text-sm leading-6 text-muted">
                        <a href="https://t.me/resume_parser_auth_bot" target="_blank"
                            class="font-medium text-primary transition-colors hover:text-primary/80">
                            @resume_parserbot
                        </a>
                        botiga kiring va sizga yuborilgan
                        <span class="font-medium text-white">
                            6 xonali kodni
                        </span>
                        kiriting.
                    </p>

                    <!-- Code -->
                    <div class="mt-8 flex justify-center">
                        <LoginForm />
                    </div>

                    <!-- Helper -->
                    <p class="mt-5 text-xs text-muted">
                        Kod 1 daqiqa davomida amal qiladi
                    </p>
                </div>

                <!-- Footer text -->
                <p class="mt-6 text-center text-xs text-muted">
                    Telegram orqali xavfsiz autentifikatsiya
                </p>
            </div>
        </UContainer>
    </div>
</template>