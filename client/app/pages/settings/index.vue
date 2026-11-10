<script setup lang="ts">
import { PrimaryColorPicker } from '~/features/theme/change-primary-color';
import { NeutralColorPicker } from '~/features/theme/change-neutral-color';

definePageMeta({
    middleware: "auth",
    layout: "settings"
})

</script>

<template>
    <div>
        General
        <PrimaryColorPicker />
        <NeutralColorPicker />
    </div>
</template>
