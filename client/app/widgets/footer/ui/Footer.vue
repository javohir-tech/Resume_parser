<script setup lang="ts">
const { t } = useI18n()
</script>

<template>
    <footer id="footer" class="py-16 border-t-1 border-gray-500">
        <UContainer>
            <div class="grid gap-10 sm:grid-cols-2 lg:grid-cols-[1.6fr_1fr_1fr_1fr] items-baseline">
                <div>
                    <h3 class="text-2xl text-primary font-medium">Resume Parser</h3>
                    <p class="text-xs text-gray-500 mt-3">{{ t('footer.description') }}</p>
                </div>
                <div>
                    <h2 class="font-mono text-gray-500 tracking-[0.18em] uppercase font-medium">
                        {{ t('footer.product') }}
                    </h2>
                    <ul class="flex flex-col mt-2 gap-2">
                        <li>
                            <a class="text-sm text-gray-500 transition-colors hover:text-primary"
                                href="">{{ t('footer.features') }}</a>
                        </li>
                        <li>
                            <a class="text-sm text-gray-500 transition-colors hover:text-primary" href="">{{ t('footer.pricing') }}</a>
                        </li>
                    </ul>
                </div>
                <div>
                    <h2 class="font-mono text-gray-500 tracking-[0.18em] uppercase font-medium">
                        {{ t('footer.resources') }}
                    </h2>
                    <ul class="flex flex-col mt-2 gap-2">
                        <li>
                            <a class="text-sm text-gray-500 transition-colors hover:text-primary" href="">{{ t('footer.contact') }}</a>
                        </li>
                    </ul>
                </div>
            </div>

            <div class="border-t-1 border-gray-500 mt-5 py-5">
                <div class="text-gray-500 flex md:justify-between flex-col md:flex-row gap-4 text-sm font-medium">
                    <p>{{ t('footer.copyright') }}</p>
                    <p>{{ t('footer.createdBy') }} <a class="text-primary font-mono"
                            href="https://www.linkedin.com/in/javohir-suvonov-a98925303/" target="_blank">Suvonov Javohir</a></p>
                </div>
            </div>
        </UContainer>
    </footer>
</template>