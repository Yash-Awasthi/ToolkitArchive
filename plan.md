# ToolkitArchive — status and next steps

## What this repo is

A set of hand-maintained markdown tables (frontend / backend / models / agents /
free-access / credits / media / skills / references) plus one generated-charts
pipeline (`data/models.json` + `data/extra_charts.json` → `charts/gen_charts.py`
→ `charts/*.png`) and one on-demand link-check script (`scripts/link_check.py`).
There is no application code and no tests. "Feature work" here means tooling that
keeps the tables honest, not product features.

## Status — 17 Aug 2026

All work through 17 Aug 2026 is **committed and pushed** on the single branch
`main` (in sync with `origin/main`). The day's passes: August free-AI wave
(OmniRoute, aerolink, NaraRouter, LongCat-2.0, OrcaRouter, findaicredits),
models/benchmarks refresh (DeepSeek V4 Pro GA + peak/off-peak pricing, Qwen
3.8-Max, Gemini 3.7 Flash, Grok 4.6, GLM-5.3 + ZCode, Muse Code, MCP 2.0 spec),
full fact-check overhaul (Gemini 3.7 caveat cleared, stale prices killed,
Terminus-2 clarified, dead links removed), plus: Codex for Students, Anthropic
AI-for-Science grants, AMD GPU credits, Imagen shutdown (Aug 17) → Gemini 3.1
Flash Image, aerolink multi-account warning, and the reorganisation pass (TOCs +
freshness ledger).

Historical per-pass logs were trimmed from this file in that cleanup — they live
in git history if ever needed.

## Freshness ledger (17 Aug 2026 — mirrored in README Map)

- ✅ Fully re-checked 17 Aug: `MODELS.md`, `FREE-ACCESS.md`, `AGENTS.md` (Parts
  1–5, 5A, 11), `REFERENCES.md`, `CREDITS.md` Part 6.
- ⏳ June-2026 content (honestly labelled, refresh when time allows):
  - `FRONTEND.md` Parts 1.5–5 (Part 1 full-stack builders ✅ 17 Aug)
  - `MEDIA.md` Parts 2–4 (Part 1 image-gen ✅ 17 Aug — Imagen shutdown)
  - `BACKEND.md` (except Part 1A + a few rows), `SKILLS.md` (link fixes only),
    `CREDITS.md` Parts 1–5 (new rows added 17 Aug but bulk is June-era)

## What's still open

### Please-verify list (could not independently confirm this pass)

- Disputed numbers flagged in-file: **Grok Build 0.1 price** ($5/$25 vs $1/$2),
  **Grok 4.5 exact release date** (Jul 8 vs Jul 16), **Codex IDE free-tier
  limits**, **Qoder 1.0 pricing details**, **NaraRouter 5M vs 7M tokens/day**,
  **aerolink.lat exact weekly credit** (community-reported only).
- **CREDITS.md Part 6 "Clean" list** (marked Clean by an earlier pass, not
  re-verified since): Arena.ai, Genspark, Hix.ai, Deepgram, Ninjachat.ai,
  Zenmux.ai, Studentoffers.co, Kimi K2, GLM 5.3, DeepSeek Harness, Blaxel, E2B,
  Modal, Vercel, Northflank, Comet.com, Dokie.ai, Mwm.ai, Architecto.dev,
  Framer.com, RelevanceAI.com, Manus.im, Magnific.com, Pomelli, Opal.
- All June-era free-tier/price rows in `MEDIA.md` (image/TTS/LLMOps), `FRONTEND.md`
  Parts 1.5–5, `BACKEND.md`, `SKILLS.md` (star counts incl. gstack ~117K★),
  `CREDITS.md` Parts 1–5, `AGENTS.md` Parts 6–14.

### Tooling

- **`data/trust.json` not built** — the Clean/Caveat/Unverified/Kept-out lists
  live only as markdown in `CREDITS.md` Part 6. Deliberately deferred; revisit
  only if keeping tables in sync becomes a recurring manual pain.
- **`scripts/link_check.py` is on-demand only** (no CI, by design). Revisit if
  stale links become a recurring complaint.
- **Known link-check noise (expected, not bugs):** `api.tokenlb.net/v1` 401,
  `api.tokenrouter.com` 404 (authless examples), Vercel/Railway sample curls
  400/403 (authless code examples), a HN 429 + businesswire timeout (transient).

## How to run the tooling

```bash
python charts/gen_charts.py    # regenerate all 10 charts from the JSON data files
python scripts/link_check.py   # HEAD/GET every markdown URL, report dead links
```

## Note on style

The task asked for the caveman chat style to be used everywhere, including in this
file. Global instructions restrict that style to conversation only — anything
written to disk, this file included, stays in normal prose, with commit messages
as the one documented exception.
