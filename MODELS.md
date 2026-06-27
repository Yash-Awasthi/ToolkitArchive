# AI Models — Full Reference (June 2026)

> `[open]` = public leaderboard · `[V]` = vendor-reported (10-20pt inflated) · `[C]` = closed
> **Data source:** all charts + the tables below derive from [`data/models.json`](./data/models.json) — edit there, then run `python3 charts/gen_charts.py`.

---

## SWE-bench Leaderboard

![SWE-bench](./charts/swe-bench.png)

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
| **Fable 5** | Mythic | **95.0%** | [C] | — | — | — | SWE-bench record. Export-suspended Jun 12 (US controls). Not publicly usable |
| **GPT-5.6 Sol** | OpenAI | ~91%[est] | [V] | $5 | $30 | 1.5M | Preview Jun 26. Flagship. TB 2.1 **88.8%** (Sol Ultra 91.9%). Max + Ultra (parallel subagents). Cerebras 750 tok/s in July |
| **GPT-5.6 Terra** | OpenAI | ~88%[est] | [V] | $2.50 | $15 | 1M | Preview Jun 26. GPT-5.5-class at half price |
| **GPT-5.6 Luna** | OpenAI | ~84%[est] | [V] | $1 | $6 | 1M | Preview Jun 26. Fast/high-volume tier |
| GPT-5.5 | OpenAI | 88.7% | open | $5 | $30 | 1M | Leads Terminal-Bench 2.1 (83.4% via Codex CLI) |
| Claude Opus 4.8 | Anthropic | 88.6% | [V] | $5 | $25 | 1M | Released May 28. Best SWE-bench Pro (69.2%). Scale SEAL ~51.9% |
| GPT-5.3 Codex | OpenAI | 85.0% | [C] | $1.75 | $14 | 1M | Codex API, agentic coding focus |
| GPT-5.4 | OpenAI | 84.1% | open | $2.50 | $15 | 1M | Scale SEAL 59.1% (xHigh) |
| Claude Sonnet 4.6 | Anthropic | 82.8% | [V] | $3 | $15 | 1M | Best-value Anthropic flagship |
| GLM-5.1 | Z.AI | 81.0% | [V] | $1.40 | $4.40 | 200K | First open model to top SWE-bench Pro |
| DeepSeek V4 Pro | DeepSeek | 80.6% | open | $0.44 | **$0.87** | 1M | MIT license. Cache hits $0.001/M. Sweet spot |
| Gemini 3.1 Pro | Google | 80.6% | open | $2 | $12 | 1M | Price doubles >200K ctx |
| MiniMax M3 | MiniMax | 80.5% | open | $0.30 | **$1.20** | 1M | Open-weight MIT. Sweet spot |
| Qwen 3.7 Max | Alibaba | 80.4% | open | $1.25 | $3.75 | 1M | Promo; list $2.50/$7.50 |
| Qwen 3.7 Plus | Alibaba | ~78% | open | $0.50 | $2.00 | 1M | Reasoning model, 1M ctx |
| Kimi K2.6 | Moonshot | 80.2% | open | $0.95 | **$1.50** | 262K | 4,000+ tool calls/session. Sweet spot |
| Grok 4.3 | xAI | ~78% | [C] | $3 | $15 | 128K | Closed eval |
| Gemini 3.5 Flash | Google | 78.8% | open | $1.50 | $9 | 1M | |
| Qwen3-Coder 480B | Alibaba | 78.0% | open | $0.22 | $1.80 | 1M | Apache 2.0, MoE 35B active. Free on OpenRouter |
| Mistral Medium 3.5 | Mistral | 77.6% | open | $1.50 | $7.50 | 256K | EU-hosted, GDPR |
| Laguna M.1 | Poolside | ~78% | [C] | $4 | $8 | 256K | Coding specialist |
| MiMo V2.5 Pro | Xiaomi | 75.0% | open | $0.44 | **$0.87** | 1M | 40-60% fewer tokens/trajectory. Sweet spot |
| Claude Haiku 4.5 | Anthropic | 74.8% | [V] | $1 | $5 | 200K | Fast, cheap Claude |
| Llama 4 Maverick | Meta | 74.0% | open | $0.20 | $0.39 | 1M | Apache 2.0 via third-party |
| Gemini 3.1 Flash | Google | 74.0% | open | $0.30 | $2.50 | 1M | Cheapest Google |
| Devstral 2 | Mistral | 72.2% | open | $0.40 | $0.90 | 256K | Best-value Mistral open-weight |
| DeepSeek V4 Flash | DeepSeek | 72.0% | open | $0.14 | **$0.28** | 1M | Cheapest serious coding API |
| GLM-5.2 | Z.AI | ~72% | [V] | $0.14 | **$0.28** | 1M | MIT. Free on chat.z.ai + Puter.js. Released Jun 16 |
| Grok Build 0.1 | xAI | ~76% | [C] | $5 | $25 | 128K | Coding-specialist, limited |
| Nemotron 3 Ultra | NVIDIA | ~67% | [C] | $0.20 | $0.50 | 1M | Open-weight, 30% fewer tokens |
| Step 3.7 Flash | StepFun | ~69% | [C] | $0.30 | $0.60 | 256K | Interpolated |
| GPT-oss-20b | OpenAI | 57.0% | open | $0.07 | $0.14 | 64K | OpenAI open-weight |

