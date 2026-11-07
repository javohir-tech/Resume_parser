export default function usePrimaryColor() {
  const cookie = useCookie("primary-color");
  const appConfig = useAppConfig();

  const setPrimary = (color: string) => {
    appConfig.ui.colors.primary = color;
    cookie.value = color;
  };

  return { primary: cookie, setPrimary };
}
