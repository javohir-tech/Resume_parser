<script setup lang="ts">

</script>

<template>
    <UContainer>
        <div class="my-3">
            <div class="mb-5">
                <h1>Resumeni moslashtirish</h1>
                <p>rezyumeingizni tanlang va vakansiyani kiriting ai moslashtirp beradi</p>
            </div>
            <div class="mb-3 grid grid-cols-8 gap-4">
                <div class="bg-muted/40 col-span-3 p-2 rounded-lg border-1 border-default">
                    Resumelar
                </div>
                <div class="bg-muted/40 col-span-5 p-2 rounded-lg border-1 border-default">
                    <h1 class="mb-3">Vakansiya tekstini shu joyga joylashtiring</h1>
                    <UTextarea class="w-100" />
                </div>
            </div>
            <div class="text-end">
                <UButton>Moslashtirish</UButton>
            </div>
        </div>
    </UContainer>
</template>