---

## Sweet Spot Analysis

75-81% quality at 17-34x cheaper than GPT-5.5. Under 9% quality gap.

| Model | SWE-bench | Out $/1M | vs GPT-5.5 gap | vs GPT-5.5 cost |
|---|---|---|---|---|
| DeepSeek V4 Pro | 80.6% | $0.87 | -8.1% | **34x cheaper** |
| MiniMax M3 | 80.5% | $1.20 | -8.2% | **25x cheaper** |
| Kimi K2.6 | 80.2% | $1.50 | -8.5% | **20x cheaper** |
| MiMo V2.5 Pro | 75.0% | $0.87 | -13.7% | **34x cheaper** |

---

## Table 2 — Free Tier / Near-Free Models

| Model | Company | SWE-bench | In $/1M | Out $/1M | Access | Notes |
|---|---|---|---|---|---|---|
| Kimi K2.6 | Moonshot | 80.2% | $0 | $0 | Free trial credits | Best free quality |
| Qwen3-Coder 480B | Alibaba | 78.0% | $0 | $0 | OpenRouter `:free` | 20 RPM, 50 req/day |
| Llama 4 Maverick | Meta | 74.0% | $0 | $0 | OpenRouter `:free` | Rate-limited |
| Qwen3-Coder-Next | Alibaba | 70.6% | $0 | $0 | New account trial | 1M tok/model, 90-day |
| GLM-5.2 | Z.AI | ~72% | $0 | $0 | chat.z.ai / Puter.js | 1M ctx, MIT. Released Jun 16 |
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
| Opus 4.8 | 88.6% [V] | $5/$25 | 1M |
| Sonnet 4.6 | 82.8% [V] | $3/$15 | 1M |
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
| Gemini 3.5 Flash | 78.8% | $1.50/$9 | 1M |
| Gemini 3.1 Flash | 74.0% | $0.30/$2.50 | 1M |
| Gemini 3.1 Flash Lite | ~62% | $0.10/$0.40 | — |

### Z.AI (Zhipu)
| Model | SWE-bench | In/Out $/1M | Context | Access |
|---|---|---|---|---|
| GLM-5.1 | 81.0% [V] | $1.40/$4.40 | 200K | API paid |
| GLM-5.2 | ~72% [V] | $0.14/$0.28 | 1M | chat.z.ai free, Puter.js free |
| GLM-4.7-Flash | 58.0% | $0/$0 | — | Z.AI API free tier |

