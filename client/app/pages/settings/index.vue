<script setup lang="ts">
import { PrimaryColorPicker } from '~/features/theme/change-primary-color';
import { NeutralColorPicker } from '~/features/theme/change-neutral-color';
import { FontPicker } from '~/features/theme/change-font';

definePageMeta({
    middleware: "auth",
    layout: "settings"
})

</script>

<template>
    <div>
        Appearance
        <PrimaryColorPicker />
        <NeutralColorPicker />
        <FontPicker />
    </div>
</template>
