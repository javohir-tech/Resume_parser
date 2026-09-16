import { getErrorMessage } from "./handleApiError";

export function useApiToast() {
  const toast = useToast();

  function showError(err: unknown, fallback = "Internal Server Error") {
    toast.add({ title: getErrorMessage(err, fallback), color: "error" });
  }

  function showSuccess(message: string) {
    toast.add({ title: message, color: "success" });
  }

  return { showError, showSuccess };
}
