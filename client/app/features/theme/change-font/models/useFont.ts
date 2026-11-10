import { fonts, type AppFont } from "./fonts";

export default function useFont() {
  const cookie = useCookie<AppFont>("app-font", {
    maxAge: 60 * 60 * 24 * 365,
    default: () => "Inter",
    sameSite: "lax",
  });

  const font = useState<AppFont>("app-font", () => cookie.value);

  function setFont(value: AppFont) {
    if (!fonts.includes(value)) return;
    font.value = value;
    cookie.value = value;
  }

  return { font, setFont };
}
