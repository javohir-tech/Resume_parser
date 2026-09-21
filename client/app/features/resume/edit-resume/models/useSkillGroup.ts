import {
  createSkillGroupFetch,
  editSkillGroupFetch,
  deleteSkillGroupFetch,
} from "../api/skills";
import { useResumeStore } from "~/entities/resume";
import { useApiToast } from "~/shared/lib";

export function useSkillsGroup() {
  const resumeStore = useResumeStore();
  const { showError } = useApiToast();

  const isCreating = ref(false);
  const deletingIds = ref(new Set<string>());

  async function createSkillsGroup(resume_id: string = resumeStore.resume.id) {
    isCreating.value = true;
    try {
      const response = await createSkillGroupFetch(resume_id);
      resumeStore.resume.skills?.push({
        id: response.skills_id,
        title: "",
        skills: [],
      });
    } catch (error) {
      showError(error);
    } finally {
      isCreating.value = false;
    }
  }

  const isDeleting = (skills_id: string) => deletingIds.value.has(skills_id);

  async function deleteSkillsGroup(skills_id: string) {
    if (isDeleting(skills_id)) return;

    deletingIds.value.add(skills_id);
    try {
      await deleteSkillGroupFetch(skills_id);
      resumeStore.resume.skills = resumeStore.resume.skills?.filter(
        (sg) => sg.id !== skills_id,
      );
    } catch (error) {
      showError(error);
    } finally {
      deletingIds.value.delete(skills_id);
    }
  }

  return {isCreating , createSkillsGroup ,  isDeleting , deleteSkillsGroup}
}
