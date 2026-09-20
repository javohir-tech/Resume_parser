import { getResumeFetch, useResumeStore, type Resume } from "~/entities/resume";
import { useApiToast } from "~/shared/lib";

export function useGetResume() {
  const loading = ref(false);
  const { showError } = useApiToast();
  const resumeStore = useResumeStore();

  async function getResume(resume_id: string) {
    loading.value = true;
    try {
      const response = await getResumeFetch(resume_id);
      resumeStore.resume = response
      console.log(response);
    } catch (error) {
      showError(error);
    } finally {
      loading.value = false;
    }
  }

  return { loading, getResume };
}
