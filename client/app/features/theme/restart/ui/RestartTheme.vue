<script setup lang="ts">
import useRestartTheme from '../models/useRestartTheme';
const { t } = useI18n()

const { restartTheme } = useRestartTheme()
</script>

<template>
    <div class="shrink-0 max-sm:self-end">
        <UButton :label="t('settings.actions.reset')" @click="restartTheme" color="neutral" variant="soft" />
    </div>
</template>
