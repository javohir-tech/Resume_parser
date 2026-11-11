<script setup lang="ts">
import { UserAccount } from '~/entities/user';
import { useAccount } from '~/features/user';
definePageMeta({
    layout: "settings"
})

const { loading, editAccount } = useAccount()

const handleSaveUsername = async (value: string) => {
    if (!value) return

    await editAccount({ username: value })
}

const handleSaveFullname = async (value : string) =>{
    if(!value) return

    await editAccount({full_name : value})
}
</script>

<template>
    <UserAccount @save-username="handleSaveUsername" @save-fullname="handleSaveFullname" :loading="loading"/>
</template>