import { nextTick } from "vue";

const PAGE_SELECTOR = "[data-pdf-page]";


// Shrift faylini HTML ichiga joylash uchun data URL'ga aylantiradi.
function blobToDataUrl(blob: Blob): Promise<string> {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();

    reader.onload = () => resolve(String(reader.result));
    reader.onerror = () =>
      reject(new Error("Shrift faylini o'qib bo'lmadi"));

    reader.readAsDataURL(blob);
  });
}

// @font-face ichidagi URL'larni faylning o'zi bilan almashtiradi.
async function embedFontUrls(
  css: string,
  baseUrl: string,
): Promise<string> {
  const matches = [
    ...css.matchAll(/url\(\s*(['"]?)(.*?)\1\s*\)/g),
  ];

  for (const match of matches) {
    const source = match[2];

    if (!source || source.startsWith("data:")) continue;

    const url = new URL(source, baseUrl);

    if (!["http:", "https:"].includes(url.protocol)) {
      throw new Error("Shrift manzili qo'llab-quvvatlanmaydi");
    }

    const response = await fetch(url.href, {
      signal: AbortSignal.timeout(15_000),
    });

    if (!response.ok) {
      throw new Error("PDF uchun shriftni yuklab bo'lmadi");
    }

    const dataUrl = await blobToDataUrl(await response.blob());

    css = css.replace(match[0], `url("${dataUrl}")`);
  }

  return css;
}

// Sahifadagi ishlatilgan shrift oilalarining @font-face qoidalari.
async function collectFonts(
  usedFamilies: Set<string>,
): Promise<string> {
  const rulesToEmbed = new Map<string, string>();
  const visited = new Set<CSSStyleSheet>();

  function visitSheet(sheet: CSSStyleSheet) {
    if (visited.has(sheet) || sheet.disabled) return;
    visited.add(sheet);

    let rules: CSSRuleList;

    try {
      rules = sheet.cssRules;
    } catch {
      throw new Error(
        "Tashqi CSS'ni o'qib bo'lmadi. " +
        "PDF shriftlarini same-origin orqali yuklash kerak.",
      );
    }

    visitRules(rules, sheet.href ?? document.baseURI);
  }

  function visitRules(rules: CSSRuleList, baseUrl: string) {
    for (const rule of Array.from(rules)) {
      if (rule instanceof CSSFontFaceRule) {
        const family = rule.style
          .getPropertyValue("font-family")
          .replace(/['"]/g, "")
          .trim()
          .toLowerCase();

        if (usedFamilies.has(family)) {
          rulesToEmbed.set(rule.cssText, baseUrl);
        }
      } else if (rule instanceof CSSImportRule) {
        if (rule.styleSheet) visitSheet(rule.styleSheet);
      } else if ("cssRules" in rule) {
        visitRules(
          (rule as CSSGroupingRule).cssRules,
          baseUrl,
        );
      }
    }
  }

  for (const sheet of Array.from(document.styleSheets)) {
    visitSheet(sheet);
  }

  const fonts = await Promise.all(
    [...rulesToEmbed].map(([css, baseUrl]) =>
      embedFontUrls(css, baseUrl),
    ),
  );

  return fonts.join("\n");
}

// Oddiy DOM elementlari va inline SVG stillarini ko'chiradi.
function copyStyles(
  source: Element,
  target: Element,
  usedFamilies: Set<string>,
) {
  const computed = window.getComputedStyle(source);

  for (const family of computed.fontFamily.split(",")) {
    usedFamilies.add(
      family.replace(/['"]/g, "").trim().toLowerCase(),
    );
  }

  if (
    target instanceof HTMLElement ||
    target instanceof SVGElement
  ) {
    target.removeAttribute("style");

    for (const property of Array.from(computed)) {
      target.style.setProperty(
        property,
        computed.getPropertyValue(property),
      );
    }
  }

  // HTML nusxasida inline event handlerlar qolmasin.
  for (const attribute of Array.from(target.attributes)) {
    if (attribute.name.toLowerCase().startsWith("on")) {
      target.removeAttribute(attribute.name);
    }
  }

  const sourceChildren = Array.from(source.children);
  const targetChildren = Array.from(target.children);

  sourceChildren.forEach((child, index) => {
    const targetChild = targetChildren[index];

    if (targetChild) {
      copyStyles(child, targetChild, usedFamilies);
    }
  });
}

export async function buildResumeHtml(): Promise<string> {
  if (typeof document === "undefined") {
    throw new Error("PDF faqat brauzerda tayyorlanadi");
  }

  await nextTick();
  await document.fonts.ready;

  const jobs: Promise<void>[] = [];
  window.dispatchEvent(new CustomEvent('resume:prepare-pdf', { detail: jobs }));
  await Promise.all(jobs);
  await nextTick();

  const pages = Array.from(
    document.querySelectorAll<HTMLElement>(PAGE_SELECTOR),
  );


  if (!pages.length) {
    throw new Error(
      "Resume sahifalari topilmadi. data-pdf-page ni tekshiring.",
    );
  }

  const output = document.implementation.createHTMLDocument(
    "Resume",
  );

  output.documentElement.lang = document.documentElement.lang;

  const charset = output.createElement("meta");
  charset.setAttribute("charset", "utf-8");
  output.head.prepend(charset);

  const usedFamilies = new Set<string>();

  for (const page of pages) {
    const clone = page.cloneNode(true) as HTMLElement;

    copyStyles(page, clone, usedFamilies);

    clone
      .querySelectorAll("script, iframe, object, embed")
      .forEach((element) => element.remove());

    // Preview masshtabi va joylashuvini PDF uchun bekor qilamiz.
    clone.style.setProperty("position", "relative", "important");
    clone.style.setProperty("inset", "auto", "important");
    clone.style.setProperty("transform", "none", "important");
    clone.style.setProperty("box-shadow", "none", "important");
    clone.style.setProperty("margin", "0", "important");
    clone.style.setProperty("width", "210mm", "important");
    clone.style.setProperty("height", "auto", "important");
    
    output.body.appendChild(clone);
  }

  const fontCss = await collectFonts(usedFamilies);

  const style = output.createElement("style");

  style.textContent = `
    ${fontCss}

    @page {
      size: A4;
      margin: 0;
    }

    html, body {
      margin: 0;
      padding: 0;
      background: white;
    }

    *, *::before, *::after {
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
      animation: none !important;
      transition: none !important;
    }

    ${PAGE_SELECTOR} {
      break-after: page !important;
    }

    ${PAGE_SELECTOR}:last-child {
      break-after: auto !important;
    }
  `;

  output.head.appendChild(style);

  return `<!DOCTYPE html>\n${output.documentElement.outerHTML}`;
}
