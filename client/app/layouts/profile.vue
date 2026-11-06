<script setup lang="ts">
const localPath = useLocalePath()

</script>

<template>
    <NuxtLayout name="default">
        <div class="pt-8">
            <UContainer>
                <div class="grid grid-cols-12 gap-4">
                    <div class="col-span-2 flex flex-col gap-2">
                        <UButton :to="localPath('/profile')" icon="i-lucide-user" color="neutral" variant="ghost">
                            Profile</UButton>
                        <UButton :to="localPath('/profile/billing')" icon="i-lucide-credit-card" color="neutral"
                            variant="ghost">
                            Billing
                        </UButton>
                        <UButton :to="localPath('/profile/devices')" icon="i-lucide-monitor-smartphone" color="neutral"
                            variant="ghost">
                            Devices
                        </UButton>
                        <UButton :to="localPath('/profile/settings')" icon="i-lucide-settings" color="neutral"
                            variant="ghost">
                            Settings
                        </UButton>
                    </div>
                    <div class="col-span-10">
                        <slot />
                    </div>
                </div>
            </UContainer>
        </div>
    </NuxtLayout>
</template>