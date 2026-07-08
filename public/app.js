'use strict';

// ── Seal colour lookup ────────────────────────────────────────────────────
const SEAL_COLOURS = {
  1:'red',2:'white',3:'blue',4:'yellow',5:'red',6:'white',7:'blue',8:'yellow',
  9:'red',10:'white',11:'blue',12:'yellow',13:'red',14:'white',15:'blue',16:'yellow',
  17:'red',18:'white',19:'blue',20:'yellow',
};

function sealClass(sealNum) { return SEAL_COLOURS[sealNum] || ''; }

// ── DOM helpers ───────────────────────────────────────────────────────────
function el(tag, cls, text) {
  const e = document.createElement(tag);
  if (cls)  e.className = cls;
  if (text !== undefined) e.textContent = text;
  return e;
}

function sep() { return el('hr', 'sep'); }

// Convert newline-delimited text into a <p> with <br> nodes — no innerHTML.
function multilineP(cls, text) {
  const p = el('p', cls);
  text.split('\n').forEach((line, i) => {
    if (i > 0) p.appendChild(document.createElement('br'));
    p.appendChild(document.createTextNode(line));
  });
  return p;
}

// ── Fetch helpers ─────────────────────────────────────────────────────────
async function api(path) {
  const res = await fetch(path);
  const data = await res.json();
  if (!res.ok) throw new Error(data.error || 'Unknown error');
  return data;
}

// ── Oracle board widget ───────────────────────────────────────────────────
function makeOracleBoard(data) {
  const grid = el('div', 'oracle-grid');

  // guide is a plain string (seal name only, no tone)
  const guideCell = el('div', 'oracle-cell');
  guideCell.appendChild(el('span', 'oracle-role', 'GUIDE'));
  guideCell.appendChild(el('span', 'oracle-seal gold-s', data.guide || '—'));
  grid.appendChild(guideCell);

  // analog, antipode, occult are full dicts
  [
    { label: 'ANALOG',   key: 'analog' },
    { label: 'ANTIPODE', key: 'antipode' },
    { label: 'OCCULT',   key: 'occult' },
  ].forEach(({ label, key }) => {
    const info = data[key] || {};
    const cell = el('div', 'oracle-cell');
    cell.appendChild(el('span', 'oracle-role', label));
    cell.appendChild(el('span', `oracle-seal ${sealClass(info.seal_number)}`, info.seal || '—'));
    cell.appendChild(el('span', 'oracle-tone', info.tone || ''));
    grid.appendChild(cell);
  });
  return grid;
}

// ── Expandable section ────────────────────────────────────────────────────
function makeExpandable(title, bodyFn) {
  const wrap   = el('div', 'expandable card');
  const header = el('div', 'expand-header');
  const label  = el('span', 'sm bold', title);
  const arrow  = el('span', 'expand-arrow', '▾');
  header.appendChild(label);
  header.appendChild(arrow);

  const body = el('div', 'expand-body');
  bodyFn(body);

  header.addEventListener('click', () => {
    const open = body.classList.toggle('open');
    header.classList.toggle('open', open);
  });

  wrap.appendChild(header);
  wrap.appendChild(body);
  return wrap;
}

