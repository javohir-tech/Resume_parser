import { useResumeStore } from "~/entities/resume";
import type { Languages } from "~/entities/resume";
import {
  createLanguageFetch,
  editLanguageFetch,
  deleteLanguageFetch,
} from "../api/language";
import { useApiToast } from "~/shared/lib";

type LanguagePatch = Partial<Omit<Languages, "id">>;

type Savequeue = {
  pending: LanguagePatch;
  running: Promise<boolean> | null;
};

export function useLanguage() {
  const isCreating = ref(false);
  const deletingIds = ref(new Set<string>());
  const { showError } = useApiToast();
  const resumeStore = useResumeStore();

  const queues = new Map<string, Savequeue>();
  const savingIds = reactive(new Set<string>());

  const isSaving = computed(() => savingIds.size > 0);
  const isLangaugeSaving = (id: string) => savingIds.has(id);

  async function createLanguage(resume_id: string = resumeStore.resume.id) {
    isCreating.value = true;
    try {
      const response = await createLanguageFetch(resume_id);
      resumeStore.resume.languages?.push({
        id: response.language_id,
        language: "",
        degree: "",
      });
    } catch (error) {
      showError(error);
    } finally {
      isCreating.value = false;
    }
  }

  function editLanguage(id: string, changes: Partial<Omit<Languages, "id">>) {
    let queue = queues.get(id);

    if (!queue) {
      queue = { pending: {}, running: null };
      queues.set(id, queue);
    }

    Object.assign(queue.pending, changes);

    if (queue.running) {
      return queue.running;
    }

    savingIds.add(id);

    queue.running = Promise.resolve().then(() => drainQueue(id, queue));

    return queue.running;
  }

  async function drainQueue(id: string, queue: Savequeue): Promise<boolean> {
    try{
      while (Object.keys(queue.pending).length > 0) {
        const changes = queue.pending;
        queue.pending = {};
      try {
        await editLanguage(id, changes);
      } catch (error) {
        queue.pending = { ...changes, ...queue.pending };
        showError(error)
        return false;
      }
    }
    return true
  }finally{
    queue.running = null
    savingIds.delete(id)

    if(Object.keys(queue.pending).length === 0){
      queues.delete(id)
    }
  }
}

  const isDeleting = (language_id: string) =>
    deletingIds.value.has(language_id);

  async function deleteLanguage(language_id: string) {
    if (isDeleting(language_id)) return;
    deletingIds.value.add(language_id);
    try {
      await deleteLanguageFetch(language_id);
      resumeStore.resume.languages = resumeStore.resume.languages?.filter(
        (l) => l.id !== language_id,
      );
    } catch (error) {
      showError(error);
    } finally {
      deletingIds.value.delete(language_id);
    }
  }

  return { isCreating,  isSaving , savingIds , createLanguage, isDeleting, deleteLanguage , editLanguage };
}
