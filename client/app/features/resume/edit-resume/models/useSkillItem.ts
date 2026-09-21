import { useResumeStore } from "~/entities/resume";
import { createSkillItemFetch, deleteSkillItemFetch } from "../api/skills";
import { useApiToast } from "~/shared/lib";

export function useSkillItem() {
  const isCreating = ref(false);
  const deletingIds = ref(new Set<string>());
  const { showError } = useApiToast();
  const resumeStore = useResumeStore();

  async function createSkillItem(
    skills_group_id: string,
    skill_info: { skill: string },
  ) {
    isCreating.value = true;
    try {
      const response = await createSkillItemFetch(skills_group_id, skill_info);
      const skillGroup = resumeStore.resume.skills?.find(
        (sk) => sk.id === skills_group_id,
      );
      if (skillGroup) {
        skillGroup.skills.push({
          id: response.skill_item_id ,
          skill: skill_info.skill,
        });
      } else {
        throw new Error("SkillGroup not found");
      }
    //   console.log(response);
    } catch (error) {
    } finally {
      isCreating.value = false;
    }
  }

  return { isCreating, createSkillItem };
}
