<script setup lang="ts">

// components
import { CardList, SectionHeader } from '~/shared/components';
import type { ICard } from '~/shared/components';

const { t, tm } = useI18n()

const cards_inof = computed<ICard[]>(() => {
    const icons = ['i-lucide-file-user', 'i-lucide-sparkles', 'i-lucide-download']
    const delays = [0, 200, 400]

    return icons.map((icon, i) => ({
        icon :icons[i],
        title: t(`howItWorks.steps.${i}.title`),
        subtitle: t(`howItWorks.steps.${i}.subtitle`),
        delay: delays[i]
    }))
})


const cards_info = ref<ICard[]>([
    {
        icon: "i-lucide-file-user",
        title: "O'zingizni tasvirlang",
        subtitle:
            "Bir necha jumla yozing yoki eski rezyumengizni joylashtiring. Format va tuzilma haqida o'ylamang.",
        delay: 0
    },
    {
        icon: "i-lucide-sparkles",
        title: "AI tuzilma beradi",
        subtitle:
            "Sarlavha, qisqacha ma'lumot, tajriba, ko'nikmalar: hammasi bo'limlarga ajraladi. Har bir bandni o'zingiz tahrirlaysiz.",
        delay: 200
    },
    {
        icon: "i-lucide-download",
        title: "Tanlang va yuklab oling",
        subtitle:
            "Shablon, shrift, o'lcham va rangni sozlang. Natijani darhol ko'ring va PDF qilib yuklab oling.",
        delay: 400
    }
])
</script>

<template>
    <section id="how_it_works" class="bg-default py-20">
        <UContainer>
            <SectionHeader eyebrow="Qanday ishlaydi" title="Uch bosqichda tayyor rezyume"
                subtitle="Import qilishdan yuklab olishgacha — uch qadam." />
            <CardList :cards_info="cards_info" />
        </UContainer>
    </section>
</template>