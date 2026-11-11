<script setup lang="ts">
import { UserAccount } from '~/entities/user';
import { DeleteProfile, useAccount } from '~/features/user';
const { t } = useI18n()
definePageMeta({
    layout: "settings"
})

const { loading, editAccount } = useAccount()

const handleSaveUsername = async (value: string) :Promise<boolean> => {
    if (!value) return false

    const success = await editAccount({ username: value })

    if(success) return true

    return false
}

const handleSaveFullname = async (value: string): Promise<boolean> => {
    if (!value) return false

    const success = await editAccount({ full_name: value })

    if (success) return true

    return false
}
</script>

<template>
    <div class="mx-auto flex w-full max-w-4xl flex-col gap-8">
        <header>
            <h1 class="m-0 text-3xl font-bold tracking-tight text-highlighted">{{ t('settings.account.title') }}</h1>
        </header>

        <section class="flex flex-col gap-3">
            <h2 class="m-0 text-base font-semibold text-highlighted">{{ t('settings.general') }}</h2>
            <div class="overflow-hidden rounded-2xl border border-default bg-default text-default">
                <UserAccount :username_success="handleSaveUsername" :loading="loading"
                    :full_name_success="handleSaveFullname" />
            </div>
        </section>

        <section class="rounded-2xl border border-error/20 bg-default px-5 py-4">
            <DeleteProfile />
        </section>
    </div>
</template>
