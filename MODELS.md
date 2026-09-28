# 🧠 AI Models — Current Lineup (verified 29 September 2026)

<p align="center"><a href="./README.md">🏠 Home</a> · <a href="https://yash-awasthi.github.io/ToolkitArchive/">🔎 Explorer</a> · <a href="https://yash-awasthi.github.io/ToolkitArchive/benchmarks.html">📊 Benchmarks</a> · <a href="./NEWS.md">📰 News</a> · <a href="./STUDENTS.md">🎓 $0 guide</a> · <a href="./FREE-ACCESS.md">🆓 Free AI</a></p>


> [!NOTE]
> Every price, context window and benchmark on this page was checked against vendor pages or
> independent leaderboards on 29 Sep 2026. Numbers marked "vendor" come from the maker's own launch
> table. The machine-readable copy is [`data/models.json`](./data/models.json); charts are rebuilt
> from it with `python charts/gen_charts.py`.

> [!IMPORTANT]
> **Benchmark hygiene:** Terminal-Bench, SWE-bench, GPQA and the arenas measure different things,
> and the same model scores differently under different harnesses. Compare within one chart, never
> across. Interactive per-benchmark rankings: [benchmarks.html](https://yash-awasthi.github.io/ToolkitArchive/benchmarks.html).

**Contents:** [Current lineup](#current-lineup--29-september-2026) · [Head-to-head verdict](#whos-actually-best--head-to-head-across-34-benchmarks) · [Pick one](#pick-one) · [Diffusion LLMs](#diffusion-llms-new-category) · [Typed decision models](#typed-decision-models-new-category) · [Charts](#charts) · [Superseded models](#superseded-models) · [Upcoming](#upcoming--early-stage-models) · [Release timeline](#release-timeline-2026)

---

## Current Lineup — 29 September 2026

> Everything released or repriced since the 17 Aug pass. Prices are official list prices per 1M tokens.
> Benchmark numbers are vendor launch tables unless marked; per-benchmark rankings with sources are in
> [benchmarks.html](https://yash-awasthi.github.io/ToolkitArchive/benchmarks.html). **SWE-bench Verified is retired** (Vals archived its board Sept 1)
> — the charts below still plot it, so treat them as history.

### Frontier (closed)

| Model | Released | In $/1M | Out $/1M | Context | Best at (vendor-reported) |
|---|---|---|---|---|---|
| **Claude Opus 5.5** | Sept 22 | $4 | $20 | 1M / 128K out | Terminal-Bench 4.0 66.4 (xhigh), FrontierCode 1.1 54.4 (#1), CursorBench 4.0 57.8 (#1), GDPval-AA 1846 (#1), OSWorld 2.1 81.8, HLE+tools 67.7. Anthropic: Fable-5.1-level on most work |
| **Claude Sonnet 5.5** | Sept 28 | $2 | $10 | 1M | Terminal-Bench 4.0 **70.6** (highest published), CursorBench 4.0 55.5, OSWorld 2.1 80.1. 30%+ faster than Sonnet 5 |
| **Claude Fable 5.1** | Sept 2 | $10 | $50 | 1M | SWE-bench Pro 81.2, TB 4.0 55.8. Cache reads $0.25 (−75%). Mythos 5.1 = same model, trusted-access only |
| **GPT-6 Astra** | Sept 3 | $10 | $50 | 1.05M | GPQA 96.0, FrontierMath T4 97.6, BrowseComp 91.5, AutomationBench 41.4, TB 4.0 57.9. Cached input $1 |
| **GPT-6 Sol** | Sept 22 | $2 | $10 | 1.05M | AutomationBench 33.2 at $0.27/task. Half the price GPT-5.6 Sol carried going into launch ($4/$20) |
| **GPT-6 Luna** | Sept 22 | $0.10 | $0.50 | 1.05M | Cheapest OpenAI tier; Free/Go ChatGPT desktop users get it. Luna Pro variant on OpenRouter |
| **Grok 4.7** (SpaceXAI) | Sept 21 | $2 | $6 | 500K | CursorBench 4.0 46.3, TB 4.0 38. Larger base than 4.6 |
| **Gemini 3.8 Flash** | Sept 2 | $0.75 | $3.75 | 1M / 64K out | Intro price to Dec 31 (then $1.50/$7.50). GPQA 95.3, TB 2.1 89.4. **Free on AI Studio** |
| **Muse Spark 1.3** (Meta) | Sept 2 | $1.25 | $4.25 | 1M | AA Intelligence Index #6. Cheaper "contributor" tier lets Meta keep your data |

### Open-weight / value tier

| Model | Released | In $/1M | Out $/1M | Context | Notes |
|---|---|---|---|---|---|
| **DeepSeek V4.1 Flash** | Sept 10 | **$0.15** off-peak ($0.30 peak) | **$0.60** off-peak ($1.20 peak) | 1M / 384K out | 552B MoE, 8B active in / 16B out, native vision, MIT. Id `deepseek-flash`. TB 2.1 90.6, DeepSWE 74.2, CyberGym 88.1 (vendor). Replaces V4 Flash. **Best price/performance in the archive** |
| **Kimi K3** | Jul 16 (weights Jul 27) | $3 | $15 | 1M | 2.8T params, largest open model. Modified-MIT with $20M MaaS revenue clause. Free on kimi.com and (for now) in Cline Desktop |
| **GLM-5.3** | Aug 14 (weights Aug 28) | $1.40 (cached $0.26) | $4.40 | — | TB 2.1 88.2, SWE-bench Verified 95.4 (Vals). Licence needs a security review for providers >$10B revenue. ⚠️ Don't use it via ZCode — see [NEWS.md](./NEWS.md) |
| **MiMo-V2.6 Pro / Flash** | Sept 21 | Pro $0.435 · Flash $0.14 | Pro $0.87 · Flash $0.28 | Pro 1M | MIT, omnimodal. Pro ≈ Opus 5 on agent benches (vendor). AA Index 46 |
| **Qwen 3.8-Max** | Aug 2 | $2 | $6 | 1M | SWE-bench Pro 67.7. Free on Qwen Chat |
| **Qwen3.8-Flash-Next** | Aug 26 | open weights | — | 262K (1M YaRN) | 125B / 6B active, Qwen 4 architecture preview. Runs locally (Unsloth GGUF) |
| **Laguna S 2.1 / XS 2.1** (Poolside) | Jul 21 / Jul 2 | free on OpenRouter | — | 1M / 262K | S 118B/8B active, TB 2.1 70.2. XS 33B/3B active — local. OpenMDW-1.1 |
| **Inkling / Inkling-Small** (Thinking Machines) | Jul 15 / Jul 31 | free on OpenRouter | — | 1M | 975B/41B and 276B/12B, Apache 2.0 |
| **Solar Pro 4** (Upstage) | Aug 10 | $0.30 | $1.20 | 524K | TB 2.1 57. Free in Cline and Freebuff |
| **MiniMax M3.1-Flash-Preview** | Sept 27 | not priced | — | 1M | Only inside MiniMax Code so far |

### Who's actually best — head-to-head across 34 benchmarks

[benchmarks.html](https://yash-awasthi.github.io/ToolkitArchive/benchmarks.html) now covers 34 model benchmarks (Terminal-Bench 4.0 and 2.1, SWE-bench
Pro/Verified, DeepSWE, FrontierCode, CursorBench, GPQA, HLE, FrontierMath, AIME 2026, MMLU-Pro,
BrowseComp, Toolathlon, GDPval, OSWorld, MMMU-Pro, LMArena Text + WebDev, the Artificial Analysis
Intelligence Index and more) and 58 language models, plus 4 image and video arenas. Every time two models appear on the same chart, the
higher score wins that matchup; the rating is the share of matchups won (confidence-adjusted, models
need 6+ charts to rank overall). Result on 29 Sep 2026:

| # | Model | Matchups won | Charts | Out $/1M |
|---|---|---|---|---|
| 1 | **Claude Opus 5.5** | 98% | 14 | $20 |
| 2 | Claude Sonnet 5.5 | 86% | 9 | $10 |
| 3 | GPT-6 Astra | 76% | 16 | $50 |
| 4 | Claude Fable 5.1 | 75% | 16 | $50 |
| 5 | Claude Opus 5 | 66% | 21 | $25 |
| 6 | Claude Fable 5 | 58% | 16 | — |
| 7 | **Kimi K3** (best open-weight) | 55% | 19 | $15 |
| 8 | GPT-5.6 Sol | 53% | 26 | — |
| 9 | GPT-6 Sol | 56% | 10 | $10 |
| 10 | Gemini 3.8 Flash | 51% | 8 | $3.75 |
| 11 | **DeepSeek V4.1 Flash** (best value) | 51% | 10 | $0.60 |
| 12 | Qwen3.8 Max | 50% | 8 | $6 |
| 13–16 | Opus 4.8 · GPT-5.6 Terra · DeepSeek V4 Pro · GLM-5.3 | 41–44% | 7–13 | — |

**Verdict:**
- **Best overall and best for coding: Claude Opus 5.5.** It tops FrontierCode, CursorBench, GDPval, AA-Briefcase, OSWorld 2.1, HLE (with tools), Chartography, the AA Intelligence Index and both LMArena boards, and places #2 on Terminal-Bench 4.0. Sonnet 5.5 is a close second at half the price and scores higher on Terminal-Bench 4.0 itself.
- **Hardest math and science: GPT-6 Astra.** It wins GPQA (96.0), FrontierMath Tier 4 (97.6), Terminal-Bench-Science and BrowseComp. Opus 5.5 hasn't published GPQA or FrontierMath, so this is the one area where the head-to-head can't settle it.
- **Best open-weight: Kimi K3**, with GLM-5.3, Qwen3.8 Max and MiMo-V2.6 Pro close behind on the charts they report.
- **Best value: DeepSeek V4.1 Flash.** It wins half its matchups (incl. #1 on Terminal-Bench 2.1, DeepSWE and CyberGym) at $0.60/M output — 33× cheaper than Opus 5.5.
- **Caveat:** Chinese labs mostly skip Terminal-Bench 4.0 and OSWorld, and closed labs skip AIME/MMLU-Pro, so every model is judged on the charts it chose to report. Read the per-chart detail in the HTML before a big decision.

### Pick one

| Need | Pick |
|---|---|
| Best overall / coding-agent model | **Claude Opus 5.5** ($4/$20) — #1 head-to-head; Sonnet 5.5 ($2/$10) for half the price |
| Hardest reasoning / math / research | GPT-6 Astra |
| Cheap and strong | DeepSeek V4.1 Flash ($0.60/M out off-peak) · MiMo-V2.6 Flash ($0.28) · GPT-6 Luna ($0.50) |
| Best open weights to self-host | Kimi K3 (huge) · GLM-5.3 · MiMo-V2.6 Pro · Qwen3.8-Flash-Next / Laguna XS 2.1 (single GPU) |
| Free | Gemini 3.8 Flash (AI Studio) · OpenRouter free list · Cline/Freebuff free models — see [FREE-ACCESS.md](./FREE-ACCESS.md) |

---

## Diffusion LLMs (new category)

Instead of writing one token at a time, a diffusion LLM drafts the whole answer and refines it in
parallel — much faster output at similar quality to small frontier models.

| Model | By | Speed | Price in/out per 1M | Notes |
|---|---|---|---|---|
| **Mercury 2.5** (Sept 8) | Inception Labs | ~785–1,100 tok/s | $0.20 / $0.75 (launch promo $0.04 / $0.15) | 260K ctx, 65K out. ~40% smarter than Mercury 2; comparable to GPT-5.6 Luna (low), Gemini 3.5 Flash-Lite, Haiku 4.5. On OpenRouter (`inception/mercury-2.5`) |
| **Mercury 2** | Inception Labs | sub-300 ms first token | — | First reasoning dLLM; still on OpenRouter |
| **Open dLLMs** | Research labs | — | free weights | dLLM framework (arXiv 2602.22661), Open-dLLM, LLaDA line; list at github.com/VILA-Lab/Awesome-DLMs |

Use them for autocomplete, fast edits, voice agents and anything latency-bound. For hard reasoning, stay on autoregressive frontier models.

---

## Typed Decision Models (new category)

Not chat models. They answer a typed question about a state with a calibrated probability, without generating text.

| Model | By | Speed | Price / license | Use it for |
|---|---|---|---|---|
| **Jev** | TypeSafe AI (early access Sept 15) | 70–500 ms | $0.042/M input, output free. `pip install typesafe-sdk` · `npm i @typesafe-ai/sdk` · also on Vercel AI Gateway | Routing, classification, "should the agent do X?" guardrails. Question types: Choice (≤255 options), Score (2–10 levels), Noul (yes/no). Weak at arithmetic and dates |
| **Laya** (via [laya-mlx](https://github.com/mizorewww/laya-mlx)) | Convai Innovations; community MLX port | 7–14 ms on M3 Max | Apache-2.0, local | Same job, fully on-device on Apple Silicon (`pip install laya-mlx`, macOS 14+). 6.6K★. Core ML sibling: laya-coreml (~5 ms) |

---

## Charts

![Head-to-head](./charts/head-to-head.png)

![Intelligence vs price](./charts/intelligence-vs-price.png)

![Terminal-Bench 4.0](./charts/terminal-bench-4.png)

![Context windows](./charts/context-windows.png)

> **Standardized-harness reference (vals.ai, Aug 2026 — harness-sensitive, treat as a ceiling, do NOT mix with the chart numbers):**
> GPT-5.6 Sol ~96-97% (leader) · DeepSeek V4 Pro 0813 **96.4%** · Claude Fable 5 95.0% · Kimi K3 **93.4%** ·
> GPT-5.6 Luna 93.0% · Claude Opus 4.8 88.6% · Grok 4.5 86.6%. These come from vals.ai's own
> standardized harness and run 10-15pts above the official-leaderboard / vendor numbers used in the
> charts and tables below; vals.ai itself labels them harness-sensitive. The SWE-bench Pro angle
> (Aug 2026): Claude Mythos 5 80.3% · Fable 5 80.0% · Opus 5 79.2% · Kimi K3 80.0% · Qwen 3.8-Max 67.7%.

---

## Output Cost

![Output price](./charts/output-price.png)

---

## Superseded models

These still work on their providers' APIs but have a better, usually cheaper, replacement. Old
prices and scores from earlier passes were removed rather than left to go stale — check the
provider's pricing page if you need one of them.

| Old model | Replaced by |
|---|---|
| Claude Opus 5 · Opus 4.8 · Opus 4.7 | Claude Opus 5.5 ($4/$20) |
| Claude Sonnet 5 · Sonnet 4.6 | Claude Sonnet 5.5 ($2/$10) |
| Claude Fable 5 | Claude Fable 5.1 |
| GPT-5.6 Sol / Terra · GPT-5.5 · GPT-5.4 | GPT-6 Sol ($2/$10) or GPT-6 Astra |
| GPT-5.6 Luna | GPT-6 Luna ($0.10/$0.50) |
| Gemini 3.7 / 3.6 / 3.5 Flash | Gemini 3.8 Flash |
| Grok 4.5 / 4.6 | Grok 4.7 (same $2/$6) |
| DeepSeek V4 Flash (0731) | DeepSeek V4.1 Flash — **retired**, old ids route to V4.1 Flash |
| GLM-5.1 / 5.2 | GLM-5.3 (same $1.40/$4.40) |
| Kimi K2.6 / K2.7-Code | Kimi K3 |
| MiMo V2.5 Pro | MiMo-V2.6 Pro |
| Qwen 3.7 Max | Qwen 3.8-Max |
| Muse Spark 1.1 / 1.2 | Muse Spark 1.3 |
| Solar Pro 3 | Solar Pro 4 |
| Mercury 2 | Mercury 2.5 |

---

## Upcoming & Early-Stage Models

| Model | Company | Status (29 Sep 2026) |
|---|---|---|
| **Gemini 4 Pro** | Google | In post-training, tested as "Argon". Google (Sept 24): "as soon as possible", October expected. Gemini 3.5 Pro was cancelled |
| **Claude Haiku 5.5** | Anthropic | Confirmed for "the coming weeks" |
| **Qwen 4** | Alibaba | Announced at Apsara, "very soon"; Qwen3.8-Flash-Next previews the architecture |
| **MiniMax M3.1** | MiniMax | Flash-Preview live in MiniMax Code since Sept 27; API not priced |
| **Claude Fable 5.2** | Anthropic | ⚠️ Rumour (one X account): new pretrain, end Sept / early Oct. No "Fable 5.5" exists |
| **DeepSeek V5** | DeepSeek | ⚠️ Rumour only — no announcement, roadmap or date |
| **Grok 5** | SpaceXAI | Still training, no date |
| **Kimi K3.1 · GLM-5.5** | Moonshot · Z.ai | ⚠️ Unverified leaks |

Full rumour tracker: [NEWS.md](./NEWS.md#leaks--whats-coming-verified-vs-rumour).

> Where to get these models free or cheap: [FREE-ACCESS.md](./FREE-ACCESS.md) and [STUDENTS.md](./STUDENTS.md).

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
| Aug 26–28 | Qwen3.8-Flash-Next (open, Qwen 4 preview) · GLM-5.3-Flash open · GLM-5.3 weights on HF |
| Sept 2 | Claude Fable 5.1 / Mythos 5.1 · Gemini 3.8 Flash + Flash Cyber · Muse Spark 1.3 |
| Sept 3 | **GPT-6 Astra** — $10/$50, 1.05M ctx |
| Sept 10 | **DeepSeek V4.1 Flash** — $0.15/$0.60 off-peak, vision, replaces V4 Flash |
| Sept 15 | TypeSafe **Jev** early access (typed decision model) |
| Sept 21 | Grok 4.7 · MiMo-V2.6 Pro/Flash (MIT) |
| Sept 22 | **Claude Opus 5.5** ($4/$20) · **GPT-6 Sol/Luna** ($2/$10, $0.10/$0.50) |
| Sept 27 | MiniMax M3.1-Flash-Preview (MiniMax Code only) |
| Sept 28 | **Claude Sonnet 5.5** ($2/$10) |
