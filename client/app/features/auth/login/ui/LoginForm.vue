<script setup lang="ts">
import useLogin from '../models/useLogin';

const code = ref<number[]>([])

const {loading , err , login} = useLogin()


function handleLogin(){
    const code_str = String(code.value.join(""))
    login(code_str)
}
// watch(code, () => {
//     if (code.value.length === 6) {
//         console.log(code.value)
//     }
// })
</script>

<template>
    <UPinInput v-model="code" type="number" :length="6" size="xl" />
        <UButton class="block" @click="handleLogin">Login</UButton>
</template>