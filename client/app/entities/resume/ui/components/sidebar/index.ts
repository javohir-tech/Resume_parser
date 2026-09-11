import type { ResumeTemplateBlokcs } from '../../../models/template-contract';
import { ProfessionalTemplate } from '../professional';
import SidebarPage from './SidebarPage.vue';
import SidebarHeader from './SidebarHeader.vue';
import SidebarRenderer from './SidebarRenderer.vue';

export const SidebarTemplate: ResumeTemplateBlokcs = {
  ...ProfessionalTemplate,
  page: SidebarPage,
  header: SidebarHeader,
  renderer: SidebarRenderer,
};
