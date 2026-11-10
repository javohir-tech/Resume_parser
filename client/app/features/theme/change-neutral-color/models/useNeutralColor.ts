import { type color_types } from "./colors";

export default function useNeutralColor() {
  const cookie = useCookie("neutral_color");
  const appConfig = useAppConfig();

  const setNeutralColor = (color: color_types) => {
    appConfig.ui.colors.neutral = color;
    cookie.value = color;
  };

  return { neutral: cookie, setNeutralColor };
}
