import { useResumeStore } from "~/entities/resume";
import { editSkillGroupRequest } from "../api/skills";
import { type SkillGroup } from "~/entities/resume";

const fields = ["title"] as const;

type Snapshot = Record<(typeof fields)[number], string>;

export function useSkillsGroupAvtoSave(delay = 800) {
  const store = useResumeStore();
  const isSaving = ref(false);
  const error = ref<string | null>(null);
  const saved = ref<Snapshot | null>(null);
  const activeId = ref("");

  let disposed = false;
  let timer: ReturnType<typeof setTimeout> | undefined;
  let running: Promise<boolean> | null = null;

  function getSkillsGroup(): SkillGroup | undefined {
    if (!activeId.value) return undefined;

    return store.resume.skills?.find((s) => s.id === activeId.value);
  }

  function snapshot(): Snapshot | null {
    const skills_group = getSkillsGroup();
    if (!skills_group) return null;

    return Object.fromEntries(
      fields.map((field) => [field, skills_group[field] ?? ""]),
    ) as Snapshot;
  }

  const isDirty = computed(() => {
    if (!saved.value) return false;

    const skills_group = getSkillsGroup();
    if (!skills_group) return false;

    return fields.some(
      (field) => (skills_group[field] ?? "") !== saved.value![field],
    );
  });

  function clearTimer() {
    clearTimeout(timer);
    timer = undefined;
  }

  function start(skills_group_id: string) : boolean {
    if (disposed || running || !skills_group_id) return false;

    clearTimer();
    activeId.value = skills_group_id;
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
        const skills_group = getSkillsGroup();
        if (!skills_group) return false;
        
        const previous = saved.value;
        if (!previous) return false;

        const sent = snapshot();
        if (!sent) return false;

        const changes: Partial<Snapshot> = {};

        for (const field of fields) {
          if (sent[field] !== previous[field]) {
            changes[field] = skills_group[field];
          }
        }

        if (!Object.keys(changes).length) return true;

        await editSkillGroupRequest(id, changes);

        if (disposed || !skills_group) return false;

        saved.value = sent;
      }
      return false;
    } catch (err) {
      if (!disposed) {
        error.value = "saqlanmadi qaytadan urunip ko'ring";
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

    const skills_group = getSkillsGroup();

    if (!skills_group) return false;
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
    isSaving,
    error,
    isDirty,
    start,
    flush,
  };
}
