<script setup lang="ts">
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
</script>

<template>
    <section id="hero_section" class="hero relative isolate overflow-hidden bg-default" aria-labelledby="hero-title">
        <div class="hero-grid pointer-events-none absolute inset-0" aria-hidden="true" />
        <UContainer class="relative pt-8 pb-3 sm:pt-10 lg:pt-[clamp(1rem,3vh,2rem)]">
            <div class="grid items-center gap-12 lg:grid-cols-[1.05fr_1fr] lg:gap-8 xl:gap-16">
                <div class="hero-enter relative z-10 min-w-0">
                    <p
                        class="mb-5 inline-flex max-w-full items-center gap-2.5 rounded-full border border-primary/20 bg-primary/5 px-3.5 py-2 text-[10px] font-semibold tracking-[0.12em] text-primary sm:text-xs">
                        <span class="relative flex size-2 shrink-0" aria-hidden="true"><span
                                class="absolute inset-0 rounded-full bg-primary/20 ring-4 ring-primary/10" /><span
                                class="relative size-2 rounded-full bg-primary" /></span>
                        {{ t('hero.subtitle') }}
                    </p>
                    <h1 id="hero-title"
                        class="hero-title text-[2rem] font-semibold leading-[1.15] tracking-[-0.04em] text-highlighted sm:text-[2.5rem] xl:text-[3rem]">
                        {{ t('hero.title_line1') }}
                        <span class="mt-2 block text-primary">{{ t('hero.title_line2') }}</span>
                    </h1>
                    <p class="mt-6 max-w-lg text-sm leading-relaxed text-muted sm:text-base">
                        {{ t('hero.description') }}
                    </p>
                    <div class="mt-6 flex flex-col gap-3 sm:flex-row sm:flex-wrap">
                        <UButton size="lg" color="primary" trailing-icon="i-lucide-arrow-up-right"
                            class="justify-center rounded-xl px-5 py-3 font-semibold shadow-lg shadow-primary/10 transition-transform hover:-translate-y-0.5">
                            {{ t('hero.btn_start') }}
                        </UButton>
                        <UButton size="lg" variant="outline" color="neutral" leading-icon="i-lucide-circle-play"
                            class="justify-center rounded-xl px-5 py-3">
                            {{ t('hero.btn_templates') }}
                        </UButton>
                    </div>
                    <p class="mt-4 flex items-center gap-2 text-xs text-muted">
                        <UIcon name="i-lucide-check" class="size-3.5 text-primary" aria-hidden="true" />
                        {{ t('hero.no_card') }}
                    </p>
                </div>

                <!-- Decorative product illustration, not an interactive editor. -->
                <div class="hero-stage hero-enter relative mx-auto w-full max-w-lg min-w-0 lg:max-w-none"
                    aria-hidden="true">
                    <div class="hero-orbit hero-orbit-outer" />
                    <div class="hero-orbit hero-orbit-inner" />
                    <span class="hero-cross absolute top-10 right-8 text-3xl font-light text-primary/40">+</span>
                    <span class="absolute bottom-20 left-0 size-2 rounded-full bg-primary/40" />

                    <div
                        class="hero-note relative z-20 mr-8 rounded-2xl border border-default bg-elevated p-4 shadow-lg sm:mr-16 sm:p-4">
                        <div class="mb-3 flex items-center gap-2.5">
                            <span
                                class="flex size-8 shrink-0 items-center justify-center rounded-lg bg-primary/10 text-primary">
                                <UIcon name="i-lucide-briefcase-business" class="size-4" />
                            </span>
                            <span class="text-[10px] font-semibold tracking-widest text-muted">{{ t('hero.step1_label')
                                }}</span>
                            <span class="ml-auto flex gap-1"><i v-for="dot in 3" :key="dot"
                                    class="size-1 rounded-full bg-dimmed/40" /></span>
                        </div>
                        <p class="text-sm leading-relaxed text-highlighted">{{ t('hero.step1_example') }}</p>
                    </div>

                    <div class="relative z-20 my-2 ml-10 flex items-center gap-3 text-primary sm:ml-16">
                        <span class="h-8 w-px bg-primary/30" />
                        <span
                            class="flex size-9 items-center justify-center rounded-full border border-primary/20 bg-default shadow-sm">
                            <UIcon name="i-lucide-sparkles" class="size-4" />
                        </span>
                        <span class="h-px w-16 bg-primary/30" />
                        <UIcon name="i-lucide-arrow-down-right" class="size-5" />
                    </div>

                    <div
                        class="hero-paper relative ml-6 rounded-2xl border border-default bg-default p-5 shadow-2xl shadow-black/10 sm:ml-14 sm:p-5">
                        <div class="mb-4 flex items-center justify-between gap-3 border-b border-default pb-3">
                            <span class="text-[9px] font-semibold tracking-[0.13em] text-muted sm:text-[10px]">{{
                                t('hero.step2_label') }}</span>
                            <span
                                class="inline-flex items-center gap-1 rounded-md bg-primary/10 px-2 py-1 text-[10px] font-bold text-primary">
                                <UIcon name="i-lucide-sparkles" class="size-3" />{{ t('hero.step2_badge') }}
                            </span>
                        </div>
                        <div class="flex items-start gap-4">
                            <span
                                class="flex size-12 shrink-0 items-center justify-center rounded-xl border border-primary/15 bg-primary/5 text-primary">
                                <UIcon name="i-lucide-user-round" class="size-6" />
                            </span>
                            <div class="min-w-0 flex-1">
                                <p
                                    class="text-lg font-semibold leading-tight tracking-tight text-highlighted sm:text-xl">
                                    {{ t('hero.step2_title') }}</p>
                                <div class="mt-3 flex gap-2"><span class="h-1.5 w-16 rounded-full bg-accented" /><span
                                        class="h-1.5 w-12 rounded-full bg-accented" /></div>
                            </div>
                        </div>
                        <div class="mt-5 grid grid-cols-[1fr_0.45fr] gap-5">
                            <div class="space-y-3">
                                <div v-for="section in ['summary', 'experience']" :key="section">
                                    <p class="mb-2 text-[10px] font-semibold uppercase tracking-wider text-primary">{{
                                        t(`resumeDocument.sections.${section}`) }}</p>
                                    <div class="space-y-2">
                                        <div class="h-1.5 w-full rounded-full bg-accented" />
                                        <div class="h-1.5 w-[90%] rounded-full bg-accented" />
                                        <div class="h-1.5 w-3/4 rounded-full bg-accented" />
                                    </div>
                                </div>
                            </div>
                            <div class="border-l border-default pl-4">
                                <p class="mb-2 text-[10px] font-semibold uppercase tracking-wider text-primary">{{
                                    t('resumeDocument.sections.skills') }}</p>
                                <div class="flex flex-wrap gap-1.5"><span
                                        v-for="skill in ['Vue.js', 'TypeScript', 'Nuxt']" :key="skill"
                                        class="rounded-md border border-default px-2 py-1 text-[9px] text-muted">{{
                                        skill }}</span></div>
                            </div>
                        </div>
                        <div class="mt-4 flex items-center gap-2 border-t border-default pt-3"><span
                                class="size-1.5 rounded-full bg-primary" /><span
                                class="h-1 w-16 rounded-full bg-primary/20" /><span
                                class="ml-auto font-mono text-[9px] text-dimmed">01 / 01</span></div>
                    </div>
                    <div
                        class="absolute -right-1 bottom-12 z-20 flex size-14 rotate-12 items-center justify-center rounded-2xl border border-primary/25 bg-primary text-inverted shadow-lg shadow-primary/20 sm:size-16">
                        <UIcon name="i-lucide-file-check-2" class="size-7 sm:size-8" />
                    </div>
                </div>
            </div>

            <div class="mt-8 grid grid-cols-1 border-t border-default py-3 sm:mt-6 sm:grid-cols-3 lg:mt-4">
                <div v-for="(item, index) in [
                    { icon: 'i-lucide-panels-top-left', label: 'hero.stat_templates' },
                    { icon: 'i-lucide-languages', label: 'hero.stat_languages' },
                    { icon: 'i-lucide-scan-text', label: 'hero.stat_ats' }
                ]" :key="item.label"
                    class="flex items-center justify-center gap-3 py-2 text-xs font-medium tracking-wider text-muted"
                    :class="{ 'sm:border-l sm:border-default': index > 0 }">
                    <UIcon :name="item.icon" class="size-4 text-primary" aria-hidden="true" />
                    {{ t(item.label) }}
                </div>
            </div>
        </UContainer>
    </section>
