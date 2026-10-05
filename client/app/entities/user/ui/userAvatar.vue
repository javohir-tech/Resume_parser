<script setup lang="ts">
import { useUserStore } from '../models/store'

withDefaults(defineProps<{ size?: 'sm' | 'lg' }>(), { size: 'sm' })
const userStore = useUserStore()

const initials = computed(() => {
  const parts = userStore.user?.full_name?.trim().split(/\s+/).filter(Boolean) ?? []
  return parts.slice(0, 2).map(part => Array.from(part)[0]).join('').toLocaleUpperCase() || '?'
})

const gradients = [
  'from-violet-500 to-indigo-700',
  'from-sky-500 to-blue-700',
  'from-emerald-500 to-teal-700',
  'from-amber-500 to-orange-700',
  'from-rose-500 to-pink-700',
  'from-indigo-500 to-violet-700',
]

const gradientClass = computed(() => {
  const name = userStore.user?.full_name ?? ''
  const hash = [...name].reduce((acc, char) => acc + char.charCodeAt(0), 0)
  return gradients[hash % gradients.length]
})
</script>

<template>
  <div
    class="relative isolate flex shrink-0 select-none items-center justify-center overflow-hidden rounded-full bg-gradient-to-br font-semibold text-white shadow-sm ring-1 ring-inset ring-black/5"
    :class="[gradientClass, size === 'lg' ? 'size-24 text-3xl' : 'size-7 text-[10px]']" aria-hidden="true">
    <span class="pointer-events-none absolute -left-1/4 -top-1/2 size-full rounded-full bg-white/15" />
    <span class="relative tracking-wide">{{ initials }}</span>
  </div>
</template>
