import { useResumeStore } from "~/entities/resume";
import { useUpdatePersonal } from "./useUpdatePersonal";

const personalFields = [
  "fullname",
  "title",
  "email",
  "phone",
  "location",
  "website",
  "github_link",
  "linkedin_link",
  "summary",
] as const;

type PersonalField = (typeof personalFields)[number];
type PersonalSnapshot = Record<PersonalField, string>;
type PersonalChanges = Partial<PersonalSnapshot>;

type SaveStatus = "idle" | "unsaved" | "saving" | "saved" | "error";

export function usePersonalAvtoSave(delay = 800) {
  const resumeStore = useResumeStore();
  const { isSaving, updatePersonal } = useUpdatePersonal();

  const active = ref(false)
  const error = ref<string | null>(null)
  const lastSaved = ref<Date | null>(null)

  const savedSnapshot = ref<PersonalSnapshot | null>(null)

  let resumeId = "";
  let disposed = false ;
  let timer : ReturnType<typeof setTimeout>  | undefined

  let queue : Promise<boolean> = Promise.resolve(true)
}
