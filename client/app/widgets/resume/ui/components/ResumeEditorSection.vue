<script setup lang="ts" generic="T extends {id : string}">

const open = ref(false)

const props = defineProps<{
    section_header: string,
    section_icon: string,
    section_empty: string,

    items_count: number,
    items: T[],
    item_header: string,

    delete_button_title: string,
    delete_pending?: (id: string) => boolean,


    add_button_title: string
}>()

defineSlots<{
    default(props: { item: T; index: number }): any
}>()

const add_pending = defineModel<boolean>("add_pending", { default: false })
const openedForms = ref<Set<string>>(new Set<string>())

const emit = defineEmits<{
    add: [],
    delete: [id: string]
}>()


</script>

<template>
    <section class="overflow-hidden rounded-xl border border-default bg-default">
        <UCollapsible v-model:open="open" class="flex flex-col">

            <div class="flex items-center gap-2.5 border-b border-default bg-elevated/50 px-4 py-3">
                <UIcon :name="props.section_icon" class="size-4 text-muted" />
                <h2 class="flex-1 text-sm font-semibold">{{ props.section_header }}</h2>
                <span class="rounded-md bg-default px-2 py-0.5 text-xs font-medium tabular-nums text-muted">
                    {{ props.items_count || 0 }}
                </span>
                <UIcon :name="open ? 'i-lucide-chevron-up' : 'i-lucide-chevron-down'" />
            </div>

            <template #content>

                <div class="space-y-3 p-3">

                    <div v-for="(item, index) in items" :key="item.id" class="rounded-lg border border-default p-3">
                        <UCollapsible @update:open="$event ?  openedForms?.add(item.id) : openedForms?.delete(item.id)">

                            <div class="flex items-center ">

                                <span class="min-w-0 flex-1 truncate text-xs font-semibold text-muted">
                                    {{ props.item_header }} - {{ index + 1 }}
                                </span>
                                <div class="felx items-center gap-2">
                                    <UButton type="button" color="neutral" variant="ghost" size="xs"
                                        icon="i-lucide-trash-2" class="shrink-0 hover:bg-error/10 hover:text-error"
                                        :aria-label="props.delete_button_title" :title="props.delete_button_title"
                                        :loading="props.delete_pending?.(item.id) ?? false"
                                        :disabled="props.delete_pending?.(item.id) ?? false"
                                        @click="emit('delete', item.id)" />
                                    <UIcon size="xs"
                                        :name="openedForms?.has(item.id) ? 'i-lucide-chevron-up' : 'i-lucide-chevron-down'" />
                                </div>
                            </div>

                            <template #content>
                                <slot :item="item" :index="index" />
                            </template>

                        </UCollapsible>
                    </div>

                    <p v-if="!items?.length" class="px-1 py-2 text-xs leading-relaxed text-muted">
                        {{ props.section_empty }}
                    </p>
                    <UButton type="button" color="neutral" variant="outline" size="sm" icon="i-lucide-plus"
                        class="w-full justify-center rounded-lg border-dashed py-2" :loading="add_pending"
                        :disabled="add_pending" @click="emit('add')">
                        {{ props.add_button_title }}
                    </UButton>
                </div>

            </template>
        </UCollapsible>

    </section>
</template>