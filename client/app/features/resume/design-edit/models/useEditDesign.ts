import { useApiToasts, apiError } from "~/shared/lib";
import { useResumeStore, type DesignInfo } from "~/entities/resume";
import { editDesignRequest } from "../api";

const fields = [
  "template",
  "heading_title_color",
  "entry_title_color",
  "font",
] as const satisfies readonly (keyof DesignInfo)[];

type Snapshot = Pick<DesignInfo, (typeof fields)[number]>;

export function useEditDesign(delay = 800) {
  const store = useResumeStore();
  const { showError } = useApiToasts();
  const isSaving = ref(false);
  const error = ref<string | null>(null);
  const saved = ref<Snapshot | null>(null);
  const activeId = ref("");

  let disposed = false;
  let timer: ReturnType<typeof setTimeout> | undefined;
  let running: Promise<boolean> | null = null;

  function snapshot(): Snapshot {
    const design = store.designInfo;
    // Copy colors so edits cannot mutate saved or in-flight snapshots.
    return {
      template: design.template,
      font: design.font,
      heading_title_color: design.heading_title_color
        ? { name: design.heading_title_color.name, hex: design.heading_title_color.hex }
        : null,
      entry_title_color: design.entry_title_color
        ? { name: design.entry_title_color.name, hex: design.entry_title_color.hex }
        : null,
    };
  }

  function changedFields(previous: Snapshot, current: Snapshot) {
    const changes: Partial<Snapshot> = {};
    function compare<K extends keyof Snapshot>(field: K) {
      if (JSON.stringify(previous[field]) !== JSON.stringify(current[field])) {
        changes[field] = current[field];
      }
    }
    fields.forEach(compare);
    return changes;
  }

  const isDirty = computed(() => {
    if (!saved.value || store.resume.id !== activeId.value) return false;
    return Object.keys(changedFields(saved.value, snapshot())).length > 0;
  });

  const status = computed(() => {
    if (isSaving.value) return "saving";
    if (error.value) return "error";
    if (isDirty.value) return "unsaved";
    return saved.value ? "saved" : "idle";
  });

  function clearTimer() {
    clearTimeout(timer);
    timer = undefined;
  }

  // Start only after both the resume and its design have loaded.
  function start() {
    if (disposed || running || !store.resume.id) return false;
    clearTimer();
    activeId.value = store.resume.id;
    saved.value = snapshot();
    error.value = null;
    return true;
  }

  async function drain(): Promise<boolean> {
    const id = activeId.value;
    isSaving.value = true;
    error.value = null;

    try {
      while (!disposed) {
        if (store.resume.id !== id || !saved.value) return false;
        const sent = snapshot();
        const changes = changedFields(saved.value, sent);
        if (!Object.keys(changes).length) return true;

        await editDesignRequest(id, changes);

        if (disposed || store.resume.id !== id) return false;
        saved.value = sent;
      }
      return false;
    } catch (err) {
      // Preserve unsaved changes for retry without flooding failed requests.
      
      return false;
    } finally {
      isSaving.value = false;
    }
  }

  async function flush(): Promise<boolean> {
    clearTimer();
    if (disposed || !saved.value || store.resume.id !== activeId.value) return false;

    if (running) {
      if (!(await running)) return false;
      return flush();
    }

    if (!isDirty.value) {
      error.value = null;
      return true;
    }

    running = drain();
    try {
      return await running;
    } finally {
      running = null;
    }
  }

  watch(snapshot, () => {
    if (disposed || !saved.value || store.resume.id !== activeId.value) return;
    clearTimer();
    if (isDirty.value) {
      timer = setTimeout(() => { void flush(); }, delay);
    } else {
      error.value = null;
    }
  }, { flush: "sync" });

  function beforeUnload(event: BeforeUnloadEvent) {
    if (!isDirty.value && !isSaving.value) return;
    event.preventDefault();
    event.returnValue = "";
  }

  onMounted(() => {
    window.addEventListener("beforeunload", beforeUnload);
  });

  onScopeDispose(() => {
    disposed = true;
    clearTimer();
    if (typeof window !== "undefined") {
      window.removeEventListener("beforeunload", beforeUnload);
    }
  });

  return { start, flush, isDirty, isSaving, error, status };
}
