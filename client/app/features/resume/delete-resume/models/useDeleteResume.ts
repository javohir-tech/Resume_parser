import { deleteResumeRequest } from "../api";
import { useApiToasts, apiError } from "~/shared/lib";

export function useDeleteResume() {
  const { showError, showSuccess } = useApiToasts();
  const deleteingIds = ref(new Set<string>());

  const isDeleting = (id: string) => deleteingIds.value.has(id);

  async function deleteResume(resume_id: string): Promise<boolean> {
    if (isDeleting(resume_id)) return false;

    deleteingIds.value.add(resume_id);

    try {
      const response = await deleteResumeRequest(resume_id);
      if (response.success) {
        showSuccess(response.message);
        return true;
      }

      // console.log(response)
      return false;
    } catch (error) {
      const err = apiError(error);
      showError(err.message);
      return false;
    } finally {
      deleteingIds.value.delete(resume_id);
    }
  }

  return { deleteResume, isDeleting };
}
