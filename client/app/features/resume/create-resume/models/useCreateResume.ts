import { createResumeRequest } from "../api";
import { useApiToasts, apiError } from "~/shared/lib";

export function useCreateResume() {
  const localPath = useLocalePath();
  const loading = ref(false);
  const { showError } = useApiToasts();

  async function createResume() {
    loading.value = true;
    try {
      const response = await createResumeRequest();
      if (response.success) {
        await navigateTo(localPath(`/resume/${response.resume_id}`));
      }
    } catch (error) {
      const err = apiError(error);
      showError(err.message);
    } finally {
      loading.value = false;
    }
  }

  return { loading, createResume };
}
