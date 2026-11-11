<script setup lang="ts">
import { getMeRequest } from '../api';

const { data, status, pending, error } = useLazyAsyncData("my_account", () => getMeRequest())

</script>

<template>
    <div class="flex flex-col">
        <div class="flex justify-between">
            <p>Username</p>
            <div class="flex items-center gap-2">
                <p>{{ data?.username }}</p>
                <UModal>
                    <UButton icon="i-lucide-pencil-line" variant="ghost" color="neutral" />
                    <template #content>
                        salom aleykum
                    </template>
                </UModal>
            </div>
        </div>
        <div class="flex justify-between">
            <p>fullname</p>
            <div class="flex items-center gap-2">
                <p>{{ data?.full_name }}</p>
                <UModal>
                    <UButton icon="i-lucide-pencil-line" variant="ghost" color="neutral" />
                    <template #content>
                        fullname edit
                    </template>
                </UModal>
            </div>
        </div>
        <div class="flex justify-between">
            <p>plan</p>
            <p>{{ data?.plan }}</p>
        </div>
        <div class="flex justify-between">
            <p>telegram id</p>
            <p>{{ data?.telegram_id }}</p>
        </div>
        <div class="flex justify-between">
            <p>registred</p>
            <p>{{ data?.registered_at }}</p>
        </div>
    </div>
</template>