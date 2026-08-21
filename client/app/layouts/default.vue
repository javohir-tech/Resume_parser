<script setup lang="ts">
import { Footer } from '~/widgets/footer';
import { Navbar } from '~/widgets/navbar';


</script>

<template>
    <Navbar />
    <main>
        <slot />
    </main>
    <Footer />
</template>