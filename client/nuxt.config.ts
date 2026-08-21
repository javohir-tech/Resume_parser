// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2025-07-15",
  modules: ["@nuxt/ui", "@nuxtjs/i18n", "@vueuse/nuxt", "@nuxt/icon"],
  icon: {
    serverBundle: {
      collections: ["lucide"],
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
      { path: "~/widgets/home-hero", pathPrefix : true },
      { path: "~/widgets/how-it-works", pathPrefix: false },
      { path: "~/widgets/home-features", pathPrefix: false },
      { path: "~/widgets/home-pricing", pathPrefix: false },
      { path: "~/widgets/home-requests", pathPrefix: false },
      { path: "~/widgets/home-start", pathPrefix: false },
    ],
  },
});
