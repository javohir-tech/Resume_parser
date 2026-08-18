// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2025-07-15",
  modules: ["@nuxt/ui", "@nuxtjs/i18n"],
  i18n: {
    langDir: "locales/",
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
});
