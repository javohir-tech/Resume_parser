import {
  createEducationFetch,
  deleteEducationFetch,
} from "../api/education";
import { useResumeStore } from "~/entities/resume";
import { useApiToasts , apiError } from "~/shared/lib";

export function useEducation() {
  const isCreating = ref(false);
  const deletingIds = ref(new Set<string>());
  const resumeStore = useResumeStore();
  const { showError } = useApiToasts();

  async function createEducation(resume_id: string = resumeStore.resume.id) {
    isCreating.value = true;
    try {
      const response = await createEducationFetch(resume_id);
      resumeStore.resume.education?.push({
        id: response.education_id,
        fieldOfStudy: "",
        institution: "",
        degree: "",
        location: "",
        startDate: "",
        endDate: "",
      });
    } catch (error) {
      const err = apiError(error)
      showError(err.message);
    } finally {
      isCreating.value = false;
    }
  }

  const isDeleting = (education_id: string) =>
    deletingIds.value.has(education_id);

  async function deleteEducation(education_id: string) {
    if (isDeleting(education_id)) return;
    deletingIds.value.add(education_id);
    try {
      await deleteEducationFetch(education_id);
      resumeStore.resume.education = resumeStore.resume.education?.filter(
        (edc) => edc.id !== education_id,
      );
    } catch (error) {
      const err = apiError(error)
      showError(err.message);
    } finally {
      deletingIds.value.delete(education_id);
    }
  }

  return { isCreating, createEducation, isDeleting, deleteEducation };
}
