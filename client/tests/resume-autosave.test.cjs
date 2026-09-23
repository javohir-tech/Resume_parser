const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const ts = require('typescript');
const vue = require('vue');
const { setTimeout: sleep } = require('node:timers/promises');

function setup(kind, save = async () => {}) {
  const names = {
    education: ['useEducationAvtoSave', 'useEducationSaveAvto', 'editEducationFetch', 'degree'],
    experience: ['useExperienceAvtoSave', 'useExperienceAvtoSave', 'editExperienceFetch', 'position'],
    personal: ['usePersonalAvtoSave', 'usePersonalAvtoSave', 'editResumeFetch', 'fullname'],
  };
  const [file, factory, api, field] = names[kind];
  const entry = vue.reactive({ id: 'entry', [field]: 'Original' });
  const store = vue.reactive({ resume: kind === 'personal' ? entry : { id: 'resume', [kind]: [entry] } });
  const listeners = new Map();
  const window = {
    addEventListener: (name, handler) => listeners.set(name, handler),
    removeEventListener: name => listeners.delete(name),
  };
  const calls = [];
  const request = async (id, changes) => { calls.push({ id, changes }); await save(); };
  const code = ts.transpileModule(fs.readFileSync(path.join(__dirname,
    '../app/features/resume/edit-resume/models', file + '.ts'), 'utf8'), {
    compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 },
  }).outputText;
  const exports = {};
  const injected = { ref: vue.ref, computed: vue.computed, watch: vue.watch,
    onMounted: fn => fn(), onScopeDispose: vue.onScopeDispose, window };
  new Function('require', 'exports', ...Object.keys(injected), code)(
    id => id === '~/entities/resume' ? { useResumeStore: () => store } : { [api]: request },
    exports, ...Object.values(injected));
  const scope = vue.effectScope();
  const autosave = scope.run(() => exports[factory](10));
  assert.equal(autosave.start(entry.id), true);
  return { autosave, calls, entry, field, listeners, scope };
}

for (const kind of ['education', 'experience', 'personal']) {
  test(`${kind}: repeated navigation flushes finish without unnecessary requests`, async () => {
    const ctx = setup(kind);
    try {
      assert.equal(await ctx.autosave.flush(), true);
      assert.equal(await ctx.autosave.flush(), true);
      assert.equal(ctx.calls.length, 0);
      ctx.entry[ctx.field] = 'Updated';
      assert.equal(await ctx.autosave.flush(), true);
      assert.equal(await ctx.autosave.flush(), true);
      assert.deepEqual(ctx.calls, [{ id: 'entry', changes: { [ctx.field]: 'Updated' } }]);
    } finally { ctx.scope.stop(); }
  });

  test(`${kind}: edits autosave after debounce and disposal cancels pending saves`, async () => {
    const ctx = setup(kind);
    try {
      ctx.entry[ctx.field] = 'Updated';
      await sleep(40);
      assert.equal(ctx.calls.length, 1);
      ctx.entry[ctx.field] = 'Do not save after disposal';
      ctx.scope.stop();
      await sleep(40);
      assert.equal(ctx.calls.length, 1);
    } finally { ctx.scope.stop(); }
  });

  test(`${kind}: concurrent flushes save edits made during an in-flight request`, async () => {
    let release;
    const gate = new Promise(resolve => { release = resolve; });
    const ctx = setup(kind, () => gate);
    try {
      ctx.entry[ctx.field] = 'First';
      const first = ctx.autosave.flush();
      const second = ctx.autosave.flush();
      ctx.entry[ctx.field] = 'Second';
      release();
      assert.deepEqual(await Promise.all([first, second]), [true, true]);
      assert.equal(ctx.calls.length, 2);
      assert.equal(ctx.calls[1].changes[ctx.field], 'Second');
      assert.equal(await ctx.autosave.flush(), true);
    } finally { ctx.scope.stop(); }
  });

  test(`${kind}: failed saves can be retried`, async () => {
    let fail = true;
    const ctx = setup(kind, async () => { if (fail) throw new Error('Offline'); });
    try {
      ctx.entry[ctx.field] = 'Updated';
      assert.equal(await ctx.autosave.flush(), false);
      fail = false;
      assert.equal(await ctx.autosave.flush(), true);
      assert.equal(ctx.calls.length, 2);
    } finally { ctx.scope.stop(); }
  });
}

test('education: beforeunload only blocks unsaved changes and is removed on disposal', async () => {
  const ctx = setup('education');
  let prevented = false;
  const event = { preventDefault() { prevented = true; } };
  try {
    ctx.listeners.get('beforeunload')(event);
    assert.equal(prevented, false);
    ctx.entry.degree = 'Updated';
    ctx.listeners.get('beforeunload')(event);
    assert.equal(prevented, true);
    await ctx.autosave.flush();
    prevented = false;
    ctx.listeners.get('beforeunload')(event);
    assert.equal(prevented, false);
  } finally { ctx.scope.stop(); }
  assert.equal(ctx.listeners.size, 0);
});