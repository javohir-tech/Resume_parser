import { deleteResumeFetch } from "../api";
import { useApiToast } from "~/shared/lib";

export function useDeleteResume() {
  const { showError, showSuccess } = useApiToast();
  const deleteingIds = ref(new Set<string>());

  const isDeleting = (id: string) => deleteingIds.value.has(id);

  async function deleteResume(resume_id: string) {
    if (isDeleting(resume_id)) return;

    deleteingIds.value.add(resume_id);

    try {
      const response = await deleteResumeFetch(resume_id);
      if (response.success) {
        showSuccess(response.message);
      }
      // console.log(response)
    } catch (error) {
      showError(error);
    } finally {
      deleteingIds.value.delete(resume_id);
    }
  }

  return { deleteResume, isDeleting };
}
