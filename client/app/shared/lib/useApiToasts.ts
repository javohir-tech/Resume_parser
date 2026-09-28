export function useApiToasts() {
  const toast = useToast();

  function showError(message: string) {
    toast.add({ title: message, color: "error" });
  }

  function showSuccess(message: string) {
    toast.add({ title: message, color: "success" });
  }

  return {showError , showSuccess}
}