### DeepSeek
| Model | SWE-bench | In/Out $/1M | Context |
|---|---|---|---|
| V4 Pro | 80.6% | $0.44/$0.87 | 1M |
| V4 Flash | 72.0% | $0.14/$0.28 | 1M |

---

## Context Window Reference

| Context | Models |
|---|---|
| 1M | GPT-5.5, GPT-5.4, GPT-5.3, Opus 4.8, Sonnet 4.6, DeepSeek V4 Pro/Flash, MiniMax M3, Qwen 3.7 Max, Qwen3-Coder 480B, Llama 4 Mav, Gemini 3.x, MiMo V2.5 Pro, Nemotron 3, GLM-5.2 |
| 262K | Kimi K2.6 |
| 256K | Mistral Medium 3.5, Devstral 2, Laguna M.1, Step 3.7 Flash |
| 200K | GLM-5.1, Claude Haiku 4.5 |
| 128K | Grok 4.3, Grok Build 0.1 |
| 64K | GPT-oss-20b |

---

## Scale SEAL vs Vendor-Reported

| Model | SEAL Score | Vendor-Reported | Inflation |
|---|---|---|---|
| GPT-5.4 xHigh | 59.1% | 84.1% | ~25pt |
| Claude Opus 4.6 thinking | 51.9% | ~88% | ~36pt |
| Claude Haiku 4.5 | 39.5% | 74.8% | ~35pt |

---

## Upcoming & Early-Stage Models

> Preview / rumored / restricted — not yet generally usable. Tracked so you can chase early access. See [`data/models.json`](./data/models.json) → `upcoming`.

| Model | Company | Status |
|---|---|---|
| **Gemini 3.5 Pro** | Google | Announced Google I/O (May 19), GA imminent. ~$15/$60 expected, **2M ctx**, Deep Think mode |
| **Fable 5** | Mythic | SWE-bench record (95%). **Export-suspended Jun 12** (US controls) — not publicly usable |
| **DeepSeek V5** | DeepSeek | Rumored Q2–Q3 2026 — expected to push Tier-1 capability + drop cost further |
| **Kimi K3** | Moonshot | Rumored Q3 2026 |

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

> ⚠️ Subscription proxies are reverse-engineered — ToS/account-ban risk. `iFlow`, `Qwen`, and `Gemini CLI` free tiers were **discontinued in 2026**; use Kiro / OpenCode-Free / Vertex instead.

**Multi-tier routing (the dominant 2026 production pattern):** Tier 1 ~70% → DeepSeek V4 Flash ($0.28/M) · Tier 2 ~25% → Kimi K2.6 / GLM-5.1 (~$1/M) · Tier 3 ~5% → Opus 4.8. Saves **85–95%** on coding-API cost vs all-Opus, <10% quality loss.

---

## Release Timeline (2026)

| Date | Event |
|---|---|
| Mar 18 | MiniMax M2.7 — "self-evolution" agentic training |
| Apr 7 | GLM-5.1 (Z.AI) — 744B MoE, 200K ctx, MIT |
| Apr 16 | Claude Opus 4.7 |
| Apr 21 | Kimi K2.6 — briefly tops open SWE-bench Pro (58.6%) |
| Apr 23 | GPT-5.5 |
| Apr 24 | DeepSeek V4 Pro (1.6T/49B) + V4 Flash (284B/13B), MIT, 1M ctx |
| May 28 | Claude Opus 4.8 — 1M ctx, hybrid reasoning |
| Jun 12 | Fable 5 (95%) export-suspended |
| Jun 13 | GLM-5.2 — 1M ctx, MIT |
| Jun 16 | MiniMax M3 tops open SWE-bench Pro (59.0%) |
| Jun 26 | GPT-5.6 Sol/Terra/Luna preview — gated to ~20 orgs pending US-gov 30-day cyber review (EO Jun 2); GA "coming weeks" |
