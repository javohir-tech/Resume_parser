import type { Personal } from "~/entities/resume";
import { editResumeFetch } from "../api/personal";

export type PersonalPatch = Partial<Omit<Personal, "id">>;

export function useUpdatePersonal() {
  const isSaving = ref(false);

  async function updatePersonal(resume_id: string, changes: PersonalPatch) {
    isSaving.value = true;
    try {
      await editResumeFetch(resume_id, changes);
    } finally {
      isSaving.value = false;
    }
  }

  return { isSaving, updatePersonal };
}


