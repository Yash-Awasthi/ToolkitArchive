# AI Models — Full Reference (re-checked 17 August 2026)

> `[open]` = public leaderboard · `[V]` = vendor-reported (10-20pt inflated) · `[C]` = closed
> **Data source:** all charts + the tables below derive from [`data/models.json`](./data/models.json) — edit there, then run `python3 charts/gen_charts.py`.

> **Benchmark hygiene:** SWE-bench, Terminal-Bench, Scale SEAL, and vendor evaluations do not
> measure the same thing. Terminal-Bench scores are agent+model+effort configurations; its current
> TB 2.1 snapshot lives in [AGENTS.md](./AGENTS.md#terminal-bench-21--reproducible-snapshot-17-aug-2026).
> Never convert one into the other or use either as a model-only ranking.

---

## SWE-bench Leaderboard

![SWE-bench](./charts/swe-bench.png)

> **Standardized-harness reference (vals.ai, Aug 2026 — harness-sensitive, treat as a ceiling, do NOT mix with the chart numbers):**
> GPT-5.6 Sol ~96-97% (leader) · DeepSeek V4 Pro 0813 **96.4%** · Claude Fable 5 95.0% · Kimi K3 **93.4%** ·
> GPT-5.6 Luna 93.0% · Claude Opus 4.8 88.6% · Grok 4.5 86.6%. These come from vals.ai's own
> standardized harness and run 10-15pts above the official-leaderboard / vendor numbers used in the
> charts and tables below; vals.ai itself labels them harness-sensitive. The SWE-bench Pro angle
> (Aug 2026): Claude Mythos 5 80.3% · Fable 5 80.0% · Opus 5 79.2% · Kimi K3 80.0% · Qwen 3.8-Max 67.7%.

---

## Price vs Performance Scatter

![Scatter](./charts/all-models-scatter.png)

---

## Output Cost

![Output cost](./charts/all-models-cost.png)

---

## Table 1 — Premium / Paid API Models

| Model | Company | SWE-bench | Src | In $/1M | Out $/1M | Context | Notes |
|---|---|---|---|---|---|---|---|
| **Claude Opus 5** | Anthropic | — | $5 | $25 | 1M | Released Jul 24, 2026 at Opus 4.8 pricing ($5/$25). Price + date confirmed from anthropic.com/news/claude-opus-5 this pass; no public SWE-bench number yet |
| **Claude Sonnet 5** | Anthropic | — | $2 | $10 | 1M | Released Jun 30, 2026. Intro pricing $2/$10 made **permanent Aug 10, 2026** (standard would have been $3/$15) — confirmed from anthropic.com/news/claude-sonnet-5 edit note. No public SWE-bench number yet |
| **Fable 5** | Anthropic | **95.0%** | [V] | $10 | $50 | 1M | Mythos-class (tier above Opus). GA Jun 9 → pulled from subs Jun 23, export-suspended Jun 12 (US controls). SWE-bench Pro 80.3%. 30-day forced retention. Only the 1M context was re-confirmed this pass — price, SWE-bench number, and the export-suspend story are from the prior pass, not re-checked, treat as stale |
| **GPT-5.6 Sol** | OpenAI | ~91%[est] | [V] | $5 | $30 | 1.05M | **GA Jul 9, 2026** (no longer preview). Flagship. TB 2.1 **88.8%** (Sol Ultra 91.9%). Max + Ultra (parallel subagents). Cerebras 750 tok/s in July. vals.ai SWE-bench Verified ~96-97% (standardized harness — ceiling; the ~91% chart figure is the community estimate kept for consistency). Context corrected from a prior 1.5M error — 1.05M is what OpenAI states |
| **GPT-5.6 Terra** | OpenAI | ~88%[est] | [V] | $2.50 | $15 | **1.05M** | GA Jul 9, 2026. OpenAI docs: 1.05M context / 128K output. TB 2.1: Codex + Terra, max effort = 78.4%—not a model-only score |
| **GPT-5.6 Luna** | OpenAI | ~84%[est] | [V] | $1 | $6 | **1.05M** | GA Jul 9, 2026. OpenAI docs: 1.05M context / 128K output. TB 2.1: Codex + Luna, max effort = 75.7%—not a model-only score |
| GPT-5.5 | OpenAI | 88.7% | open | $5 | $30 | 1M | TB 2.1: Codex + GPT-5.5, xhigh = **83.1% ± 1.1%** (not model-only) |
| Claude Opus 4.8 | Anthropic | 88.6% | [V] | $5 | $25 | 1M | Released May 28. Best SWE-bench Pro (69.2%). Scale SEAL ~51.9%. **Superseded** — Claude Opus 5 is now the current flagship, kept here as history |
| GPT-5.3 Codex | OpenAI | 85.0% | [C] | $1.75 | $14 | 1M | Codex API, agentic coding focus |
| GPT-5.4 | OpenAI | 84.1% | open | $2.50 | $15 | 1M | Scale SEAL 59.1% (xHigh) |
| Claude Sonnet 4.6 | Anthropic | 82.8% | [V] | $3 | $15 | 1M | Best-value Anthropic flagship. **Superseded** — Claude Sonnet 5 is now the current mid tier, kept here as history |
| **Ornith-1.0-397B** | DeepReinforce | 82.4% | open | — | — | — | Jun 25, MIT weights (HF, self-host). 397B MoE flagship; family also 9B/31B/35B. Self-scaffolding RL — writes own agent scaffold before solving. TB 2.1 77.5%. Beats Opus 4.7, not 4.8. Vendor benches |
| GLM-5.1 | Z.AI | 81.0% | [V] | $1.40 | $4.40 | 200K | First open model to top SWE-bench Pro. Price confirmed on docs.z.ai llms.txt. Context is not stated on the official pricing doc — treat 200K as unverified, carried from a prior pass |
| DeepSeek V4 Pro | DeepSeek | 80.6% | open | $1.32 | **$3.96** | 1M | **GA Aug 13, 2026 (deepseek-v4-pro-0813).** Official pricing re-checked Aug 17: peak cache-miss $1.32/M in, $3.96/M out; off-peak (all hours outside 01-04 & 06-10 UTC) half that — $0.66/$1.98. Cache hit $0.022-0.044/M. TB 2.1 **87.9** reported by DeepSeek via its own harness (DeepSeek Harness minimal mode, max effort) — vendor-reported, not the official tbench.ai leaderboard. vals.ai SWE-bench Verified: **96.4%** (standardized harness, treat as ceiling). Native Responses API + Codex support, thinking effort low/high/max. The chart's 80.6 is the April preview's official-leaderboard score — no GA official SWE-bench published yet |
| Gemini 3.1 Pro | Google | 80.6% | open | $2 | $12 | 1M | Price doubles >200K ctx. The preview id and status are confirmed on Google's own model list; the 1M ctx, price, and SWE-bench figures were not re-checked against that list this pass — treat as a prior-pass caveat |
| MiniMax M3 | MiniMax | 80.5% | open | $0.30 | **$1.20** | 1M | Open-weight MIT. Sweet spot |
| Qwen 3.7 Max | Alibaba | 80.4% | open | $1.25 | $3.75 | 1M | Promo; list $2.50/$7.50. The `qwen3.7-max` id is confirmed on Alibaba's Model Studio list; the 1M ctx figure and the "open" weight tag are not backed by that primary source (a secondary aggregator claims closed-weight instead, which contradicts "open") — both numbers here are unverified, carried from a prior pass |
| **Qwen 3.8-Max** | Alibaba | — | — | $2 | $6 | 1M | Released **Aug 2, 2026** (qwen.ai blog primary). 2.4T MoE / 95B active. TB 2.1 **86.6** (standardized-harness aggregator figure). **First open-weight Max-class Qwen**: Qwen3.8-2.4T-A95B on HuggingFace Aug 12 — but open weights are text-only and stripped of vision + 1M ctx (per HF discussion). Free via Qwen Chat. No public SWE-bench yet — text row only, not in charts |
| Qwen 3.7 Plus | Alibaba | ~78% | open | $0.50 | $2.00 | 1M | Reasoning model, 1M ctx |
| Kimi K2.6 | Moonshot | 80.2% | open | $0.95 | **$1.50** | 256K | 4,000+ tool calls/session. Sweet spot |
| **Kimi K2.7-Code** | Moonshot | ~80%[est] | open | $0.95 | **$4** | 256K | Jun 12. 1T MoE/32B active, forced thinking. +21.8% Kimi Code Bench v2 vs K2.6, -30% reasoning tokens. Modified MIT. Vendor benches only |
| **Kimi K3** | Moonshot | ~93.4% (vals harness) / 80.0% SWE-bench Pro | [V] | — | — | 1M | Confirmed live on platform.kimi.ai, "most capable to date". SWE-bench figures added this pass from vals.ai (93.4%, harness-sensitive ceiling) and SWE-bench Pro (80.0% — per launch coverage); no official API price published yet. Moved up from the Upcoming table now that it has shipped |
| Grok 4.3 | xAI | ~78% | [C] | $3 | $15 | 1M | Closed eval. Context corrected from a prior 128K error — docs.x.ai states 1M |
| Gemini 3.5 Flash | Google | 78.8% | open | $1.50 | $9 | 1M | **Superseded** — Gemini 3.7 Flash (below) is now the workhorse tier, kept here as history |
| **Gemini 3.7 Flash** | Google | — | — | $0.75 | $3.75 | 1M | Released **Aug 13, 2026**; "most intelligent workhorse model yet" for coding/agents. Intro pricing $0.75/$3.75 through end of 2026 (half the previous workhorse price). TB 2.1 85.8% (standardized-harness aggregator figure, not official leaderboard). No public SWE-bench number yet — text row only, not in charts |
| **Grok 4.6** | xAI (now SpaceXAI) | — | — | $2 | $6 | 500K | Released **Aug 12, 2026**; focus on long-running agents + interactive/visual work. Price $2/$6 per kie.ai + llm-stats coverage of the launch. VentureBeat: third-best on Artificial Analysis overall. No public SWE-bench — text row only |
| **Grok 4.5** | xAI (now SpaceXAI) | 86.6% (vals harness) | [V] | $2 | $6 | 500K | Released Jul 2026 (date disputed between sources: ~Jul 8 by one analysis, Jul 16 per the x.ai news post; xAI rebranded to **SpaceXAI** around this launch). Price $2/$6 per the official Grok 4.5 announcement. SWE-bench 86.6% is vals.ai's harness-sensitive ceiling, not an official-leaderboard number |
| Qwen3-Coder 480B | Alibaba | 78.0% | open | $0.22 | $1.80 | 1M | Apache 2.0, MoE 35B active. Free on OpenRouter |
| Mistral Medium 3.5 | Mistral | 77.6% | open | $1.50 | $7.50 | 256K | EU-hosted, GDPR. Context is from a prior pass, not re-confirmed against a primary source this time |
| **Meta Muse Spark** | Meta (MSL) | 77.4% | [V] | — | — | — | Apr 8. First Meta Superintelligence Labs model (not Llama). Free on meta.ai, API private-preview only. Strong multimodal/health, weak agentic (TB 2.0 59%). Closed. Meta's own blog confirms the Muse family exists and is not Llama-branded, but the launch post itself wasn't fetched this pass — the rest of this row (SWE-bench, "free on meta.ai", Apr 8 date) is a prior-pass claim, not re-verified |
| Laguna M.1 | Poolside | ~78% | [C] | $4 | $8 | 256K | Coding specialist |
| MiMo V2.5 Pro | Xiaomi | 75.0% | open | $0.44 | **$0.87** | 1M | 40-60% fewer tokens/trajectory. Sweet spot |
| Claude Haiku 4.5 | Anthropic | 74.8% | [V] | $1 | $5 | 200K | Fast, cheap Claude |
| **MAI-Code-1-Flash** | Microsoft | ~74%[est] | [V] | — | — | — | 137B MoE/5B active. "Haiku-class but cheaper." Bundled into all Copilot plans + VS Code. Weights tunable. OpenRouter/Fireworks/Baseten |
| Llama 4 Maverick | Meta | 74.0% | open | $0.20 | $0.39 | 1M | Apache 2.0 via third-party. Meta's own blog does not restate the 1M figure — treat context as a caveat, not confirmed by the primary source |
| Gemini 3.1 Flash | Google | 74.0% | open | $0.30 | $2.50 | 1M | Cheapest Google |
| Devstral 2 | Mistral | 72.2% | open | $0.40 | $0.90 | 256K | Best-value Mistral open-weight |
| DeepSeek V4 Flash | DeepSeek | 72.0% | open | $0.44 | **$1.32** | 1M | **Official release Jul 31, 2026 (deepseek-v4-flash-0731).** Pricing re-checked Aug 17: peak cache-miss $0.44/M in, $1.32/M out; off-peak half ($0.22/$0.66). Cache hit $0.007-0.014/M. TB 2.1 **82.7** (vendor-reported, DeepSeek Harness). Native Responses API + Codex support. SWE-bench 72.0 is the preview's public score — no new one published |
| GLM-5.2 | Z.AI | ~72% | [V] | $1.40 | **$4.40** | 1M | Corrected from a prior $0.14/$0.28 — that was a 10x error, docs.z.ai llms.txt gives $1.40/$4.40. Context (1M) is not on the official pricing doc, treat as unverified. MIT license claim comes from a secondary blog, not confirmed. Free access is chat.z.ai's web chat only, not the paid API — don't read "free" onto the API tier |
| Grok Build 0.1 | xAI | ~76% | [C] | $5 | $25 | 256K | Coding-specialist, limited. Context corrected from a prior 128K error — docs.x.ai states 256K. ⚠️ **Price disputed this pass:** $5/$25 (prior pass) vs $1/$2 per OpenRouter/Kilo listings — verify before relying |
| Nemotron 3 Ultra | NVIDIA | ~67% | [C] | $0.20 | $0.50 | 1M | Open-weight, 30% fewer tokens |
| Step 3.7 Flash | StepFun | ~69% | [C] | $0.30 | $0.60 | 256K | Interpolated |
| GPT-oss-20b | OpenAI | 57.0% | open | $0.07 | $0.14 | 64K | OpenAI open-weight |

> **Sakana Fugu** (Jun 22) — not a model row but an *orchestration meta-model*: one API endpoint that routes each request across a swappable pool of frontier LLMs (recursively including itself). Hosted = proprietary; the repo + ICLR papers (TRINITY, Conductor) are open, and [OpenFugu](https://github.com/trotsky1997/OpenFugu) reimplements it Apache-2.0. Same idea as the multi-tier routing below, sold as a single model. [SakanaAI/fugu](https://github.com/SakanaAI/fugu)

---

## Sweet Spot Analysis

75-81% quality at 20-34x cheaper than GPT-5.5 (DeepSeek V4 Pro moved out of this band on its Aug 16 GA pricing). Under 9% quality gap.

| Model | SWE-bench | Out $/1M | vs GPT-5.5 gap | vs GPT-5.5 cost |
|---|---|---|---|---|
| MiniMax M3 | 80.5% | $1.20 | -8.2% | **25x cheaper** |
| Kimi K2.6 | 80.2% | $1.50 | -8.5% | **20x cheaper** |
| MiMo V2.5 Pro | 75.0% | $0.87 | -13.7% | **34x cheaper** |
| DeepSeek V4 Pro | 80.6% | $1.98–3.96 | -8.1% | **7.6-15x cheaper** (off-peak/peak; GA pricing Aug 16 — was 34x at preview price) |

---

## Table 2 — Free Tier / Near-Free Models

| Model | Company | SWE-bench | In $/1M | Out $/1M | Access | Notes |
|---|---|---|---|---|---|---|
| Kimi K2.6 | Moonshot | 80.2% | $0.95 | $1.50 | Trial credit, amount unverified | Not a free tier — Moonshot's own docs say only the file-extraction endpoint is temporarily free, inference is paid. Dropped the "$0/$0 best free quality" framing this pass; see [CREDITS.md](./CREDITS.md) Part 6 |
| Qwen3-Coder 480B | Alibaba | 78.0% | $0 | $0 | OpenRouter `:free` | 20 RPM, 50 req/day |
| Llama 4 Maverick | Meta | 74.0% | $0 | $0 | OpenRouter `:free` | Rate-limited |
| Qwen3-Coder-Next | Alibaba | 70.6% | $0 | $0 | New account trial | 1M tok/model, 90-day claim from an aggregator (apidog), not Alibaba directly — unverified |
| GLM-5.2 | Z.AI | ~72% | $0 | $0 | chat.z.ai / Puter.js | This $0 is the web chat and Puter.js passthrough, not the paid API ($1.40/$4.40, see Table 1). Context and MIT-license claim are unverified this pass |
| DeepSeek V4 Flash | DeepSeek | 72.0% | $0.14 | **$0.28** | Paid (near-free) | No rate limit |
| Nemotron 3 Super | NVIDIA | ~65% | $0 | $0 | build.nvidia.com NIM | Rate-limited |
| GLM-4.7-Flash | Z.AI | 58.0% | $0 | $0 | Z.AI free tier | Generous limits |
| Devstral Small 2 | Mistral | ~55% | $0 | $0 | OpenRouter `:free` | Rate-limited |
| Gemini 3.1 Flash Lite | Google | ~62% | $0.10 | **$0.40** | Paid (near-free) | No rate limit |
| Cohere North Mini Code | Cohere | N/A | $0 | $0 | OpenRouter `:free` | Apache 2.0, 256K ctx |

---

## Provider Breakdown

### Anthropic
| Model | SWE-bench | In/Out $/1M | Context |
|---|---|---|---|
| Opus 5 | — | — | 1M |
| Sonnet 5 | — | — | 1M |
| Opus 4.8 (superseded) | 88.6% [V] | $5/$25 | 1M |
| Sonnet 4.6 (superseded) | 82.8% [V] | $3/$15 | 1M |
| Haiku 4.5 | 74.8% [V] | $1/$5 | 200K |

### OpenAI
| Model | SWE-bench | In/Out $/1M | Context |
|---|---|---|---|
| GPT-5.5 | 88.7% | $5/$30 | 1M |
| GPT-5.4 | 84.1% | $2.50/$15 | 1M |
| GPT-5.3 Codex | 85.0% [C] | $1.75/$14 | 1M |
| GPT-oss-20b | 57.0% | $0.07/$0.14 | 64K |

### Google
| Model | SWE-bench | In/Out $/1M | Context |
|---|---|---|---|
| Gemini 3.1 Pro | 80.6% | $2/$12 | 1M |
| Gemini 3.7 Flash | — (no public SWE-bench) | $0.75/$3.75 (thru 2026) | 1M |
| Gemini 3.5 Flash | 78.8% | $1.50/$9 | 1M |
| Gemini 3.1 Flash | 74.0% | $0.30/$2.50 | 1M |
| Gemini 3.1 Flash Lite | ~62% | $0.10/$0.40 | — |

### Z.AI (Zhipu)
| Model | SWE-bench | In/Out $/1M | Context | Access |
|---|---|---|---|---|
| GLM-5.3 | — | — | — | Id confirmed live on docs.z.ai llms.txt this pass; no price or SWE-bench number published there |
| GLM-5.2 | ~72% [V] | $1.40/$4.40 | 1M (unverified) | Corrected from a prior $0.14/$0.28 (10x error). API is paid — chat.z.ai and Puter.js are free front-ends, not a free API tier |
| GLM-5.1 | 81.0% [V] | $1.40/$4.40 | 200K (unverified) | API paid. Context not on the official pricing doc |
| GLM-5 | — | — | — | Id + price ($1.00/$3.20) confirmed on docs.z.ai llms.txt; no SWE-bench or context published there |
| GLM-5-Turbo | — | — | — | Id + price ($1.20/$4.00) confirmed on docs.z.ai llms.txt; no SWE-bench or context published there |
| GLM-4.7-Flash | 58.0% | $0/$0 | — | Z.AI API free tier — this one is actually free, unlike the GLM-5.x line |

### DeepSeek
| Model | SWE-bench | In/Out $/1M | Context |
|---|---|---|---|
| V4 Pro (0813, GA Aug 13) | 80.6% (preview SWE-bench) | Peak $1.32/$3.96 · off-peak $0.66/$1.98 (cache hit $0.022-0.044/M) | 1M |
| V4 Flash (0731, official Jul 31) | 72.0% (preview SWE-bench) | Peak $0.44/$1.32 · off-peak $0.22/$0.66 (cache hit $0.007-0.014/M) | 1M |

> Pricing above was re-checked against DeepSeek's live API documentation on 17 August 2026. The
> provider changed to peak/off-peak pricing effective Aug 16, 2026 (off-peak = half of peak; peak
> hours 01-04 and 06-10 UTC) — the old flat preview prices ($0.435/$0.87 and $0.14/$0.28) are gone.
> Use the pricing page—not a cached table—for purchasing decisions.

**DeepSeek DSpark** (HF, not a separate model): the V4-Pro and V4-Flash checkpoints also ship as
`DeepSeek-V4-Pro-DSpark` / `DeepSeek-V4-Flash-DSpark` on HuggingFace — the same weights with an
open-source **speculative decoding** module attached, giving 50-600% faster generation (one
write-up reports ~85% per-user speedup). Serve it via HF Inference Providers / DeepInfra or
self-host. It does not change model quality, only speed — and it is *not* the GA `0813`/`0731`
API updates above, which add thinking-effort levels (low/high/max) and Responses-API support.

---

## Context Window Reference

| Context | Models |
|---|---|
| 1.05M | GPT-5.6 Sol, Terra, Luna |
| 1M | Opus 5, Sonnet 5, Kimi K3, GPT-5.5, GPT-5.4, GPT-5.3, Opus 4.8, Sonnet 4.6, Fable 5, DeepSeek V4 Pro/Flash, MiniMax M3, Qwen 3.7 Max (unverified), **Qwen 3.8-Max**, **Gemini 3.7 Flash**, Qwen3-Coder 480B, Llama 4 Mav, Gemini 3.x, MiMo V2.5 Pro, Nemotron 3, GLM-5.2 (unverified), Grok 4.3 |
| 500K | Grok 4.6, Grok 4.5 |
| 256K | Kimi K2.6, Kimi K2.7-Code, Grok Build 0.1, Mistral Medium 3.5, Devstral 2, Laguna M.1, Step 3.7 Flash |
| 200K | GLM-5.1 (unverified), Claude Haiku 4.5 |
| 64K | GPT-oss-20b |

> Grok 4.3 and Grok Build 0.1 contexts were corrected this pass — the archive previously had both at 128K, which was wrong; docs.x.ai states 1M and 256K respectively. Kimi's 262K figure was replaced with 256K archive-wide — same number (262,144), one unit, not a correction.

---

## Scale SEAL vs Vendor-Reported

| Model | SEAL Score | Vendor-Reported | Inflation |
|---|---|---|---|
| GPT-5.4 xHigh | 59.1% | 84.1% | ~25pt |
| Claude Opus 4.6 thinking | 51.9% | ≈88% | ≈36pt |
| Claude Haiku 4.5 | 39.5% | 74.8% | ~35pt |

---

## Upcoming & Early-Stage Models

> Preview / rumored / restricted — not yet generally usable. Tracked so you can chase early access. See [`data/models.json`](./data/models.json) → `upcoming`.

| Model | Company | Status |
|---|---|---|
| **Gemini 3.5 Pro** | Google | Announced Google I/O (May 19), **still not GA as of Aug 12, 2026** — promised June, then Jul 17, then a rumored Aug 12 date that also passed. Google DeepMind says only "coming soon". ~$15/$60 expected, **2M ctx**, Deep Think mode |
| **Fable 5** | Anthropic | Mythos-class (95%), GA Jun 9 → **export-suspended Jun 12** (US controls). Now in Table 1. Only its context was re-confirmed this pass; the rest is a prior-pass claim |
| **DeepSeek V5** | DeepSeek | Rumored Q2–Q3 2026 — expected to push Tier-1 capability + drop cost further |
| **MAI-Thinking-1** | Microsoft | Flagship reasoning, private preview via Foundry (Build 2026, Jun 2). 35B MoE, 97% AIME 2025, 53% SWE-bench Pro, 256K ctx. Trained no-distillation, preferred over Sonnet 4.6 in blind evals |
| **Mythos 5** | Anthropic | Invite-only twin of Fable 5 (same base, safety classifiers removed), not GA. "World's strongest cyber model" claim (ExploitBench 78%) and the $10/$50, 95.5% SWE-bench numbers are vendor-reported and not re-verified this pass — treat as unconfirmed, not fact. Project-Glasswing-only with US gov |
| **Gemini Omni Pro** | Google | Full any-in/any-out follow-up to Omni Flash (I/O May 19). Dev API "coming weeks", no pricing yet |

---

## Consumer / On-Device (not API-accessible)

> Frontier-adjacent models you can't call from code — listed so the archive stays complete.

| Model | Company | What it is |
|---|---|---|
| **Apple AFM 3** | Apple | WWDC Jun 8 family powering new Siri AI. On-device: Core (3B dense), Core Advanced (20B sparse, ~1–4B active via Instruction-Following Pruning). Cloud: AFM 3 Cloud, ADM 3 Cloud (image), Cloud Pro (Nvidia GPUs in Google Cloud under Private Cloud Compute). Gemini used as distillation *teacher*, not runtime. No EU/China at launch |
| **Gemini Omni Flash** | Google | First "any-to-any" Google model (I/O May 19). Any input → ~10s video+audio out, conversational editing, personal avatars (number-handshake anti-deepfake), SynthID + C2PA baked in. AI Plus/Pro/Ultra + free in YouTube Shorts. No dev API yet |
| **Meta Muse Spark** | Meta | Free on meta.ai (also in Table 1) — listed here as the consumer entry point; API is partner-only |

> **Row added this pass:** the `qwen3.8-max` id (2.4T param, 1M ctx, $2/$6, launched Aug 2, 2026) was previously held out as unverified — it is now confirmed on Alibaba's qwen.ai blog and listed above as a text-only row (no public SWE-bench yet).

**How to find early access:** search `"<model> early access" / "<model> preview" / "<model> waitlist"`, the vendor's Discord/X, and `r/LocalLLaMA` + `r/singularity`. Open-weight Chinese models (GLM/DeepSeek/Kimi/Qwen/MiniMax) usually ship **directly as MIT/Apache weights** — no waitlist; grab them on HuggingFace/ModelScope day one.

---

## Access Routes — Get Frontier Models Free / Cheap

> The archive's models are reachable far below list price via proxies, routers, and OAuth passthroughs. Full detail + ToS warnings in [CREDITS.md](./CREDITS.md) Part 4 and [REFERENCES.md](./REFERENCES.md).

| Route | What you get | Tool |
|---|---|---|
| **Kiro AI (OAuth)** | Free unlimited Claude 4.5 + GLM-5 + MiniMax (routed) | via [9router](https://github.com/decolua/9router) |
| **OpenCode Free** | No-auth passthrough proxy | 9router |
| **Vertex AI $300** | Claude + Gemini on cloud trial credit | [CREDITS.md](./CREDITS.md) |
| **GLM Coding Plan** | Flat-rate GLM-5.x in Claude Code (`api.z.ai/api/anthropic`) | [jodavan/claude-code-proxy](https://github.com/jodavan/claude-code-proxy) |
| **Tier-routing** | Cheap model for 95% traffic, Opus for the hard 5% | [Alorse/cc-compatible-models](https://github.com/Alorse/cc-compatible-models) |
| **Ollama Cloud** | `glm-5.1:cloud`, `kimi-k2.5:cloud`, `qwen3.5:cloud` | ollama.com |

> ⚠️ Subscription proxies are reverse-engineered — ToS/account-ban risk. `iFlow` and `Qwen` free tiers were **discontinued in 2026**; use Kiro / OpenCode-Free / Vertex instead. `Gemini CLI`'s free tier is still live (60 req/min, 1,000 req/day) — a discontinuation claim here in a prior pass was unverified and has been removed. See [AGENTS.md](./AGENTS.md) Part 1.

**Multi-tier routing (the dominant 2026 production pattern):** Tier 1 ≈70% → DeepSeek V4 Flash ($0.66/M out off-peak — GA pricing since Aug 16) · Tier 2 ≈25% → Kimi K2.6 / GLM-5.1 (≈$1/M) · Tier 3 ≈5% → Opus 5. Saves **85–95%** on coding-API cost vs all-Opus, <10% quality loss.

---

## Release Timeline (2026)

| Date | Event |
|---|---|
| Mar 18 | MiniMax M2.7 — "self-evolution" agentic training |
| Apr 7 | GLM-5.1 (Z.AI) — 744B MoE, 200K ctx, MIT |
| Apr 8 | Meta Muse Spark — first Meta Superintelligence Labs model (77.4%), free on meta.ai |
| Apr 16 | Claude Opus 4.7 |
| Apr 21 | Kimi K2.6 — briefly tops open SWE-bench Pro (58.6%) |
| Apr 23 | GPT-5.5 |
| Apr 24 | DeepSeek V4 Pro (1.6T/49B) + V4 Flash (284B/13B), MIT, 1M ctx |
| May 19 | Gemini Omni Flash — Google's first any-to-any multimodal (I/O) |
| May 28 | Claude Opus 4.8 — 1M ctx, hybrid reasoning |
| Jun 2 | Microsoft MAI models (Build 2026) — MAI-Thinking-1, MAI-Code-1-Flash, +image/voice/transcribe |
| Jun 8 | Apple AFM 3 family — new Siri AI (WWDC), Gemini-distilled |
| Jun 9 | Claude Fable 5 + Mythos 5 GA — Mythos-class tier above Opus, $10/$50 |
| Jun 12 | Fable 5 export-suspended (US controls); Kimi K2.7-Code released |
| Jun 13 | GLM-5.2 — 1M ctx, MIT |
| Jun 16 | MiniMax M3 tops open SWE-bench Pro (59.0%) |
| Jun 22 | Sakana Fugu — LLM-orchestration meta-model (routes a pool of frontier LLMs behind one endpoint) |
| Jun 25 | Ornith-1.0 (DeepReinforce) — open MIT coding models (9B/31B/35B/397B), self-scaffolding RL, 82.4% SWE-bench |
| Jun 26 | GPT-5.6 Sol/Terra/Luna preview — gated to ~20 orgs pending US-gov 30-day cyber review (EO Jun 2) |
| Jun 30 | Claude Sonnet 5 — $2/$10 intro pricing (made permanent Aug 10) |
| Jul 8 | Grok 4.5 — 500K ctx (SpaceXAI, then still "xAI") |
| Jul 9 | **GPT-5.6 GA** — Sol/Terra/Luna across ChatGPT, Codex, API |
| Jul 21 | Gemini 3.6 Flash + 3.5 Flash-Lite + 3.5 Flash Cyber |
| Jul 24 | Claude Opus 5 — $5/$25, same price as Opus 4.8 |
| Jul 31 | DeepSeek V4 Flash official release (0731) — TB 2.1 82.7 (vendor harness) |
| Aug 2 | **Qwen 3.8-Max** — 2.4T MoE/95B active, $2/$6, 1M ctx |
| Aug 12 | Qwen3.8-2.4T-A95B **open weights** (text-only, no vision/1M-ctx); Grok 4.6 — $2/$6, 500K ctx; xAI rebrands to **SpaceXAI** |
| Aug 13 | **DeepSeek V4 Pro GA** (0813) — TB 2.1 87.9 (vendor harness), Responses API, thinking effort levels; **Gemini 3.7 Flash** — $0.75/$3.75 through 2026 |
| Aug 16 | DeepSeek switches to peak/off-peak API pricing (off-peak = half; old flat preview prices retired) |
