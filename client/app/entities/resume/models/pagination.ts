import type {
  Experience,
  Education,
  SkillGroup,
  ResumeBlock,
  Resume,
} from "./types";

const MM_TO_PX = 3.7795275591;

export const PAGE_WIDTH_PX = 210 * MM_TO_PX;
export const PAGE_HEIGHT_PX = 297 * MM_TO_PX;
export const PAGE_PADDING_PX = 15 * MM_TO_PX;
export const PAGE_GAP_PX = 10 *MM_TO_PX;
export const PAGE_CONTENT_WIDTH_PX = PAGE_WIDTH_PX - PAGE_PADDING_PX * 2;
export const PAGE_CONTENT_HEIGHT_PX = PAGE_WIDTH_PX - PAGE_PADDING_PX * 2;

export function packBlocksIntoPages(
  blocks: ResumeBlock[],
  heigths: Map<string, number>,
): ResumeBlock[][] {
  const pages: ResumeBlock[][] = [[]];
  let pageIndex = 0;
  let used = 0;

  for (let i = 0; i < blocks.length; i++) {
    const block = blocks[i];
    if (!block) continue;
    const h = heigths.get(block.id) ?? 0;
    let needed = h;

    if (block.type === "section-title") {
      const next = blocks[i + 1];
      if (next) needed += heigths.get(next.id) ?? 0;
    }
    const currentPage = pages[pageIndex];
    if (
      used + needed > PAGE_CONTENT_HEIGHT_PX &&
      currentPage &&
      currentPage.length > 0
    ) {
      pageIndex++;
      pages[pageIndex] = [];
      used = 0;
    }

    pages[pageIndex]?.push(block);
    used += h;
  }

  return pages;
}

export interface ResumePageContent {
  showHeader: boolean;
  showSummary: boolean;
  experience: { showTitle: boolean; items: Experience[] };
  education: { showTitle: boolean; items: Education[] };
  skills: { showTitle: boolean; items: SkillGroup[] };
}

export function toPageContent(pages: ResumeBlock[][]): ResumePageContent[] {
  return pages.map((blocks) => {
    const content: ResumePageContent = {
      showHeader: false,
      showSummary: false,
      experience: { showTitle: false, items: [] },
      education: { showTitle: false, items: [] },
      skills: { showTitle: false, items: [] },
    };

    for (const block of blocks) {
      if (block.type === "header") content.showHeader = true;
      else if (block.type === "summary") content.showSummary = true;
      else if (block.type === "section-title")
        content[block.section].showTitle = true;
      else if (block.type === "education-item")
        content.education.items.push(block.item);
      else if (block.type === "experience-item")
        content.experience.items.push(block.item);
      else if (block.type === "skills-group")
        content.skills.items.push(block.item);
    }

    return content;
  });
}
