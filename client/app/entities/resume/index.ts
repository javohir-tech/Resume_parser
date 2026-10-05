// --> Compoenents
export { default as PaginatedResume } from "./ui/PaginatedResume.vue.vue";
export { default as ResumeCard } from "./ui/resumeCard.vue";

// --> Store
export { useResumeStore } from "./models/store.ts";

// --> Resume Templates
export { ClassicTemplate } from "./ui/components/classic";
export { ModernTemplate } from "./ui/components/modern";
export { MinimalTemplate } from "./ui/components/minimal";
export { ProfessionalTemplate } from "./ui/components/professional";
export { SidebarTemplate } from "./ui/components/sidebar";

// --> models  or composables
export { useGetResume } from "./models/useGetResume.ts";
export { getResumeFetch } from "./api/index.ts";
export { getMyResumes } from "./api/index.ts";

// --> types and contants
export * from "./models/types.ts";
export * from "./models/constants.ts";
