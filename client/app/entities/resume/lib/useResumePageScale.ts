import type { Ref } from "vue";
import { PAGE_WIDTH_PX } from "../models/pagination";

export function useResumePageScale(
  containerRef: Ref<HTMLElement | null>,
  horizontalPaddingPx = 80,
) {
  const scale = ref(1);

  function update() {
    if (!containerRef.value) return;
    const available = containerRef.value.clientWidth - horizontalPaddingPx;
    scale.value = Math.min(available / PAGE_WIDTH_PX, 1);
  }

  let observer: ResizeObserver;
  onMounted(() => {
    update();
    observer = new ResizeObserver(update);
    if (containerRef.value) observer.observe(containerRef.value);
  });
  onUnmounted(() => observer.disconnect());

  return { scale };
}
