const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const ts = require('typescript');
const vue = require('vue');
const { setTimeout: sleep } = require('node:timers/promises');

function setup(save = async () => {}) {
  const store = vue.reactive({ resume: { id: 'resume' }, designInfo: {
    template: 'classic', font: 'Inter', heading_title_color: null, entry_title_color: null,
  } });
  const calls = [], errors = [], listeners = new Map();
  const code = ts.transpileModule(fs.readFileSync(path.join(__dirname,
    '../app/features/resume/design-edit/models/useEditDesign.ts'), 'utf8'), {
    compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 },
  }).outputText;
  const exports = {};
  const injected = { ref: vue.ref, computed: vue.computed, watch: vue.watch,
    onMounted: fn => fn(), onScopeDispose: vue.onScopeDispose,
    window: { addEventListener: (name, fn) => listeners.set(name, fn),
      removeEventListener: name => listeners.delete(name) } };
  new Function('require', 'exports', ...Object.keys(injected), code)(id => {
    if (id === '~/entities/resume') return { useResumeStore: () => store };
    if (id === '~/shared/lib') return { useApiToasts: () => ({ showError: e => errors.push(e) }),
      apiError: e => ({ message: e.message }) };
    return { editDesignRequest: async (id, changes) => { calls.push({ id, changes }); await save(); } };
  }, exports, ...Object.values(injected));
  const scope = vue.effectScope();
  const autosave = scope.run(() => exports.useEditDesign(10));
  return { store, calls, errors, listeners, scope, autosave };
}

test('initial load is ignored; all four controls debounce into one partial PATCH', async () => {
  const c = setup();
  try {
    c.store.designInfo.font = 'Arial';
    await sleep(30);
    assert.equal(c.calls.length, 0);
    assert.equal(c.autosave.start(), true);
    assert.equal(await c.autosave.flush(), true);
    c.store.designInfo.template = 'modern';
    c.store.designInfo.font = 'Inter';
    c.store.designInfo.heading_title_color = { name: 'Red', hex: '#ff0000' };
    c.store.designInfo.entry_title_color = { name: 'Blue', hex: '#0000ff' };
    await sleep(40);
    assert.deepEqual(c.calls, [{ id: 'resume', changes: { ...c.store.designInfo } }]);
    assert.equal(c.autosave.status.value, 'saved');
    assert.equal(await c.autosave.flush(), true);
    assert.equal(c.calls.length, 1);
  } finally { c.scope.stop(); }
});

test('colors compare by value, nested edits are captured, and default sends null', async () => {
  const c = setup();
  try {
    c.store.designInfo.heading_title_color = { name: 'Red', hex: '#ff0000' };
    c.autosave.start();
    c.store.designInfo.heading_title_color = { name: 'Red', hex: '#ff0000' };
    await c.autosave.flush();
    assert.equal(c.calls.length, 0);
    c.store.designInfo.heading_title_color.hex = '#ee0000';
    await c.autosave.flush();
    c.store.designInfo.heading_title_color = null;
    await c.autosave.flush();
    assert.deepEqual(c.calls.map(c => c.changes), [
      { heading_title_color: { name: 'Red', hex: '#ee0000' } },
      { heading_title_color: null },
    ]);
  } finally { c.scope.stop(); }
});

test('concurrent flushes serialize edits made while a request is pending', async () => {
  let release;
  let first = true;
  const c = setup(() => first ? (first = false, new Promise(r => { release = r; })) : Promise.resolve());
  try {
    c.autosave.start();
    c.store.designInfo.heading_title_color = { name: 'Red', hex: '#ff0000' };
    const a = c.autosave.flush();
    const b = c.autosave.flush();
    c.store.designInfo.heading_title_color.hex = '#ee0000';
    assert.equal(c.calls[0].changes.heading_title_color.hex, '#ff0000');
    release();
    assert.deepEqual(await Promise.all([a, b]), [true, true]);
    assert.equal(c.calls.length, 2);
    assert.equal(c.calls[1].changes.heading_title_color.hex, '#ee0000');
    assert.equal(c.autosave.isDirty.value, false);
  } finally { c.scope.stop(); }
});

