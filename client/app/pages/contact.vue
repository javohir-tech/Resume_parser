<script setup lang="ts">
import { SendMessageForm } from '~/features/send-message';
import { SectionHeader } from '~/shared/components';
import { ContactLink, type IContactLink } from '~/shared/components/Contact-Link';

const { t } = useI18n()

const contact_links: IContactLink[] = [
    {
        title: "suvonovjavohir625@gmail.com",
        link: "mailto:suvonovjavohir625@gmail.com",
        icon: "lucide:mail"
    },
    {
        title: "Linkdin",
        link: "https://www.linkedin.com/in/javohir-suvonov-a98925303/",
        icon: "simple-icons:linkedin"
    },
    {
        title: "Telegram",
        link: "https://t.me/@Suvonov_Javoh1r",
        icon: "simple-icons:telegram"
    }
]

</script>

<template>
    <section id="contact">
        <UContainer>
            <div class="grid grid-cols-1 md:grid-cols-2 py-10 md:py-25 gap-3 items-stretch">
                <div>
                    <SectionHeader :eyebrow="t('contact.eyebrow')" :title="t('contact.title')"
                        :subtitle="t('contact.subtitle')" justify="start" />
                    <div class="flex flex-col gap-4 mt-5 md:mt-10">
                        <ContactLink v-for="contact in contact_links" :key="contact.link" :contact="contact" />
                    </div>
                    <div class="py-6">
                        <p class="text-gray-500 text-sm font-medium">Odatda 1-2 ish kuni ichida javob beramiz.</p>
                    </div>
                </div>
                <div class="rounded-xl border border-gray-500 p-5">
                    <SendMessageForm />
                </div>
            </div>
        </UContainer>
    </section>
</template>