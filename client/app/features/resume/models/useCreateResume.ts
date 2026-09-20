import { createResumeFetch } from "../api";
import { useApiToast } from "~/shared/lib";
import { useResumeStore } from "~/entities/resume";

export function useCreateResume(){
    const localPath = useLocalePath()
    const loading = ref(false)
    const {showError} = useApiToast()
    const resumeStore = useResumeStore()

    async function createResume(){
        loading.value = true ;
        try {
            const response = await createResumeFetch()
            if(response.success){
                resumeStore.resume.id = response.resume_id
                await navigateTo(localPath(`/resume/${response.resume_id}`))
            }
        } catch (error) {
            showError(error)
        }finally{
            loading.value = false
        }
    }
    
    return {loading , createResume}
}