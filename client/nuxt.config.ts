// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2025-07-15",
  modules: ["@nuxt/ui", "@nuxtjs/i18n", "@vueuse/nuxt", "@nuxt/icon"],
  routeRules: {
    "/": { prerender: true },
  },
  icon: {
    serverBundle: {
      collections: ["lucide"],
    },
    clientBundle: {
      scan: true,
    },
  },
  i18n: {
    defaultLocale: "uz",
    langDir: "locales/",
    strategy: "prefix_except_default",
    locales: [
      {
        code: "uz",
        name: "Uzbek",
        file: "uz.json",
      },
      {
        code: "en",
        name: "English",
        file: "en.json",
      },
      {
        code: "ru",
        name: "Russian",
        file: "ru.json",
      },
    ],
  },
  css: ["~/assets/css/main.css"],
  devtools: { enabled: true },
  components: {
    dirs: [
      "~/widgets/home-hero",
      "~/widgets/how-it-works",
      "~/widgets/home-features",
      "~/widgets/home-pricing",
      "~/widgets/home-requests",
      "~/widgets/home-start",
    ],
  },
});
