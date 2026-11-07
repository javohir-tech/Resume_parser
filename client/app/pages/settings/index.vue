<script setup lang="ts">
import { PrimaryColorPicker } from '~/features/theme/change-primary-color';

definePageMeta({
    middleware: "auth",
    layout: "settings"
})

</script>

<template>
    <div>
        General
        <PrimaryColorPicker/>
    </div>
</template>
