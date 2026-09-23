import { useResumeStore } from "~/entities/resume";
import type { Languages } from "~/entities/resume";
import {
  createLanguageFetch,
  editLanguageFetch,
  deleteLanguageFetch,
} from "../api/language";
import { useApiToast } from "~/shared/lib";

export function useLanguage() {
  const isCreating = ref(false);
  const isSaving = ref(false)
  const deletingIds = ref(new Set<string>());
  const { showError } = useApiToast();
  const resumeStore = useResumeStore();

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

  async function editLanguage(language_id : string , language_info : Partial<Omit<Languages , "id">> ){
    isSaving.value = true ; 
    try { 
      await editLanguageFetch(language_id , language_info)
    } catch (error) {
      showError(error)
    }finally{
      isSaving.value = false
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
        showError(error)
    }finally{
        deletingIds.value.delete(language_id)
    }
  }

  return {isCreating , createLanguage , isDeleting , deleteLanguage}
}
