import { useResumeStore } from "~/entities/resume";
import { editResumeFetch } from "../api/personal";

const fields = [
  "fullname",
  "title",
  "email",
  "phone",
  "location",
  "website",
  "github_link",
  "linkedin_link",
  "summary",
] as const;

type Snapshot = Record<(typeof fields)[number], string>;

export function usePersonalAvtoSave(delay = 800) {
  const store = useResumeStore();
  const isSaving = ref(false);
  const error = ref<string | null>(null);
  const saved = ref<Snapshot | null>(null);
  const activeId = ref("");

  let disposed = false;
  let timer: ReturnType<typeof setTimeout> | undefined;
  let running: Promise<boolean> | null = null;

  function snapshot(): Snapshot {
    return Object.fromEntries(
      fields.map((field) => [field, store.resume[field] ?? ""]),
    ) as Snapshot;
  }

  const isDirty = computed(() => {
    if (!saved.value || store.resume.id !== activeId.value) {
      return false;
    }

    return fields.some(
      (field) => (store.resume[field] ?? "") !== saved.value![field],
    );
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
        if (store.resume.id !== id || activeId.value !== id) {
          return false;
        }

        const previous = saved.value;
        if (!previous) return false;

        const sent = snapshot();
        const changes: Partial<Snapshot> = {};

        for (const field of fields) {
          if (sent[field] !== previous[field]) {
            changes[field] = sent[field];
          }
        }

        if (!Object.keys(changes).length) return true;

        await editResumeFetch(id, changes);

        if (disposed || activeId.value !== id || store.resume.id !== id) {
          return false;
        }

        saved.value = sent;
      }

      return false;
    } catch (err) {
      if (!disposed) {
        error.value = "saqlanmadi . qayta urunip ko'ring";
      }
      return false;
    } finally {
      if (!disposed) {
        isSaving.value = false;
      }
    }
  }

  async function flush(): Promise<boolean> {
    clearTimer();

    if (disposed || !saved.value) return false;

    if (running) {
      const success = await running;
      if (!success) return false;

      return flush();
    }

    if (store.resume.id !== activeId.value) return false;
    if (!isDirty.value) return true;

    running = drain();

    try {
      return await running;
    } finally {
      running = null;
    }
  }

  watch(
    snapshot,
    () => {
      if (disposed || !saved.value || store.resume.id !== activeId.value) {
        return;
      }

      clearTimer();

      if (isDirty.value) {
        timer = setTimeout(() => {
          void flush();
        }, delay);
      }
    },
    { flush: "sync" },
  );

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

  return {
    start,
    flush,
    isDirty,
    isSaving,
    error,
    status,
  };
}
