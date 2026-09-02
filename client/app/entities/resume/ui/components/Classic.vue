<!-- entities/resume/ui/components/Classic.vue -->
<script setup lang="ts">
import ResumePage from '../ResumePage.vue'

interface Experience {
    id: string
    position: string
    company: string
    location?: string
    startDate: string
    endDate?: string // yo'q bo'lsa "hozirgacha"
    description?: string
}

interface Education {
    id: string
    degree: string
    institution: string
    location?: string
    startDate: string
    endDate?: string
}

interface SkillGroup {
    id: string
    title: string
    skills: string[]
}

defineProps<{
    fullname: string
    title?: string // masalan "Frontend Developer"
    email?: string
    phone?: string
    location?: string
    website?: string
    summary?: string
    experience?: Experience[]
    education?: Education[]
    skills?: SkillGroup[]
}>()
</script>

<template>
    <ResumePage>
        <div class="font-serif text-gray-900">
            <!-- Header -->
            <header class="text-center border-b-2 border-gray-900 pb-4 mb-6">
                <h1 class="text-3xl font-bold tracking-wide uppercase">
                    {{ fullname }}
                </h1>
                <p v-if="title" class="text-lg text-gray-600 mt-1">
                    {{ title }}
                </p>
                <div class="flex justify-center flex-wrap gap-x-3 gap-y-1 text-sm text-gray-600 mt-3">
                    <span v-if="email">{{ email }}</span>
                    <span v-if="phone">·</span>
                    <span v-if="phone">{{ phone }}</span>
                    <span v-if="location">·</span>
                    <span v-if="location">{{ location }}</span>
                    <span v-if="website">·</span>
                    <span v-if="website">{{ website }}</span>
                </div>
            </header>

            <!-- Summary -->
            <section v-if="summary" class="mb-6">
                <h2 class="text-sm font-bold uppercase tracking-wider border-b border-gray-400 mb-2 pb-1">
                    Malumot
                </h2>
                <p class="text-sm leading-relaxed text-gray-800">
                    {{ summary }}
                </p>
            </section>

            <!-- Experience -->
            <section v-if="experience?.length" class="mb-6">
                <h2 class="text-sm font-bold uppercase tracking-wider border-b border-gray-400 mb-3 pb-1">
                    Ish tajribasi
                </h2>
                <div v-for="item in experience" :key="item.id" class="mb-4 last:mb-0 break-inside-avoid">
                    <div class="flex justify-between items-baseline">
                        <h3 class="font-bold text-sm">{{ item.position }}</h3>
                        <span class="text-xs text-gray-500 whitespace-nowrap ml-2">
                            {{ item.startDate }} — {{ item.endDate || 'Hozirgacha' }}
                        </span>
                    </div>
                    <p class="text-sm text-gray-600 italic">
                        {{ item.company }}<span v-if="item.location"> · {{ item.location }}</span>
                    </p>
                    <p v-if="item.description" class="text-sm text-gray-800 mt-1 leading-relaxed">
                        {{ item.description }}
                    </p>
                </div>
            </section>

            <!-- Education -->
            <section v-if="education?.length" class="mb-6">
                <h2 class="text-sm font-bold uppercase tracking-wider border-b border-gray-400 mb-3 pb-1">
                    Ta'lim
                </h2>
                <div v-for="item in education" :key="item.id" class="mb-3 last:mb-0 break-inside-avoid">
                    <div class="flex justify-between items-baseline">
                        <h3 class="font-bold text-sm">{{ item.degree }}</h3>
                        <span class="text-xs text-gray-500 whitespace-nowrap ml-2">
                            {{ item.startDate }} — {{ item.endDate || 'Hozirgacha' }}
                        </span>
                    </div>
                    <p class="text-sm text-gray-600 italic">
                        {{ item.institution }}<span v-if="item.location"> · {{ item.location }}</span>
                    </p>
                </div>
            </section>

            <!-- Skills -->
            <section v-if="skills?.length">
                <h2 class="text-sm font-bold uppercase tracking-wider border-b border-gray-400 mb-3 pb-1">
                    Ko'nikmalar
                </h2>
                <div v-for="group in skills" :key="group.id" class="mb-2 last:mb-0">
                    <span class="text-sm font-bold">{{ group.title }}: </span>
                    <span class="text-sm text-gray-800">{{ group.skills.join(', ') }}</span>
                </div>
            </section>
        </div>
    </ResumePage>
</template>