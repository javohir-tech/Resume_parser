<script setup lang="ts">

interface ICard {
    icon: string;
    title: string;
    subtitle: string;
    delay: number;
}


import Card from './Card.vue';

const props = defineProps<{
    cards_info: ICard[],
    col?: number
}>()
</script>

<template>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mt-10">
        <Card v-for="card in cards_info" :key="card.title" :icon="card.icon" :title="card.title"
            :subtitle="card.subtitle" :delay="card.delay" />
    </div>
</template>
