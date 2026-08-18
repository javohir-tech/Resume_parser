<script setup lang="ts">
import { Navbar } from '~/widgets/navbar';


</script>

<template>
    <Navbar />
    <main>
        <slot />
    </main>
    <footer>
        footer
    </footer>
</template>