<script setup lang="ts" generic="T extends {id : string}">
const props = defineProps<{
    section_header: string,
    section_icon : string , 
    section_empty: string,

    items_count: number,
    items: T[],
    item_header: string,

    delete_button_title : string,
    delete_pending ?: (id : string) => boolean , 


    add_button_title: string
}>()

defineSlots<{
    default(props: { item: T; index: number }): any
}>()

const add_pending = defineModel<boolean>("add_pending", { default: false })

const emit = defineEmits<{
    add: [],
    delete: [id: string]
}>()


</script>

<template>
    <section class="overflow-hidden rounded-xl border border-default bg-default">
        <div class="flex items-center gap-2.5 border-b border-default bg-elevated/50 px-4 py-3">
            <UIcon :name="props.section_icon" class="size-4 text-muted" />
            <h2 class="flex-1 text-sm font-semibold">{{ props.section_header }}</h2>
            <span class="rounded-md bg-default px-2 py-0.5 text-xs font-medium tabular-nums text-muted">
                {{ props.items_count || 0 }}
            </span>
        </div>
        <div class="space-y-3 p-3">

            <div v-for="(item, index) in items" :key="item.id" class="rounded-lg border border-default p-3">
                <div class="mb-3 flex items-center gap-2 border-b border-default pb-2">

                    <span class="min-w-0 flex-1 truncate text-xs font-semibold text-muted">
                        {{ props.item_header }} - {{ index+1 }}
                    </span>

                    <UButton type="button" color="neutral" variant="ghost" size="xs" icon="i-lucide-trash-2"
                        class="shrink-0 hover:bg-error/10 hover:text-error" :aria-label="props.delete_button_title"
                        :title="props.delete_button_title" :loading="props.delete_pending?.(item.id) ?? false" :disabled="props.delete_pending?.(item.id) ?? false"
                        @click="emit('delete', item.id)" />

                </div>

                <slot :item="item" :index="index"/>

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
    </section>
</template>