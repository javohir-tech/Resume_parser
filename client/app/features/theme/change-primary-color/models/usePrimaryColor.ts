import { type color_types } from "./colors";

export default function usePrimaryColor() {
  const cookie = useCookie("primary-color");
  const appConfig = useAppConfig();

  const setPrimary = (color: color_types) => {
    appConfig.ui.colors.primary = color;
    cookie.value = color;
  };

  return { primary: cookie, setPrimary };
}
