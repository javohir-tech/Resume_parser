<script setup lang="ts">
import useRestartTheme from '../models/useRestartTheme';

const { restartTheme } = useRestartTheme()
</script>

<template>
    <div class="">
        <UButton block label="Restart" @click="restartTheme" color="error" variant="soft" />
    </div>
</template>