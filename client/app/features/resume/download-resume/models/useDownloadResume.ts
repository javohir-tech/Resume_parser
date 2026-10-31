import { downloadResumeRequest } from "../api";
import { apiError, useApiToasts } from "~/shared/lib";
import { buildResumeHtml } from "./buildResumeHtml";

export const useDownloadResume = () => {
    const loading = ref(false)
    const {showError} = useApiToasts()

    async function downloadResume(resume_id : string) : Promise<boolean> {
        if (loading.value || !resume_id) return false
        loading.value = true
        try{
            const html = await buildResumeHtml()
            const response = await downloadResumeRequest(resume_id, html)
            const url = URL.createObjectURL(response)
            const link = document.createElement("a")
            link.href = url
            link.download = `resume-${resume_id}.pdf`
            document.body.appendChild(link)
            link.click()
            link.remove()
            setTimeout(() => URL.revokeObjectURL(url), 60_000)
            return true
        }catch(error){
            const fetchError = error as { data?: unknown; response?: unknown }
            if (fetchError.data instanceof Blob) {
                try {
                    const data = JSON.parse(await fetchError.data.text())
                    showError(apiError({ response: fetchError.response, data }).message)
                    return false
                } catch { /* Use default error below. */ }
            }
            if (error instanceof Error && !fetchError.response && error.name !== 'FetchError') {
                showError(error.message)
                return false
            }
            const err = apiError(error)
            showError(err.message)
            return false
        }finally{
            loading.value = false
        }
    }

    return {loading , downloadResume}   

};
