import {
  createEducationFetch,
  deleteEducationFetch,
  editEducationFetch,
} from "../api/education";
import { useResumeStore } from "~/entities/resume";
import { useApiToast } from "~/shared/lib";

export function useEducation() {
  const isCreating = ref(false);
  const deletingIds = ref(new Set<string>());
  const resumeStore = useResumeStore();
  const { showError } = useApiToast();

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
      showError(error);
    } finally {
      isCreating.value = false;
    }
  }

  return { isCreating, createEducation };
}