</template>

<style scoped>
.hero-grid {
    background-image: radial-gradient(var(--ui-border-accented) 1px, transparent 1px);
    background-size: 24px 24px;
    mask-image: linear-gradient(to right, transparent 25%, black 100%);
    opacity: 0.45;
}

.hero-title {
    text-wrap: balance;
}

.hero-stage {
    padding: 14px 10px 16px;
}

.hero-orbit {
    position: absolute;
    pointer-events: none;
    border: 1px solid color-mix(in srgb, var(--ui-primary) 15%, transparent);
    border-radius: 50%;
    inset: 4%;
}

.hero-orbit-inner {
    transform: scale(0.82);
    border-style: dashed;
}

.hero-orbit-outer {
    background: radial-gradient(circle, color-mix(in srgb, var(--ui-primary) 7%, transparent), transparent 70%);
}

.hero-note {
    transform: rotate(-3deg);
}

.hero-paper {
    transform: rotate(2deg);
}

@media (prefers-reduced-motion: no-preference) {
    .hero-enter {
        animation: hero-reveal 700ms ease-out both;
    }

    .hero-stage {
        animation-delay: 120ms;
    }

    .hero-cross {
        animation: hero-turn 18s linear infinite;
    }
}

@keyframes hero-reveal {
    from {
        opacity: 0;
        translate: 0 16px;
    }

    to {
        opacity: 1;
        translate: 0 0;
    }
}

@keyframes hero-turn {
    to {
        rotate: 360deg;
    }
}

@media (max-width: 639px) {
    .hero-note {
        transform: rotate(-1deg);
    }

    .hero-paper {
        transform: rotate(1deg);
    }
}
</style>
