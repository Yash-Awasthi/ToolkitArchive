# ToolkitArchive — status and next steps

## Second refresh pass — target date: 17 August 2026 (user-requested follow-up)

User asked to bring the archive fully up to date to 17 August 2026: add the named free-AI sources
(aerolink.lat, omniroute, tokenrouter, agentrouter, bluesminds), sweep Reddit/Discord/Instagram for
the weekly wave of new free AIs, and redo benchmarks where the numbers changed. Plan:

1. **Verify the named sites** (all five) against live pages + independent secondary sources; keep
   each in the correct trust tier. Done: aerolink.lat (live credit-gateway, site blocks bots —
   verified via community + secondary sources), omniroute (verified live, MIT self-hosted gateway),
   tokenrouter (live unified gateway, JS-rendered site — existing caveat stands), agentrouter
   (confirmed Oct-2025 non-profit gateway), bluesminds (confirmed GitHub-login credits gateway).
2. **Social sweep (Reddit/Instagram/Discord-adjacent):** community gist updated 11 Aug 2026 and
   Instagram reels surfaced the August wave — OmniRoute, NaraRouter (5-7M tok/day), LongCat-2.0
   free quotas, GoRouter, Tokeness, OpenRouter Fusion. Each was cross-checked against a live page
   before being added; social-only numbers stay labelled as community-reported.
3. **Model/benchmark refresh:** DeepSeek V4 Pro GA (13 Aug, TB 2.1 87.9 via own harness, new
   peak/off-peak pricing effective 16 Aug), DeepSeek V4 Flash official (31 Jul, TB 2.1 82.7),
   Qwen 3.8-Max (2 Aug, $2/$6, open weights 12 Aug), Gemini 3.7 Flash (13 Aug, $0.75/$3.75),
   Grok 4.6 (12 Aug, $2/$6) + xAI→SpaceXAI rebrand, Claude Sonnet 5 ($2/$10 permanent 10 Aug)
   and Opus 5 ($5/$25, 24 Jul), GPT-5.6 GA (9 Jul), Gemini 3.5 Pro still unreleased (12 Aug).
4. **Charts:** DeepSeek price corrections in data/models.json -> regenerate charts. New models
   without confirmed SWE-bench stay as text rows in MODELS.md (charts require both numbers).
5. **Docs:** FREE-ACCESS.md (new providers), AGENTS.md (OmniRoute router + TB 2.1 vendor-note),
   README.md (banner, quick-reference, August developments), MODELS.md (rows, timeline).
6. **Verify:** run scripts/link_check.py; note expected auth-required failures.

### Completed in the second pass (17 Aug 2026)

- **aerolink.lat verified and added** (FREE-ACCESS.md Table 1B, caveat tier). Site blocks bots
  (403), so verification used independent secondary sources: YouTube walkthroughs, a community
  gist updated 11 Aug 2026, and Threads/Instagram posts. Recorded facts: ~$35/week free credits,
  Telegram verification, paid credits ~94% cheaper. Exact credit amounts are community-reported.
- **OmniRoute verified and added** (FREE-ACCESS.md aggregators + AGENTS.md routers). Live site +
  GitHub confirmed: MIT self-hosted gateway, 340 providers (90+ free), ~1.5B free tokens/month
  pooled with a deduped honest dashboard, quota-aware auto-fallback, MCP/A2A, works with Claude
  Code/Codex/Cursor/OpenCode/Cline/Copilot. Security caveat added: CVE-2026-49352 and the fact it
  proxies your keys.
- **AgentRouter and Bluesminds promoted from unverified to caveat.** AgentRouter: confirmed
  launched Oct 2025, non-profit/"public-welfare", GitHub login, OpenAI- and Anthropic-wire
  compatible; credit amounts vary by source ($100/$200 referral vs $150 community gist).
  Bluesminds: confirmed GitHub-login credits gateway; credit amounts conflict ($100 vs 500).
- **August free-AI wave added** from Reddit/Instagram/gist discovery, each cross-checked against a
  live page before inclusion: NaraRouter (router.bynara.id, 5-7M tokens/day), LongCat-2.0 (free
  API quotas, MIT), GoRouter + Tokeness (kept unverified — community-reported only), OpenRouter
  Fusion API noted on the OpenRouter row.
