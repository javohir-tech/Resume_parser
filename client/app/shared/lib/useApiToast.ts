import { getErrorMessage } from "./handleApiError";

export function useApiToast() {
  const toast = useToast();

  function showError(err: unknown | null, fallback = "Internal Server Error") {
    if (!err) {
      toast.add({ title: fallback, color: "error" });
    }else {
      toast.add({ title: getErrorMessage(err, fallback), color: "error" });
    }
  }

  function showSuccess(message: string) {
    toast.add({ title: message, color: "success" });
  }

  return { showError, showSuccess };
}
