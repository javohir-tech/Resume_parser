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

export function usePersonalAvtoSave(delay = 800){
    
}