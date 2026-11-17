import {
  createSkillGroupRequest,
  deleteSkillGroupRequest,
} from "../api/skills";
import { useResumeStore } from "~/entities/resume";
import { useApiToasts, apiError } from "~/shared/lib";

export function useSkillsGroup() {
  const resumeStore = useResumeStore();
  const { showError } = useApiToasts();

  const isCreating = ref(false);
  const deletingIds = ref(new Set<string>());

  async function createSkillsGroup(resume_id: string = resumeStore.resume.id):Promise<string | null> {
    isCreating.value = true;
    try {
      const response = await createSkillGroupRequest(resume_id);
      resumeStore.resume.skills?.push({
        id: response.skills_id,
        title: "",
        skills: [],
      });
      return response.skills_id
    } catch (error) {
      const err = apiError(error);
      showError(err.message);
      return null
    } finally {
      isCreating.value = false;
    }
  }

  const isDeleting = (skills_id: string) => deletingIds.value.has(skills_id);

  async function deleteSkillsGroup(skills_id: string) {
    if (isDeleting(skills_id)) return;

    deletingIds.value.add(skills_id);
    try {
      await deleteSkillGroupRequest(skills_id);
      resumeStore.resume.skills = resumeStore.resume.skills?.filter(
        (sg) => sg.id !== skills_id,
      );
    } catch (error) {
      const err = apiError(error);
      showError(err.message);
    } finally {
      deletingIds.value.delete(skills_id);
    }
  }

  return {
    isCreating,
    createSkillsGroup,
    isDeleting,
    deleteSkillsGroup,
  };
}
