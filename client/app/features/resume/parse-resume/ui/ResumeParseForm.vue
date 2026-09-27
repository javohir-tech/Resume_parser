<script setup lang="ts">
const { t } = useI18n()
</script>

<template>
  <div class="space-y-4">
    <UFileUpload accept=".pdf,.docx" name="resume-upload" size="lg" variant="area"
      icon="i-lucide-cloud-upload" :label="t('resumeWorkspace.dropFile')" :description="t('resumeWorkspace.fileTypes')"
      :ui="{ base: 'min-h-56 rounded-2xl bg-muted/30', label: 'text-base font-medium' }" />
    <p class="flex items-start gap-2 text-xs leading-relaxed text-muted">
      <UIcon name="i-lucide-info" class="mt-0.5 size-4 shrink-0" />
      {{ t('resumeWorkspace.uploadHint') }}
    </p>
    <div class="flex justify-end">
      <UButton type="submit" size="lg" icon="i-lucide-sparkles" class="w-full justify-center sm:w-auto">
        {{ t('resumeWorkspace.parseAction') }}
      </UButton>
    </div>
  </div>
</template>
