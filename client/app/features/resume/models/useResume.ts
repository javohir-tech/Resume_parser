import { createResumeFetch, deleteResumeFetch } from "../api";
import { useApiToast } from "~/shared/lib";

export function useResume() {
  const loading = ref(false);
  const { showError, showSuccess } = useApiToast();

  async function createResume() {
    loading.value = true;
    try {
      const response = await createResumeFetch();
      if (response.success) {
        await navigateTo(`/resume/${response.resume_id}`);
      }
      //   console.log(response);
    } catch (err) {
      showError(err);
    } finally {
      loading.value = false;
    }
  }

  async function deleteResume(resume_id: string) {
    try {
      const response = await deleteResumeFetch(resume_id);
      if (response.success) {
        showSuccess(response.message);
      }
    } catch (error) {
      showError(error);
    }
  }

  return { loading, createResume, deleteResume };
}
