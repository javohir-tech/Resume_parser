<script setup lang="ts">
import { SectionHeader } from '~/shared/components';
import type { AccordionItem } from '@nuxt/ui/runtime/components/Accordion.vue.js';

const items = ref<AccordionItem[]>([
    {
        label: "ATS dasturlari rezyumemni o'qiy oladimi?",
        content:
            "Ha, muammosiz. Har bir shablon matn qatlami bor PDF sifatida yaratiladi va bo'limlar odatiy nomlar bilan belgilanadi — natijada kuzatish tizimlari kontentni to'g'ri tanib oladi."
    },
    {
        label: "Pullik obunasiz ham ishlatsam bo'ladimi?",
        content:
            "Albatta. Yaratish, tahrirlash va ko'rish har doim bepul — oyiga 5 marta AI generatsiya, 20 marta AI tahrirdan foydalanasiz. Faqat PDF yuklab olish, premium shablonlar va cheksiz AI uchun Pro kerak bo'ladi, uni istalgan payt bekor qilishingiz mumkin."
    },
    {
        label: "Platforma qaysi tillarni qo'llab-quvvatlaydi?",
        content:
            "Hozircha o'zbek va ingliz — shu ikkalasida ham interfeys, ham rezyume matni to'liq ishlaydi. Bitta profilda ikki tilli versiyani parallel saqlab, kerakli tilini vakansiyaga qarab tanlab yuborasiz."
    },
    {
        label: "AI tuzgan matnga o'zgartirish kiritsam bo'ladimi?",
        content:
            "Ha, to'liq erkinsiz. AI shunchaki boshlang'ich qoralamani tayyorlaydi — qolgani sizga bog'liq: istalgan bo'lim yoki bandni oddiy matn maydonida to'g'ridan-to'g'ri tahrirlaysiz."
    },
    {
        label: "Kiritgan ma'lumotlarim xavfsizmi va qayerda turadi?",
        content:
            "Kontent hisobingizga bog'lab bizning bazamizda saqlanadi. Har qanday rezyumeni xohlagan vaqtda o'chirib tashlashingiz mumkin, hisob butunlay o'chirilganda esa unga tegishli barcha ma'lumot izsiz yo'qoladi."
    },
    {
        label: "Bir nechta rezyume saqlash mumkinmi?",
        content:
            "Ha, cheklovsiz. Har bir vakansiya uchun alohida nusxa oching, sarlavha va tajriba bandlarini o'sha ish o'rniga moslashtirib qo'ying."
    }
])
</script>

<template>
    <section id="requests-section" class="py-20">
        <UContainer>
            <SectionHeader eyebrow="savollar" title="savollarizni beringlar haromilar"
                subtitle="chunmadingmi contactga ot aloqaga chiq" />
            <div class="grid grid-cols-1 items-start md:grid-cols-2  mt-6  ">
                <div>
                    <h3 class="py-4 text-4xl font-medium">Ko'p beriladigan savollar</h3>
                    <p class="text-gray-500 text-sm">Javobini topa olmadingizmi? Aloqa sahifasidan yozing, javob beramiz.</p>
                </div>
                <div class="block">
                    <UAccordion :items="items" />
                </div>
            </div>
        </UContainer>
    </section>
</template>