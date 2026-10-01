import { useApiToasts, apiError } from "~/shared/lib";
import { useResumeStore } from "~/entities/resume";

export function useEditDesign() {
  const resumeStore = useResumeStore();
  const { showError } = useApiToasts();

  async function editDesign() {
    console.log(1);
  }

 
}