// ── HOME screen ───────────────────────────────────────────────────────────
async function loadHome() {
  const container = document.getElementById('home-content');
  try {
    const d = await api('/api/today');
    container.innerHTML = '';

    container.appendChild(el('h1', 'screen-title', 'THE LIVING SPIRAL'));

    if (d.is_day_out_of_time) {
      renderDayOutOfTime(container, d);
      return;
    }

    // Moon card
    const moonCard = el('div', 'card');
    moonCard.appendChild(el('p', 'bold gold-s center', d.moon.toUpperCase()));
    moonCard.appendChild(sep());
    moonCard.appendChild(el('p', 'center sm', `Day ${d.moon_day}  ·  ${d.plasma}`));
    const progWrap = el('div', 'progress-wrap');
    const progBar  = el('div', 'progress-bar');
    progBar.style.width = `${Math.round(d.moon_day / 28 * 100)}%`;
    progWrap.appendChild(progBar);
    moonCard.appendChild(progWrap);
    if (d.moon_question) moonCard.appendChild(el('p', 'center xs muted', `"${d.moon_question}"`));
    container.appendChild(moonCard);

    // Galactic signature card
    const sigCard = el('div', 'card card2');
    sigCard.appendChild(el('p', `xl bold gold center`, `KIN  ${d.kin_number}`));
    sigCard.appendChild(el('p', `lg bold ${sealClass(d.seal_number)} center`, d.seal.toUpperCase()));
    sigCard.appendChild(el('p', `center sm`, `${d.tone} Tone`));
    sigCard.appendChild(sep());
    if (d.is_galactic_portal) sigCard.appendChild(el('div', 'portal-badge', '✦ Galactic Activation Portal ✦'));
    sigCard.appendChild(makeOracleBoard(d));
    container.appendChild(sigCard);

    // Affirmation card
    const affCard = el('div', 'card');
    affCard.appendChild(el('p', 'section-label', "TODAY'S CODE SPELL"));
    affCard.appendChild(sep());
    affCard.appendChild(multilineP('affirmation-text center', d.affirmation));
    container.appendChild(affCard);

  } catch (err) {
    container.innerHTML = '';
    container.appendChild(el('p', 'fetch-error', `Failed to load: ${err.message}`));
  }
}

function renderDayOutOfTime(container, d) {
  container.appendChild(el('p', 'xl bold gold center', '✦  DAY OUT OF TIME  ✦'));
  container.appendChild(el('p', 'center gold-s', 'July 25'));
  const card = el('div', 'card');
  card.appendChild(multilineP('affirmation-text', d.message || ''));
  container.appendChild(card);
}

// ── KIN FINDER screen ─────────────────────────────────────────────────────
function setupKinFinder() {
  const yearEl  = document.getElementById('kin-year');
  const monthEl = document.getElementById('kin-month');
  const dayEl   = document.getElementById('kin-day');
  const errEl   = document.getElementById('kin-error');
  const result  = document.getElementById('kin-result');

  document.getElementById('use-today-btn').addEventListener('click', () => {
    const t = new Date();
    yearEl.value  = t.getFullYear();
    monthEl.value = t.getMonth() + 1;
    dayEl.value   = t.getDate();
  });

  document.getElementById('calc-btn').addEventListener('click', async () => {
    errEl.textContent = '';
    result.innerHTML  = '';
    const y = yearEl.value.trim();
    const m = monthEl.value.trim();
    const d = dayEl.value.trim();
    if (!y || !m || !d) { errEl.textContent = 'Please fill in all three fields.'; return; }

    try {
      const kin = await api(`/api/kin?year=${encodeURIComponent(y)}&month=${encodeURIComponent(m)}&day=${encodeURIComponent(d)}`);
      renderKinResult(result, kin);
    } catch (err) {
      errEl.textContent = err.message;
    }
  });
}

function renderKinResult(container, kin) {
  const card = el('div', 'card card2');
  card.appendChild(el('p', `xl bold gold center`, `KIN  ${kin.kin_number}`));
  card.appendChild(el('p', `lg bold ${sealClass(kin.seal_number)} center`, kin.seal.toUpperCase()));
  card.appendChild(el('p', `center sm`, `${kin.tone} Tone  ·  ${kin.seal_color} Family`));
  card.appendChild(sep());
  if (kin.is_galactic_portal) card.appendChild(el('div', 'portal-badge', '✦ Galactic Activation Portal ✦'));
  card.appendChild(makeOracleBoard(kin));
  card.appendChild(sep());
  card.appendChild(el('p', 'section-label', 'YOUR CODE SPELL'));
  card.appendChild(multilineP('affirmation-text center', kin.affirmation));
  container.appendChild(card);
}

