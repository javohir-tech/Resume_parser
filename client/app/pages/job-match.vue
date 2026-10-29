<script setup lang="ts">

</script>

<template>
    <UContainer class="flex min-h-[calc(100vh-4rem)] min-w-0 flex-col py-6 sm:py-10 lg:py-12">
        
        <header class="mb-8 max-w-2xl">
            <p class="font-semibold text-xs text-primary mb-3 uppercase tracking-[0.18em]">Yakuniy qadam shu yerda
            </p>
            <h1 class="font-semibold text-3xl sm:text-4xl mb-3 tracking-tight text-highlighted">Resumeni moslashtirish
            </h1>
            <p class="text-base text-muted">
                rezyumeingizni tanlang va vakansiyani kiriting AI rezyumeingizni vakansiyaga moslashtirip beradi
            </p>
        </header>

        <div class="mb-3 grid flex-1 grid-cols-1 lg:grid-cols-8 gap-4 ">
            <div class="flex flex-col bg-muted/40 lg:col-span-3 p-5 rounded-lg border-1 border-default">
                <h2 class="mb-3 font-semibold text-highlighted">
                    Resumelar
                </h2>
            </div>
            <div class="flex flex-col bg-muted/40 lg:col-span-5 p-5 rounded-lg border-1 border-default">
                <h1 class="mb-3 font-semibold text-highlighted">Vakansiya tekstini shu joyga joylashtiring</h1>
                <UTextarea class="w-full flex-1"
                    :ui="{ root: 'flex flex-1 w-full', base: 'h-full w-full resize-none' }" />
            </div>
        </div>

        <div class="text-end">
            <UButton>Moslashtirish</UButton>
        </div>

    </UContainer>
</template>