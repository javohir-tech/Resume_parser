export interface ResumeBlock {
  id: string;
  type: "personal-info" | "experience-item" | "education-item" | "skill-group";
  data: Record<string, any>;
}
