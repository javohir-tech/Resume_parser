<script setup lang="ts">
import { useResumeParse } from '../models/useResumeParse';

const { t } = useI18n()
const { resumeParse , resumeImport } = useResumeParse()
const localePath = useLocalePath()

const loading = ref(false)
const selectedFile = ref<File | null>()

async function uploadFile() {
  if (!selectedFile.value) return
  loading.value = true
  try{
    const parse_resume = await resumeParse(selectedFile.value)
    if(parse_resume){
        const resume = await resumeImport(parse_resume)
        if(resume?.success){
          await navigateTo(`${localePath(`/resume/${resume?.resume_id}`)}`)
        }
    }
  }finally{
    loading.value = false
  }

}

</script>

<template>
  <div class="space-y-4">
    <UFileUpload accept=".pdf,.docx" name="resume-upload" size="lg" variant="area" icon="i-lucide-cloud-upload"
      :label="t('resumeWorkspace.dropFile')" :description="t('resumeWorkspace.fileTypes')"
      :ui="{ base: 'min-h-56 rounded-2xl bg-muted/30', label: 'text-base font-medium' }" v-model="selectedFile" />
    <p class="flex items-start gap-2 text-xs leading-relaxed text-muted">
      <UIcon name="i-lucide-info" class="mt-0.5 size-4 shrink-0" />
      {{ t('resumeWorkspace.uploadHint') }}
    </p>
    <div class="flex justify-end">
      <UButton @click="uploadFile" type="submit" :loading="loading" :disabled="loading" size="lg" icon="i-lucide-sparkles" class="w-full justify-center sm:w-auto">
        {{ t('resumeWorkspace.parseAction') }}
      </UButton>
    </div>
  </div>
</template>
