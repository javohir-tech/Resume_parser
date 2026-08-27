<script setup lang="ts">
import { Footer } from '~/widgets/footer';
import { Navbar } from '~/widgets/navbar';


</script>

<template>
    <div class="min-h-screen flex flex-col">
        <Navbar />
        <main class="flex-1">
            <slot />
        </main>
    </div>
        <Footer />
</template>