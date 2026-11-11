export default function useRestartTheme() {
  const primary_color = useCookie("primary-color");
  const neutral_color = useCookie("neutral_color");
  const font_cookie = useCookie("app-font");
  const appConfig = useAppConfig();

  const font = useState("app-font" , ()=>font_cookie.value)

  function restartTheme() {
    primary_color.value = "green";
    neutral_color.value = "slate";
    font_cookie.value = "Inter";
    font.value = "Inter"
    appConfig.ui.colors.primary = primary_color.value;
    appConfig.ui.colors.neutral = neutral_color.value;

  }

  return { restartTheme };
}
