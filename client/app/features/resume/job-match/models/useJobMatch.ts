import { apiError, useApiToasts } from "~/shared/lib";
import { JobMatchRequest } from "../api";

export const useJobMatch = () => {
  const loading = ref<boolean>(false);
  const { showError, showSuccess } = useApiToasts();
  const localPath = useLocalePath();
  async function jobMatchResume(resume_id: string, vacancy_text: string) {
    loading.value = true;
    try {
      const response = await JobMatchRequest({ resume_id, vacancy_text });
      if (response.success) {
        showSuccess("Rezyumeingiz moslashtirldi");
        await navigateTo(localPath(`/resume/${response.resume_id}/job-match`));
      }
    } catch (error) {
      const err = apiError(error);
      showError(err.message);
    } finally {
      loading.value = false;
    }
  }

  return { loading, jobMatchResume };
};
