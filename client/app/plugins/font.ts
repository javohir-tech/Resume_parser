import useFont from "~/features/theme/change-font/models/useFont";

export default defineNuxtPlugin(() => {
  const { font } = useFont();

  useHead({
    htmlAttrs: { style: () => `--app-font: '${font.value}'` },
  });
});
