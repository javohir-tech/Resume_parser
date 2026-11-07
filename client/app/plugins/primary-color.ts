export default defineNuxtPlugin(() => {
  const appConfig = useAppConfig();

  const cookie = useCookie<string>("primary-color", {
    maxAge: 60 * 6024 * 365,
    default: () => "green",
    sameSite: "lax",
  });

  appConfig.ui.colors.primary = cookie.value;
});
