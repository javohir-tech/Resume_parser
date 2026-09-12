<template>
    <UContainer class="space-y-8 py-10">
        <div class="flex flex-wrap items-end gap-4">
            <UButton to="/resume/create" icon="i-lucide-plus" size="lg">
                Resume yaratish
            </UButton>
            <div class="space-y-2">
                <label for="resume-upload" class="block text-sm font-medium">Resume yuklash</label>
                <input id="resume-upload" type="file"
                    class="block w-full rounded-lg border border-default p-2 text-sm file:mr-3 file:rounded-md file:border-0 file:bg-elevated file:px-3 file:py-1 file:text-default" />
            </div>
        </div>
        <h1 class="text-2xl font-semibold">Resumelarim</h1>
    </UContainer>
</template>
