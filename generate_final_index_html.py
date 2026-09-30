import json
import os

with open(r'C:\Users\mm\.gemini\antigravity\scratch\book_project\book_data_full.json', 'r', encoding='utf-8') as f:
    units_data = json.load(f)

html_template = '''<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover">
  <title>瞬時に話せる英会話大特訓 (全90 UNIT 完全版)</title>
  <meta name="description" content="瞬時に話せる英会話大特訓 全90 UNIT (800項目) 完全版Webリーダー。PC全画面フィット見開き表示＆スマホ単語帳モード対応。">
  <meta name="theme-color" content="#21242d">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="瞬時英会話">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🗣️</text></svg>">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=BIZ+UDMincho:wght@400;700&family=Inter:wght@400;500;600;700;800&family=Noto+Sans+JP:wght@400;500;600;700&family=Noto+Serif+JP:wght@500;700;900&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-desk: #21242d;
      --paper-bg: #fdfbf7;
      --paper-border: #e6dfd3;
      --text-main: #1f2328;
      --text-sub: #4b5563;
      --text-muted: #8c959f;
      --accent-red: #c92a2a;
      --accent-red-light: #fff5f5;
      --accent-red-border: #ffc9c9;
      --accent-blue: #1864ab;
      --accent-blue-light: #e7f5ff;
      --accent-gold: #f59f00;
      --accent-gold-light: #fff9db;
      --card-bg: #ffffff;
      --card-border: #eae4d8;
      --card-hover: #faf8f3;
      --shadow-book: 0 20px 45px -10px rgba(0, 0, 0, 0.45), 0 0 0 1px rgba(0, 0, 0, 0.08);
      --badge-left: #c92a2a;
      --badge-right: #212529;
    }

    [data-theme="white"] {
      --bg-desk: #edf2f7;
      --paper-bg: #ffffff;
      --paper-border: #cbd5e1;
      --text-main: #0f172a;
      --text-sub: #334155;
      --card-bg: #f8fafc;
      --card-border: #e2e8f0;
      --card-hover: #f1f5f9;
      --shadow-book: 0 15px 35px -8px rgba(0, 0, 0, 0.15), 0 0 0 1px rgba(0, 0, 0, 0.05);
      --badge-right: #334155;
    }

    [data-theme="dark"] {
      --bg-desk: #090d16;
      --paper-bg: #151d2e;
      --paper-border: #2a374d;
      --text-main: #f8fafc;
      --text-sub: #cbd5e1;
      --text-muted: #94a3b8;
      --accent-red: #ff6b6b;
      --accent-red-light: #3d1414;
      --accent-red-border: #661a1a;
      --accent-blue: #4dabf7;
      --accent-blue-light: #102847;
      --accent-gold: #fcc419;
      --accent-gold-light: #382d0d;
      --card-bg: #1c263b;
      --card-border: #2d3b55;
      --card-hover: #222f47;
      --shadow-book: 0 25px 60px rgba(0, 0, 0, 0.7), 0 0 0 1px rgba(255, 255, 255, 0.05);
      --badge-left: #e03131;
      --badge-right: #475569;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background-color: var(--bg-desk);
      color: var(--text-main);
      font-family: 'Noto Sans JP', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      height: 100vh;
      display: flex;
      flex-direction: column;
      overflow: hidden; /* Default to no scroll in fit mode */
      transition: background-color 0.25s ease;
    }

    body.scroll-mode {
      overflow-y: auto;
      height: auto;
      min-height: 100vh;
    }

    /* Top Sticky Toolbar */
    .top-bar {
      background: rgba(18, 22, 33, 0.96);
      backdrop-filter: blur(12px);
      color: #fff;
      padding: 6px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-shrink: 0;
      z-index: 1000;
      box-shadow: 0 2px 14px rgba(0,0,0,0.35);
      gap: 10px;
      height: 48px;
    }

    .brand-section {
      display: flex;
      align-items: center;
      gap: 8px;
      white-space: nowrap;
    }

    .brand-title {
      font-size: 0.98rem;
      font-weight: 800;
      letter-spacing: 0.03em;
      color: #f8fafc;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .badge-master {
      background: linear-gradient(135deg, #c92a2a, #e03131);
      color: #fff;
      font-size: 0.68rem;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 999px;
    }

    .toolbar-actions {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: nowrap;
    }

    .unit-select {
      background: #1e2538;
      color: #fff;
      border: 1px solid #3b4561;
      padding: 5px 10px;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 600;
      outline: none;
      cursor: pointer;
      max-width: 220px;
    }

    .search-bar-wrap {
      position: relative;
      width: 170px;
    }

    .search-input {
      width: 100%;
      background: #1e2538;
      border: 1px solid #3b4561;
      color: #fff;
      padding: 5px 10px 5px 28px;
      border-radius: 6px;
      font-size: 0.82rem;
      outline: none;
      transition: width 0.2s;
    }
    .search-input:focus {
      border-color: #4dabf7;
      width: 210px;
    }
    .search-icon {
      position: absolute;
      left: 8px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 0.8rem;
      color: #8c959f;
      pointer-events: none;
    }

    .btn-tool {
      background: #1e2538;
      color: #f1f5f9;
      border: 1px solid #3b4561;
      padding: 5px 10px;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.15s;
      white-space: nowrap;
    }
    .btn-tool:hover { background: #2b344d; }
    .btn-tool.active {
      background: #c92a2a;
      border-color: #e03131;
      color: #fff;
    }

    /* Main Presentation Stage */
    .book-stage {
      flex: 1;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 8px 16px;
      overflow: hidden;
      position: relative;
    }

    body.scroll-mode .book-stage {
      overflow-y: visible;
      height: auto;
      padding: 20px 16px 40px;
    }

    /* SYNCHRONIZED CSS GRID SPREAD (FIT TO VIEWPORT) */
    .book-spread-grid {
      display: grid;
      grid-template-columns: 1fr 14px 1fr;
      grid-template-rows: auto repeat(9, 1fr) auto;
      gap: clamp(3px, 0.6vh, 6px) 0;
      background: var(--paper-bg);
      box-shadow: var(--shadow-book);
      border-radius: 10px;
      width: 100%;
      max-width: 1300px;
      height: calc(100vh - 98px); /* exact fit between top and bottom nav */
      margin: 0 auto;
      padding: clamp(10px, 1.4vh, 18px) clamp(16px, 1.8vw, 28px);
      position: relative;
      border: 1px solid var(--paper-border);
      transition: transform 0.15s ease-out;
    }

    body.scroll-mode .book-spread-grid {
      height: auto;
      grid-template-rows: auto repeat(9, minmax(72px, auto)) auto;
      gap: 8px 0;
      padding: 24px 28px;
    }

    /* Center Spine Divider */
    .book-spine-divider {
      grid-column: 2;
      grid-row: 1 / span 11;
      background: linear-gradient(to right,
        rgba(0,0,0,0.12) 0%,
        rgba(0,0,0,0.03) 35%,
        rgba(0,0,0,0.01) 50%,
        rgba(0,0,0,0.03) 65%,
        rgba(0,0,0,0.12) 100%
      );
      position: relative;
      margin: -18px 0;
    }
    .book-spine-divider::after {
      content: '';
      position: absolute;
      top: 0; bottom: 0; left: 50%;
      width: 1px;
      background: rgba(0,0,0,0.12);
      transform: translateX(-50%);
    }

    .left-col-item {
      grid-column: 1;
      padding-right: clamp(10px, 1.2vw, 18px);
    }
    .right-col-item {
      grid-column: 3;
      padding-left: clamp(10px, 1.2vw, 18px);
    }

    /* Row 1: Header Row */
    .header-left {
      grid-row: 1;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      border-bottom: 2px solid var(--accent-red);
      padding-bottom: clamp(4px, 0.8vh, 8px);
      margin-bottom: 2px;
    }

    .header-right {
      grid-row: 1;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      border-bottom: 2px solid var(--card-border);
      padding-bottom: clamp(4px, 0.8vh, 8px);
      margin-bottom: 2px;
    }

    .unit-meta-bar {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 2px;
    }

    .unit-badge-pill {
      background: var(--accent-red);
      color: #fff;
      font-size: clamp(0.72rem, 1.1vh, 0.82rem);
      font-weight: 800;
      padding: 2px 10px;
      border-radius: 999px;
      letter-spacing: 0.05em;
    }

    .chapter-tag {
      font-size: clamp(0.72rem, 1.1vh, 0.8rem);
      font-weight: 600;
      color: var(--text-sub);
    }

    .unit-main-title {
      font-family: 'Noto Serif JP', 'BIZ UDMincho', serif;
      font-size: clamp(1.15rem, 2.1vh, 1.55rem);
      font-weight: 900;
      color: var(--text-main);
      line-height: 1.2;
      letter-spacing: 0.02em;
      margin-bottom: 4px;
    }

    .mascot-intro-box {
      background: var(--accent-red-light);
      border-left: 3px solid var(--accent-red);
      border-radius: 4px;
      padding: clamp(3px, 0.6vh, 6px) clamp(6px, 0.8vw, 10px);
      font-size: clamp(0.74rem, 1.15vh, 0.84rem);
      line-height: 1.35;
      color: var(--text-sub);
      display: flex;
      gap: 6px;
      align-items: flex-start;
    }
    .mascot-intro-box .mascot-icon { font-size: 0.95rem; flex-shrink: 0; }

    /* Right Header: CD Badge & Key Box */
    .cd-track-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 2px;
    }

    .cd-pill {
      background: var(--accent-blue);
      color: #fff;
      font-size: clamp(0.72rem, 1.1vh, 0.8rem);
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 4px;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }

    .repetition-header-badge {
      font-size: clamp(0.68rem, 1vh, 0.76rem);
      font-weight: 600;
      color: var(--text-muted);
    }

    .key-box-card {
      background: var(--accent-gold-light);
      border: 1px solid rgba(245, 159, 0, 0.3);
      border-radius: 4px;
      padding: clamp(3px, 0.6vh, 6px) clamp(6px, 0.8vw, 10px);
      font-size: clamp(0.72rem, 1.15vh, 0.82rem);
      line-height: 1.35;
      color: var(--text-sub);
    }

    .key-box-title {
      font-weight: 800;
      color: #d97706;
      font-size: clamp(0.74rem, 1.15vh, 0.84rem);
      display: flex;
      align-items: center;
      gap: 4px;
      margin-bottom: 2px;
    }
    [data-theme="dark"] .key-box-title { color: #fcc419; }

    /* ITEM CARDS - BALANCED IN EXACT SAME ROW */
    .item-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 6px;
      padding: clamp(4px, 0.65vh, 8px) clamp(8px, 0.9vw, 12px);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
      box-shadow: 0 1px 2px rgba(0,0,0,0.02);
      transition: background-color 0.15s, border-color 0.15s;
    }
    .item-card:hover {
      border-color: #cbd5e1;
      background: var(--card-hover);
    }

    .item-header-row {
      display: flex;
      align-items: flex-start;
      gap: 8px;
    }

    .item-num-badge {
      width: clamp(19px, 2.3vh, 23px);
      height: clamp(19px, 2.3vh, 23px);
      border-radius: 50%;
      background: var(--badge-left);
      color: #fff;
      font-size: clamp(0.72rem, 1.1vh, 0.82rem);
      font-weight: 800;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      margin-top: 1px;
    }

    .right-card .item-num-badge {
      background: var(--badge-right);
    }

    .item-text-area {
      flex: 1;
      min-width: 0;
    }

    .japanese-sentence {
      font-size: clamp(0.88rem, 1.45vh, 1.05rem);
      font-weight: 600;
      color: var(--text-main);
      line-height: 1.3;
      letter-spacing: 0.01em;
    }

    .hint-note-row {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 2px;
      font-size: clamp(0.68rem, 1.05vh, 0.78rem);
    }

    .hint-tag {
      background: var(--accent-red-light);
      color: var(--accent-red);
      border: 1px solid var(--accent-red-border);
      padding: 0 5px;
      border-radius: 3px;
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      gap: 2px;
      line-height: 1.3;
    }

    .note-text {
      color: var(--text-sub);
      line-height: 1.25;
    }

    /* 5-step Checkboxes */
    .checks-row {
      display: flex;
      align-items: center;
      gap: 4px;
      margin-top: 2px;
      padding-top: 2px;
      border-top: 1px dashed var(--card-border);
      font-size: clamp(0.65rem, 0.95vh, 0.72rem);
      color: var(--text-muted);
      font-weight: 600;
    }

    .check-box-input {
      appearance: none;
      width: clamp(11px, 1.4vh, 13px);
      height: clamp(11px, 1.4vh, 13px);
      border: 1.5px solid #a0aec0;
      border-radius: 2px;
      cursor: pointer;
      position: relative;
      background: transparent;
    }
    .check-box-input:checked {
      background: var(--accent-red);
      border-color: var(--accent-red);
    }
    .check-box-input:checked::after {
      content: '✓';
      position: absolute;
      color: #fff;
      font-size: 8px;
      font-weight: 900;
      top: 50%; left: 50%;
      transform: translate(-50%, -50%);
    }

    /* Right Card: English Content */
    .english-top-row {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 6px;
    }

    .english-sentence {
      font-family: 'Inter', -apple-system, sans-serif;
      font-size: clamp(0.92rem, 1.55vh, 1.12rem);
      font-weight: 700;
      color: var(--text-main);
      line-height: 1.25;
      letter-spacing: -0.01em;
    }

    .pronunciation-tag {
      display: inline-block;
      font-size: clamp(0.68rem, 1vh, 0.76rem);
      color: var(--text-muted);
      background: rgba(0,0,0,0.04);
      padding: 0 4px;
      border-radius: 3px;
      margin-top: 1px;
    }
    [data-theme="dark"] .pronunciation-tag { background: rgba(255,255,255,0.06); }

    .btn-speak {
      background: var(--accent-blue-light);
      color: var(--accent-blue);
      border: 1px solid rgba(24, 100, 171, 0.25);
      width: clamp(22px, 2.6vh, 26px);
      height: clamp(22px, 2.6vh, 26px);
      border-radius: 4px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: clamp(0.75rem, 1.2vh, 0.85rem);
      cursor: pointer;
      flex-shrink: 0;
      transition: all 0.15s;
    }
    .btn-speak:hover {
      background: var(--accent-blue);
      color: #fff;
    }

    .explanation-callout {
      margin-top: 2px;
      padding-top: 2px;
      border-top: 1px dashed var(--card-border);
      font-size: clamp(0.68rem, 1.05vh, 0.78rem);
      line-height: 1.25;
      color: var(--text-sub);
    }

    /* Mask Mode Styling (Blur Answer) */
    .book-spread-grid.masked .right-card .english-sentence,
    .book-spread-grid.masked .right-card .pronunciation-tag,
    .book-spread-grid.masked .right-card .explanation-callout {
      filter: blur(7px);
      user-select: none;
      cursor: pointer;
      transition: filter 0.2s ease;
    }
    .book-spread-grid.masked .right-card.revealed .english-sentence,
    .book-spread-grid.masked .right-card.revealed .pronunciation-tag,
    .book-spread-grid.masked .right-card.revealed .explanation-callout {
      filter: none;
    }
    .book-spread-grid.masked .right-card {
      cursor: pointer;
      position: relative;
      transition: background-color 0.2s ease;
    }
    .book-spread-grid.masked .left-card {
      cursor: pointer;
    }
    .book-spread-grid.masked .right-card:not(.revealed) {
      background: rgba(24, 100, 171, 0.05);
      border: 1px dashed rgba(24, 100, 171, 0.35);
    }
    .book-spread-grid.masked .right-card:not(.revealed)::after {
      content: "👁️ タップして英文を表示";
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 5px 12px;
      margin-top: 6px;
      background: var(--accent-blue);
      color: #ffffff;
      border-radius: 4px;
      font-size: 0.76rem;
      font-weight: 700;
      letter-spacing: 0.02em;
      box-shadow: 0 1px 3px rgba(0,0,0,0.15);
    }
    .book-spread-grid.masked .right-card.revealed::after {
      content: "🙈 タップで再非表示";
      display: inline-block;
      font-size: 0.68rem;
      color: var(--text-muted);
      margin-top: 4px;
    }

    /* Row 11: Footer (Page Numbers) */
    .footer-left {
      grid-row: 11;
      padding-right: 18px;
      display: flex;
      justify-content: flex-start;
      align-items: center;
      font-size: clamp(0.72rem, 1.1vh, 0.8rem);
      font-weight: 700;
      color: var(--text-muted);
      border-top: 1px solid var(--paper-border);
      padding-top: 3px;
      margin-top: 1px;
    }

    .footer-right {
      grid-row: 11;
      padding-left: 18px;
      display: flex;
      justify-content: flex-end;
      align-items: center;
      font-size: clamp(0.72rem, 1.1vh, 0.8rem);
      font-weight: 700;
      color: var(--text-muted);
      border-top: 1px solid var(--paper-border);
      padding-top: 3px;
      margin-top: 1px;
    }

    /* Scan View Spread Mode */
    .scan-view-stage {
      display: flex;
      justify-content: center;
      align-items: center;
      width: 100%;
      height: 100%;
      max-width: 1300px;
      margin: 0 auto;
      background: #111;
      border-radius: 8px;
      overflow: hidden;
      box-shadow: var(--shadow-book);
    }
    .scan-view-img {
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      cursor: pointer;
    }

    /* Bottom Navigation Bar */
    .bottom-nav {
      background: rgba(18, 22, 33, 0.96);
      backdrop-filter: blur(12px);
      color: #fff;
      padding: 6px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-shrink: 0;
      z-index: 1000;
      box-shadow: 0 -2px 14px rgba(0,0,0,0.35);
      height: 48px;
    }

    .btn-nav-action {
      background: #252e44;
      color: #fff;
      border: 1px solid #3d4a6c;
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 0.88rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s;
    }
    .btn-nav-action:hover:not(:disabled) { background: #344061; }
    .btn-nav-action:disabled { opacity: 0.35; cursor: not-allowed; }

    .btn-nav-mask {
      background: #252e44;
      color: #f1f5f9;
      border: 1px solid #4a5880;
      padding: 6px 16px;
      border-radius: 20px;
      font-size: 0.86rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
      user-select: none;
      -webkit-tap-highlight-color: transparent;
      box-shadow: 0 2px 6px rgba(0,0,0,0.25);
    }
    .btn-nav-mask:hover {
      background: #364264;
      border-color: #6577aa;
    }
    .btn-nav-mask:active {
      transform: scale(0.96);
    }
    .btn-nav-mask.active {
      background: #c92a2a;
      border-color: #ff8787;
      color: #ffffff;
      box-shadow: 0 0 12px rgba(201, 42, 42, 0.6);
    }
    [data-theme="white"] .btn-nav-mask {
      background: #e2e8f0;
      color: #0f172a;
      border-color: #cbd5e1;
    }
    [data-theme="white"] .btn-nav-mask.active {
      background: #c92a2a;
      color: #ffffff;
      border-color: #ff8787;
    }
    [data-theme="dark"] .btn-nav-mask {
      background: #1c263b;
      color: #f8fafc;
      border-color: #3b4e75;
    }
    [data-theme="dark"] .btn-nav-mask.active {
      background: #e03131;
      color: #ffffff;
      border-color: #ff6b6b;
    }

    .page-indicator-badge {
      font-size: 0.92rem;
      font-weight: 800;
      letter-spacing: 0.04em;
      color: #f1f5f9;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    /* SMARTPHONE RESPONSIVE STYLING (< 860px) */
    @media (max-width: 860px) {
      body {
        overflow-y: auto !important;
        height: auto !important;
        min-height: 100vh;
      }

      /* Compact horizontal toolstrip on mobile */
      .top-bar {
        position: sticky;
        top: 0;
        height: auto;
        min-height: 46px;
        padding: 6px 10px;
        flex-wrap: wrap;
        gap: 6px;
      }
      .brand-section {
        flex: 1 1 auto;
      }
      .brand-title {
        font-size: 0.88rem;
      }
      .brand-title span:last-child {
        display: none;
      }
      .toolbar-actions {
        width: 100%;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        padding-bottom: 2px;
        gap: 6px;
      }
      .toolbar-actions::-webkit-scrollbar {
        display: none;
      }
      .unit-select {
        flex-shrink: 0;
        max-width: 145px;
        font-size: 0.76rem;
        padding: 4px 6px;
      }
      .search-bar-wrap {
        flex-shrink: 0;
        width: 110px;
      }
      .search-input {
        font-size: 0.76rem;
        padding: 4px 8px 4px 24px;
      }
      .search-input:focus {
        width: 135px;
      }
      .btn-tool {
        flex-shrink: 0;
        padding: 4px 8px;
        font-size: 0.76rem;
      }
      #fitScreenBtn, .btn-print {
        display: none !important;
      }

      /* Content container */
      .book-stage {
        padding: 8px 8px 65px 8px;
        overflow-y: visible;
        height: auto;
      }
      .book-spread-grid {
        display: flex;
        flex-direction: column;
        padding: 12px 10px;
        gap: 0;
        height: auto !important;
        border-radius: 8px;
      }
      .book-spine-divider { display: none; }
      .left-col-item, .right-col-item {
        padding: 0;
        width: 100%;
      }

      /* Unit header on mobile */
      .header-left {
        border-bottom: none;
        margin-bottom: 0;
        padding-bottom: 4px;
      }
      .header-right {
        border-bottom: 2px solid var(--accent-red);
        margin-bottom: 10px;
        padding-bottom: 8px;
      }
      .unit-main-title {
        font-size: 1.25rem;
        margin-bottom: 6px;
      }
      .mascot-intro-box {
        font-size: 0.8rem;
        padding: 6px 8px;
        margin-bottom: 6px;
      }
      .key-box-card {
        font-size: 0.78rem;
        padding: 6px 8px;
      }

      /* Seamless Q&A Flashcard Pairing for mobile */
      .left-col-item {
        margin-top: 10px;
      }
      .left-col-item .item-card {
        border-bottom: 1px dashed var(--card-border);
        border-bottom-left-radius: 0;
        border-bottom-right-radius: 0;
        box-shadow: none;
        padding: 10px 12px;
      }
      .right-col-item {
        margin-top: 0;
        margin-bottom: 6px;
      }
      .right-col-item .item-card {
        border-top: none;
        border-top-left-radius: 0;
        border-top-right-radius: 0;
        background: rgba(0, 0, 0, 0.02);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.04);
        padding: 10px 12px;
      }
      [data-theme="dark"] .right-col-item .item-card {
        background: rgba(255, 255, 255, 0.03);
      }

      .japanese-sentence {
        font-size: 1.02rem;
        line-height: 1.35;
      }
      .english-sentence {
        font-size: 1.08rem;
        line-height: 1.3;
      }
      .btn-speak {
        width: 36px !important;
        height: 36px !important;
        font-size: 1.1rem !important;
      }
      .check-box-input {
        width: 16px !important;
        height: 16px !important;
      }

      .footer-left, .footer-right {
        display: none;
      }

      /* Scan view on mobile */
      .scan-view-stage {
        height: auto;
        min-height: 50vh;
      }
      .scan-view-img {
        max-height: none;
        width: 100%;
      }

      /* Sticky bottom bar with safe-area support */
      .bottom-nav {
        position: sticky;
        bottom: 0;
        height: auto;
        min-height: 52px;
        padding: 6px 10px max(10px, env(safe-area-inset-bottom));
        gap: 6px;
        justify-content: space-between;
      }
      .btn-nav-action {
        padding: 8px 12px;
        font-size: 0.82rem;
        flex-shrink: 0;
      }
      .btn-nav-mask {
        padding: 8px 14px;
        font-size: 0.85rem;
        border-radius: 20px;
        flex-shrink: 0;
        font-weight: 800;
        background: #2b354f;
      }
      .btn-nav-mask.active {
        background: #c92a2a;
        box-shadow: 0 0 10px rgba(201, 42, 42, 0.6);
      }
      .page-indicator-badge {
        font-size: 0.78rem;
        padding: 2px 6px;
        white-space: nowrap;
      }
      @media (max-width: 410px) {
        .nav-label-text {
          display: none;
        }
        .btn-nav-action {
          padding: 8px 10px;
        }
        .btn-nav-mask {
          padding: 8px 12px;
          font-size: 0.82rem;
        }
      }
    }
  </style>
</head>
<body>

  <!-- Top Sticky Navigation -->
  <header class="top-bar">
    <div class="brand-section">
      <div class="brand-title">
        <span>📖</span>
        <span>瞬時に話せる英会話大特訓</span>
        <span class="badge-master">全90 UNIT</span>
      </div>
    </div>

    <div class="toolbar-actions">
      <!-- Unit Selector -->
      <select id="unitSelect" class="unit-select" onchange="goToUnit(parseInt(this.value))">
        <!-- populated by JS -->
      </select>

      <!-- Mask Mode (Study / Blur answers) - Prioritized first for easy mobile access -->
      <button class="btn-tool" id="maskToggleBtn" onclick="toggleMaskMode()" title="英語を伏せて自力で言えるかテストします">
        <span>🙈</span>
        <span id="maskBtnText">暗記テスト</span>
      </button>

      <!-- Auto Play Speech -->
      <button class="btn-tool" id="playAllBtn" onclick="playAllPhrases()" title="UNIT内の全フレーズを順番に読み上げます">
        <span>🔊</span>
        <span>連続再生</span>
      </button>

      <!-- Search Input -->
      <div class="search-bar-wrap">
        <span class="search-icon">🔍</span>
        <input type="text" id="searchInput" class="search-input" placeholder="フレーズ検索..." oninput="handleSearch(this.value)">
      </div>

      <!-- Fit Screen Toggle -->
      <button class="btn-tool active" id="fitScreenBtn" onclick="toggleFitScreen()" title="画面サイズに合わせてスクロールなしの全画面表示にします">
        <span id="fitScreenIcon">📐</span>
        <span id="fitScreenText">全画面フィット</span>
      </button>

      <!-- View Mode (Typeset Spread <-> Scan Spread) -->
      <button class="btn-tool" id="viewModeBtn" onclick="toggleViewMode()" title="組版テキストと原本スキャン画像を切り替えます">
        <span id="viewModeIcon">🖼️</span>
        <span id="viewModeText">原本スキャン</span>
      </button>

      <!-- Theme Switcher -->
      <button class="btn-tool" onclick="cycleTheme()" title="用紙テーマ切り替え">
        <span id="themeIcon">📜</span>
        <span id="themeText">生成り紙</span>
      </button>

      <!-- Print / PDF -->
      <button class="btn-tool btn-print" onclick="window.print()" title="本を印刷またはPDFとして保存">
        <span>🖨️</span>
        <span>印刷</span>
      </button>
    </div>
  </header>

  <!-- Main Presentation Stage -->
  <main class="book-stage">
    <div id="mainContainer" style="width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;">
      <!-- Spread or Scan rendered dynamically -->
    </div>
  </main>

  <!-- Bottom Navigation Controls (Thumb Friendly) -->
  <footer class="bottom-nav">
    <button class="btn-nav-action" id="prevBtn" onclick="prevUnit()">
      <span>◀</span>
      <span class="nav-label-text">前のUNIT</span>
    </button>

    <!-- Prominent Bottom Mask Toggle Button -->
    <button class="btn-nav-mask" id="bottomMaskBtn" onclick="toggleMaskMode()" title="暗記テスト切替 (英語を隠す/表示)">
      <span id="bottomMaskIcon">🙈</span>
      <span id="bottomMaskText">暗記テスト</span>
    </button>

    <div class="page-indicator-badge" id="pageIndicator">
      UNIT 1 / 90
    </div>

    <button class="btn-nav-action" id="nextBtn" onclick="nextUnit()">
      <span class="nav-label-text">次のUNIT</span>
      <span>▶</span>
    </button>
  </footer>

  <script>
    const unitsData = ''' + json.dumps(units_data, ensure_ascii=False) + ''';

    let currentUnitIndex = 0;
    let isMasked = false;
    let isFitMode = true; // Default: Screen Fit with Zero Scroll
    let viewMode = 'typeset'; // 'typeset' | 'scan'
    const themes = ["sepia", "white", "dark"];
    let themeIndex = 0;
    let isPlayingAll = false;

    function getStoredProgress() {
      try {
        return JSON.parse(localStorage.getItem('english_study_progress_v2') || '{}');
      } catch (e) {
        return {};
      }
    }

    function saveProgress(unitNum, itemNum, checkIndex, isChecked) {
      const prog = getStoredProgress();
      const key = `${unitNum}_${itemNum}_${checkIndex}`;
      prog[key] = isChecked;
      localStorage.setItem('english_study_progress_v2', JSON.stringify(prog));
    }

    // Populate dropdown
    const unitSelect = document.getElementById('unitSelect');
    unitsData.forEach((u, idx) => {
      const opt = document.createElement('option');
      opt.value = idx;
      opt.textContent = `UNIT ${u.unit} : ${u.title}`;
      unitSelect.appendChild(opt);
    });

    function renderUnit(index) {
      currentUnitIndex = index;
      const u = unitsData[index];
      unitSelect.value = index;

      document.getElementById('pageIndicator').textContent = `UNIT ${u.unit} / 90 (${u.book_pages})`;
      document.getElementById('prevBtn').disabled = (index === 0);
      document.getElementById('nextBtn').disabled = (index === unitsData.length - 1);

      const container = document.getElementById('mainContainer');

      if (viewMode === 'scan') {
        container.innerHTML = `
          <div class="scan-view-stage">
            <img class="scan-view-img" src="${u.scan_image}" alt="UNIT ${u.unit} 原本スキャン" onclick="nextUnit()" title="クリックで次のUNITへ">
          </div>
        `;
        return;
      }

      // Render Synchronized CSS Grid
      const progress = getStoredProgress();
      const leftPageNum = u.book_pages.split('-')[0].replace(/[^0-9]/g, '') || '';
      const rightPageNum = u.book_pages.split('-')[1] ? u.book_pages.split('-')[1].replace(/[^0-9]/g, '') : '';

      let rowsHtml = '';

      // Row 1: Headers
      rowsHtml += `
        <!-- Left Header (col 1, row 1) -->
        <div class="header-left left-col-item">
          <div>
            <div class="unit-meta-bar">
              <span class="unit-badge-pill">UNIT ${u.unit}</span>
              <span class="chapter-tag">${u.chapter}</span>
            </div>
            <h1 class="unit-main-title">${u.title}</h1>
          </div>
          <div class="mascot-intro-box">
            <span class="mascot-icon">💡</span>
            <div>${u.intro}</div>
          </div>
        </div>

        <!-- Center Spine (spanning rows 1 to 11) -->
        <div class="book-spine-divider"></div>

        <!-- Right Header (col 3, row 1) -->
        <div class="header-right right-col-item">
          <div class="cd-track-bar">
            <span class="cd-pill">💿 ${u.cd_info}</span>
            <span class="repetition-header-badge">5段階 反復トレーニング</span>
          </div>
          <div class="key-box-card">
            <div class="key-box-title">🗝️ ${u.key_title || '英会話のカギ'}</div>
            <div>${u.key_content}</div>
          </div>
        </div>
      `;

      // Rows 2 to 10: Items 1 to 9 in horizontal lockstep
      u.items.forEach((it, idx) => {
        const gridRow = idx + 2;
        const escapedEn = (it.en || '').replace(/'/g, "\\\\'");

        // Left Checkboxes
        let checksHtml = '';
        for (let c = 1; c <= 5; c++) {
          const key = `${u.unit}_${it.num}_${c}`;
          const checked = progress[key] ? 'checked' : '';
          checksHtml += `<input type="checkbox" class="check-box-input" title="第${c}回チェック" ${checked} onclick="event.stopPropagation()" onchange="saveProgress(${u.unit}, ${it.num}, ${c}, this.checked)">`;
        }

        rowsHtml += `
          <!-- Left Item ${it.num} (col 1, row ${gridRow}) -->
          <div class="left-col-item" style="grid-row: ${gridRow};">
            <div class="item-card left-card" onclick="revealCardFromLeft(this)">
              <div class="item-header-row">
                <div class="item-num-badge">${it.num}</div>
                <div class="item-text-area">
                  <div class="japanese-sentence">${it.ja}</div>
                  <div class="hint-note-row">
                    ${it.hint ? `<span class="hint-tag">🔑 ${it.hint}</span>` : ''}
                    ${it.notes ? `<span class="note-text">${it.notes}</span>` : ''}
                  </div>
                </div>
              </div>
              <div class="checks-row">
                <span>Check:</span>
                ${checksHtml}
              </div>
            </div>
          </div>

          <!-- Right Item ${it.num} (col 3, row ${gridRow}) -->
          <div class="right-col-item" style="grid-row: ${gridRow};">
            <div class="item-card right-card" onclick="revealCard(this)">
              <div class="item-header-row">
                <div class="item-num-badge">${it.num}</div>
                <div class="item-text-area">
                  <div class="english-top-row">
                    <div class="english-sentence">${it.en}</div>
                    <button class="btn-speak" onclick="event.stopPropagation(); speakPhrase('${escapedEn}')" title="音声を聞く (Web Speech API)">🔊</button>
                  </div>
                  ${it.pron ? `<div class="pronunciation-tag">[${it.pron}]</div>` : ''}
                  ${it.exp ? `<div class="explanation-callout">${it.exp}</div>` : ''}
                </div>
              </div>
            </div>
          </div>
        `;
      });

      // Row 11: Footers
      rowsHtml += `
        <!-- Left Footer (col 1, row 11) -->
        <div class="footer-left left-col-item">
          <span>p. ${leftPageNum}</span>
        </div>

        <!-- Right Footer (col 3, row 11) -->
        <div class="footer-right right-col-item">
          <span>p. ${rightPageNum}</span>
        </div>
      `;

      container.innerHTML = `
        <div class="book-spread-grid ${isMasked ? 'masked' : ''}" id="bookSpreadGrid">
          ${rowsHtml}
        </div>
      `;

      if (window.innerWidth <= 860) {
        window.scrollTo({ top: 0, behavior: 'instant' });
      }

      adjustFitScreenScale();
    }

    function adjustFitScreenScale() {
      const grid = document.getElementById('bookSpreadGrid');
      if (!grid || !isFitMode || viewMode === 'scan' || window.innerWidth <= 860) {
        if (grid) grid.style.transform = 'none';
        return;
      }

      // Compute exact available space between headers
      const topH = 48;
      const botH = 48;
      const availW = window.innerWidth - 32;
      const availH = window.innerHeight - topH - botH - 16;

      grid.style.transform = 'none';
      const natW = grid.offsetWidth;
      const natH = grid.offsetHeight;

      const scaleW = availW / natW;
      const scaleH = availH / natH;
      const scale = Math.min(scaleW, scaleH);

      if (scale < 0.98) {
        grid.style.transform = `scale(${scale})`;
        grid.style.transformOrigin = 'center center';
      } else {
        grid.style.transform = 'none';
      }
    }

    window.addEventListener('resize', () => {
      adjustFitScreenScale();
    });

    function toggleFitScreen() {
      isFitMode = !isFitMode;
      const btn = document.getElementById('fitScreenBtn');
      const text = document.getElementById('fitScreenText');
      if (isFitMode) {
        document.body.classList.remove('scroll-mode');
        btn.classList.add('active');
        text.textContent = '全画面フィット';
      } else {
        document.body.classList.add('scroll-mode');
        btn.classList.remove('active');
        text.textContent = 'スクロール表示';
      }
      renderUnit(currentUnitIndex);
    }

    function revealCard(card) {
      if (isMasked) {
        card.classList.toggle('revealed');
      }
    }

    function revealCardFromLeft(leftCard) {
      if (!isMasked || window.innerWidth > 860) return;
      const leftCol = leftCard.closest('.left-col-item');
      if (leftCol) {
        const rightCol = leftCol.nextElementSibling;
        if (rightCol) {
          const rightCard = rightCol.querySelector('.right-card');
          if (rightCard) {
            rightCard.classList.toggle('revealed');
          }
        }
      }
    }

    function goToUnit(idx) {
      if (idx >= 0 && idx < unitsData.length) {
        renderUnit(idx);
      }
    }

    function prevUnit() {
      if (currentUnitIndex > 0) goToUnit(currentUnitIndex - 1);
    }

    function nextUnit() {
      if (currentUnitIndex < unitsData.length - 1) goToUnit(currentUnitIndex + 1);
    }

    function toggleViewMode() {
      viewMode = (viewMode === 'typeset') ? 'scan' : 'typeset';
      const icon = document.getElementById('viewModeIcon');
      const text = document.getElementById('viewModeText');
      if (viewMode === 'scan') {
        icon.textContent = '📖';
        text.textContent = '組版表示';
      } else {
        icon.textContent = '🖼️';
        text.textContent = '原本スキャン';
      }
      renderUnit(currentUnitIndex);
    }

    function toggleMaskMode() {
      isMasked = !isMasked;

      // Update Top Button
      const topBtn = document.getElementById('maskToggleBtn');
      const topBtnText = document.getElementById('maskBtnText');
      if (topBtn && topBtnText) {
        if (isMasked) {
          topBtn.classList.add('active');
          topBtnText.textContent = '暗記中 (タップ開示)';
        } else {
          topBtn.classList.remove('active');
          topBtnText.textContent = '暗記テスト';
        }
      }

      // Update Bottom Button
      const botBtn = document.getElementById('bottomMaskBtn');
      const botBtnText = document.getElementById('bottomMaskText');
      if (botBtn && botBtnText) {
        if (isMasked) {
          botBtn.classList.add('active');
          botBtnText.textContent = '暗記中 (ON)';
        } else {
          botBtn.classList.remove('active');
          botBtnText.textContent = '暗記テスト';
        }
      }

      renderUnit(currentUnitIndex);
    }

    function speakPhrase(phrase, onEnd) {
      if (!('speechSynthesis' in window)) return;
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(phrase);
      utterance.lang = 'en-US';
      utterance.rate = 0.92;
      if (onEnd) utterance.onend = onEnd;
      window.speechSynthesis.speak(utterance);
    }

    function playAllPhrases() {
      if (!('speechSynthesis' in window)) return;
      const btn = document.getElementById('playAllBtn');
      if (isPlayingAll) {
        window.speechSynthesis.cancel();
        isPlayingAll = false;
        btn.classList.remove('active');
        btn.querySelector('span:last-child').textContent = '連続再生';
        return;
      }

      isPlayingAll = true;
      btn.classList.add('active');
      btn.querySelector('span:last-child').textContent = '停止';

      const items = unitsData[currentUnitIndex].items;
      let currentIndex = 0;

      function speakNext() {
        if (!isPlayingAll || currentIndex >= items.length) {
          isPlayingAll = false;
          btn.classList.remove('active');
          btn.querySelector('span:last-child').textContent = '連続再生';
          return;
        }
        const phrase = items[currentIndex].en;
        currentIndex++;
        speakPhrase(phrase, () => {
          setTimeout(speakNext, 700);
        });
      }

      speakNext();
    }

    function cycleTheme() {
      themeIndex = (themeIndex + 1) % themes.length;
      const theme = themes[themeIndex];
      document.body.setAttribute('data-theme', theme);
      const icon = document.getElementById('themeIcon');
      const text = document.getElementById('themeText');
      if (theme === 'sepia') {
        icon.textContent = '📜';
        text.textContent = '生成り紙';
      } else if (theme === 'white') {
        icon.textContent = '☀️';
        text.textContent = 'ホワイト';
      } else {
        icon.textContent = '🌙';
        text.textContent = 'ダーク';
      }
    }

    window.addEventListener('keydown', (e) => {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT') return;
      if (e.key === 'ArrowLeft') prevUnit();
      else if (e.key === 'ArrowRight') nextUnit();
      else if (e.key === ' ') {
        e.preventDefault();
        playAllPhrases();
      }
    });

    // Touch swipe navigation for mobile
    let touchStartX = 0;
    let touchStartY = 0;
    let touchEndX = 0;
    let touchEndY = 0;

    document.addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].clientX;
      touchStartY = e.changedTouches[0].clientY;
    }, { passive: true });

    document.addEventListener('touchend', (e) => {
      touchEndX = e.changedTouches[0].clientX;
      touchEndY = e.changedTouches[0].clientY;
      handleSwipe();
    }, { passive: true });

    function handleSwipe() {
      const activeEl = document.activeElement;
      if (activeEl && (activeEl.tagName === 'INPUT' || activeEl.tagName === 'SELECT')) {
        return;
      }
      const diffX = touchEndX - touchStartX;
      const diffY = touchEndY - touchStartY;
      if (Math.abs(diffX) >= 60 && Math.abs(diffX) > Math.abs(diffY) * 1.6) {
        if (diffX < 0) {
          nextUnit();
          showMobileToast('次のUNITへ 👉');
        } else {
          prevUnit();
          showMobileToast('👈 前のUNITへ');
        }
      }
    }

    function showMobileToast(msg) {
      let toast = document.getElementById('mobileToast');
      if (!toast) {
        toast = document.createElement('div');
        toast.id = 'mobileToast';
        toast.style.position = 'fixed';
        toast.style.bottom = '65px';
        toast.style.left = '50%';
        toast.style.transform = 'translateX(-50%)';
        toast.style.background = 'rgba(18, 22, 33, 0.9)';
        toast.style.color = '#fff';
        toast.style.padding = '6px 14px';
        toast.style.borderRadius = '20px';
        toast.style.fontSize = '0.8rem';
        toast.style.fontWeight = '700';
        toast.style.zIndex = '9999';
        toast.style.pointerEvents = 'none';
        toast.style.boxShadow = '0 4px 12px rgba(0,0,0,0.3)';
        toast.style.transition = 'opacity 0.25s ease';
        document.body.appendChild(toast);
      }
      toast.textContent = msg;
      toast.style.opacity = '1';
      clearTimeout(toast.timer);
      toast.timer = setTimeout(() => {
        toast.style.opacity = '0';
      }, 1000);
    }

    function handleSearch(query) {
      query = query.trim().toLowerCase();
      if (!query) {
        renderUnit(currentUnitIndex);
        return;
      }

      const matches = [];
      unitsData.forEach((u, uIdx) => {
        u.items.forEach(it => {
          if ((it.ja && it.ja.toLowerCase().includes(query)) || 
              (it.en && it.en.toLowerCase().includes(query)) || 
              (it.hint && it.hint.toLowerCase().includes(query)) ||
              (it.exp && it.exp.toLowerCase().includes(query)) ||
              (u.title && u.title.toLowerCase().includes(query))) {
            matches.push({ unit: u, item: it, unitIndex: uIdx });
          }
        });
      });

      const container = document.getElementById('mainContainer');
      if (matches.length === 0) {
        container.innerHTML = `
          <div style="padding: 40px; text-align: center; color: var(--text-muted); background: var(--paper-bg); border-radius: 10px; width: 100%; max-width: 800px; box-shadow: var(--shadow-book);">
            <h2>🔍 該当するフレーズが見つかりませんでした</h2>
            <p style="margin-top: 8px;">別のキーワードで検索してみてください。</p>
          </div>
        `;
        return;
      }

      let resultsHtml = `
        <div style="background: var(--paper-bg); border-radius: 10px; padding: 20px 24px; width: 100%; max-width: 1000px; max-height: calc(100vh - 120px); overflow-y: auto; box-shadow: var(--shadow-book);">
          <h2 style="font-family: 'Noto Serif JP', serif; margin-bottom: 14px; font-size: 1.2rem; color: var(--accent-red);">
            🔍 「${query}」の検索結果: ${matches.length} 件
          </h2>
          <div style="display: flex; flex-direction: column; gap: 8px;">
      `;

      matches.forEach(m => {
        const escapedEn = (m.item.en || '').replace(/'/g, "\\\\'");
        resultsHtml += `
          <div class="item-card" style="cursor: pointer; padding: 8px 12px;" onclick="goToUnit(${m.unitIndex})">
            <div style="font-size: 0.78rem; font-weight: 800; color: var(--accent-red); margin-bottom: 3px;">
              UNIT ${m.unit.unit} : ${m.unit.title} (問 ${m.item.num}) ➔ クリックで移動
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; gap: 12px;">
              <div>
                <div class="japanese-sentence" style="font-size: 0.95rem; margin-bottom: 2px;">${m.item.ja}</div>
                <div class="english-sentence" style="font-size: 0.98rem; color: var(--accent-blue);">${m.item.en}</div>
              </div>
              <button class="btn-speak" onclick="event.stopPropagation(); speakPhrase('${escapedEn}')">🔊</button>
            </div>
          </div>
        `;
      });

      resultsHtml += `</div></div>`;
      container.innerHTML = resultsHtml;
    }

    renderUnit(0);
  </script>
</body>
</html>
'''

# Write to target 1: scratch/book_project/index.html
target_1 = r'C:\Users\mm\.gemini\antigravity\scratch\book_project\index.html'
with open(target_1, 'w', encoding='utf-8') as f:
    f.write(html_template)
print(f'Wrote {target_1} ({os.path.getsize(target_1)/1024:.1f} KB)')

# Write to target 2: scratch/pdf_merge_ocr/index.html
target_2 = r'C:\Users\mm\.gemini\antigravity\scratch\pdf_merge_ocr\index.html'
with open(target_2, 'w', encoding='utf-8') as f:
    f.write(html_template)
print(f'Wrote {target_2} ({os.path.getsize(target_2)/1024:.1f} KB)')

# Write to target 3: scratch/shunji-eikaiwa/index.html
target_3 = r'C:\Users\mm\.gemini\antigravity\scratch\shunji-eikaiwa\index.html'
with open(target_3, 'w', encoding='utf-8') as f:
    f.write(html_template)
print(f'Wrote {target_3} ({os.path.getsize(target_3)/1024:.1f} KB)')
