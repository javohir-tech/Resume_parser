<script setup lang="ts">
import { SectionHeader } from '~/shared/components';


</script>

<template>
    <section id="home-start" class="py-26 relative">
        <div class="absolute inset-0 opacity-[0.06] pointer-events-none"
            style="background-image: repeating-linear-gradient(0deg, currentColor 0 1px, transparent 1px 90px), repeating-linear-gradient(90deg, currentColor 0 1px, transparent 1px 140px); color: var(--ui-text-muted)" />
        <UContainer>
            <SectionHeader title="Rezyumengiz bugun tayyor bo'lsin"
                subtitle="Bo'sh varaqqa qarab o'tirmang. Bir necha jumla yozing, qolganini biz qilamiz." />
            <div class="text-center mt-10">
                <UButton trailing-icon="i-lucide-arrow-right">Bepul boshlash</UButton>
            </div>
        </UContainer>
    </section>
</template>