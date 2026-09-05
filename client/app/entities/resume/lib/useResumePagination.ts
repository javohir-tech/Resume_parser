import { useDebounceFn } from "@vueuse/core";
import { type ComputedRef } from "vue";
import { type Resume, type ResumeBlock } from "../models/types";
import {
  toPageContent,
  packBlocksIntoPages,
  type ResumePageContent,
} from "../models/pagination";

export function useResumePagination(
  blocks: ComputedRef<ResumeBlock[]>,
  resume: Ref<Resume> | ComputedRef<Resume>,
) {
  const measureEls = new Map<string, HTMLElement>();
  const pageContents = ref<ResumePageContent[]>([]);

  function setMeasureRef(id: string) {
    return (el: unknown) => {
      const node = (el as { $el?: HTMLElement })?.$el ?? (el as HTMLElement);
      // console.log(measureEls)
      if (node instanceof HTMLElement) measureEls.set(id, node);
      else measureEls.delete(id);
    };
  }

  const recalc = useDebounceFn(async () => {
    await nextTick();

    const heights = new Map<string, number>();
    for (const block of blocks.value) {
      heights.set(block.id, measureEls.get(block.id)?.offsetHeight ?? 0);
    }
    // console.log(heights);
    pageContents.value = toPageContent(
      packBlocksIntoPages(blocks.value, heights),
    );
  }, 150);

  watch([blocks, resume], recalc, { deep: true, immediate: true });

  return { setMeasureRef, pageContents };
}
