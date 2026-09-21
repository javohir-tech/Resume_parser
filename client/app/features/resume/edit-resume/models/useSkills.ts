import {
  createSkillItem,
  deleteSkillItem,
} from "../api/skills";
import { useResumeStore } from "~/entities/resume";
import { useApiToast } from "~/shared/lib";

export function useSkills() {
  const userResume = useResumeStore();
  const { showError } = useApiToast();
  const creatingSkillGroup = ref(false);
  const creatingSkillItem = ref(false)

}
