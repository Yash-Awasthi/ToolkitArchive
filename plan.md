# ToolkitArchive — status and next steps

## What this repo actually is

A set of hand-maintained markdown tables (frontend/backend/models/agents/free-access/credits)
plus one generated-charts pipeline (`data/models.json` -> `charts/gen_charts.py` -> `charts/*.png`).
There is no application code and no tests. "Feature work" here means tooling that keeps the
tables honest, not product features.

## What's broken

- **No automated verification behind the "Verified June 2026" badge in README.md.** The badge
  and the per-file freshness claims are asserted by hand. Nothing checks that a listed URL still
  resolves, still offers the claimed free tier, or hasn't changed pricing.
- **README.md says "31 API models"; `data/models.json` currently has 32 entries** in the `models`
  array. The count in the map table is stale relative to the data file it's supposed to summarize.
- **The new CREDITS.md "Part 6 — Provider Trust Status" section is linked from only one place**
  (the two flagged rows in FREE-ACCESS.md Table 1B). Nothing else in the archive points a reader
  at it, so a reader working from AGENTS.md, FRONTEND.md, or BACKEND.md would not know the section
  exists.

## What's half-built

- **The trust-tier rule (clean / caveat / unverified / kept-out) is applied to exactly the two
  rows that prompted it** (AgentRouter, Bluesminds in FREE-ACCESS.md Table 1B). The same rule
  has not been run against the rest of FREE-ACCESS.md, BACKEND.md, or AGENTS.md, so other
  unverified-but-plain entries likely still exist elsewhere in the archive. This was a deliberate
  scope cut on the prior pass, not an oversight, but it means the rule is not yet enforced
  archive-wide.
- **"Unverified" and "kept-out" are prose sections, not data.** They live only as markdown lists
  in CREDITS.md. There's no machine-readable registry (e.g. a `data/trust.json` keyed by domain)
  that FREE-ACCESS.md, BACKEND.md, etc. could all check against, so keeping every table in sync
  with a trust-status change is a manual grep-and-edit exercise per file.
- **`charts/gen_charts.py` has a hardcoded `COLORS` map keyed by company name.** It currently
  covers every company in `data/models.json`, but nothing enforces that — a new company added to
  the JSON silently falls back to the gray `#999999` default color instead of failing loudly.

## Concrete next steps, in order of payoff

1. **Fix the README model count** (31 -> 32, or recompute from `len(data/models.json.models)`
   at doc-review time). One-line fix, catches a class of drift that will recur every time the
   JSON changes.
2. **Cross-link Part 6 from README.md's Map table** so "Get it free" points at the trust-status
   section, not just at the two tables it currently qualifies.
3. **Run the trust-tier pass over the rest of FREE-ACCESS.md, BACKEND.md, and AGENTS.md** using
   the same four-tier rule now documented in CREDITS.md Part 6, so "clean / caveat / unverified /
   kept-out" is enforced consistently instead of only where a specific complaint triggered it.
4. **Add a link-check script** (plain `requests.head()` loop over every URL column, no framework)
   that runs on demand and reports dead or redirected domains — the cheapest way to make the
   "Verified" badges actually mean something, given the archive already ships one Python script
   for charts.
5. **Only if the manual grep-and-edit cost becomes painful**, promote the trust-status lists in
   CREDITS.md Part 6 into `data/trust.json` and have the tables reference it. Not worth doing
   ahead of need — three markdown sections don't justify a data pipeline yet.

## Note on style

The task asked for the caveman chat style to be used everywhere, including in this file. Global
instructions restrict that style to conversation only — anything written to disk, this file
included, stays in normal prose, with commit messages as the one documented exception. Say so
explicitly if that global rule should be relaxed for this repo.
