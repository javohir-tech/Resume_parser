import { useResumeStore } from "./store";
import { getResumeFetch } from "../api";
import { useApiToast } from "~/shared/lib";

export function useGetResume() {
  const loading = ref(false);
  const { showError } = useApiToast();
  const resumeStore = useResumeStore();
  
  let disposed =  false;

  onScopeDispose(()=>{
    disposed = true 
  })

  async function getResume(resume_id: string):Promise<boolean> {

    if(disposed) return false

    loading.value = true;
    try {
      const response = await getResumeFetch(resume_id);

      if (disposed) return false 
      resumeStore.resume = response

      return true
    //   console.log(response);
    } catch (error) {
      if(!disposed){
        showError(error);
      }
      return false
    } finally {
      if(!disposed){
        loading.value = false;
      }
    }
  }

  return { loading, getResume };
}
