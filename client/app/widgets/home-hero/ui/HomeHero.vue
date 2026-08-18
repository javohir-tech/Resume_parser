<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
const revealed = ref(false)

onMounted(() => {
    requestAnimationFrame(() => (revealed.value = true))
})
</script>

<template>
    <section id="hero_section" class="bg-default relative py-24">
        <div class="absolute inset-0 opacity-[0.06] pointer-events-none"
            style="background-image: repeating-linear-gradient(0deg, currentColor 0 1px, transparent 1px 90px), repeating-linear-gradient(90deg, currentColor 0 1px, transparent 1px 140px); color: var(--ui-text-muted)" />
        <UContainer>
            <!-- Markaziy matn bloki -->
            <div class="max-w-3xl mx-auto text-center transition-all duration-700 ease-out"
                :class="revealed ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-3'">
                <div class="font-mono text-xs font-medium tracking-[0.15em] text-muted mb-5">
                    {{ t('hero.subtitle') }}
                </div>

                <h1
                    class="font-bold tracking-tight leading-[1.1] text-[2.1rem] sm:text-5xl lg:text-6xl text-highlighted mb-6">
                    {{ t('hero.title_line1') }}
                    <span class="block text-primary">{{ t('hero.title_line2') }}</span>
                </h1>

                <p class="text-lg leading-relaxed text-muted max-w-xl mx-auto mb-9">
                    {{ t('hero.description') }}
                </p>

                <div class="flex flex-wrap items-center justify-center gap-3 mb-4">
                    <UButton size="xl" color="primary" class="font-semibold">
                        {{ t('hero.btn_start') }}
                        <template #trailing>→</template>
                    </UButton>
                    <UButton size="xl" variant="outline" color="neutral">
                        {{ t('hero.btn_templates') }}
                    </UButton>
                </div>

                <p class="text-sm text-muted">
                    {{ t('hero.no_card') }}
                </p>
            </div>

            <!-- Gorizontal jarayon lentasi -->
            <div class="mt-20 transition-all duration-700 ease-out delay-200"
                :class="revealed ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'">
                <div class="grid grid-cols-1 md:grid-cols-[1fr_auto_1fr] gap-6 md:gap-4 items-center max-w-5xl mx-auto">

                    <!-- 1: Siz yozasiz -->
                    <div class="rounded-xl border border-default bg-elevated p-5">
                        <div class="font-mono text-[10px] font-bold tracking-wider text-muted mb-3">
                            {{ t('hero.step1_label') }}
                        </div>
                        <p class="font-mono text-sm text-highlighted leading-relaxed">
                            {{ t('hero.step1_example') }}
                        </p>
                    </div>

                    <!-- O'q -->
                    <div class="flex md:flex-col items-center justify-center gap-2 text-muted">
                        <div class="hidden md:block w-px h-8 bg-default" />
                        <span class="text-primary text-lg rotate-90 md:rotate-0">→</span>
                        <div class="hidden md:block w-px h-8 bg-default" />
                    </div>

                    <!-- 2: AI natijasi -->
                    <div class="rounded-xl border border-primary/30 bg-elevated p-5 relative">
                        <div
                            class="absolute top-3 right-3 text-[10px] font-mono font-bold text-primary border border-primary/40 rounded px-1.5 py-0.5">
                            {{ t('hero.step2_badge') }}
                        </div>
                        <div class="font-mono text-[10px] font-bold tracking-wider text-muted mb-3">
                            {{ t('hero.step2_label') }}
                        </div>
                        <div class="font-semibold text-highlighted text-sm mb-1">
                            {{ t('hero.step2_title') }}
                        </div>
                        <div class="h-1.5 w-full rounded bg-accented mb-1.5" />
                        <div class="h-1.5 w-[70%] rounded bg-accented" />
                    </div>

                </div>

                <div
                    class="font-mono text-xs tracking-wider text-muted flex flex-wrap items-center justify-center gap-2 mt-10">
                    <span>{{ t('hero.stat_templates') }}</span>
                    <span class="text-dimmed">·</span>
                    <span>{{ t('hero.stat_languages') }}</span>
                    <span class="text-dimmed">·</span>
                    <span>{{ t('hero.stat_ats') }}</span>
                </div>
            </div>
        </UContainer>
    </section>
</template>
