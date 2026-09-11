const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const ts = require('typescript');

function loadModel(name) {
  const filename = path.join(__dirname, '../app/entities/resume/models', `${name}.ts`);
  const code = ts.transpileModule(fs.readFileSync(filename, 'utf8'), {
    compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 },
  }).outputText;
  const exports = {};
  new Function('require', 'exports', code)(id => loadModel(id.replace('./', '')), exports);
  return exports;
}

const { packSidebarColumn, isSidebarBlock } = loadModel('sidebar-pagination');
const { PAGE_CONTENT_HEIGHT_PX } = loadModel('pagination');
const { buildBlock } = loadModel('build-blocks');
const title = { id: 'experience-title', type: 'section-title', section: 'experience' };
const item = id => ({ id, type: 'experience-item', item: { id, position: id } });

test('reserves the full-width header on page one only', () => {
  const blocks = [item('a'), item('b'), item('c')];
  const pages = packSidebarColumn(blocks, new Map(blocks.map(block => [block.id, 400])), 300);
  assert.deepEqual(pages.map(page => page.map(block => block.id)), [['a'], ['b', 'c']]);
});

test('keeps section titles with their first entry', () => {
  const summary = { id: 'summary', type: 'summary' };
  const pages = packSidebarColumn([summary, title, item('a')],
    new Map([['summary', 600], [title.id, 40], ['a', 200]]), 200);
  assert.deepEqual(pages.map(page => page.map(block => block.id)), [['summary'], [title.id, 'a']]);
});

test('repeats the correct section title on continuation pages without duplicating entries', () => {
  const entries = Array.from({ length: 10 }, (_, index) => item(`job-${index}`));
  const heights = new Map([[title.id, 40], ...entries.map(block => [block.id, 280])]);
  const pages = packSidebarColumn([title, ...entries], heights, 160);
  assert.ok(pages.length > 1);
  pages.forEach((page, index) => {
    assert.equal(page[0].id, title.id);
    assert.ok(page.reduce((sum, block) => sum + heights.get(block.id), 0)
      <= PAGE_CONTENT_HEIGHT_PX - (index === 0 ? 160 : 0));
  });
  assert.deepEqual(pages.flat().filter(block => block.type === 'experience-item'), entries);
});

test('switches continuation titles when a new section starts', () => {
  const education = { id: 'education-title', type: 'section-title', section: 'education' };
  const degree = id => ({ id, type: 'education-item', item: { id } });
  const pages = packSidebarColumn([title, item('a'), education, degree('b'), degree('c')],
    new Map([[title.id, 30], ['a', 500], [education.id, 30], ['b', 400], ['c', 600]]), 150);
  assert.equal(pages[1][0].section, 'education');
  assert.equal(pages[2][0].section, 'education');
});

test('places all resume fields into exactly one column', () => {
  const blocks = buildBlock({ fullname: 'Sample', summary: 'Summary',
    experience: [{ id: 'job' }], education: [{ id: 'degree' }],
    skills: [{ id: 'skills', skills: ['SQL'] }], languages: [{ id: 'lang' }] });
  const side = blocks.filter(isSidebarBlock);
  const main = blocks.filter(block => !isSidebarBlock(block));
  assert.deepEqual(side.map(block => block.type), ['header', 'section-title', 'skills-group', 'section-title', 'languages-item']);
  assert.deepEqual(main.map(block => block.type), ['summary', 'section-title', 'experience-item', 'section-title', 'education-item']);
  assert.equal(new Set([...side, ...main].map(block => block.id)).size, blocks.length);
});

test('handles empty columns and the initial unmeasured render', () => {
  assert.deepEqual(packSidebarColumn([], new Map(), 0), [[]]);
  const blocks = [title, item('a')];
  assert.deepEqual(packSidebarColumn(blocks, new Map(), 0), [blocks]);
});
