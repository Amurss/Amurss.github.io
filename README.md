# Amurss.github.io

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="referrer" content="no-referrer">
  <title>Tesla Listings — ss.com</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background: #0d0d0d;
      color: #e0e0e0;
      font-family: 'Segoe UI', system-ui, sans-serif;
      min-height: 100vh;
    }

    /* ── HEADER ── */
    header {
      background: #111;
      border-bottom: 1px solid #222;
      padding: 16px 32px;
      display: flex;
      align-items: center;
      gap: 14px;
      position: sticky;
      top: 0;
      z-index: 100;
      min-height: 58px;
    }

    .logo {
      font-size: 1.4rem;
      font-weight: 800;
      letter-spacing: 2px;
      color: #e82127;
    }

    .subtitle {
      font-size: 0.85rem;
      color: #555;
    }

    #updated-label {
      font-size: 0.75rem;
      color: #444;
      display: none;
    }

    .header-right {
      margin-left: auto;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    #refresh-btn {
      background: transparent;
      border: 1px solid #333;
      color: #666;
      font-size: 0.78rem;
      padding: 5px 12px;
      border-radius: 20px;
      cursor: pointer;
      transition: border-color 0.15s, color 0.15s;
    }
    #refresh-btn:hover { border-color: #e82127; color: #e82127; }
    #refresh-btn:disabled { opacity: 0.4; cursor: default; }

    #count {
      background: #e82127;
      color: #fff;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 20px;
      display: none;
    }

    /* ── LAYOUT ── */
    #layout {
      display: flex;
      align-items: flex-start;
    }

    /* ── SIDEBAR ── */
    #sidebar {
      width: 210px;
      min-width: 210px;
      background: #111;
      border-right: 1px solid #1e1e1e;
      padding: 24px 18px;
      position: sticky;
      top: 58px;
      height: calc(100vh - 58px);
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 28px;
    }

    /* Thin scrollbar for sidebar */
    #sidebar::-webkit-scrollbar { width: 4px; }
    #sidebar::-webkit-scrollbar-track { background: transparent; }
    #sidebar::-webkit-scrollbar-thumb { background: #2a2a2a; border-radius: 2px; }

    .filter-section {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .filter-label {
      font-size: 0.7rem;
      color: #555;
      letter-spacing: 0.9px;
      text-transform: uppercase;
      margin-bottom: 2px;
    }

    /* Model pills — stacked */
    .pills-col {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .pill {
      background: #1a1a1a;
      border: 1px solid #2a2a2a;
      color: #888;
      font-size: 0.8rem;
      padding: 7px 12px;
      border-radius: 8px;
      cursor: pointer;
      transition: background 0.15s, color 0.15s, border-color 0.15s;
      user-select: none;
      text-align: left;
      width: 100%;
    }
    .pill:hover { border-color: #555; color: #ccc; }
    .pill.active { background: #e82127; border-color: #e82127; color: #fff; }

    /* Range inputs */
    .range-pair {
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .range-pair .sep { color: #383838; font-size: 0.8rem; }

    .filter-input {
      background: #1a1a1a;
      border: 1px solid #2a2a2a;
      color: #ddd;
      font-size: 0.78rem;
      padding: 7px 8px;
      border-radius: 6px;
      width: 100%;
      outline: none;
      transition: border-color 0.15s;
    }
    .filter-input:focus { border-color: #555; }
    .filter-input::placeholder { color: #333; }

    .input-with-unit {
      position: relative;
      flex: 1;
    }
    .input-with-unit .filter-input { padding-right: 24px; }
    .input-unit {
      position: absolute;
      right: 7px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 0.68rem;
      color: #444;
      pointer-events: none;
    }

    #fav-toggle {
      background: #1a1a1a;
      border: 1px solid #2a2a2a;
      color: #888;
      font-size: 0.8rem;
      padding: 7px 12px;
      border-radius: 8px;
      cursor: pointer;
      transition: background 0.15s, color 0.15s, border-color 0.15s;
      display: flex;
      align-items: center;
      gap: 6px;
      width: 100%;
      text-align: left;
    }
    #fav-toggle.active { background: #2a0a0a; border-color: #e82127; color: #e82127; }
    #fav-toggle:hover { border-color: #e82127; color: #e82127; }

    #clear-btn {
      background: transparent;
      border: 1px solid #2a2a2a;
      color: #555;
      font-size: 0.75rem;
      padding: 7px 12px;
      border-radius: 8px;
      cursor: pointer;
      transition: border-color 0.15s, color 0.15s;
      display: none;
      width: 100%;
      text-align: left;
    }
    #clear-btn:hover { border-color: #888; color: #ccc; }
    #clear-btn.visible { display: inline-flex; align-items: center; gap: 5px; }

    .sidebar-divider {
      height: 1px;
      background: #1e1e1e;
      margin: -10px 0;
    }

    /* ── MAIN ── */
    #main {
      flex: 1;
      min-width: 0;
    }

    #app {
      padding: 32px 28px;
    }

    #loading {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 16px;
      padding: 80px 0;
      color: #555;
    }

    .spinner {
      width: 44px;
      height: 44px;
      border: 3px solid #222;
      border-top-color: #e82127;
      border-radius: 50%;
      animation: spin 0.8s linear infinite;
    }
    @keyframes spin { to { transform: rotate(360deg); } }

    #error {
      display: none;
      background: #1a0a0a;
      border: 1px solid #5a1a1a;
      color: #ff6b6b;
      padding: 20px 24px;
      border-radius: 10px;
      margin: 40px auto;
      max-width: 600px;
      text-align: center;
    }

    #empty-state {
      display: none;
      text-align: center;
      padding: 60px 0;
      color: #555;
    }
    #empty-state a {
      color: #e82127;
      cursor: pointer;
      text-decoration: none;
    }
    #empty-state a:hover { text-decoration: underline; }

    #grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
      gap: 24px;
    }

    /* ── CARD ── */
    .card {
      background: #161616;
      border: 1px solid #222;
      border-radius: 14px;
      overflow: hidden;
      transition: transform 0.2s, box-shadow 0.2s;
      display: flex;
      flex-direction: column;
    }
    .card:hover {
      transform: translateY(-4px);
      box-shadow: 0 16px 40px rgba(0,0,0,0.5);
    }
    .card.hidden { display: none; }

    /* ── SLIDER ── */
    .slider-wrap {
      position: relative;
      width: 100%;
      padding-top: 75%; /* 4:3 ratio — explicit height for all browsers */
      background: #0a0a0a;
      overflow: hidden;
    }

    .slides {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      display: flex;
      transition: transform 0.35s cubic-bezier(.4,0,.2,1);
    }

    .slide {
      min-width: 100%;
      height: 100%;
    }

    .slide img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .slide .no-img {
      width: 100%;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #333;
      font-size: 3rem;
    }

    .arrow {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      background: rgba(0,0,0,0.65);
      border: none;
      color: #fff;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      cursor: pointer;
      font-size: 1rem;
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 10;
      transition: background 0.15s;
      user-select: none;
    }
    .arrow:hover { background: rgba(232,33,39,0.85); }
    .arrow.prev { left: 10px; }
    .arrow.next { right: 10px; }

    .slider-dots {
      position: absolute;
      bottom: 8px;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      gap: 5px;
    }

    .dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: rgba(255,255,255,0.35);
      transition: background 0.2s;
    }
    .dot.active { background: #e82127; }

    .img-count {
      position: absolute;
      top: 10px;
      right: 10px;
      background: rgba(0,0,0,0.65);
      color: #ccc;
      font-size: 0.72rem;
      padding: 3px 8px;
      border-radius: 12px;
    }

    /* Favorite button */
    .fav-btn {
      position: absolute;
      top: 10px;
      left: 10px;
      background: rgba(0,0,0,0.6);
      border: none;
      color: rgba(255,255,255,0.45);
      width: 34px;
      height: 34px;
      border-radius: 50%;
      cursor: pointer;
      font-size: 1.05rem;
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 11;
      transition: color 0.2s, background 0.2s;
      line-height: 1;
    }
    .fav-btn:hover { background: rgba(0,0,0,0.85); color: #e82127; }
    .fav-btn.active { color: #e82127; }

    /* ── CARD BODY ── */
    .card-body {
      padding: 16px 18px 18px;
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .card-title {
      font-size: 1rem;
      font-weight: 600;
      color: #f0f0f0;
      line-height: 1.4;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    .card-meta {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    .tag {
      background: #1e1e1e;
      border: 1px solid #2a2a2a;
      border-radius: 6px;
      padding: 4px 10px;
      font-size: 0.78rem;
      color: #aaa;
      display: flex;
      align-items: center;
      gap: 5px;
    }
    .tag .icon { font-size: 0.85rem; }

    .model-tag {
      background: #1a0e0e;
      border-color: #3a1a1a;
      color: #c06060;
    }

    .card-price {
      font-size: 1.4rem;
      font-weight: 800;
      color: #e82127;
      margin-top: auto;
    }

    .card-footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-top: 10px;
      border-top: 1px solid #1f1f1f;
    }

    .view-btn {
      text-decoration: none;
      background: transparent;
      border: 1px solid #333;
      color: #aaa;
      font-size: 0.78rem;
      padding: 6px 14px;
      border-radius: 20px;
      transition: border-color 0.15s, color 0.15s;
    }
    .view-btn:hover { border-color: #e82127; color: #e82127; }

    .source-badge {
      font-size: 0.68rem;
      font-weight: 600;
      padding: 2px 8px;
      border-radius: 10px;
      letter-spacing: 0.4px;
    }
    .source-badge.ss  { background: #0d1a2e; color: #4a8acc; border: 1px solid #1a3a5e; }
    .source-badge.dba { background: #0d1e0d; color: #4aaa4a; border: 1px solid #1a3e1a; }

    /* ── LOAD MORE ── */
    #load-more-wrap {
      display: none;
      flex-direction: column;
      align-items: center;
      gap: 10px;
      padding: 40px 0 20px;
    }
    #load-more-info {
      font-size: 0.78rem;
      color: #555;
    }
    #load-more-btn {
      background: #1a1a1a;
      border: 1px solid #2a2a2a;
      color: #aaa;
      font-size: 0.85rem;
      padding: 10px 32px;
      border-radius: 24px;
      cursor: pointer;
      transition: border-color 0.15s, color 0.15s, background 0.15s;
    }
    #load-more-btn:hover { border-color: #e82127; color: #e82127; background: #1a0808; }
    #load-more-btn:disabled { opacity: 0.4; cursor: default; }

    /* ── RESPONSIVE ── */
    @media (max-width: 700px) {
      #grid { grid-template-columns: 1fr; }
      header { padding: 12px 16px; }
      #layout { flex-direction: column; }
      #sidebar {
        position: static;
        width: 100%;
        height: auto;
        border-right: none;
        border-bottom: 1px solid #1e1e1e;
        flex-direction: row;
        flex-wrap: wrap;
        gap: 16px;
        padding: 16px;
      }
      .pills-col { flex-direction: row; flex-wrap: wrap; }
      .pill { width: auto; }
      #app { padding: 20px 16px; }
    }
  </style>
</head>
<body>

<header>
  <div class="logo">⚡ TESLA</div>
  <div>
    <div class="subtitle">Tesla listings · ss.com &amp; dba.dk · DKK prices converted to € (~7.46 DKK/€)</div>
    <div id="updated-label"></div>
  </div>
  <div class="header-right">
    <button id="refresh-btn" title="Refresh listings">↻ Refresh</button>
    <div id="count">0 listings</div>
  </div>
</header>

<div id="layout">
  <!-- LEFT SIDEBAR -->
  <div id="sidebar">

    <div class="filter-section">
      <div class="filter-label">Source</div>
      <div class="pills-col">
        <button class="pill source-pill active" data-source="all">All sources</button>
        <button class="pill source-pill" data-source="ss">ss.com</button>
        <button class="pill source-pill" data-source="dba">dba.dk</button>
      </div>
    </div>

    <div class="sidebar-divider"></div>

    <div class="filter-section">
      <div class="filter-label">Model</div>
      <div class="pills-col">
        <button class="pill active" data-model="all">All models</button>
        <button class="pill" data-model="Model 3">Model 3</button>
        <button class="pill" data-model="Model Y">Model Y</button>
        <button class="pill" data-model="Model S">Model S</button>
        <button class="pill" data-model="Model X">Model X</button>
        <button class="pill" data-model="Other">Other</button>
      </div>
    </div>

    <div class="sidebar-divider"></div>

    <div class="filter-section">
      <div class="filter-label">Price <span style="color:#333;font-size:0.65rem;text-transform:none;letter-spacing:0">(€)</span></div>
      <div class="range-pair">
        <input class="filter-input" id="price-min" type="number" placeholder="min" min="0">
        <span class="sep">—</span>
        <input class="filter-input" id="price-max" type="number" placeholder="max" min="0">
      </div>
    </div>

    <div class="filter-section">
      <div class="filter-label">Year</div>
      <div class="range-pair">
        <input class="filter-input" id="year-min" type="number" placeholder="from" min="2012" max="2030">
        <span class="sep">—</span>
        <input class="filter-input" id="year-max" type="number" placeholder="to" min="2012" max="2030">
      </div>
    </div>

    <div class="filter-section">
      <div class="filter-label">Max mileage</div>
      <div class="input-with-unit">
        <input class="filter-input" id="mile-max" type="number" placeholder="e.g. 100000" min="0">
        <span class="input-unit">km</span>
      </div>
    </div>

    <div class="sidebar-divider"></div>

    <div class="filter-section">
      <button id="fav-toggle">♡ Favorites only</button>
      <button id="clear-btn">✕ Clear filters <span id="active-count"></span></button>
    </div>

  </div>

  <!-- MAIN CONTENT -->
  <div id="main">
    <div id="app">
      <div id="loading">
        <div class="spinner"></div>
        <div id="loading-msg">Loading today's listings…</div>
      </div>
      <div id="error">
        <strong>Could not load listings.</strong><br>
        <span id="err-msg"></span>
      </div>
      <div id="empty-state">
        No listings match your filters. <a onclick="clearFilters()">Clear filters</a>
      </div>
      <div id="grid"></div>
      <div id="load-more-wrap">
        <div id="load-more-info"></div>
        <button id="load-more-btn">Load more listings</button>
      </div>
    </div>
  </div>
</div>

<script>
  const SS_BASE    = 'https://www.ss.com';
  const SS_URL     = SS_BASE + '/lv/transport/cars/tesla/today/';
  const DBA_URL    = 'https://www.dba.dk/mobility/search/car?variant=0.8078';

  // Danish krone → EUR conversion (fixed rate)
  const DKK_RATE   = 7.46; // 1 EUR ≈ 7.46 DKK
  function dkkToEur(dkk) { return Math.round(dkk / DKK_RATE); }

  // ── Cache keys ────────────────────────────────────────────────────────────
  const CACHE_DATE = 'tesla_cache_date';
  const CACHE_TIME = 'tesla_cache_time';
  const CACHE_SS   = 'tesla_cache_ss';
  const CACHE_DBA  = 'tesla_cache_dba';
  const FAVS_KEY      = 'tesla_favs';
  const FAVS_DATA_KEY = 'tesla_favs_data';

  function getTodayStr() {
    return new Date().toISOString().slice(0, 10);
  }

  function isCacheValid() {
    return localStorage.getItem(CACHE_DATE) === getTodayStr();
  }

  function getCachedSource(key) {
    try {
      const raw = localStorage.getItem(key);
      return raw ? JSON.parse(raw) : null;
    } catch { return null; }
  }

  function setCacheSource(key, listings) {
    localStorage.setItem(key, JSON.stringify(listings));
  }

  function stampCache() {
    const now = new Date();
    const t = now.getHours().toString().padStart(2,'0') + ':' + now.getMinutes().toString().padStart(2,'0');
    localStorage.setItem(CACHE_DATE, getTodayStr());
    localStorage.setItem(CACHE_TIME, t);
  }

  function getCacheTime() {
    return localStorage.getItem(CACHE_TIME) || '';
  }

  function clearCache() {
    [CACHE_DATE, CACHE_TIME, CACHE_SS, CACHE_DBA].forEach(k => localStorage.removeItem(k));
  }

  // ── Favorites ─────────────────────────────────────────────────────────────
  let favorites = new Set();
  let favoritesData = {}; // url -> full listing object, persists across days
  function loadFavs() {
    try { favorites = new Set(JSON.parse(localStorage.getItem(FAVS_KEY) || '[]')); }
    catch { favorites = new Set(); }
    try { favoritesData = JSON.parse(localStorage.getItem(FAVS_DATA_KEY) || '{}'); }
    catch { favoritesData = {}; }
  }
  function saveFavs() {
    localStorage.setItem(FAVS_KEY, JSON.stringify([...favorites]));
    localStorage.setItem(FAVS_DATA_KEY, JSON.stringify(favoritesData));
  }
  function toggleFav(url) {
    if (favorites.has(url)) {
      favorites.delete(url);
      delete favoritesData[url];
    } else {
      favorites.add(url);
      const listing = allListings.find(l => l.url === url);
      if (listing) favoritesData[url] = listing;
    }
    saveFavs();
    const card = document.querySelector(`.card[data-url="${CSS.escape(url)}"]`);
    if (card) {
      const btn = card.querySelector('.fav-btn');
      btn.classList.toggle('active', favorites.has(url));
      btn.textContent = favorites.has(url) ? '♥' : '♡';
    }
    if (filterState.favOnly) applyFilters();
  }
  window.toggleFav = toggleFav;

  // Inject saved favorites that aren't in today's fresh listings
  function mergeWithFavorites(listings) {
    const urlSet = new Set(listings.map(l => l.url));
    const saved = Object.values(favoritesData).filter(l => favorites.has(l.url) && !urlSet.has(l.url));
    return [...listings, ...saved];
  }

  // ── Filter state ──────────────────────────────────────────────────────────
  const filterState = {
    sources: new Set(['all']),
    models: new Set(['all']),
    priceMin: null, priceMax: null,
    yearMin: null,  yearMax: null,
    mileMax: null,
    favOnly: false
  };

  function hasActiveFilters() {
    return !(
      filterState.sources.has('all') &&
      filterState.models.has('all') &&
      filterState.priceMin === null && filterState.priceMax === null &&
      filterState.yearMin  === null && filterState.yearMax  === null &&
      filterState.mileMax  === null &&
      !filterState.favOnly
    );
  }

  function applyFilters() {
    const cards = document.querySelectorAll('#grid .card');
    let visible = 0;
    cards.forEach(card => {
      const model   = card.dataset.model;
      const price   = card.dataset.price   !== '' ? parseFloat(card.dataset.price)   : null;
      const year    = card.dataset.year    !== '' ? parseInt(card.dataset.year)       : null;
      const mileage = card.dataset.mileage !== '' ? parseFloat(card.dataset.mileage) : null;
      const url     = card.dataset.url;

      let show = true;

      // Source filter
      if (!filterState.sources.has('all')) {
        if (!filterState.sources.has(card.dataset.source)) show = false;
      }

      // Model filter
      if (show && !filterState.models.has('all')) {
        if (!filterState.models.has(model)) show = false;
      }

      // Price filter
      if (show && filterState.priceMin !== null && price !== null && price < filterState.priceMin) show = false;
      if (show && filterState.priceMax !== null && price !== null && price > filterState.priceMax) show = false;

      // Year filter
      if (show && filterState.yearMin !== null && year !== null && year < filterState.yearMin) show = false;
      if (show && filterState.yearMax !== null && year !== null && year > filterState.yearMax) show = false;

      // Mileage filter
      if (show && filterState.mileMax !== null && mileage !== null && mileage > filterState.mileMax) show = false;

      // Favorites filter
      if (show && filterState.favOnly && !favorites.has(url)) show = false;

      card.classList.toggle('hidden', !show);
      if (show) visible++;
    });

    // Update count badge
    const total = cards.length;
    const countEl = document.getElementById('count');
    if (hasActiveFilters()) {
      countEl.textContent = `${visible} / ${total} listing${total !== 1 ? 's' : ''}`;
    } else {
      countEl.textContent = `${total} listing${total !== 1 ? 's' : ''}`;
    }

    // Clear button
    const clearBtn = document.getElementById('clear-btn');
    const activeCount = document.getElementById('active-count');
    if (hasActiveFilters()) {
      clearBtn.classList.add('visible');
      let n = 0;
      if (!filterState.sources.has('all')) n++;
      if (!filterState.models.has('all')) n++;
      if (filterState.priceMin !== null || filterState.priceMax !== null) n++;
      if (filterState.yearMin  !== null || filterState.yearMax  !== null) n++;
      if (filterState.mileMax  !== null) n++;
      if (filterState.favOnly) n++;
      activeCount.textContent = n > 0 ? `(${n})` : '';
    } else {
      clearBtn.classList.remove('visible');
    }

    // Empty state
    const emptyEl = document.getElementById('empty-state');
    emptyEl.style.display = visible === 0 && total > 0 ? 'block' : 'none';
  }

  function clearFilters() {
    filterState.sources = new Set(['all']);
    filterState.models  = new Set(['all']);
    filterState.priceMin = filterState.priceMax = null;
    filterState.yearMin  = filterState.yearMax  = null;
    filterState.mileMax  = null;
    filterState.favOnly  = false;

    document.querySelectorAll('.source-pill').forEach(p => p.classList.toggle('active', p.dataset.source === 'all'));
    document.querySelectorAll('.pill[data-model]').forEach(p => p.classList.toggle('active', p.dataset.model === 'all'));
    document.getElementById('price-min').value = '';
    document.getElementById('price-max').value = '';
    document.getElementById('year-min').value  = '';
    document.getElementById('year-max').value  = '';
    document.getElementById('mile-max').value  = '';
    document.getElementById('fav-toggle').classList.remove('active');
    applyFilters();
  }
  window.clearFilters = clearFilters;

  // ── Filter UI listeners ───────────────────────────────────────────────────
  function makePillToggle(pills, stateSet, allKey) {
    pills.forEach(pill => {
      pill.addEventListener('click', () => {
        const val = pill.dataset[allKey === 'all' ? (pill.dataset.source !== undefined ? 'source' : 'model') : allKey];
        const key = pill.dataset.source !== undefined ? 'source' : 'model';
        const set = key === 'source' ? filterState.sources : filterState.models;
        const allPillSel = key === 'source' ? '.source-pill[data-source="all"]' : '.pill[data-model="all"]';
        const sibSel     = key === 'source' ? '.source-pill' : '.pill[data-model]';

        if (val === 'all') {
          (key === 'source' ? filterState.sources : filterState.models).clear();
          (key === 'source' ? filterState.sources : filterState.models).add('all');
          document.querySelectorAll(sibSel).forEach(p => p.classList.toggle('active', p.dataset[key] === 'all'));
        } else {
          set.delete('all');
          document.querySelector(allPillSel).classList.remove('active');
          if (set.has(val)) {
            set.delete(val);
            pill.classList.remove('active');
            if (set.size === 0) {
              set.add('all');
              document.querySelector(allPillSel).classList.add('active');
            }
          } else {
            set.add(val);
            pill.classList.add('active');
          }
        }
        applyFilters();
      });
    });
  }

  makePillToggle(document.querySelectorAll('.source-pill'), filterState.sources, 'all');
  makePillToggle(document.querySelectorAll('.pill[data-model]'), filterState.models, 'all');

  function numOrNull(val) {
    const n = parseFloat(val);
    return isNaN(n) ? null : n;
  }

  document.getElementById('price-min').addEventListener('input', e => { filterState.priceMin = numOrNull(e.target.value); applyFilters(); });
  document.getElementById('price-max').addEventListener('input', e => { filterState.priceMax = numOrNull(e.target.value); applyFilters(); });
  document.getElementById('year-min').addEventListener('input',  e => { filterState.yearMin  = numOrNull(e.target.value); applyFilters(); });
  document.getElementById('year-max').addEventListener('input',  e => { filterState.yearMax  = numOrNull(e.target.value); applyFilters(); });
  document.getElementById('mile-max').addEventListener('input',  e => { filterState.mileMax  = numOrNull(e.target.value); applyFilters(); });

  document.getElementById('fav-toggle').addEventListener('click', () => {
    filterState.favOnly = !filterState.favOnly;
    document.getElementById('fav-toggle').classList.toggle('active', filterState.favOnly);
    applyFilters();
  });

  document.getElementById('clear-btn').addEventListener('click', clearFilters);

  document.getElementById('load-more-btn').addEventListener('click', loadMore);

  document.getElementById('refresh-btn').addEventListener('click', () => {
    clearCache();
    allListings   = [];
    renderedCount = 0;
    document.getElementById('grid').innerHTML = '';
    document.getElementById('load-more-wrap').style.display = 'none';
    document.getElementById('load-more-btn').style.display = '';
    document.getElementById('error').style.display = 'none';
    document.getElementById('empty-state').style.display = 'none';
    document.getElementById('count').style.display = 'none';
    document.getElementById('updated-label').style.display = 'none';
    document.getElementById('loading').style.display = 'flex';
    document.getElementById('loading-msg').textContent = 'Loading listings…';
    document.getElementById('refresh-btn').disabled = true;
    init();
  });

  // ── Helpers ───────────────────────────────────────────────────────────────
  function detectModel(title) {
    const t = (title || '').toUpperCase();
    if (/MODEL\s*3/.test(t)) return 'Model 3';
    if (/MODEL\s*Y/.test(t)) return 'Model Y';
    if (/MODEL\s*S/.test(t)) return 'Model S';
    if (/MODEL\s*X/.test(t)) return 'Model X';
    if (/CYBERTRUCK/.test(t)) return 'Cybertruck';
    if (/ROADSTER/.test(t)) return 'Roadster';
    return 'Other';
  }

  function parsePrice(str) {
    if (!str || str === '—') return null;
    const m = str.replace(/[\s,]/g, '').match(/\d+/);
    return m ? parseInt(m[0]) : null;
  }

  function parseMileage(str) {
    if (!str) return null;
    const clean = str.replace(/[\s,]/g, '');
    const n = parseInt((clean.match(/\d+/) || [])[0]);
    if (isNaN(n)) return null;
    return /tūkst/i.test(str) ? n * 1000 : n;
  }

  // ── Proxies ───────────────────────────────────────────────────────────────
  async function withTimeout(promise, ms) {
    return Promise.race([
      promise,
      new Promise((_, reject) => setTimeout(() => reject(new Error('timeout')), ms))
    ]);
  }

  const PROXIES = [
    async url => {
      // corsproxy.io expects the URL unencoded as the query string
      const r = await withTimeout(fetch('https://corsproxy.io/?' + url), 10000);
      if (!r.ok) throw new Error('corsproxy ' + r.status);
      return r.text();
    },
    async url => {
      const r = await withTimeout(fetch('https://api.codetabs.com/v1/proxy?quest=' + encodeURIComponent(url)), 10000);
      if (!r.ok) throw new Error('codetabs ' + r.status);
      return r.text();
    },
    async url => {
      // thingproxy expects the URL appended as a path (unencoded)
      const r = await withTimeout(fetch('https://thingproxy.freeboard.io/fetch/' + url), 10000);
      if (!r.ok) throw new Error('thingproxy ' + r.status);
      return r.text();
    },
    async url => {
      const r = await withTimeout(fetch('https://api.allorigins.win/get?url=' + encodeURIComponent(url)), 10000);
      if (!r.ok) throw new Error('allorigins ' + r.status);
      const d = await r.json();
      return d.contents || '';
    }
  ];

  async function fetchHtml(url) {
    const errors = [];
    for (const proxy of PROXIES) {
      try {
        const html = await proxy(url);
        if (html && html.length > 500) return html;
        errors.push('empty response');
      } catch (e) {
        errors.push(e.message);
      }
    }
    throw new Error('All proxies failed: ' + errors.join(' | '));
  }

  // ── Parse main listing page ───────────────────────────────────────────────
  function parseMainPage(html) {
    const listings = [];
    const rowPattern = /<tr[^>]*id="tr_[^"]*"[^>]*>([\s\S]*?)<\/tr>/gi;
    let match;
    while ((match = rowPattern.exec(html)) !== null) {
      const row = match[1];
      const linkM = row.match(/href="(\/msg\/lv\/transport\/cars\/tesla\/[^"]+\.html)"/);
      if (!linkM) continue;
      const url = linkM[1];
      const imgM = row.match(/src="(https?:\/\/i\.ss\.com\/gallery\/[^"]+\.th2\.jpg)"/);
      const thumb = imgM ? imgM[1] : null;
      let title = '';
      const titleRe = /href="[^"]+\.html"[^>]*>([^<]{5,})</g;
      let tm;
      while ((tm = titleRe.exec(row)) !== null) {
        const t = tm[1].trim();
        if (!/^[\d,.\s€]+$/.test(t) && /^[A-Za-z]/.test(t)) { title = t; break; }
      }
      const priceM = row.match(/([\d\s]{3,}\s*€)/);
      const price = priceM ? priceM[1].replace(/\s+/g, ' ').trim() : '';
      const mileM = row.match(/([\d]+\s*tūkst\.?)/);
      const mileage = mileM ? mileM[1] : '';
      const yearM = row.match(/\b(19|20)\d{2}\b/);
      const year = yearM ? yearM[0] : '';
      listings.push({ url, thumb, title, price, mileage, year });
    }

    if (listings.length === 0) {
      const blocks = html.split(/(?=href="\/msg\/lv\/transport\/cars\/tesla\/)/);
      for (const block of blocks.slice(1)) {
        const linkM = block.match(/href="(\/msg\/lv\/transport\/cars\/tesla\/[^"]+\.html)"/);
        if (!linkM) continue;
        const url = linkM[1];
        const imgM = block.match(/src="(https?:\/\/i\.ss\.com\/gallery\/[^"]+\.th2\.jpg)"/);
        const thumb = imgM ? imgM[1] : null;
        const titleM = block.match(/>([A-Za-z0-9 ,\-]+(?:Long Range|Standard|Performance|Dual|AWD|RWD)?[^<]{0,80})</);
        const title = titleM ? titleM[1].trim() : '';
        const priceM = block.match(/([\d][\d\s,.]{2,}\s*€)/);
        const price = priceM ? priceM[1].trim() : '';
        const mileM = block.match(/([\d]+\s*tūkst\.?)/);
        const mileage = mileM ? mileM[1] : '';
        const yearM = block.match(/\b(19|20)\d{2}\b/);
        const year = yearM ? yearM[0] : '';
        if (!listings.find(l => l.url === url)) {
          listings.push({ url, thumb, title, price, mileage, year });
        }
      }
    }
    return listings;
  }

  // ── Parse detail page ─────────────────────────────────────────────────────
  function parseDetailPage(html) {
    const images = [];

    // New ss.com format: IMG_D = "baseUrl/" + MSG_GALLERY_PREFIX; var IMGS = ["1|w|h|id", ...]
    const prefixM = html.match(/MSG_GALLERY_PREFIX\s*=\s*"([^"]+)"/);
    const basePM  = html.match(/IMG_D\s*=\s*"([^"]+)"\s*\+\s*MSG_GALLERY_PREFIX/);
    const imgsM   = html.match(/var\s+IMGS\s*=\s*(\[[^\]]+\])/);
    if (prefixM && basePM && imgsM) {
      try {
        const baseUrl = basePM[1] + prefixM[1]; // e.g. "https://i.ss.com/images/.../tesla-model-3-3-"
        const imgs = JSON.parse(imgsM[1]);
        imgs.forEach(entry => {
          const parts = entry.split('|');
          const imgId = parts[3];
          if (imgId) images.push(`https://i.ss.com/gallery/${imgId}.th2.jpg`);
        });
      } catch {}
    }

    // Fallback: old format href links
    if (images.length === 0) {
      const imgRe = /href="(https?:\/\/i\.ss\.com\/gallery\/[^"]+\.800\.jpg)"/gi;
      let m;
      while ((m = imgRe.exec(html)) !== null) {
        if (!images.includes(m[1])) images.push(m[1]);
      }
    }

    const norm = html
      .replace(/&euro;/gi, '€')
      .replace(/&#8364;/g, '€')
      .replace(/&nbsp;/g, ' ');

    let price = '';
    const pm = norm.match(/Cena[\s\S]{0,200}?([\d][\d\s]{1,8})\s*€/i);
    if (pm) price = pm[1].replace(/\s+/g, ' ').trim() + ' €';

    let mileage = '';
    const mm = norm.match(/Nobraukums[\s\S]{0,100}?([\d][\d\s]{2,8})/i);
    if (mm) mileage = mm[1].replace(/\s+/g, ' ').trim() + ' km';

    let year = '';
    const ym = norm.match(/(?:Izlaiduma\s+gads|Gads)[\s\S]{0,80}?((?:19|20)\d{2})/i);
    if (ym) year = ym[1];

    let model = '';
    const modM = html.match(/<title>[^-]*-\s*([^<]+?)\s*-[^<]*<\/title>/i);
    if (modM) model = modM[1].trim(); // e.g. "Tesla Model 3"

    return { images, price, mileage, year, model };
  }

  // ── dba.dk parser ────────────────────────────────────────────────────────
  function deepFindListings(obj, depth) {
    if (depth > 15 || !obj || typeof obj !== 'object') return null;
    if (Array.isArray(obj) && obj.length >= 2) {
      const f = obj[0];
      if (f && typeof f === 'object' && !Array.isArray(f)) {
        const hasTitle = !!(f.heading || f.name || f.title);
        const hasData  = f.price !== undefined || f.priceCurrency || f.year || f.mileage
                       || f.canonicalUrl || f.url || f.listingUrl || f.permalink
                       || f.images || f.image || f.photos || f.media;
        if (hasTitle && hasData) return obj;
      }
      // Recurse into array items in case listings are nested inside another array
      for (const item of obj) {
        if (item && typeof item === 'object') {
          const r = deepFindListings(item, depth + 2);
          if (r) return r;
        }
      }
      return null;
    }
    if (!Array.isArray(obj)) {
      for (const key of Object.keys(obj)) {
        const r = deepFindListings(obj[key], depth + 1);
        if (r) return r;
      }
    }
    return null;
  }

  function normalizeDbaItem(item) {
    if (!item || typeof item !== 'object') return null;

    // Schema.org Product: build title from brand + model if name is missing
    const brandName = item.brand?.name || '';
    const modelName = item.model || '';
    const schemaTitle = [brandName, modelName].filter(Boolean).join(' ');
    const title = String(item.heading || item.name || item.title || schemaTitle || '');
    if (!title) return null;

    // Price — check offers.price (Schema.org Product) and direct fields
    // Danish numbers use '.' as thousand separator (299.000 = 299000), so strip all non-digits
    let price = '';
    let priceNum = null;
    const rawPrice = item.price ?? item.offers?.price ?? item.priceValue ?? item.listPrice ?? item.priceCash;
    if (rawPrice != null) {
      const priceVal = (rawPrice && typeof rawPrice === 'object')
        ? (rawPrice.amount ?? rawPrice.value ?? rawPrice.price ?? null)
        : rawPrice;
      if (priceVal != null) {
        priceNum = parseInt(String(priceVal).replace(/\D/g, ''), 10);
        if (!isNaN(priceNum) && priceNum > 0) price = dkkToEur(priceNum).toLocaleString('en') + ' €';
      }
    }

    // Year
    const year = item.year ? String(item.year) : (item.modelYear ? String(item.modelYear) : '');

    // Mileage — can be a plain number (km) or nested object
    // Danish numbers use '.' as thousand separator, so strip all non-digits
    let mileage = '';
    const rawMile = item.mileage ?? item.kilometertal ?? item.odometer
                  ?? item.mileageFromOdometer?.value ?? item.kilometers
                  ?? item.kilometerstand ?? item.km ?? item.milage;
    if (rawMile != null) {
      const mileVal = (rawMile && typeof rawMile === 'object')
        ? (rawMile.amount ?? rawMile.value ?? rawMile.km ?? null)
        : rawMile;
      if (mileVal != null) {
        const mn = parseInt(String(mileVal).replace(/\D/g, ''), 10);
        if (!isNaN(mn) && mn >= 0) mileage = mn.toLocaleString('da-DK') + ' km';
      }
    }

    // URL — check offers.url (Schema.org Product) and direct fields
    const url = String(item.canonicalUrl || item.url || item.offers?.url || item.href
                     || item.listingUrl || item.permalink || item.link
                     || item['@id'] || '');
    if (!url || !url.startsWith('http')) return null;

    // Images — handle array of objects [{url:"..."}], array of strings, or single image object
    let images = [];
    const imgSrc = item.images || item.image || item.photos || item.media || item.pictures;
    if (Array.isArray(imgSrc) && imgSrc.length > 0) {
      images = imgSrc.map(img =>
        img && typeof img === 'object'
          ? (img.url || img.src || img.href || img.originalUrl || img.largeUrl || img.fullUrl || '')
          : String(img || '')
      ).filter(s => s && /^https?:\/\//.test(s));
    } else if (imgSrc && typeof imgSrc === 'object' && !Array.isArray(imgSrc)) {
      const u = imgSrc.url || imgSrc.src || imgSrc.href || imgSrc.originalUrl || '';
      if (u) images = [u];
    } else if (typeof imgSrc === 'string' && imgSrc) {
      images = [imgSrc];
    }
    // Fallback to thumbnail or primaryImage
    if (images.length === 0) {
      const thumb = item.thumbnail || item.primaryImage || item.coverImage || item.mainImage;
      if (thumb) images = [String(typeof thumb === 'object' ? (thumb.url || thumb.src || '') : thumb)].filter(Boolean);
    }

    return { url, title, price, mileage, year, model: '', images, source: 'dba' };
  }

  function parseDbaPage(html) {
    console.log('[dba debug] html length:', html.length, '| has __NEXT_DATA__:', /<script id="__NEXT_DATA__"/.test(html), '| has __next_f:', /self\.__next_f/.test(html), '| has INITIAL_STATE:', /__(?:INITIAL|PRELOADED)_STATE__/.test(html));

    // Strategy 1: __NEXT_DATA__ (Next.js)
    const nextM = html.match(/<script id="__NEXT_DATA__"[^>]*>([\s\S]*?)<\/script>/);
    if (nextM) {
      try {
        const parsed = JSON.parse(nextM[1]);
        const items = deepFindListings(parsed, 0);
        console.log('[dba debug] deepFindListings result:', items ? items.length + ' items' : 'null');
        if (items && items.length > 0) {
          console.log('[dba debug] raw first item:', JSON.stringify(items[0], null, 2));
          const out = items.map(normalizeDbaItem).filter(Boolean);
          if (out.length > 0) return out;
        }
        // Log a sample of the parsed JSON keys to help diagnose structure
        console.log('[dba debug] __NEXT_DATA__ top-level keys:', Object.keys(parsed || {}).join(', '));
        if (parsed?.props?.pageProps) console.log('[dba debug] pageProps keys:', Object.keys(parsed.props.pageProps).join(', '));
      } catch(e) { console.log('[dba debug] __NEXT_DATA__ parse error:', e.message); }
    }

    // Strategy 2: JSON-LD
    const ldRe = /<script[^>]*type="application\/ld\+json"[^>]*>([\s\S]*?)<\/script>/g;
    let ldM;
    while ((ldM = ldRe.exec(html)) !== null) {
      try {
        const data = JSON.parse(ldM[1]);
        let items = null;
        // Root is ItemList
        if (data['@type'] === 'ItemList') {
          items = (data.itemListElement || []).map(i => i.item || i);
        }
        // ItemList nested under mainEntity (DBA's actual structure)
        else if (data.mainEntity && data.mainEntity['@type'] === 'ItemList') {
          items = (data.mainEntity.itemListElement || []).map(i => i.item || i);
        }
        // Array of items
        else if (Array.isArray(data)) {
          items = data;
        }
        if (items && items.length > 0) {
          console.log('[dba debug] strategy2 found', items.length, 'items, first:', JSON.stringify(items[0]).slice(0, 300));
          const out = items.map(item => {
            const normalized = normalizeDbaItem(item);
            if (!normalized) return null;
            // JSON-LD doesn't include mileage or multiple images — extract from raw HTML near listing ID
            const idMatch = (normalized.url || '').match(/(\d{7,})/);
            if (idMatch) {
              const extraImgs = new Set(normalized.images);
              let searchFrom = 0;
              let mileageFound = !!normalized.mileage;
              while (true) {
                const idx = html.indexOf(idMatch[1], searchFrom);
                if (idx === -1) break;
                const ctx = html.slice(Math.max(0, idx - 500), idx + 1500);
                // Mileage
                if (!mileageFound) {
                  const kmM = ctx.match(/\b(\d{1,3}(?:\.\d{3})*)\s*km\b/i);
                  if (kmM) {
                    const mn = parseInt(kmM[1].replace(/\D/g, ''), 10);
                    if (!isNaN(mn) && mn > 0 && mn < 2000000) {
                      normalized.mileage = mn.toLocaleString('da-DK') + ' km';
                      mileageFound = true;
                    }
                  }
                }
                // Additional images from DBA's CDN
                const imgRe = /https?:\/\/[^"'\s>]*dbastatic[^"'\s>]*\.(?:jpg|jpeg|png|webp)/gi;
                let imgM;
                while ((imgM = imgRe.exec(ctx)) !== null) extraImgs.add(imgM[0]);
                searchFrom = idx + 1;
              }
              if (extraImgs.size > normalized.images.length) normalized.images = [...extraImgs];
            }
            return normalized;
          }).filter(Boolean);
          console.log('[dba debug] strategy2 normalized', out.length, 'items, first mileage:', out[0]?.mileage);
          if (out.length > 0) return out;
        }
      } catch(e) { console.log('[dba debug] strategy2 parse error:', e.message); }
    }

    // Strategy 3: Regex scan for dba listing URLs + surrounding JSON context
    const listings = [];
    const seen = new Set();
    const urlRe = /"(https?:\/\/(?:www\.)?dba\.dk\/[^"]*\/\d{6,}[^"]*)"/g;
    let m;
    let firstCtxLogged = false;
    while ((m = urlRe.exec(html)) !== null) {
      const url = m[1].split('?')[0];
      if (seen.has(url) || !/\d{6,}/.test(url)) continue;
      seen.add(url);
      const ctx = html.slice(Math.max(0, m.index - 800), m.index + 2000);
      if (!firstCtxLogged) { console.log('[dba debug] first url:', url, '\nctx sample:', ctx.slice(0, 500)); firstCtxLogged = true; }
      const priceM = ctx.match(/"(?:price|amount|priceCash|listPrice|buyNowPrice)"\s*:\s*"?([\d.,]+)"?/);
      const yearM  = ctx.match(/"(?:year|modelYear|registrationYear)"\s*:\s*(\d{4})/);
      const mileM  = ctx.match(/"(?:mileage|kilometertal|kilometerstand|odometer|kilometers|km|milage|mileageFromOdometer)"\s*:\s*"?([\d.,]+)"?/);
      const titleM = ctx.match(/"(?:heading|name|title|label)"\s*:\s*"([^"]{5,120})"/);
      const imgM   = ctx.match(/"(?:url|src|originalUrl|largeUrl|imageUrl|image_url)"\s*:\s*"(https?:\/\/[^"]*(?:dbastatic|dba\.dk|dba-static)[^"]*\.(?:jpg|jpeg|png|webp)[^"]*)"/i);
      // Strip all non-digits to handle Danish dot-separated thousands (299.000 → 299000)
      const priceNum = priceM ? parseInt(priceM[1].replace(/\D/g, ''), 10) : null;
      const mileNum  = mileM  ? parseInt(mileM[1].replace(/\D/g, ''), 10)  : null;
      listings.push({
        url,
        title: titleM ? titleM[1] : '',
        price: (priceNum && priceNum > 0) ? dkkToEur(priceNum).toLocaleString('en') + ' €' : '',
        year: yearM ? yearM[1] : '',
        mileage: (mileNum != null && !isNaN(mileNum)) ? mileNum.toLocaleString('da-DK') + ' km' : '',
        images: imgM ? [imgM[1]] : [],
        source: 'dba'
      });
    }
    return listings;
  }

  // ── Render helpers ────────────────────────────────────────────────────────
  function makeSlider(images, url) {
    const favActive = favorites.has(url);
    const favBtn = `<button class="fav-btn${favActive ? ' active' : ''}" onclick="toggleFav('${url.replace(/'/g, "\\'")}')">${favActive ? '♥' : '♡'}</button>`;

    if (!images || images.length === 0) {
      return `<div class="slider-wrap">
        ${favBtn}
        <div class="slides"><div class="slide"><div class="no-img">🚗</div></div></div>
      </div>`;
    }

    const slides = images.map(src =>
      `<div class="slide"><img src="${src}" loading="lazy" referrerpolicy="no-referrer" onerror="this.style.display='none'"></div>`
    ).join('');

    const dots = images.length > 1
      ? `<div class="slider-dots">${images.map((_, i) => `<div class="dot${i === 0 ? ' active' : ''}"></div>`).join('')}</div>`
      : '';

    const arrows = images.length > 1
      ? `<button class="arrow prev" onclick="slide(this,-1)">&#8249;</button>
         <button class="arrow next" onclick="slide(this,1)">&#8250;</button>`
      : '';

    const countBadge = images.length > 1
      ? `<div class="img-count">1 / ${images.length}</div>`
      : '';

    return `<div class="slider-wrap" data-idx="0" data-total="${images.length}">
      ${favBtn}
      <div class="slides">${slides}</div>
      ${arrows}${dots}${countBadge}
    </div>`;
  }

  function slide(btn, dir) {
    const wrap = btn.closest('.slider-wrap');
    const total = +wrap.dataset.total;
    let idx = +wrap.dataset.idx + dir;
    if (idx < 0) idx = total - 1;
    if (idx >= total) idx = 0;
    wrap.dataset.idx = idx;
    wrap.querySelector('.slides').style.transform = `translateX(-${idx * 100}%)`;
    wrap.querySelectorAll('.dot').forEach((d, i) => d.classList.toggle('active', i === idx));
    const badge = wrap.querySelector('.img-count');
    if (badge) badge.textContent = `${idx + 1} / ${total}`;
  }
  window.slide = slide;

  function makeCard(info) {
    const { url, title, price, mileage, year, model, images, source } = info;
    // ss.com uses relative paths; dba.dk provides full URLs
    const fullUrl   = source === 'dba' ? url : SS_BASE + url;
    const cardUrl   = url; // used as unique key for favorites / data-url
    const modelName = detectModel(title || model);
    const priceNum  = parsePrice(price);
    const mileNum   = parseMileage(mileage);
    const yearNum   = year ? parseInt(year) : '';

    const displayTitle = title || (model ? `Tesla ${model}` : 'Tesla');
    const yearTag  = year    ? `<div class="tag"><span class="icon">📅</span>${year}</div>` : '';
    const mileTag  = mileage ? `<div class="tag"><span class="icon">🛣️</span>${mileage}</div>` : '';
    const modelTag = `<div class="tag model-tag">${modelName}</div>`;
    const srcLabel  = source === 'dba' ? 'dba.dk' : 'ss.com';
    const srcClass  = source === 'dba' ? 'dba' : 'ss';

    return `
      <div class="card"
        data-url="${cardUrl}"
        data-source="${source || 'ss'}"
        data-model="${modelName}"
        data-price="${priceNum !== null ? priceNum : ''}"
        data-year="${yearNum}"
        data-mileage="${mileNum !== null ? mileNum : ''}">
        ${makeSlider(images, cardUrl)}
        <div class="card-body">
          <div class="card-title">${displayTitle}</div>
          <div class="card-meta">
            ${modelTag}${yearTag}${mileTag}
          </div>
          <div class="card-price">${price || '—'}</div>
          <div class="card-footer">
            <a class="view-btn" href="${fullUrl}" target="_blank">View listing ↗</a>
            <span class="source-badge ${srcClass}">${srcLabel}</span>
          </div>
        </div>
      </div>`;
  }

  // ── Pagination ────────────────────────────────────────────────────────────
  const PAGE_SIZE = 12;
  let allListings   = [];
  let renderedCount = 0;

  function updateLoadMore() {
    const wrap = document.getElementById('load-more-wrap');
    const info = document.getElementById('load-more-info');
    const btn  = document.getElementById('load-more-btn');
    const remaining = allListings.length - renderedCount;

    if (remaining > 0) {
      wrap.style.display = 'flex';
      info.textContent = `Showing ${renderedCount} of ${allListings.length} listings`;
      btn.textContent  = `Load ${Math.min(remaining, PAGE_SIZE)} more`;
      btn.disabled = false;
    } else if (allListings.length > 0) {
      wrap.style.display = 'flex';
      info.textContent = `All ${allListings.length} listings loaded`;
      btn.style.display = 'none';
    } else {
      wrap.style.display = 'none';
    }
  }

  function loadMore() {
    const grid  = document.getElementById('grid');
    const batch = allListings.slice(renderedCount, renderedCount + PAGE_SIZE);
    renderedCount += batch.length;
    grid.insertAdjacentHTML('beforeend', batch.map(makeCard).join(''));
    applyFilters();
    updateLoadMore();
  }
  window.loadMore = loadMore;

  // ── Render listings ───────────────────────────────────────────────────────
  function renderListings(details) {
    allListings   = details;
    renderedCount = 0;

    const grid    = document.getElementById('grid');
    const countEl = document.getElementById('count');

    document.getElementById('loading').style.display = 'none';
    document.getElementById('refresh-btn').disabled = false;

    countEl.textContent = `${details.length} listing${details.length !== 1 ? 's' : ''}`;
    countEl.style.display = '';

    const cacheTime = getCacheTime();
    if (cacheTime) {
      const lbl = document.getElementById('updated-label');
      lbl.textContent = `Updated today at ${cacheTime}`;
      lbl.style.display = 'block';
    }

    // Render first batch
    grid.innerHTML = '';
    const first = details.slice(0, PAGE_SIZE);
    renderedCount = first.length;
    grid.innerHTML = first.map(makeCard).join('');
    applyFilters();
    updateLoadMore();
  }

  // ── Fetch ss.com listings ──────────────────────────────────────────────────
  async function fetchSsListings() {
    const mainHtml = await fetchHtml(SS_URL);
    const listings = parseMainPage(mainHtml);
    if (listings.length === 0) return [];

    return Promise.all(listings.map(async l => {
      try {
        const dHtml = await fetchHtml(SS_BASE + l.url);
        const d = parseDetailPage(dHtml);
        return {
          url: l.url, source: 'ss',
          title: l.title || d.model,
          price: d.price || l.price,
          mileage: d.mileage || l.mileage,
          year: d.year || l.year,
          model: d.model,
          images: d.images.length > 0 ? d.images : (l.thumb ? [l.thumb.replace('.th2.jpg', '.800.jpg')] : [])
        };
      } catch {
        return { url: l.url, source: 'ss', title: l.title, price: l.price,
                 mileage: l.mileage, year: l.year, model: '', images: l.thumb ? [l.thumb] : [] };
      }
    }));
  }

  // ── Fetch dba.dk listings ──────────────────────────────────────────────────
  async function fetchDbaListings() {
    const html = await fetchHtml(DBA_URL);
    return parseDbaPage(html);
  }

  // ── Init ──────────────────────────────────────────────────────────────────
  async function init() {
    loadFavs();

    const loadingMsg = document.getElementById('loading-msg');

    // Try cache first
    if (isCacheValid()) {
      const cachedSs  = getCachedSource(CACHE_SS)  || [];
      const cachedDba = getCachedSource(CACHE_DBA) || [];
      const combined  = [...cachedSs, ...cachedDba];
      if (combined.length > 0) {
        renderListings(mergeWithFavorites(combined));
        return;
      }
    }

    document.getElementById('loading').style.display = 'flex';
    loadingMsg.textContent = 'Loading listings from ss.com & dba.dk…';

    const [ssResult, dbaResult] = await Promise.allSettled([
      fetchSsListings(),
      fetchDbaListings()
    ]);

    const ssListings  = ssResult.status  === 'fulfilled' ? ssResult.value  : [];
    const dbaListings = dbaResult.status === 'fulfilled' ? dbaResult.value : [];
    const combined    = mergeWithFavorites([...ssListings, ...dbaListings]);

    stampCache();
    setCacheSource(CACHE_SS,  ssListings);
    setCacheSource(CACHE_DBA, dbaListings);

    if (combined.length === 0) {
      document.getElementById('loading').style.display = 'none';
      document.getElementById('refresh-btn').disabled = false;
      const errorEl = document.getElementById('error');
      const errMsg  = document.getElementById('err-msg');
      errorEl.style.display = 'block';
      const msgs = [];
      if (ssResult.status  === 'rejected') msgs.push('ss.com: '  + ssResult.reason?.message);
      if (dbaResult.status === 'rejected') msgs.push('dba.dk: ' + dbaResult.reason?.message);
      errMsg.textContent = msgs.join(' · ') || 'No listings found.';
      return;
    }

    if (ssResult.status === 'rejected' || dbaResult.status === 'rejected') {
      const failed = ssResult.status === 'rejected' ? 'ss.com' : 'dba.dk';
      loadingMsg.textContent = `⚠ ${failed} failed to load — showing results from other source`;
    }

    renderListings(combined);
  }

  init();
</script>
</body>
</html>

