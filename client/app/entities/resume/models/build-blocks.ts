import type { Resume, ResumeBlock } from "./types";

export function buildBlock(resume: Resume): ResumeBlock[] {
  const blocks: ResumeBlock[] = [{ id: "header", type: "header" }];

  if (resume.summary) {
    blocks.push({ id: "summary", type: "summary" });
  }

  if (resume.experience?.length) {
    blocks.push({
      id: "section-title-experience",
      type: "section-title",
      section: "experience",
    });
    resume.experience.forEach((item) =>
      blocks.push({
        id: `experience-item-${item.id}`,
        type: "experience-item",
        item,
      }),
    );
  }

  if (resume.education?.length) {
    blocks.push({
      id: "section-title-education",
      type: "section-title",
      section: "education",
    });
    resume.education.forEach((item) =>
      blocks.push({
        id: `education-item-${item.id}`,
        type: "education-item",
        item,
      }),
    );
  }

  if (resume.skills?.length) {
    blocks.push({
      id: "education-title-skills",
      type: "section-title",
      section: "skills",
    });
    resume.skills.forEach((item) =>
      blocks.push({ id: `skills-item-${item.id}`, type: "skills-group", item }),
    );
  }

  return blocks;
}
