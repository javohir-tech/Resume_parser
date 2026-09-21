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
        showError(error)
    } finally {
      isCreating.value = false;
    }
  }

  const isDeleting = (item_id : string) => deletingIds.value.has(item_id)

  async function deleteSkillItem(skills_group_id : string , skill_item_id : string){
    if(isDeleting(skill_item_id)) return
    deletingIds.value.add(skill_item_id)

    try {
        await deleteSkillItemFetch(skill_item_id)
        const  skillsGroup = resumeStore.resume.skills?.find(sk => sk.id === skills_group_id)
        if(skillsGroup){
            skillsGroup.skills = skillsGroup.skills.filter(skill => skill.id !== skill_item_id)
        }else{
            throw new Error("SkillGroup not found")
        }
    } catch (error) {
        showError(error)
    }finally{
        deletingIds.value.delete(skill_item_id)
    }

  }


  return { isCreating, createSkillItem , isDeleting ,  deleteSkillItem };
}
