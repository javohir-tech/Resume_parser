<script setup lang="ts">
import { useUserStore } from '../models/store'

const userStore = useUserStore()

const initial = computed(() =>
  userStore.user?.full_name?.charAt(0).toUpperCase() ?? '?'
)

const gradients = [
  'from-violet-500 to-purple-600',
  'from-blue-500 to-cyan-600',
  'from-emerald-500 to-teal-600',
  'from-orange-500 to-amber-600',
  'from-pink-500 to-rose-600',
  'from-indigo-500 to-blue-600',
]

const gradientClass = computed(() => {
  const name = userStore.user?.full_name ?? ''

  const hash = [...name].reduce(
    (acc, char) => acc + char.charCodeAt(0),
    0
  )

  return gradients[hash % gradients.length]
})
</script>

<template>
  <div
    class="size-7 shrink-0 rounded-full flex items-center justify-center
           font-semibold text-sm text-white
           bg-gradient-to-br shadow-sm select-none"
    :class="gradientClass"
  >
    {{ initial }}
  </div>
</template>