import { resumeParseRequest, resumeImportRequest } from "../api";
import { useApiToast } from "~/shared/lib";

export function useResumeParse() {
  const loading = ref<boolean>(false);
  const { showError } = useApiToast();

  async function resumeParse(file : File) {
    try {
      const response  = resumeParseRequest(file)
      console.log(response)
    } catch (error) {
        console.log(error)    
    }
  }

  return {loading , resumeParse}
}
