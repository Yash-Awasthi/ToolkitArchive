# 📰 Latest News — re-checked 29 September 2026

<p align="center"><a href="./README.md">🏠 Home</a> · <a href="https://yash-awasthi.github.io/ToolkitArchive/">🔎 Explorer</a> · <a href="https://yash-awasthi.github.io/ToolkitArchive/benchmarks.html">📊 Benchmarks</a> · <a href="./NEWS.md">📰 News</a> · <a href="./STUDENTS.md">🎓 $0 guide</a> · <a href="./FREE-ACCESS.md">🆓 Free AI</a></p>


> What changed between 17 August and 29 September 2026, distilled. Vendor-reported numbers are
> labelled as such. Full benchmark tables live in [benchmarks.html](https://yash-awasthi.github.io/ToolkitArchive/benchmarks.html).
> See also [MODELS.md](./MODELS.md).

**Contents:** [⚠️ Security alert](#security-alert-do-not-use-zcode) · [Frontier models](#frontier-model-releases) ·
[Open-weight models](#open-weight--cheap-models) · [Agents & tools](#coding-agents--tools) ·
[Free access](#free-ai-access-news) · [Leaks](#leaks--whats-coming-verified-vs-rumour) · [Tools wave](#tools-skills--mcps-wave) · [New categories](#new-category-typed-decision-models) · [Corrections](#corrections-to-earlier-passes)

---

## Security alert: do not use ZCode

**ZCode (Z.ai's free desktop coding agent) silently uploaded users' workspaces.** Disclosed Sept 18 by
developer *ferstar*: the default-on Codebase Indexing / Repo Wiki feature packed whole repositories —
including full Git history (so secrets deleted in old commits too), large-file caches, and in one
reported case database passwords and employee data — encrypted them with a key only Z.ai holds, and
uploaded them to an Alibaba Cloud bucket (`zcode-prod`). One report counted 564 upload attempts of a
313 MB archive. There was no setting to turn it off and the privacy policy did not mention it.

- Z.ai disabled the feature Sept 21 (v3.14.0 removes the upload pipeline and Repo Wiki), apologised,
  said the data was "never used for training", and open-sourced ZCode on Sept 22 — but with the commit
  history wiped, so the uploading code can't be audited. No count of affected workspaces has been published.
- **If you ran ZCode on a real repo:** assume that repo, its full history, and every secret ever
  committed to it has left your machine. Rotate those credentials.
- The GLM **models** themselves (API, open weights, chat.z.ai) are a separate matter — this incident
  is about the ZCode client. This archive no longer recommends ZCode anywhere.
- Sources: tomshardware.com · thenextweb.com (open-source/commit-history piece) · caixinglobal.com (Sept 22) · esecurityplanet.com

---

## Frontier model releases

| Date | Model | Price in/out per 1M | Key facts |
|---|---|---|---|
| Sept 28 | **Claude Sonnet 5.5** (Anthropic) | $2 / $10 (cache read $0.20) | Terminal-Bench 4.0 **70.6%** (Sonnet 5: 10.3%), CursorBench 4.0 55.5%, OSWorld 2.1 80.1%. 30%+ faster than Sonnet 5, fewer tokens per task. `claude-sonnet-5-5`. **Haiku 5.5 "in the coming weeks."** |
| Sept 22 | **Claude Opus 5.5** (Anthropic) | **$4 / $20** (cache read $0.20) | Cut from Opus 5's $5/$25. 1M ctx, 128K output, always-on adaptive thinking. Anthropic: "performs at the level of Fable 5.1 on most work", ~40% cheaper than Opus 5 on typical workloads. Leads Terminal-Bench 4.0 (66.4%), FrontierCode 1.1 (54.4%), GDPval-AA v2.1 (1846). Default Opus on Pro/Max/Team/Enterprise |
| Sept 22 | **GPT-6 Sol** + **GPT-6 Luna** (OpenAI) | Sol **$2 / $10** · Luna **$0.10 / $0.50** | Permanent 50%+ cut vs GPT-5.6 Sol/Luna. In API, ChatGPT Work, Codex. Luna reaches Free/Go users in the desktop app. **GPT-6 Luna Pro** also listed on OpenRouter Sept 22. Astra price unchanged |
| Sept 21 | **Grok 4.7** (SpaceXAI) | $2 / $6 | Larger base model than 4.6, same price. 500K ctx. CursorBench 4.0 46.3% (4.6: 40.4%). In Cursor, Grok Build, Copilot, API |
| Sept 3 | **GPT-6 Astra** (OpenAI) | $10 / $50 (cached $1) | Flagship, 1.05M ctx. Leads GPQA (96.0), FrontierMath T4 (97.6), BrowseComp (91.5), Terminal-Bench-Science. Also on Azure Foundry + Bedrock |
| Sept 2 | **Claude Fable 5.1 / Mythos 5.1** (Anthropic) | $10 / $50 (cache read $0.25, −75%) | Same model; Mythos 5.1 = fewer safeguards, trusted-access programs only. Fable 5.1 is on paid Claude plans |
| Sept 2 | **Gemini 3.8 Flash** + 3.8 Flash Cyber (Google) | $0.75 / $3.75 intro to Dec 31, then $1.50 / $7.50 | 1M ctx, 64K out. **Free tier on AI Studio** (data used for training). Added to Antigravity free plan Sept 1 |
| Sept 2 | **Muse Spark 1.3** (Meta) | $1.25 / $4.25 (private tier) | ~20% fewer tool calls, ~25% fewer tokens than 1.2. 1M ctx. Cheaper "contributor" tier lets Meta keep your data. In Muse Code + Meta Model API |

**Coming:** Gemini 4 Pro — Google says "as soon as possible", checkpoints tested as "Argon" since mid-Sept,
October most likely. **Gemini 3.5 Pro was cancelled** (never shipped). Qwen 4 "very soon" (Apsara, no date).
Claude Haiku 5.5 "coming weeks". MiniMax M3.1 full release (only Flash-Preview so far).

Sources: anthropic.com/claude-sonnet-5-5 · anthropic.com/news · venturebeat.com (GPT-6 Sol/Luna) · marktechpost.com (Grok 4.7, Sept 21) · research.meta.ai (Muse Spark 1.3) · ai.google.dev pricing · 9to5google.com (Gemini 4, Sept 24)

---

## Open-weight / cheap models

| Date | Model | Price in/out per 1M | Key facts |
|---|---|---|---|
| Sept 27 | **MiniMax M3.1-Flash-Preview** | not priced yet | 1M ctx coding model, **only inside MiniMax Code** for now; five effort levels. Double sign-in credits Sept 28–Oct 7. Widely believed to be the stealth "Space Bunny Alpha" on OpenRouter (tokenizer tests; unconfirmed) |
| Sept 21 | **Xiaomi MiMo-V2.6 Pro / Flash** | Pro $0.435 / $0.87 · Flash $0.14 / $0.28 | MIT, open weights (+ a 9B research model + RL recipes). Omnimodal. Pro ≈ Opus 5 / GPT-5.6 Sol on agent benches (vendor); AA Intelligence Index 46 |
| Sept 20 | **Qwen-Image-2.1** | — | 7B open image model with native transparency; non-commercial licence |
| Sept 10 | **DeepSeek V4.1 Flash** | **$0.15 / $0.60 off-peak** ($0.30 / $1.20 peak) | 552B MoE, 8B active in / 16B out, 1M ctx, 384K max out, **native vision**, MIT. Model id `deepseek-flash`. Beats V4-Pro on most vendor benches at a fraction of the price. Retires V4-Flash and V4-Flash-Vision-Exp. **V4-Pro stays live** — DeepSeek reversed its Sept 14 phase-out on Sept 11 |
| Aug 28 | **GLM-5.3** weights on HF | API $1.40 / $4.40 class | Open weights delayed ~2 weeks for a cyber-capability review (found 2,436 real vulns in 269 OSS projects). New licence: security review needed for providers above $10B revenue. GLM-5.3-Flash open since Aug 26 |
| Aug 26 | **Qwen3.8-Flash-Next** | open weights | 125B MoE / 6B active, 262K native (1M with YaRN), text+image+video. Preview of the Qwen 4 architecture (Gated DeltaNet + sparse attention) |
| Jul–Aug | **Kimi K3** (Moonshot) | $3 / $15 official | 2.8T params, largest open-weight model; weights Jul 27 under a modified-MIT licence with a $20M MaaS revenue clause. **Free on kimi.com** |
| Jul–Aug | **Poolside Laguna S 2.1 / XS 2.1** | **free on OpenRouter** | S: 118B / 8B active, 1M ctx, TB 2.1 70.2%. XS: 33B / 3B active, runs locally. Both OpenMDW-1.1 (fully permissive) |
| Jul–Aug | **Thinking Machines Inkling / Inkling-Small** | free on OpenRouter | Mira Murati's lab. Inkling 975B / 41B active, Inkling-Small 276B / 12B active, Apache 2.0, 1M ctx |
| Aug 10 | **Upstage Solar Pro 4** | $0.30 / $1.20 | 524K ctx, TB 2.1 57%. Free in Cline and Freebuff |

Sources: api-docs.deepseek.com (changelog + pricing) · siliconangle.com (Sept 10) · mimo.mi.com · eweek.com · pandaily.com (M3.1) · huggingface.co/Qwen/Qwen3.8-Flash-Next · thinkingmachines.ai · poolside.ai · upstage.ai

---

## Coding agents & tools

- **Claude Code** — Opus 5.5 is the default Opus on every paid plan. Five-hour limits raised on
  Pro/Max/Team/Enterprise on Sept 22 plus a one-time saved rate-limit reset; weekly limits got a
  permanent +25% over the old baseline on Sept 14. **Plugins** are now the official third-party
  extension format (directory, validation, analytics) with MCP 2.0 + MCP Apps support.
  Plans: Pro $17/mo annual ($20 monthly) · Max 5x $100 · Max 20x $200.
- **Codex (OpenAI)** — GPT-6 Sol/Luna in Codex (Sept 22), Bedrock support in the CLI, fullscreen
  `/tui`, voice on by default, `/usage` dashboard, worktree sessions by default.
- **Cursor is now owned by SpaceX** ($60B, closed Aug 14). Grok 4.5/4.6/4.7 and Composer 2.5 are
  Cursor's "first-party" models; plans now have two usage pools (first-party vs third-party models).
  Prices unchanged: Hobby free · Pro $20 · Pro+ $60 · Ultra $200 · Teams $40.
- **Cline Desktop** (Sept 14, beta, macOS/Windows, open source) — imports sessions from Claude Code /
  Codex, cron-scheduled jobs, parallel sessions. **ClinePass $9.99/mo** covers 13 open-weight models
  (Z.ai, Moonshot, DeepSeek, MiniMax, MiMo, Qwen). **Kimi K3 free in Cline Desktop** since Sept 18
  ("as long as we can").
- **GitHub Copilot** — Opus 5.5 + GPT-6 Sol (Pro+/Max/Business/Enterprise), GPT-6 Luna + Grok 4.7
  (from Pro). Auto model selection now has efficiency / balance / intelligence tiers. Local
  sandboxing for agents in public preview.
- **Muse Code** (Meta) — now runs Muse Spark 1.3 with max reasoning.
- **Kimi Code CLI 2.1.0** (Sept 23) · **MiniMax Code** gets M3.1-Flash-Preview · **Grok Build** gets Grok 4.7.
- **OpenCode** — Entra ID sign-in for Azure, session JSON export, V1/V2 config compatibility.
  ⚠️ OpenCode V2 can't reach Zen free models (Big Pickle etc.) yet — open issue #49908.
- **Hermes Agent v0.21.x** (Sept) — desktop app, Bot Mode, agent group chats, A2A. **OpenClaw 2.0**
  (Aug 30) — shared cloud sessions, rebuilt Control UI, automatic skill learning.
- **Antigravity** — free Individual plan still $0 with weekly agent limits; Gemini 3.8 Flash added Sept 1.
- **Terminal-Bench 4.0** is now the live terminal benchmark (66 tasks, flat 8-hour timeout). TB 2.1 is
  saturated (top models ~88-90%) — see [AGENTS.md](./AGENTS.md#terminal-bench-40).

---

## Free AI access news

| Item | What's free | Caveats |
|---|---|---|
| **Cline free models** | DeepSeek V4.1 Flash, Muse Spark 1.3 (contributor tier), GLM-5.3-Flash, Solar Pro 4, Laguna S 2.1, **Kimi K3 (Cline Desktop)** | Rotating, quota-limited, IDE extension + CLI + Desktop only (not the Cline API). Muse "contributor" tier = Meta keeps your data |
| **Freebuff** (Codebuff team, YC) | 100 "Freebucks"/day: GLM-5.3 Flash 20 h, Solar Mini 4 20 h, MiMo 2.6 Flash 10 h, Solar Pro 4 10 h, **DeepSeek V4.1 Flash 6 h, GPT-6 Luna 5 h**, MiMo 2.6 Pro 3 h; Space Bunny Alpha unlimited | Ad-supported. CLI (`npm i -g freebuff`), desktop, web builder, cloud IDE, chat. Gemini 3.8 Flash / Muse Spark need a paid plan |
| **OpenRouter free list** | Space Bunny Alpha (1M ctx, stealth), Nemotron 3 Ultra, Laguna S/XS 2.1, Inkling + Inkling Small, Qwen3.8 27B, Nemotron 3.5 Lightning, Dots3-Note, Ling 3.0 Flash, North Mini Code | Laguna/Liquid/stealth models may train on your prompts. 50 req/day under $10 lifetime spend, 1,000 at $10+ |
| **TokenRa** (tokenra.io) | **Union Alpha** (262K, multimodal, stealth) and **Ox Alpha** (1M ctx) — both $0 | Stealth models on shared capacity; Union Alpha ~17 s P50 latency, ~14 tok/s — batch jobs only. Works in OpenCode/Cline natively. Keys start `sk-or-v1-` |
| **Token Harbor** (tokenharbor.ai) | **`deepseek-v4.1-flash:free`**, **`qwen3.8-flash:free`**, **`mimo-v2.6-flash:free`** — never billed, draw on a free allowance | OpenAI + Anthropic compatible, base URL `https://tokenharbor.ai/v1`. Allowance size not published (reviews say ~150 req/day). Singapore company |
| **TokenRouter** | $0 model IDs incl. `deepseek/deepseek-v4-pro-0813-free`, `qwen/qwen3.8-max-free` | Free capacity limited, "stability and concurrency not guaranteed" |
| **Gemini 3.8 Flash** | Free tier on AI Studio / Gemini API | Free-tier data used to improve Google products |
| **GPT-6 Luna** | Free/Go ChatGPT users (desktop app), 5 h/day on Freebuff | — |
| **Kilo Code** | `kilo-auto/free` router, Space Bunny Alpha, Laguna M.1, Nemotron 3 Ultra | 200 req/h anonymous |
| **GitHub Copilot Free** | Haiku 4.5, GPT-5 mini, agent mode, CLI | 2,000 completions/mo |

---

> **Best way to use free models:** OpenCode with any OpenAI-compatible key (Token Harbor, TokenRa, OpenRouter, Groq) — see [FREE-ACCESS.md](./FREE-ACCESS.md#how-to-use-all-of-this-opencode--any-openai-compatible-key).

## Leaks & what's coming (verified vs rumour)

| Item | Status on 29 Sep 2026 | Evidence |
|---|---|---|
| **OpenAI DevDay — "20+ launches"** | **Happening today (Sept 29, San Francisco).** OpenAI's Tibo Sottiaux said GPT-6 Astra's productivity boost enabled 20 launches across 22 sessions. Confirmed so far: **Images 2.5** and **ChatGPT for Financial Services**. Already shipped this month: GPT-6 Astra (Sept 3), Agents API public beta (Sept 10), GPT-6 Sol/Luna (Sept 22) | cryptobriefing.com · openai.com/devday |
| **OpenAI "o" always-on agent** (a.k.a. "Aeon", "Orbit", "dots") | ⚠️ Rumour. Cloud agent that runs continuously, has its own email address, for all Pro tiers incl. $100. Also rumoured: Cerebras-powered "Fast Mode" on a $500 plan, and a shared message board for agents. Only config strings seen — no product page, price or model id | orcarouter.ai · Reddit r/singularity |
| **"Fable 5.5"** | ❌ No such leak. The rumour is **Fable 5.2** — a new pretrain, "end of Sept or early Oct", from one X account (@kimmonismus). Polymarket 53% by Oct 31; Manifold 25% before Oct 1 | cellcog.ai |
| **Claude Haiku 5.5** | ✅ Confirmed by Anthropic for "the coming weeks" | anthropic.com |
| **DeepSeek V5** | ⚠️ Rumour only. X posts said "next week" in early September; nothing shipped. DeepSeek has no announced V5, roadmap or date | deepseek.ai blog · news roundups |
| **Gemini 4 Pro** | ✅ Coming ("as soon as possible", Google, Sept 24; tested as "Argon"). ⚠️ Leaked benchmark sheet (DeepSWE 88.7, TB 2.1 95.3) is unverified | 9to5google.com · Reddit |
| **Qwen 4** | ✅ Announced at Apsara (in training, "very soon", Qwen 4.5/5 to reach 5–10T params). No date | Reddit r/LocalLLaMA · Yotta Labs |
| **Kimi K3.1** | ⚠️ Leak: pruned chain-of-thought to cut token waste on the 2.8T base | towardsai.net |
| **GLM-5.5** | ⚠️ Old leak (July) claiming Fable-5 level; Z.ai shipped GLM-5.3 instead | cellcog.ai |
| **Grok 5** | Still training, no date (Musk: 6T params claimed). Grok got a new autoregressive image model ("Aurora" update) this month | x.ai/news |
| **MiniMax M3.1** | ✅ Flash-Preview live in MiniMax Code; full API pending | pandaily.com |

> Rule of thumb: a leak becomes a row in [MODELS.md](./MODELS.md) only once there's a model id, a price, or an official post.

---

## Tools, skills & MCPs wave

Full tables with install commands: [SKILLS.md](./SKILLS.md#new-skills-plugins--mcps--sept-2026-wave).

- **Design taste skills went mainstream:** Impeccable (72K★), Taste Skill (91K★), Emil Kowalski's skills, UI UX Pro Max, and `DESIGN.md` (Google Stitch's open format; VoltAgent's awesome-design-md has files from 59+ real sites).
- **Design tools opened to agents:** Figma MCP can now write to the canvas (beta, paid seats); Paper and Pencil are agent-native design canvases; Claude Design (Anthropic Labs) makes prototypes and slides.
- **Motion:** official Motion AI Kit (skill + MCP) and GSAP skills; Remotion skills for video-from-code; Anime.js and Three.js skills.
- **Browsing:** Playwright MCP + CLI now ship inside Playwright itself; Chrome DevTools MCP attaches to your live Chrome; Browser Harness (self-healing CDP harness); Agent-Reach (86K★, free Twitter/Reddit/YouTube/XiaoHongShu access); Vercel agent-browser; Stagehand v3.
- **Dev & memory:** Context7 and Serena MCPs, ECC (269K★), GSD (64K★), claude-mem (95K★), Hindsight, OpenMemory; Paperclip (93K★) runs a company of agents; Google open-sourced `ax` / Agent Executor.
- **New model types:** Mercury 2.5 diffusion LLM (Sept 8, ~760 tok/s measured, $0.25/$0.75, AA Index 12) and Jev typed decisions — see [MODELS.md](./MODELS.md#diffusion-llms-new-category).
- **Local:** LM Studio **Bionic** — a free agent app for open models (code + documents + transcription).
- **Media:** GPT Image 2.5 (Sept 8) in ChatGPT free; Sakana Fugu Ultra v2 (Sept 11) orchestrates many models behind one API.

---

## New category: typed decision models

- **Jev** (TypeSafe AI, early access Sept 15) — a "System One" model that doesn't generate text. You
  ask a typed question (Choice among up to 255 options, Score on a 2–10 scale, or Noul yes/no) against
  a state and get back a calibrated probability in 70–500 ms. $0.042/M input, output free.
  `pip install typesafe-sdk` · `npm i @typesafe-ai/sdk`. Can't do arithmetic or dates; accuracy drops
  as the state fills with noise. Use it for routing, classification, and agent guardrails, not generation.
- **laya-mlx** (github.com/mizorewww/laya-mlx, 6.6K★, Apache-2.0) — an independent MLX port of
  Convai Innovations' **Laya** typed-decision models: 7–14 ms per decision on an M3 Max, no PyTorch, no
  cloud. `pip install laya-mlx` (Apple Silicon, macOS 14+, Python 3.11+). Sibling: laya-coreml (~5 ms on the Neural Engine).

---

## Corrections to earlier passes

- **Gemini CLI *was* retired for free and Pro/Ultra users on June 18, 2026.** The 17 Aug pass "corrected"
  this as an unverified aggregator claim — that was wrong. Google's own Developers Blog (May 19) says Gemini
  CLI stopped serving free and AI Pro/Ultra users on June 18 and moved them to **Antigravity CLI**; it keeps
  working only with paid Gemini API keys and enterprise licences. Fixed across the archive.
- **Claude Max 20x is $200/mo** — confirmed by multiple Sept pricing write-ups; the "unverified" hedge is gone.
- **SWE-bench Verified is archived** — Vals froze its board Sept 1. The model charts in this repo still
  plot SWE-bench Verified; treat them as history and use [benchmarks.html](https://yash-awasthi.github.io/ToolkitArchive/benchmarks.html) for current rankings.
