import {
  createSkillItem,
  deleteSkillItem,
} from "../api/skills";
import { useResumeStore } from "~/entities/resume";
import { useApiToasts } from "~/shared/lib";

export function useSkills() {
  const userResume = useResumeStore();
  const { showError } = useApiToasts();
  const creatingSkillGroup = ref(false);
  const creatingSkillItem = ref(false)

}
