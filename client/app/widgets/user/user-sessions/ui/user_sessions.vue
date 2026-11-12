<script setup lang="ts">
import { GetSessionsRequest, UserSessionCard } from '~/entities/user';
import { useSessionRevoke } from '~/features/user';

const { t } = useI18n()

const { isDeleting, revokeSession } = useSessionRevoke()

const { data, pending, error, refresh } = useLazyAsyncData(
    'sessions',
    () => GetSessionsRequest(),
    { server: false }
)

const deleteSession = async (device_id: string) => {
    if (!data.value) return
    const is_deleted = await revokeSession(device_id)
    if (is_deleted) {
        data.value = {
            ...data.value,
            sessions: data.value.sessions.filter(session => session.device_id !== device_id)
        }
    }

}


</script>

<template>
    <div class="flex flex-col gap-8">

        <section class="flex flex-col gap-3">
            <h2 class="m-0 text-base font-semibold text-highlighted">
                {{ t('profile.sessions.description') }}
            </h2>
            <div class="overflow-hidden rounded-2xl border border-default bg-default text-default">
                <ClientOnly>
                    <div v-if="pending" class="space-y-3 p-5">
                        <USkeleton v-for="i in 3" :key="i" class="h-20 w-full rounded-xl" />
                    </div>

                    <UAlert v-else-if="error" class="m-5" color="error" variant="soft"
                        :title="t('profile.sessions.loadError')" />

                    <div v-else class="divide-y divide-default">
                        <div v-for="session in data?.sessions ?? []" :key="session.id" class="px-5 py-4">
                            <UserSessionCard :session="session" @delete="deleteSession" :is_deleting="isDeleting" />
                        </div>
                    </div>

                    <template #fallback>
                        <div class="space-y-3 p-5">
                            <USkeleton v-for="i in 3" :key="i" class="h-20 w-full rounded-xl" />
                        </div>
                    </template>
                </ClientOnly>
            </div>
        </section>
    </div>
</template>
