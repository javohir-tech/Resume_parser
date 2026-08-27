<script setup lang="ts">
import useLogin from '../models/useLogin';

const props = defineProps<{
    query_code?: string | null
}>()

const code = ref<number[]>([])
const pinKey = ref(0)

const { loading, login } = useLogin()

watch(code, async (newCode) => {
    if (newCode.length === 6) {
        const code_str = String(code.value.join(""))
        await login(code_str)
        code.value = []
        pinKey.value++
    }
})

onMounted(() => {
    if (props.query_code && props.query_code.length === 6) {
        code.value = props.query_code.split("").map((item)=> {
            return Number(item)
        })
    }
})
</script>

<template>
    <UPinInput :disabled="loading" :key="pinKey" otp v-model="code" type="number" :length="6" size="xl" />
</template>