test('failure preserves dirty state, blocks navigation flush, and permits retry', async () => {
  let fail = true;
  const c = setup(async () => { if (fail) throw new Error('Save failed'); });
  try {
    c.autosave.start();
    c.store.designInfo.template = 'modern';
    assert.equal(await c.autosave.flush(), false);
    assert.equal(c.autosave.isDirty.value, true);
    assert.equal(c.autosave.isSaving.value, false);
    assert.deepEqual(c.errors, ['Save failed']);
    await sleep(30);
    assert.equal(c.calls.length, 1);
    fail = false;
    assert.equal(await c.autosave.flush(), true);
    assert.equal(c.autosave.status.value, 'saved');
  } finally { c.scope.stop(); }
});

test('disposal cancels debounce and removes the unsaved-changes unload guard', async () => {
  const c = setup();
  c.autosave.start();
  c.store.designInfo.font = 'Arial';
  let prevented = false;
  c.listeners.get('beforeunload')({ preventDefault() { prevented = true; } });
  assert.equal(prevented, true);
  c.scope.stop();
  await sleep(30);
  assert.equal(c.calls.length, 0);
  assert.equal(c.listeners.size, 0);
  assert.equal(await c.autosave.flush(), false);
});

test('switching resumes during a request never writes edits to the wrong resume', async () => {
  let release;
  const c = setup(() => new Promise(r => { release = r; }));
  try {
    c.autosave.start();
    c.store.designInfo.font = 'Arial';
    const pending = c.autosave.flush();
    c.store.resume.id = 'other';
    c.store.designInfo.font = 'Inter';
    release();
    assert.equal(await pending, false);
    assert.equal(c.calls.length, 1);
    assert.equal(await c.autosave.flush(), false);
    assert.equal(c.autosave.start(), true);
    assert.equal(c.autosave.isDirty.value, false);
  } finally { c.scope.stop(); }
});

function loadApi(relativePath, request) {
  const code = ts.transpileModule(fs.readFileSync(path.join(__dirname, relativePath), 'utf8'), {
    compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 },
  }).outputText;
  const exports = {};
  new Function('require', 'exports', code)(id => id === '~/shared/api' ? { api: request }
    : { colorOptions: [{ name: 'red', hex: '#ef4444' }] }, exports);
  return exports;
}

test('PATCH serializes colors as HEX and preserves omitted fields and explicit null', async () => {
  const calls = [];
  const api = loadApi('../app/features/resume/design-edit/api/index.ts', async (url, options) => {
    calls.push({ url, ...options });
  });
  await api.editDesignRequest('resume', { heading_title_color: { name: 'red', hex: '#ef4444' }, entry_title_color: null });
  await api.editDesignRequest('resume', { font: 'Inter' });
  assert.deepEqual(calls, [
    { url: '/api/resume/edit/resume/design', method: 'PATCH', body: { heading_title_color: '#ef4444', entry_title_color: null } },
    { url: '/api/resume/edit/resume/design', method: 'PATCH', body: { font: 'Inter' } },
  ]);
});

test('GET restores palette colors, custom HEX colors, nulls and defaults', async () => {
  let response = { template: 'modern', font: 'Arial', heading_title_color: '#ef4444', entry_title_color: '#123456' };
  const api = loadApi('../app/entities/resume/api/index.ts', async () => response);
  assert.deepEqual(await api.getResumeDesignRequest('resume'), {
    template: 'modern', font: 'Arial', heading_title_color: { name: 'red', hex: '#ef4444' },
    entry_title_color: { name: '#123456', hex: '#123456' },
  });
  response = { template: null, font: null, heading_title_color: null, entry_title_color: null };
  assert.deepEqual(await api.getResumeDesignRequest('resume'), {
    template: 'classic', font: 'Inter', heading_title_color: null, entry_title_color: null,
  });
});
