import { useResumeStore } from "~/entities/resume";
import { editExperienceFetch } from "../api/experience";
import type { Experience } from "~/entities/resume";

const fields = [
  "position",
  "company",
  "location",
  "startDate",
  "endDate",
  "description",
] as const;

type Snapshot = Record<(typeof fields)[number], string>;

export function useExperienceAvtoSave(delay = 800) {
  const store = useResumeStore();
  const isSaving = ref(false);
  const error = ref<string | null>(null);
  const saved = ref<Snapshot | null>(null);
  const activeId = ref("");

  let disposed = false;
  let timer: ReturnType<typeof setTimeout> | undefined;
  let running: Promise<boolean> | null = null;

  function getExperience(): Experience | undefined {
    if (!activeId.value) return undefined;

    return store.resume.experience?.find((exp) => exp.id === activeId.value);
  }

  function snapshot(): Snapshot | null {
    const experience = getExperience();

    if (!experience) return null;

    return Object.fromEntries(
      fields.map((field) => [field, experience[field] ?? ""]),
    ) as Snapshot;
  }

  const isDirty = computed(() => {
    if (!saved.value) return false;

    const experience = getExperience();
    if (!experience) return false;

    return fields.some(
      (field) => (experience[field] ?? "") !== saved.value![field],
    );
  });

  function clearTimer() {
    clearTimeout(timer);
    timer = undefined;
  }

  function start(experience_id: string) {
    if (disposed || running || !experience_id) return false;

    clearTimer();
    activeId.value = experience_id;
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
        const experience = getExperience();
        if (!experience) {
          return false;
        }

        const previous = saved.value;
        if (!previous) return false;

        const sent = snapshot();
        const changes: Partial<Snapshot> = {};

        for (const field of fields) {
          if (previous[field] !== sent![field]) {
            changes[field] = experience[field];
          }
        }

        if (!Object.keys(changes).length) return true;

        await editExperienceFetch(id, changes);

        if (disposed || !experience) return false;

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

    const experience = getExperience();

    if (!experience) return false;
    if (!isDirty) return true;

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
      if (disposed || !saved.value) return;

      clearTimer();

      if (isDirty.value) {
        timer = setTimeout(() => {
          void flush();
        }, delay);
      }
    },
    { flush: "sync" },
  );

//   function beforeUnload(event: BeforeUnloadEvent) {
//     if (!isDirty.value && !isSaving.value) return;

//     event.preventDefault();
//     event.returnValue = "";
//   }

//   onMounted(() => {
//     window.addEventListener("beforeunload", beforeUnload);
//   });

  onScopeDispose(() => {
    disposed = true;
    clearTimer();

    // if (typeof window !== "undefined") {
    //   window.removeEventListener("beforeunload", beforeUnload);
    // }
  });

  return {
    isSaving,
    error,
    isDirty , 
    start,
    flush,
  };
}
