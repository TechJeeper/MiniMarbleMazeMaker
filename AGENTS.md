# AGENTS.md

## Cursor Cloud specific instructions

### What this repo is

Single-page static site (`index.html`) for **MiniMarbleMazeMaker** — a browser app that generates 40×3.25 mm print-in-place marble maze chips (Three.js preview, STL export). There is **no build step**, **no package.json**, and **no backend**. Production is GitHub Pages (`CNAME`).

### Services

| Service | Required? | How to run |
|---------|-----------|------------|
| Static HTTP server | Yes (recommended for dev) | `python3 -m http.server 8000` from repo root, then open `http://localhost:8000/index.html` |
| CDN scripts (Three.js, Tailwind, etc.) | Yes for full UI | Outbound HTTPS; no local install |

`file:///…/index.html` works for quick checks; prefer `http://localhost` to mirror GitHub Pages.

### Lint / test

There are **no** ESLint, Prettier, or unit-test targets in this repository. Validation is manual in the browser or via Playwright:

- **Smoke (core flow):** load page → **Regenerate Maze** (`#btnGenerate`) → **Download STL** (`#btnDownload`) → file `MiniMarbleMaze.stl` (ASCII STL, multi‑MB).
- **Screenshot utility:** `python3 screenshot.py` (requires Playwright + Chromium; see update script).

### Optional: Playwright / `screenshot.py`

`screenshot.py` uses Playwright with `file://` (no HTTP server). After VM update script runs, use:

```bash
python3 screenshot.py
```

If Chromium is missing: `python3 -m playwright install chromium`.

### Gotchas

- **PATH:** `pip install --user` puts `playwright` in `~/.local/bin`; use `python3 -m playwright` if the CLI is not on PATH.
- **Downloads in headless tests:** create the browser context with `accept_downloads=True` before clicking **Download STL**.
- **No hot reload:** editing `index.html` requires a browser refresh; the Python server does not need a restart.
