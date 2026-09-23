import { useResumeStore } from "~/entities/resume";
import { editEducationFetch } from "../api/education";

const fields = [
  "degree",
  "fieldOfStudy",
  "institution",
  "location",
  "startDate",
  "endDate",
] as const;

type Snapshot = Record<(typeof fields)[number], string>;

export function useEducationSaveAvto(delay = 800) {
  const store = useResumeStore();
  const isSaving = ref(false);
  const saved = ref<Snapshot | null>(null);
  const error = ref<string | null>(null);
  const activeId = ref("");

  let timer: ReturnType<typeof setTimeout> | undefined;
  let disposed = false;
  let running: Promise<boolean> | null = null;

  function getEducation() {
    if (!activeId.value) return null;

    return store.resume.education?.find((edc) => edc.id === activeId.value);
  }

  function snapshot(): Snapshot | null {
    const education = getEducation();

    if (!education) return null;

    return Object.fromEntries(
      fields.map((field) => [field, education[field] ?? ""]),
    ) as Snapshot;
  }

  const isDirty = computed(() => {
    if (!saved.value) return false;

    const education = getEducation();

    if (!education) return false;

    return fields.some((field) => (education[field] ?? "") !== saved.value![field]);
  });

  function clearTimer() {
    clearTimeout(timer);
    timer = undefined;
  }

  function start(education_id: string) {
    if (disposed || running || !education_id) return false;

    clearTimer();
    activeId.value = education_id;
    error.value = null;

    const current = snapshot();
    if (!current) return false;
    saved.value = current;

    return true;
  }

  async function drain(): Promise<boolean> {
    const id = activeId.value;
    isSaving.value = true;
    error.value = null;

    try {
      while (!disposed) {
        const education = getEducation();
        if (education?.id !== id) return false;

        const previous = saved.value;
        if (!previous) return false;

        const sent = snapshot();
        const changes: Partial<Snapshot> = {};

        for (const field of fields) {
          if (previous[field] !== sent![field]) {
            changes[field] = sent![field];
          }
        }

        if (!Object.keys(changes).length) return true;

        await editEducationFetch(id, changes);

        if (disposed) return false;

        saved.value = sent;
      }

      return false;
    } catch (error) {
      if (!disposed) {
        error = "Saqlanmadi qayta urunip ko'ring";
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

    const education = getEducation();
    if (!education || !isDirty) return false;

    running = drain();

    try {
      return await running;
    } finally {
      error.value = null;
    }
  }

  watch(
    snapshot,
    () => {
      if (disposed || !saved.value) return;
      clearTimer();

      if (!isDirty) {
        timer = setTimeout(() => {
          void flush();
        }, delay);
      }
    },
    { flush: "sync" },
  );

  function beforeUnload(event: BeforeUnloadEvent) {
    if (!isDirty && !isSaving) return;

    event.preventDefault();
    event.returnValue = "";
  }

  onMounted(() => {
    window.addEventListener("beforeunload", beforeUnload);
  });

  onScopeDispose(() => {
    disposed = true;
    error.value = null;

    if (typeof window !== "undefined") {
      window.removeEventListener("beforeunload", beforeUnload);
    }
  });

  return { isSaving, start, flush };
}
