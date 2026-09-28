<script setup lang="ts">
import { ContactLink } from '~/shared/ui'
import { SendMessageForm } from '~/features/send-message'

export interface IContactLink {
  title: string;
  link: string;
  icon: string;
}

const { t } = useI18n()

const contact_links: IContactLink[] = [
    {
        title: 'suvonovjavohir625@gmail.com',
        link: 'mailto:suvonovjavohir625@gmail.com',
        icon: 'i-lucide-mail'
    },
    {
        title: 'LinkedIn',
        link: 'https://www.linkedin.com/in/javohir-suvonov-a98925303/',
        icon: 'i-lucide-briefcase-business'
    },
    {
        title: 'Telegram',
        link: 'https://t.me/Suvonov_Javoh1r',
        icon: 'i-lucide-send'
    }
]
</script>

<template>
    <section id="contact" aria-labelledby="contact-title" class="relative isolate overflow-hidden">
        <div class="contact-glow pointer-events-none absolute inset-0 -z-10" aria-hidden="true" />
        <UContainer class="py-10 sm:py-14 lg:py-16">
            <div class="mx-auto grid max-w-6xl items-start gap-10 lg:grid-cols-[0.9fr_1.1fr] lg:gap-16">
                <div class="min-w-0 lg:pt-5">
                    <p class="mb-5 inline-flex items-center gap-2 rounded-full border border-primary/20 bg-primary/5 px-3 py-1.5 text-xs font-medium text-primary">
                        <span class="size-1.5 rounded-full bg-primary" aria-hidden="true" />
                        {{ t('contact.eyebrow') }}
                    </p>
                    <h1 id="contact-title" class="max-w-md text-3xl font-semibold leading-tight tracking-tight text-highlighted sm:text-4xl">
                        {{ t('contact.title') }}
                    </h1>
                    <p class="mt-4 max-w-md text-sm leading-7 text-muted sm:text-base">{{ t('contact.subtitle') }}</p>

                    <div class="mt-8 space-y-2">
                        <ContactLink v-for="contact in contact_links" :key="contact.link" :contact="contact" />
                    </div>

                    <div class="relative mt-8 overflow-hidden rounded-2xl border border-primary/15 bg-primary/5 p-5">
                        <div class="pointer-events-none absolute -right-5 -bottom-6 rotate-[-15deg] text-primary/10" aria-hidden="true">
                            <UIcon name="i-lucide-mail" class="size-28" />
                        </div>
                        <div class="relative flex items-start gap-3">
                            <span class="flex size-9 shrink-0 items-center justify-center rounded-xl bg-primary/10 text-primary">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" class="size-4" aria-hidden="true"><circle cx="12" cy="12" r="9" /><path d="M12 7v5l3 2" /></svg>
                            </span>
                            <p class="max-w-64 py-1 text-sm leading-relaxed text-muted">{{ t('contact.responseTime') }}</p>
                        </div>
                    </div>
                </div>

                <div class="min-w-0 rounded-3xl border border-default bg-default shadow-xl shadow-black/[0.04]">
                    <div class="flex items-center gap-3 border-b border-default px-5 py-5 sm:px-8 sm:py-6">
                        <span class="flex size-10 shrink-0 items-center justify-center rounded-xl border border-default bg-muted/50 text-primary"><UIcon name="i-lucide-send" class="size-5" aria-hidden="true" /></span>
                        <div>
                            <h2 class="text-base font-semibold text-highlighted">{{ t('contact.formTitle') }}</h2>
                            <p class="mt-1 text-xs leading-relaxed text-muted">{{ t('contact.formDescription') }}</p>
                        </div>
                    </div>
                    <div class="p-5 sm:p-8">
                        <SendMessageForm />
                    </div>
                </div>
            </div>
        </UContainer>
    </section>
</template>

<style scoped>
.contact-glow {
    background: radial-gradient(ellipse at 0% 20%, color-mix(in srgb, var(--ui-primary) 6%, transparent), transparent 55%);
}
</style>