// ── PRACTICES screen ──────────────────────────────────────────────────────
async function loadPractices() {
  const container = document.getElementById('practices-content');
  try {
    const d = await api('/api/practices');
    container.innerHTML = '';

    container.appendChild(el('h1', 'screen-title', 'DAILY PRACTICES'));

    const moonCard = el('div', 'card');
    moonCard.appendChild(el('p', 'bold gold-s center', `${d.moon.toUpperCase()} MOON — DAY ${d.moon_day}`));
    if (d.moon_question) {
      moonCard.appendChild(sep());
      moonCard.appendChild(el('p', 'center sm muted', `"${d.moon_question}"`));
    }
    container.appendChild(moonCard);

    container.appendChild(makeExpandable('Daily Code Spell', body => {
      body.appendChild(multilineP('affirmation-text', d.affirmation));
    }));

    const c = d.curriculum;
    if (c.weekly_practice) {
      container.appendChild(makeExpandable('Weekly Practice', body => {
        body.appendChild(el('p', 'sm', c.weekly_practice));
      }));
    }
    if (c.theme || c.affirmation || c.quote) {
      container.appendChild(makeExpandable('Monthly Focus', body => {
        if (c.theme)       body.appendChild(el('p', 'sm bold', c.theme));
        if (c.affirmation) body.appendChild(multilineP('sm affirmation-text', c.affirmation));
        if (c.quote)       body.appendChild(el('p', 'xs muted', `"${c.quote}"`));
      }));
    }

  } catch (err) {
    container.innerHTML = '';
    container.appendChild(el('p', 'fetch-error', `Failed to load: ${err.message}`));
  }
}

// ── MEDITATIONS screen ────────────────────────────────────────────────────
async function loadMeditations() {
  const container = document.getElementById('meditations-content');
  try {
    const list = await api('/api/meditations');
    container.innerHTML = '';
    container.appendChild(el('h1', 'screen-title', 'MEDITATIONS'));

    const medList = el('div', 'med-list');
    list.forEach(item => {
      const card = el('div', 'card med-item');
      card.appendChild(el('h3', null, item.title));
      card.addEventListener('click', () => openMeditation(container, item.key, item.title));
      medList.appendChild(card);
    });
    container.appendChild(medList);
  } catch (err) {
    container.innerHTML = '';
    container.appendChild(el('p', 'fetch-error', `Failed to load: ${err.message}`));
  }
}

async function openMeditation(container, key, title) {
  container.innerHTML = '';
  container.appendChild(el('p', 'loading', 'Loading…'));
  try {
    const med = await api(`/api/meditations?name=${encodeURIComponent(key)}`);
    container.innerHTML = '';

    const backBtn = el('button', 'link-btn', '← Back');
    backBtn.style.marginBottom = '8px';
    backBtn.addEventListener('click', () => loadMeditations());
    container.appendChild(backBtn);

    container.appendChild(el('h1', 'screen-title', med.title));
    container.appendChild(multilineP('meditation-text', med.text));
  } catch (err) {
    container.innerHTML = '';
    container.appendChild(el('p', 'fetch-error', `Failed to load: ${err.message}`));
  }
}

// ── Navigation ────────────────────────────────────────────────────────────
let loadedTabs = new Set();

function switchTab(name) {
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
  document.getElementById(`tab-${name}`).classList.add('active');
  document.querySelector(`.nav-btn[data-tab="${name}"]`).classList.add('active');

  if (!loadedTabs.has(name)) {
    loadedTabs.add(name);
    if (name === 'home')        loadHome();
    if (name === 'practices')   loadPractices();
    if (name === 'meditations') loadMeditations();
  }
}

// ── Boot ──────────────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.nav-btn').forEach(btn => {
    btn.addEventListener('click', () => switchTab(btn.dataset.tab));
  });
  setupKinFinder();
  switchTab('home');
});
