import { createResumeFetch, deleteResumeFetch } from "../api";
import { useApiToast } from "~/shared/lib";
import { useResumeStore } from "~/entities/resume";

export function useResume() {
  const loading = ref(false);
  const { showError, showSuccess } = useApiToast();
  const deleteingIds = ref(new Set<string>())
  const resumeStore = useResumeStore()

  const isDeleting = (id : string) => deleteingIds.value.has(id)

  async function createResume() {
    loading.value = true;
    try { 
      const response = await createResumeFetch();
      if (response.success) {
        resumeStore.resume.id = response.resume_id
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
    if(isDeleting(resume_id)) return 

    deleteingIds.value.add(resume_id)

    try {
      const response = await deleteResumeFetch(resume_id);
      if (response.success) {
        showSuccess(response.message);
      }
      // console.log(response)
    } catch (error) {
      showError(error);
    }finally{
      deleteingIds.value.delete(resume_id)
    }
  }

  return { loading, createResume, deleteResume , isDeleting };
}