- **Models/benchmarks refreshed.** DeepSeek V4 Pro GA (Aug 13, TB 2.1 87.9 vendor harness) and
  V4 Flash official (Jul 31, 82.7) with new peak/off-peak pricing (effective Aug 16) verified on
  api-docs.deepseek.com — the old flat preview prices in data/models.json were corrected and all
  charts regenerated. Qwen 3.8-Max, Gemini 3.7 Flash, Grok 4.6 added as text rows (price
  confirmed, no public SWE-bench — charts require both, so they stay out of models.json). Claude
  Opus 5 ($5/$25, Jul 24) and Sonnet 5 ($2/$10 permanent Aug 10) prices confirmed. GPT-5.6 GA
  (Jul 9) noted. Gemini 3.5 Pro updated: still not GA as of Aug 12.
- **Social sweep (Reddit/Instagram/Discord-adjacent) outcome:** unlike the Aug 16 pass (which
  found no usable social signals), this pass found a genuine wave on Instagram reels + a
  community gist; everything was cross-checked against primary/live sources and community-only
  numbers are labelled as such in the tables.
- **Link check re-run:** no new dead links; the known expected failures (TokenLB 401, TokenRouter
  bare /v1 404, Vercel/Railway authless examples, businesswire timeout, ollama install.sh
  timeout) are unchanged and documented.

### Open after the second pass

- GoRouter, Tokeness, oxaam.com, resourcify.com, arena.ai, genspark, hix.ai, deepgram,
  api.hcnsec.cn, ninjachat.ai, zenmux.ai remain unverified leads — GoRouter/Tokeness have no
  verifiable live page yet, the others were not re-checked this pass.
- NaraRouter's token counts (5M vs 7M/day) and aerolink's weekly credit amount come from
  community/secondary sources — worth confirming against their dashboards on a future pass.
- The trust-tier prose in CREDITS.md Part 6 was not re-run this pass; the two rows promoted
  (AgentRouter, Bluesminds) and the new rows reflect the tier rule but Part 6's text still lists
  them under their old unverified grouping.

## Active refresh — target date: 17 August 2026

The requested update is a full current-events refresh rather than a narrow edit. It includes the
`ToolkitArchive` leads recorded in `../MASTER_PROMPT.md`, TokenRouter, newly emerging free-AI
offers, and an audit of benchmark claims. Work is intentionally divided by evidence quality:

1. **Source sweep (in progress):** verify official provider, product, GitHub, and benchmark
   sources first; use Reddit, Discord, and Instagram only to discover leads or document community
   reports, never as sole support for prices, access limits, or benchmark scores.
2. **Provider and access update:** add verified routers/free tiers, including TokenRouter if its
   current product and terms can be confirmed; retain questionable providers as caveated or
   unverified instead of recommendations.
3. **Tool, model, and infrastructure update:** revise agent, model, sandbox, frontend, media,
   backend, and reference pages only where the information is current and sourceable.
4. **Benchmark audit:** replace stale figures with an exact benchmark version and source, or mark
   them vendor-reported/estimated. Do not fabricate a new benchmark run: public leaderboards
   cannot be reproduced locally without the original harness, task set, model snapshots, and
   spend budget.
5. **Verification and hand-off:** run the markdown link checker and chart generator where model
   data changes; record unresolved or social-only leads here for the next pass.

### Evidence policy for this refresh

- **Primary:** vendor docs, pricing pages, release notes, official GitHub repositories, benchmark
  operators, and reproducible public leaderboards.
- **Secondary:** reputable reporting that links the primary announcement.
- **Discovery-only:** Reddit, Discord, Instagram, Product Hunt, and similar social posts. These
  can point to a service, but a live official page is required before it is described as verified.
- **Safety:** reverse-engineered subscription proxies and unverified “free API” services remain
  clearly caveated. Claims promising paid-model access for free are never treated as a safe
  recommendation without a transparent, authorised program.

### Completed in this refresh

- **TokenRouter verified and added.** Its current site and docs establish it as a live unified
  gateway with 300+ models and OpenAI/Claude/Gemini compatibility. It is placed in router/access
  documentation as a commercial gateway: “no platform fee” is explicitly distinguished from the
  underlying model charges, and no public free-credit amount is claimed.
- **TB 2.1 benchmark snapshot replaced.** The old Codex 83.4% figure is now 83.1% for
  Codex + GPT-5.5/xhigh. The current leader is Claude Code + Fable 5/xhigh at 83.8% ± 1.2%.
  The table now gives the complete agent/model/effort/date context and explains why a local
  “redo” would be a new, non-comparable submission rather than validation.
- **Free-access correction.** Cerebras is now listed as a $5 signup-credit trial, not an assumed
  permanent 1M-token/day tier. Groq's current model-specific free-plan examples replace the old
  generic quota. DeepSeek V4 pricing and GPT-5.6 Terra/Luna context windows were verified against
  live vendor docs; the model JSON and derived charts were regenerated.
