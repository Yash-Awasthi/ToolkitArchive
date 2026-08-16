# ToolkitArchive — status and next steps

## What this repo actually is

A set of hand-maintained markdown tables (frontend/backend/models/agents/free-access/credits)
plus one generated-charts pipeline (`data/models.json` -> `charts/gen_charts.py` -> `charts/*.png`)
and one on-demand link-check script (`scripts/link_check.py`). There is no application code and
no tests. "Feature work" here means tooling that keeps the tables honest, not product features.

## Done this pass (Aug 16, 2026)

- **README model count fixed.** "31 API models" corrected to "32", matching
  `len(data/models.json.models)`, plus a standing note in README telling future editors to update
  that number whenever an entry is added or removed.
- **CREDITS.md Part 6 (provider trust status) cross-linked from README's Map table**, so a reader
  starting from "Get it free" finds it, not just the two rows in FREE-ACCESS.md that originally
  prompted it.
- **The trust-tier rule (Clean / Caveat / Unverified / Kept out) run across FREE-ACCESS.md,
  BACKEND.md, and AGENTS.md**, not just the two rows it started on. This surfaced and fixed real
  errors, not just labels: GLM-5.2's API price was off by 10x ($0.14/$0.28 -> $1.40/$4.40), Grok
  4.3 and Grok Build 0.1 both had a stale 128K context figure (corrected to 1M and 256K per
  docs.x.ai), GPT-5.6 Sol's context was corrected from 1.5M to the vendor-stated 1.05M, Northflank's
  free sandbox was corrected from "2 DBs" to "1 DB", and the "Gemini CLI retired June 18 ->
  Antigravity" claim — which had no source beyond an aggregator — was removed everywhere it
  appeared (README, AGENTS.md, CREDITS.md, MODELS.md) and replaced with what's actually confirmed
  (repo live, Apache 2.0, free tier).
- **Newly-shipped models added as text-only rows** in MODELS.md Table 1 where existence was
  confirmed on a vendor page but price and SWE-bench were not yet published: Claude Opus 5, Claude
  Sonnet 5, Kimi K3 (moved out of the Upcoming table now that it's live), Grok 4.5, Grok 4.6, and
  three new Z.AI ids (GLM-5, GLM-5-Turbo, GLM-5.3). They stay out of `data/models.json` and the
  charts on purpose — the chart pipeline plots price and SWE-bench, and these have neither yet.
- **`scripts/link_check.py` added** — plain `requests.head()` (falling back to `get()` on
  4xx/5xx) over every URL pulled out of every markdown file, threaded, no framework. It was run
  this pass and its findings are what drove several of the fixes above (e.g. the dead
  `cheahjs/free-llm-api-resources` and `Yash-Awasthi/Claude-skill` links, both since removed).
- **`charts/gen_charts.py` now raises on an unmapped company color** instead of silently falling
  back to gray — a new company in `data/models.json` will now fail the chart build loudly instead
  of rendering wrong.
- **Charts regenerated** from the current `data/models.json` (`python charts/gen_charts.py`) —
  the six PNGs in `charts/` reflect the corrected numbers above (GPT-5.6 Sol context, Grok 4.3
  context, GLM-5.2 price).
- **README rewritten to describe the current archive**: verification banner moved to Aug 16 2026,
  a new "Keeping This Archive Honest" section explains the four trust tiers in plain terms and
  documents how to run the link-check script.

## What's still open

- **`data/trust.json` not built.** The Clean/Caveat/Unverified/Kept-out lists still live only as
  markdown prose in CREDITS.md Part 6 — no machine-readable registry that FREE-ACCESS.md,
  BACKEND.md, etc. could all check against. Deliberately deferred again this pass: three markdown
  sections still don't justify a data pipeline. Revisit only if keeping tables in sync becomes a
  recurring manual pain.
- **The trust-tier pass did not reach FRONTEND.md or MEDIA.md.** Both still carry only the
  original "~June 2026" verification claim and were not touched this pass — they're now the
  oldest unverified content in the archive.
- **Freshness banners are inconsistent across files.** CREDITS.md, FREE-ACCESS.md, and BACKEND.md
  now say "Re-checked Aug 16, 2026 (prior pass: June 27, 2026)". MODELS.md, AGENTS.md, and
  REFERENCES.md received real corrections this pass (listed above) but their headers still just
  say "(June 2026)" with no re-check date. SKILLS.md's banner still says "Verified June 27, 2026"
  despite a dead-link fix this pass. A reader comparing banners across files would get a
  misleading picture of which files were actually touched.
- **First real run of `scripts/link_check.py` this pass surfaced findings that were not acted
  on**, since fixing them was outside this pass's scope:
  - REFERENCES.md: `github.com/Mozilla-Ocho/llamafile` redirects to `github.com/mozilla-ai/llamafile`
    — the doc text says "the exact new org wasn't confirmed"; the link check now confirms it. Not
    updated this pass.
  - SKILLS.md: two links resolve to a different final URL than what's written
    (`sickn33/antigravity-awesome-skills` -> `sickn33/agentic-awesome-skills`;
    `platform.claude.com/.../agent-skills` -> `.../agent-skills/overview`) — working, but worth
    pointing at the live URL directly.
  - FREE-ACCESS.md: `api.tokenlb.net/v1` returns 401 — consistent with, and already documented by,
    the Caveat/Unverified entries added for TokenLB this pass; no new action needed there.
  - AGENTS.md: the Vercel and Railway API sample endpoints return 400/403 — expected, they're
    authless example curl calls in a code block, not broken documentation links; the script has
    no way to tell the two cases apart, so this is noise to filter by eye each run, not a bug in
    the docs.
  - REFERENCES.md: a Hacker News link (429, rate-limited) and a businesswire.com link (read
    timeout) — both likely transient; re-run before concluding either is actually dead.
- **`scripts/link_check.py` is on-demand only**, per its original design — nothing runs it in CI
  or on a schedule. That's intentional for a repo with no CI at all; automating it wasn't asked
  for and would add a place for the run to happen. Revisit only if stale links become a recurring
  complaint instead of an occasional manual check.

## Note on style

The task asked for the caveman chat style to be used everywhere, including in this file. Global
instructions restrict that style to conversation only — anything written to disk, this file
included, stays in normal prose, with commit messages as the one documented exception. Say so
explicitly if that global rule should be relaxed for this repo.
