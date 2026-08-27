<script setup lang="ts">
import { lo } from '@nuxt/ui/runtime/locale/index.js';
import useLogin from '../models/useLogin';

const code = ref<number[]>([])
const pinKey = ref(0)

const {loading ,  login } = useLogin()

watch(code, async (newCode) => {
    if (newCode.length === 6) {
        const code_str = String(code.value.join(""))
        await login(code_str)
        code.value = []
        pinKey.value++
    }
})
</script>

<template>
    <UPinInput :disabled="loading" :key="pinKey" otp v-model="code" type="number" :length="6" size="xl" />
</template>