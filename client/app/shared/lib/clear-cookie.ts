export const useClearCookie = () => {
  const clearCookie = () => {
    const refresh_token = useCookie("refresh_token");
    const access_token = useCookie("access_token");

    access_token.value = null;
    refresh_token.value = null;

    const primary_color = useCookie("primary-color");
    const neutral_color = useCookie("neutral_color");
    const font_cookie = useCookie("app-font");
    const appConfig = useAppConfig();

    const font = useState("app-font", () => font_cookie.value);

    primary_color.value = "green";
    neutral_color.value = "slate";
    font_cookie.value = "Inter";

    font.value = "Inter";
    appConfig.ui.colors.primary = primary_color.value;
    appConfig.ui.colors.neutral = neutral_color.value;
  };

  return { clearCookie };
};