- **Social discovery reviewed.** Recent Reddit discussions were recorded as discovery signals;
  no unambiguous public Discord or Instagram source justified a new factual entry. That outcome
  is deliberately documented instead of padding the archive with unsourced offers.

### Open after this targeted refresh

- The dozens of older product entries in FRONTEND.md, MEDIA.md, BACKEND.md, and SKILLS.md still
  retain their stated June/August verification boundaries. They were not relabelled as newly
  checked merely because this pass updated agent/model/access material.
- Link checking intentionally reports API examples without credentials as failures (Vercel 400,
  Railway 403, TokenLB 401, and TokenRouter's bare base URL 404) and one BusinessWire timeout.
  The API base URLs remain in code examples because they are configuration values, not browseable
  pages. Re-check their authenticated endpoints manually before declaring them unavailable.

## Follow-up pass — 17 Aug 2026 (user: "gemini 3.7 came out too; HF provides dspark deepseek")

- **Gemini 3.7 Flash** was already added as a text row this morning; this pass confirmed it is on
  the **free Google AI Studio tier** (ai.google.dev pricing page) and updated the Google AI Studio
  row + use-case table in FREE-ACCESS.md. No Gemini 3.7 Pro exists; Gemini 3.5 Pro still not GA
  as of Aug 12 — the archive says so.
- **HuggingFace row corrected.** The prior "100K credits/mo" was stale — current official pricing
  is $0.10/mo free credits (free users), $2/mo PRO, $2/seat Team/Enterprise
  (huggingface.co/docs/inference-providers/en/pricing). Row updated to "HF Inference Providers"
  with the 200+ models and no-markup routing.
- **DeepSeek DSpark added.** DSpark = open-source speculative-decoding module attached to the V4
  Pro/Flash checkpoints (DeepSeek-V4-Pro-DSpark / -Flash-DSpark on HF), 50-600% faster, not a new
  model. Added to FREE-ACCESS.md (row + HF row note) and MODELS.md DeepSeek section.
- **Intuitive news digest added** to README: "In plain words — what changed the week of
  Aug 10-17, 2026", covering the model cadence, the free-router wave, tunable DeepSeek thinking,
  and the two watch items.

## "Anything else" sweep — 17 Aug 2026 (user asked for more free AIs/keys + repo honourable mentions)

- **Chinese credit-router wave added** as one compact community-reported table in FREE-ACCESS.md
  Table 1B (all ⚠️ unverified, single source = the almahmudbd gist updated Aug 11): byNara,
  Future PPO, api.hcnsec.cn (the MASTER_PROMPT lead), TabiToken, TokenLayer, AiFamily, Unity2ai,
  yunwu.ai, SwiftRouter (gist itself says "don't buy"), ProRise-Hub, AiWave, vsLLM, B.Ai,
  MonkeyCode-ai (30M tok/day coding tool).
- **Together AI** added to Table 2 trial credits (signup credits unverified + $50K startup
  accelerator per a secondary aggregator). **DeepInfra** added as a caveat row: no standalone free
  tier, small free quota via HF Inference Providers.
- **New honourable-mention repos** added to Useful Repos: open-free-llm-api/awesome-freellmapis
  (updated Aug 14), 12britz/awesome-free-models (verified Aug 7), and the almahmudbd gist itself.

## Full-overhaul / fact-check pass — 17 Aug 2026 (user: "complete it, revise it all, eliminate redundancy & hallucination, fact-check")

### Fixed (verified this pass)
- **Gemini 3.7 Flash hallucination caveat removed.** CREDITS.md Part 6 still called it a
  "likely hallucination" from the Aug 16 pass; it is now verified from primary sources (blog.google,
  DeepMind model card, ai.google.dev pricing) — moved to Clean with a re-verification note.
- **Stale numbers corrected cross-file:** Codex CLI 83.4% → 83.1% (TB 2.1, README);
  Aider+DeepSeek combo $0.87 → $1.98–3.96/M (AGENTS.md BYOK); chat-interface flagships updated
  (Claude.ai → Opus 5/Sonnet 5, ChatGPT → GPT-5.6, Gemini → 3.7 Flash/3.1 Pro, Grok → 4.6);
  xAI trial row (FREE-ACCESS.md) → Grok 4.6/Grok Build; Grok Build 0.1 model price flagged as
  disputed ($5/$25 vs $1/$2); Grok 4.5 date hedged (Jul 8 vs Jul 16); llamafile org confirmed
  (mozilla-ai) and updated in both REFERENCES.md + AGENTS.md Part 10.
- **Missing agents added (verified):** Grok Build (xAI/SpaceXAI, free tier, OSS harness
  xai-org/grok-build), Codex IDE (OpenAI), Qoder (Alibaba, free agentic platform), Qwen Chat row
  (free Qwen 3.8-Max). Terminus 2 clarified as the benchmark's reference agent, NOT a product.
- **Honest freshness labeling:** MEDIA.md + FRONTEND.md now explicitly say they are the oldest
  unverified (June-era) content; SKILLS.md banner updated; AGENTS.md header now says which parts
  were refreshed vs still June-era; README flags free-api-tiers.png as out of sync with tables.

### Could NOT be fact-checked this pass — user should verify
- **CREDITS.md Part 6 "Clean" list items not personally re-verified today** (marked Clean by the
  Aug 16 pass): Arena.ai, Genspark, Hix.ai, Deepgram, Ninjachat.ai, Zenmux.ai, Studentoffers.co,
  Kimi K2, GLM 5.3, DeepSeek Harness, Blaxel, E2B, Modal, Vercel, Northflank, Comet.com, Dokie.ai,
  Mwm.ai, Architecto.dev, Framer.com, RelevanceAI.com, Manus.im, Magnific.com, Pomelli, Opal.
- **All June-era rows** in MEDIA.md (image-gen free tiers, TTS arena scores, LLMOps free tiers,
  Langfuse/Braintrust funding), FRONTEND.md (builder credit plans), BACKEND.md (most free-tier
  numbers), SKILLS.md (skill counts, star counts, builder setups incl. gstack ~117K★), AGENTS.md
  Parts 6–14, CREDITS.md Parts 1–5, and AGENTS.md Part 11 subreddit member counts.
- **Grok Build 0.1 price** ($5/$25 vs $1/$2), **Grok 4.5 exact date** (Jul 8 vs Jul 16),
  **Codex IDE exact free-tier limits**, **Qoder 1.0 pricing details**.

## Follow-up note — 17 Aug 2026 (user-reported aerolink ban warning)

- **aerolink.lat multi-account warning added** to the Table 1B row and the CREDITS.md Part 6
  Unverified bullet: user reports that signing into multiple aerolink accounts from the same
  device triggers a ban and can lose balances; reportedly device-fingerprinted (MAC / device
  model — mechanism unconfirmed). Recommendation recorded: one account per device or Android
  Studio emulator; no signup spam.

## Benchmark revision + additions pass — 17 Aug 2026 (user: "revise all benchmarks, add more, reorganise, mention skills, remove dead github links")

- **Benchmarks revised:** added a vals.ai standardized-harness SWE-bench Verified reference block to
  MODELS.md (GPT-5.6 Sol ~96-97% · DeepSeek V4 Pro 0813 96.4% · Fable 5 95.0% · Kimi K3 93.4% ·
  Luna 93.0% · Opus 4.8 88.6% · Grok 4.5 86.6%) explicitly labelled harness-sensitive ceilings
  and kept OUT of the charts (which stay on official-leaderboard/vendor numbers). SWE-bench Pro
  snapshot added (Mythos 5 80.3% · Fable 5 80.0% · Opus 5 79.2% · Kimi K3 80.0% · Qwen 3.8-Max
  67.7%). Kimi K3, Grok 4.5, DeepSeek V4 Pro, GPT-5.6 Sol rows annotated with the vals figures.
- **Added:** DeepSeek Harness (`dsh`, MIT, open-sourced Aug 14 2026, everything-is-a-plugin) —
  AGENTS.md Part 1 + REFERENCES.md; CodeWhale as emerging (unverified); README "Best CLI agents"
  row; skills cross-ref added to AGENTS.md Part 1 and the README zero-dollar stack.
- **Reorganised:** README gains an "Agentic systems stack (2026 recipe)" table tying IDE → agent →
  skills → MCP → routing → sandbox → benchmarks into one flow. No file moves (links are stable).
- **Dead links:** audited every github.com URL in the docs with live HEAD/GET — only the dead
  `Yash-Awasthi/Claude-skill` remained (in SKILLS.md's removal note); the note was reworded to
  drop the dead URL. The gist "404" is a grep artifact (gist.github.com host) — real URL works.

## ZCode / GLM-5.3 / Zed pass — 17 Aug 2026 (user: "Zed $10 student plan; ZCode gives GLM free; GLM-5.3 free on 17 Aug")

- **GLM-5.3 (Aug 14, 2026) verified from primary sources** (z.ai blog + Interconnects, Aug 14):
  same GLM-5.2 base, gains entirely from extended post-training (~750B, a third of Kimi K3).
  Currently available ONLY through ZCode / the GLM Coding Plan — no public API price; API and
  open weights (HF) expected in ~2 weeks. Staged security release (cyber-defense capabilities,
  dual-use) — selected partners first, then API, then full weights. Vendor claims: tops Kimi K3
  on many benchmarks, some scores above Fable 5 / GPT-5.6-Sol — treated as claims, not
  independently reproduced.
- **ZCode added** (FREE-ACCESS.md Table 1 + use-case table, AGENTS.md Part 2, README quick-ref +
  digest, ide-pricing chart at $0): Z.AI's free desktop coding agent, launched Jul 2, 2026
  (VentureBeat). GLM-5.3 free on it since Aug 16-17 (community-confirmed — "GLM 5.3 Is Now FREE
  On ZCode" walkthroughs). MODELS.md Z.AI row updated from "no price published" to the release
  + free-access facts.
- **Zed student plan — already present, confirmed**: CREDITS.md Part 2 already carries "Zed
  Education — Zed Pro free 12 months + $10/mo AI credit (GitHub 30+ days, edu email)", which
  matches zed.dev/blog/student-plan + zed.dev/education (Mar 9, 2026). No edit needed; noted in
  the README digest for visibility.
- **Charts regenerated** after adding ZCode to `data/extra_charts.json` (ide_pricing).

## Instagram/Reddit sweep pass — 17 Aug 2026 (user: "find more; oxaam?; student acc; Cursor/Devin/Cline; Cline in AgentRouter")

- **OrcaRouter verified + added** (FREE-ACCESS.md aggregators): MIT OpenRouter alternative, zero-markup, 100+ models; free credits no card (PRNewswire May 8), free BYOK (Jul 24), voucher drops + student credits + hackathon grants (live offers page, Aug 17). Credit amounts are promo-based — caveated ⚠️.
- **findaicredits.com added** (FREE-ACCESS.md Useful Repos): directory of free AI credits/deals/coupons, surfaced via Instagram Aug 2026 reels (Claude/Cursor/Codex sub credits claimed) — labelled as leads, not facts.
- **oxaam.com — already mentioned, warning upgraded.** Was a caveat row in CREDITS.md Part 6; this pass added the scam flags: r/Scams (Dec 2025 "may steal your login details"), r/isthisascam, r/AI_Agents ("Oxaam is a scam guys"). Trustpilot 4.2/1195 but company-written reviews + hidden owner. Now reads as Kept-out-level risk; never a real login.
- **Student accounts — confirmed already covered:** CREDITS.md Part 2 has GitHub Student Pack (+Azure for Students $100, DigitalOcean $200, MongoDB $50…), Cursor for Students (1yr Pro), Zed Education ($10/mo credit), Cloudflare Workers for Students, Notion Edu, JetBrains/Figma/Linear. OrcaRouter's student credits added via its aggregator row.
- **Cursor / Devin (ex-Windsurf) / Cline — confirmed already covered:** AGENTS.md Part 2 (Cursor, Devin Desktop/Windsurf rebrand note) + Part 1 Tier 2 (Cline) + MCP table (Cline VS Code extension row) + CREDITS.md (Cursor for Students, Lenny's Devin codes).
- **Cline-in-AgentRouter made explicit:** FREE-ACCESS.md AgentRouter row now says to add the AgentRouter key as a custom OpenAI-compatible provider in the **Cline VS Code extension** (Settings → API Provider → OpenAI Compatible) for free Claude/GPT in the IDE.
- README digest bullet added; no chart changes (no model-price/SWE rows affected).

## Web-sweep pass 2 — 17 Aug 2026 (user: "search more on internet")

- **Codex for Students added** (CREDITS.md Part 2): $100 ChatGPT credits for Codex, US/CA university students, verify via university email — primary-sourced (chatgpt.com/codex/students, developers.openai.com/community/students, OpenAI X/TikTok).
- **Anthropic research grants added** (CREDITS.md Part 3): AI for Science Rare Disease call (up to $50K Claude API credits over 6 mo, announced Jul 20 2026) + Economic Futures ($10K-50K funding + $5K Claude credits).
- **aistudentdiscount.com/deals** referenced in CREDITS Part 2 (71 verified student deals, 21 free, $41K+ savings, Jul 2026 check).
- No chart changes (no model-price/SWE rows affected).

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
