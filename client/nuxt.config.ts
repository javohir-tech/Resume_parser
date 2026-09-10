// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2025-07-15",
  modules: [
    "@nuxt/ui",
    "@nuxtjs/i18n",
    "@vueuse/nuxt",
    "@nuxt/icon",
    "@pinia/nuxt",
    "@nuxt/fonts",
  ],
  runtimeConfig: {
    botToken: "",
    chatId: "",
  },
  fonts: {
    families: [
      { name: "Inter", provider: "google"   , global : true},
      { name: "Roboto", provider: "google"   , global : true},
      { name: "Merriweather", provider: "google"   , global : true},
      { name: "Playfair Display", provider: "google"   , global : true},
      { name: "Lato", provider: "google"  , global : true },
      { name: "Poppins", provider: "google"   , global : true},
      { name: "Nunito", provider: "google"   , global : true},
    ],
  },
  routeRules: {
    "/": { prerender: true },
    "/en": { prerender: true },
    "/ru": { prerender: true },

    "/about": { redirect: { to: "/contact", statusCode: 307 } },
    "/en/about": { redirect: { to: "/en/contact", statusCode: 307 } },
    "/ru/about": { redirect: { to: "/ru/contact", statusCode: 307 } },
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
    dirs: ["~/widgets/home"],
  },
});
