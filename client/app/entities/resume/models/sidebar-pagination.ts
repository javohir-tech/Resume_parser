import type { ResumeBlock, ResumeSection } from './types';
import { PAGE_CONTENT_HEIGHT_PX } from './pagination';

export const SIDEBAR_WIDTH_PX = 54 * 3.7795275591;
export const SIDEBAR_GAP_PX = 10 * 3.7795275591;

// Each column flows independently. Component padding is included in measured heights.
export function packSidebarColumn(
  blocks: ResumeBlock[],
  heights: Map<string, number>,
  headerHeight: number,
): ResumeBlock[][] {
  const pages: ResumeBlock[][] = [[]];
  let used = 0;
  let activeTitle: Extract<ResumeBlock, { type: 'section-title' }> | undefined;
  const height = (block: ResumeBlock) => heights.get(block.id) ?? 0;
  const capacity = () => PAGE_CONTENT_HEIGHT_PX - (pages.length === 1 ? headerHeight : 0);

  for (let index = 0; index < blocks.length; index++) {
    const block = blocks[index]!;
    const next = blocks[index + 1];
    const required = height(block) + (block.type === 'section-title' && next ? height(next) : 0);
    if (used + required > capacity() && (used > 0 || pages.length === 1 && headerHeight > 0)) {
      pages.push([]);
      used = 0;
      if (block.type !== 'section-title' && activeTitle) {
        pages[pages.length - 1]!.push(activeTitle);
        used += height(activeTitle);
      }
    }
    pages[pages.length - 1]!.push(block);
    used += height(block);
    if (block.type === 'section-title') activeTitle = block;
  }
  return pages;
}

export function isSidebarBlock(block: ResumeBlock): boolean {
  const sidebarSections: ResumeSection[] = ['skills', 'languages'];
  return block.type === 'header' || block.type === 'skills-group' || block.type === 'languages-item'
    || block.type === 'section-title' && sidebarSections.includes(block.section);
}
