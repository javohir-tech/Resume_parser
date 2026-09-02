export const useResumeStore = defineStore("resume", () => {
  const personalInfo = reactive({
    fullName: "",
  });

  return { personalInfo };
});
