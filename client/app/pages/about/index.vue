<script setup lang="ts">
const revealed = ref<boolean>(false)
onMounted(() => {
    requestAnimationFrame(() => (revealed.value = true))
})
</script>

<template>
    <UContainer>
        <div class="transition-all duration-700 ease-out delay-150" :class="revealed ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'">
            about page
        </div>
    </UContainer>
</template>