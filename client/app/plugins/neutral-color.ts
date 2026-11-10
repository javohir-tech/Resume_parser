export default defineNuxtPlugin(() => {
  const appConfig = useAppConfig();

  const cookie = useCookie<string>("neutral_color", {
    maxAge: 60 * 60 * 24 * 365,
    default: () => "slate",
    sameSite: "lax",
  });

  appConfig.ui.colors.neutral = cookie.value;
});
