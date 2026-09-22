import { useResumeStore } from "~/entities/resume";
import {
  createExperienceFetch,
  deleteExperienceFetch,
} from "../api/experience";
import { useApiToast } from "~/shared/lib";

export function useExperience() {
  const isCreating = ref(false);
  const resumeStore = useResumeStore();
  const { showError } = useApiToast();
  const deletingIds = ref(new Set<string>());

  async function createExperience(resume_id: string = resumeStore.resume.id) {
    isCreating.value = true;
    try {
      const response = await createExperienceFetch(resume_id);
      resumeStore.resume.experience?.push({
        id: response.experience_id,
        position: "",
        company: "",
        startDate: "",
        endDate: "",
        description: "",
        location: "",
      });
    } catch (error) {
      showError(error);
    } finally {
      isCreating.value = false;
    }
  }

  const isDeleting = (experience_id: string) =>
    deletingIds.value.has(experience_id);

  async function deleteExperience(experience_id: string) {
    if (isDeleting(experience_id)) return;

    deletingIds.value.add(experience_id);
    try {
      await deleteExperienceFetch(experience_id);
      resumeStore.resume.experience = resumeStore.resume.experience?.filter(
        (exp) => exp.id !== experience_id,
      );
    } catch (error) {
      showError(error);
    } finally {
      deletingIds.value.delete(experience_id);
    }
  }

  return { isCreating, createExperience, isDeleting, deleteExperience };
}
