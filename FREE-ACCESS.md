# Free API Access & Model Access — re-checked 29 September 2026

<p align="center"><a href="./README.md">🏠 Home</a> · <a href="https://yash-awasthi.github.io/ToolkitArchive/">🔎 Explorer</a> · <a href="https://yash-awasthi.github.io/ToolkitArchive/benchmarks.html">📊 Benchmarks</a> · <a href="./NEWS.md">📰 News</a> · <a href="./STUDENTS.md">🎓 $0 guide</a> · <a href="./FREE-ACCESS.md">🆓 Free AI</a></p>


> Permanent free API tiers below. For **trial-credit stacking, student/startup programs, free GPU, and subscription-as-API tricks** → [CREDITS.md](./CREDITS.md).
> 🔄 **29 Sep 2026 pass:** added the [September free wave](#september-2026-free-wave-start-here) (Cline free models, Freebuff, OpenRouter's new free list, TokenRa stealth models, Token Harbor, TokenRouter free IDs, Gemini 3.8 Flash on AI Studio, Kimi K3 free), and **removed ZCode** — it silently uploaded users' repositories (see [NEWS.md](./NEWS.md)).
>
> ✅ **Re-checked Aug 17, 2026** (prior pass: June 27, 2026; first Aug pass: Aug 16) — free tiers change weekly; confirm before relying. This pass added the August wave of free-AI offers surfaced on Reddit/Instagram and verified against live pages (OmniRoute, aerolink.lat, NaraRouter, LongCat-2.0, GoRouter, Tokeness, OpenRouter Fusion), upgraded the AgentRouter/Bluesminds rows from "unverified" to caveated, and added **ZCode** (GLM-5.3 free on it since Aug 16-17). Not every row was independently re-fetched this pass; where a number wasn't re-confirmed, the row says so.

---

**Contents:** [Sept 2026 free wave](#september-2026-free-wave-start-here) · [Table 1 no-card API tiers](#table-1--no-card-api-access-ongoing-free-tiers-and-clearly-labelled-trials) ·
[Table 1B hidden gems](#table-1b--hidden-gems--decentralized--obscure-free-providers) ·
[Aggregators](#aggregators-route-across-many-free-tiers-with-one-key) · [Chinese routers](#chinese-credit-routers--gateways-community-reported--all-unverified) ·
[Table 2 trial credits](#table-2--trial-credits-stack-these) · [Claude Opus 5 free](#how-to-access-claude-opus-5-for-free) ·
[TokenLB caveat](#tokenlb--api-marketplace--developer-credits-caveat-demoted-this-pass) ·
[Best model by use case](#best-free-model-by-use-case) · [Quick start code](#quick-start-code) · [Useful repos](#useful-repos)

---

## September 2026 free wave (start here)

> Checked against live pages on 29 Sep 2026 unless marked. Free promos rotate weekly — treat every
> quota as a snapshot. Stealth and "free" models often log or train on your prompts: keep secrets out.

### How to use all of this: OpenCode + any OpenAI-compatible key

**OpenCode is the best harness for free models** — it takes any OpenAI-compatible base URL + key,
ships with 75+ providers (TokenRa, OpenRouter, Groq, etc. via `/connect`), and has its own Zen free
models. Put a free key from the tables below into OpenCode (or Cline / Kilo) and swap models per task.

```jsonc
// opencode.json — any OpenAI-compatible free endpoint
{
  "provider": {
    "tokenharbor": {
      "npm": "@ai-sdk/openai-compatible",
      "options": { "baseURL": "https://tokenharbor.ai/v1", "apiKey": "{env:TOKENHARBOR_API_KEY}" },
      "models": { "deepseek-v4.1-flash:free": {}, "qwen3.8-flash:free": {}, "mimo-v2.6-flash:free": {} }
    }
  }
}
```

### Free coding agents with free models built in

| Tool | Free models (Sept 2026) | Limits | Catch |
|---|---|---|---|
| ★ **Cline** (VS Code / JetBrains / CLI / **Cline Desktop**) | DeepSeek V4.1 Flash, Muse Spark 1.3 (contributor), GLM-5.3-Flash, Solar Pro 4, Laguna S 2.1 — plus **Kimi K3 free in Cline Desktop** since Sept 18 | Per-model quota; the picker shows "(free)" and a reset time when you run out | Rotating promos, not available through the Cline API. Muse "contributor" tier = Meta keeps your data. ClinePass $9.99/mo raises quotas 2–5× |
| ★ **Freebuff** (`npm i -g freebuff`) | 100 "Freebucks"/day: GLM-5.3 Flash 20 h · Solar Mini 4 20 h · MiMo 2.6 Flash 10 h · Solar Pro 4 10 h · **DeepSeek V4.1 Flash 6 h** · **GPT-6 Luna 5 h** · MiMo 2.6 Pro 3 h · Space Bunny Alpha unlimited | Daily allowance | Text ads in the UI. Gemini 3.8 Flash and Muse Spark are paid-plan only. Apache 2.0, Codebuff team (YC) |
| **OpenCode Zen** | Big Pickle (stealth, 200K), Nemotron 3 Super Free, MiMo Flash Free, MiniMax Free, GPT-5 Nano | Rotating | Free models may train on your data. ⚠️ OpenCode V2 can't reach Zen free models yet (issue #49908) — stay on V1 for them |
| **Kilo Code** | `kilo-auto/free` auto-router; Space Bunny Alpha, Laguna M.1, Nemotron 3 Ultra, Step 3.7 Flash, MiniMax/GLM free models | Anonymous 200 req/h per IP | Free models rotate; some log prompts |
| **GitHub Copilot Free** | Haiku 4.5, GPT-5 mini and a few more; agent mode, Copilot CLI, MCP | 2,000 completions/mo + small AI-credit allowance | Opus 5.5 / GPT-6 Sol need Pro+ ($39) |
| **Codex / ChatGPT Free & Go** | GPT-6 Luna (desktop app) | Plan limits | Sol/Astra need Plus or higher |
| **Antigravity** (Google) | Gemini 3.8 / 3.7 Flash, 3.1 Pro, Claude Sonnet/Opus 4.6, gpt-oss-120b | Weekly agent limits; Tab + Command unlimited | Replaced Gemini CLI's free tier on June 18 |
| **Muse Code** / **MiniMax Code** / **Grok Build** | Muse Spark 1.3 · M3.1-Flash-Preview (double sign-in credits Sept 28–Oct 7) · Grok 4.7 | Varies | Vendor lock-in; free tiers are promotional |

### Free models over an API

| Where | Free models | Limits / catch |
|---|---|---|
| ★ **Google AI Studio** | **Gemini 3.8 Flash (Sept 2)**, 3.7 Flash, 3.1 Flash, Flash Lite | ~15 | ~1,500 | ~750K | **Best free tier, no card.** Multimodal, 1M ctx. Free-tier prompts are used to improve Google products. Not available EU/UK. RPM/RPD/token numbers are from a prior pass — check aistudio.google.com/rate-limit |
| ★ **OpenRouter free collection** | **Space Bunny Alpha** (stealth, 1M ctx, 524K out, multimodal — probably MiniMax M3.1, unconfirmed), **Nemotron 3 Ultra** (1M), **Laguna S 2.1** (262K) + **Laguna XS 2.1**, **Inkling** + **Inkling Small** (1.05M), **Qwen3.8 27B**, Nemotron 3.5 Lightning, Nemotron 3 Super, Nemotron 3 Nano Omni, Dots3-Note Preview (512K), Ling 3.0 Flash, Cohere North Mini Code, LFM2.5-2.6B | 50 req/day under $10 lifetime spend, 1,000/day at $10+. Laguna, Liquid and stealth providers may train on inputs |
| **TokenRa** (tokenra.io) | **Union Alpha** (`union-alpha`, 262K, text+image) · **Ox Alpha** (1M ctx, 128K out, text+image+video) | $0 today, "may change". Anonymous providers on shared capacity — Union Alpha ~17 s P50, ~14 tok/s, so batch jobs only. Built into OpenCode (`/connect` → TokenRa) and Cline. Keys start `sk-or-v1-` |
| **TokenRouter** | `deepseek/deepseek-v4-pro-0813-free`, `qwen/qwen3.8-max-free`, `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | "Free compute capacity is limited; stability and concurrency not guaranteed." Paid models billed at list with no markup |
| ★ **Token Harbor** (tokenharbor.ai) | **`deepseek-v4.1-flash:free`** (1M ctx, 128K out, text+image) · **`qwen3.8-flash:free`** (984K ctx) · **`mimo-v2.6-flash:free`** | Free-tier IDs "use the free allowance and are never billed". Base URL `https://tokenharbor.ai/v1`, OpenAI- and Anthropic-compatible. Review sites report 20 RPM / 150 req/day (1,500 with $10+ balance) and a $5 signup credit — not on its own site. Singapore company (Token Harbor PTE. LTD.) |
| **Groq** | Qwen 3.8 27B added: 30 RPM, 1,000 req/day, 200K tokens/day | Per-model limits, check the live table |
| **Venice.ai** | Free daily allowance + 500 welcome credits, no card; lists Opus 5.5 among paid models | Credits run out fast on frontier models |
| **Kimi K3** | Free on kimi.com (chat) and in Cline Desktop | API itself is $3/$15 |
| **GPT-6 Luna** | Free/Go ChatGPT users in the desktop app; 5 h/day in Freebuff | API $0.10/$0.50 — nearly free anyway |

### Community-reported (⚠️ unverified — leads from social media, check before use)

| Name | Claim | Source |
|---|---|---|
| **TabiToken** | $120 signup credit via referral (GitHub account 1+ year old), $20 per referral | gist Soheel-1 (Aug 29) |
| **JustWoker** | $70–100 credit | same gist |
| **VyceAI** | $40 credit | same gist |
| **AgentRouter** | Now reported as $50 (was $100–200) | same gist — amounts keep shrinking |
| **AtomCode** (AtomGit) | Free 30-day coding plan, 5-hour quota windows, 1,000 claims/day | mvalentsev/awesome-free-ai-coding |
| **Autohand Code** | Free plan on its own coding model, no card | same list |
| **CodeCraft API** | "Free 1M tokens of Opus 5.5" | YouTube only — treat as bait until proven |

> Commenters on these gists warn that paid token prices on several of these gateways are high once the free credit runs out. Never give them a key or repo you care about.

### Cheapest paid (when free runs out)

| Model | $/1M in / out | Why |
|---|---|---|
| **DeepSeek V4.1 Flash** | $0.15 / $0.60 off-peak (peak Mon–Fri 01–04 & 06–10 UTC: $0.30 / $1.20) | 1M ctx, vision, beats V4-Pro on vendor benches |
| **GPT-6 Luna** | $0.10 / $0.50 | Cheapest frontier-lab model |
| **MiMo-V2.6 Flash** | $0.14 / $0.28 | MIT, open weights |

---

## Table 1 — No-card API access (ongoing free tiers and clearly labelled trials)

All endpoints are OpenAI SDK-compatible unless noted.

| Provider | Best Free Models | RPM | RPD | Daily Tokens | Notes |
|---|---|---|---|---|---|
| ★ **Google AI Studio** | **Gemini 3.7 Flash (new Aug 13)**, 3.5 Flash, 3.1 Flash (74%), Flash Lite | ~15 | ~1,500 | ~750K | **Best free tier, no card.** Multimodal. Gemini 3.7 Flash confirmed on the free AI Studio tier this pass (ai.google.dev pricing page, free daily quota). Not available EU/UK. The exact RPM/RPD/token numbers are from a prior pass, not re-confirmed this pass — check aistudio.google.com/rate-limit before relying on them |
| ★ **Groq** | Llama 3.3 70B, gpt-oss-120b/20b, Qwen3.6 27B | 30 | model-specific | model-specific | Free-plan limits re-checked. Examples: Llama 3.3 = 1K RPD / 100K TPD; gpt-oss-120b = 1K RPD / 200K TPD. Limits are organization-wide and can change; use Groq's live limits page for the model you choose |
| ★ **OpenRouter `:free`** | Qwen3-Coder (78%), gpt-oss-120b, Nemotron Ultra 550B, check openrouter.ai/models live for the current free-model count — it rotates weekly and static counts (16/22/27/29) all disagree across sources | 20 | 50 | — | 50 RPD under $10 lifetime spend, 1,000 RPD at $10+. Corrected from a prior flat "200" — the real limit is a two-tier split. Single key. **Fusion API** (Jun 12, 2026) sends one prompt to a panel of models + a judge model and returns the fused best answer — usable with free models |
| ★ **Cloudflare Workers AI** | Llama 3.3 70B, Llama 4 Scout, Kimi K2.7, Gemma 4 26B, GLM-4.7-Flash, 50+ models | — | — | 10,000 neurons/day, no card, resets 00:00 UTC | Edge-distributed, serverless, global. $0.011/1K neurons past the free quota. Some models require a paid billing account attached regardless of remaining quota — check the model page before assuming a given model is reachable free |
| ★ **NVIDIA NIM** | Nemotron 3 Super, Nemotron 3 Ultra, DeepSeek-R1, Llama 405B, MiniMax M2.7, 100+ | ~40 | — | — | build.nvidia.com. NVIDIA Dev Program |
| ★ **GitHub Models** | gpt-5, gpt-4.1, gpt-4o, o4-mini, Llama 4 Scout, DeepSeek-R1, 45+ | 10–15 | 50–150 | — | GitHub account only. 8K in / 4K out per req |
| ★ **Z.AI** | GLM-4.7-Flash, GLM-4.6V-Flash (vision) | 1 concurrent | — | — | open.bigmodel.cn. Permanent free |
| ★ **Mistral** | Mistral Medium 3.5 (128B), Mistral Small 4, Codestral | ~1 RPS | — | 500K | Non-commercial, EU-hosted. The "~1B tokens/month" Experiment-tier figure is unverified — only partially confirmed by a primary source (the free chat plan with $10/mo API credit is real; the exact monthly token ceiling is not), don't treat it as a fixed number |
| ★ **SambaNova** | DeepSeek-V3.1/V3.2, Llama 3.3 70B, gpt-oss-120b, MiniMax M2.7, Gemma 4 31B | 20 | 20 | 200K | RDU hardware. Ultra-fast. No card required |
| ★ **HuggingFace Inference Providers** | 200+ open models via Fireworks/Together/Hyperbolic/DeepInfra — DeepSeek V4 (incl. DSpark), Qwen, Llama, Kimi, Gemma | Credit-metered | — | **$0.10/mo free credits** (free users; PRO $2/mo; Team/Enterprise $2/seat) | Corrected this pass: the prior "100K credits/mo" was stale — current official pricing is $0.10 monthly credits for free users (huggingface.co/docs/inference-providers/en/pricing). No markup, routes to best provider automatically; pay-as-you-go past the credits. **DeepSeek DSpark** (V4-Pro/V4-Flash-DSpark) is also served — same model + speculative-decoding module, 50-600% faster |
| **Puter.js** | GLM-5.2 (1M ctx), GLM-5.1, GLM-4.7-Flash | — | — | — | Free unlimited via Puter SDK. User-pays model |
| **OVHcloud AI Endpoints** | Qwen3.5-397B, gpt-oss-120b, Llama 3.3 70B, Qwen3-Coder, 13+ EU models | 2/IP | — | — | **No signup, no key.** EU-hosted. GDPR. Anonymous |
| **BazaarLink** | `auto:free` → best available free model (Llama/Gemma/Qwen/DeepSeek) | 10 | 150 | — | **No card, no trial expiry.** OpenAI-compatible (`sk-bl-`). Agent self-registration endpoint. TW-based |
| **Pollinations.AI** | Text + image + audio + video, one API | — | — | — | **Zero-auth, no signup.** Server keys unmetered (client keys 1 req/hr/IP). Also in Table 1B |
| **LLM7.io** | DeepSeek-R1, DeepSeek-V3, Gemini Flash Lite, GPT-4o-mini, Qwen2.5-Coder, 30+ | 30 | — | — | **Zero registration** for basic. GDPR-compliant |
| **SiliconFlow** | Qwen3-8B, DeepSeek-R1-Distill-Qwen-7B | 30 | — | 60K TPM | Chinese platform. 200+ paid models also |
| **ModelScope** | Qwen3.5-35B-A3B, Qwen3.5-27B, API-Inference models | dynamic | 2,000 | — | Alibaba Cloud. Real-name verify required |
| **Kilo Code** | Grok Code Fast, MiniMax M2.5, Nemotron Super, DOLA Seed 2.0, 6+ | ~200/hr | — | — | kilo.ai — auto-router picks best free model |
| **Ollama Cloud** | qwen3-coder:480b, deepseek-v3.1:671b, kimi-k2:1t, gpt-oss:120b, 30+ cloud models | session | session | — | Not OpenAI-compatible. Uses Ollama API |
| **AIMLAPI** | 400+ models (GPT, Claude, Gemini, DeepSeek free tier) | — | — | — | One key, 400+ models |
| **Aion Labs** | Aion 2.5, Aion 2.0, Aion-RP 1.0 | 15 | — | 20K | Roleplay/storytelling specialist. IL-based |
| **DeepSeek DSpark** (HF) | DeepSeek V4-Pro / V4-Flash **DSpark** checkpoints | — | — | Free to download (open weights); served via HF Inference Providers / DeepInfra | Not a new model — same V4 checkpoint with an open-source speculative-decoding module attached (50-600% faster generation, ~85% per one benchmark write-up). Grab the weights on HF or call it via HF Inference Providers | huggingface.co/deepseek-ai |
| **Cohere** | Command A+ (218B), Command A (111B), Command R+ | 20 | 1,000 calls/mo | — | 256K ctx on Command A. Non-commercial |
| **NLP Cloud** | Open + proprietary models (gen, NER, classification, embeddings) | limited | — | — | Free dev tier; production-NLP focus |
| **Cerebras** ⚠️ trial | Cerebras-hosted models | — | — | **$5 signup credit** | This is a free trial, not a permanent 1M-token/day allocation. Current pricing does not publish a lasting free-plan token quota; check the dashboard before building around it |
| **TokenRouter** ⚠️ caveat | 300+ models; **$0 IDs:** `deepseek/deepseek-v4-pro-0813-free`, `qwen/qwen3.8-max-free`, `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | dashboard | dashboard | limited free capacity | Hosted gateway, no markup on paid models. Free models exist but "stability and concurrency are not guaranteed" |
| **TokenLB** ⚠️ unverified | Claude Opus 4.8, GPT-5.5, DeepSeek, Qwen, 40+ providers (vendor-claimed) | — | — | — | Site returned a 401 this pass — treat as unverified. See caveat section below, not a confirmed free tier |

> **★ = best first — the rows you should actually build on.** Ordering is by usefulness, not by trust tier: a caveated or unverified provider can rank high, but it keeps its ⚠️ marker right in its row. TokenRouter/TokenLB sit at the bottom because they are paid/unverified gateways, not free tiers.

---

## Table 1B — Hidden Gems / Decentralized & Obscure Free Providers

> Lesser-known but **legitimate** free access. Mostly Bittensor-subnet / decentralized compute + niche aggregators. ⚠️ Don't abuse small free tiers (over-use gets them killed). **Excluded on purpose:** any "deep web" / cracked-key / reverse-engineered-chatbot / shared-account site — those are credential theft or scams and risk bans. Stick to the list below.

| Provider | Free access | Models | Notes | Link |
|---|---|---|---|---|
| ★ **Chutes** (Bittensor SN64) | Free tier (now leans PAYG), no card | SOTA open models *minutes after release* — DeepSeek, Kimi K2, Qwen + image/video/audio | OpenAI-compatible, LiteLLM | chutes.ai |
| ★ **Nineteen / NineteenAI** (SN19) | **Free front-end UIs, no signup**; instant public API | Best open LLMs + image gen + embeddings | Decentralized (Rayon Labs), "fastest inference subnet" | sn19.ai · app.sn19.ai |
| ★ **Pollinations.ai** | Free, server keys unmetered | Text + image + audio + video, single API | Client keys 1 req/hr/IP; server-side keys no rate limit | pollinations.ai |
| ★ **NaraRouter** | **~5–7M free tokens/day**, resets daily (07:00 WIB, UTC+7) · ~10 RPM | Open-source + hosted models (Claude, GPT, Gemini, DeepSeek, Qwen via gateway) | OpenAI-compatible AI gateway; signup with Google, no credit card. Trending hard across YouTube/studentoffers/community lists in Aug 2026. Numbers differ by source (5M vs 7M/day) — treat as approximate | router.bynara.id |
| ★ **LongCat-2.0** | Free API quota on application; ~50M tokens/day free tier is claimed on third-party router dashboards (unverified) | Meituan LongCat-2.0 (1.6T MoE, 1M ctx) | Open-source (MIT, open weights), agent-native coding model; integrates with Claude Code/OpenClaw. Also on OpenRouter ($0.30/$0.90). The "50M/day" figure comes from OmniRoute's free-tier dashboard, not Meituan — treat as unverified | longcat.ai · longcatai.org |
| **AgentRouter** ⚠️ caveat | $100 signup credit ($200 via referral; a community list reports $150 + daily-relogin bonus — amounts vary by source/promo) | Claude (incl. Opus/Sonnet 5), GPT-5.x, GLM-4.x/5.x, DeepSeek — OpenAI-compatible gateway | Confirmed this pass: launched Oct 2025, self-described non-profit/"public-welfare" gateway. **GitHub account required, and it must be 1+ year old (operator condition, user-confirmed).** OpenAI- and Anthropic-wire compatible — works w/ Claude Code, Codex, Gemini CLI, Roo, Kilo, and **Cline**: add your AgentRouter key as a custom OpenAI-compatible provider in the **Cline VS Code extension** (Settings → API Provider → OpenAI Compatible, base URL = AgentRouter endpoint) for free Claude/GPT inside the IDE. No markup claim (retail provider rates). Not for production uptime; free quota can end anytime. Operator still not independently audited — treat as caveat, not a confirmed free tier | agentrouter.org |
| **Bluesminds** ⚠️ caveat | Signup credits (amounts conflict across sources: $100 per studentoffers/YouTube walkthroughs, 500 credits per a community list) · ~20 RPM · ~300 req/day free | GPT-5.x/4o, Gemini, Claude 4.x, Kimi K2.x, DeepSeek, Qwen | Unified gateway (OpenAI/Claude/Gemini-compatible), **GitHub login required — account 1+ year old (operator condition, user-confirmed)**, no card. Claude Code + Codex support. No independent verification of the operator — treat as caveat, not a confirmed free tier | api.bluesminds.com |
| **Voyage AI** | 50M tokens/mo free | Embeddings + rerankers (RAG-tuned) | MongoDB-owned. Generous free tier, OpenAI-compatible | voyageai.com |
| **Jina AI** | 10M tokens free | Embeddings, reranker, reader | Good for RAG testing; reader API turns URLs→LLM text | jina.ai |
| **Sarvam AI** | ₹1000 signup credit | Indic-language LLMs + STT/TTS + doc digitization | Indian startup; best for Indian-language tasks | sarvam.ai |
| **LLM7.io** | **Zero registration** for basic | DeepSeek, Gemini Flash Lite, Qwen-Coder, 30+ | GDPR-friendly | llm7.io |
| **Kilo Code** | ~200 req/hr free, auto-router | Grok Code Fast, MiniMax, Nemotron | kilo.ai picks best free model | kilo.ai |
| **ModelScope** | 2,000 calls/day | Qwen3.5 variants | Alibaba; real-name verify | modelscope.cn |
| **SiliconFlow** | 60K TPM free | Qwen3, DeepSeek-R1-Distill | 200+ paid models too | siliconflow.cn |
| **Novita AI** | Free credits + free models | Many open models | Appears in aggregator lists | novita.ai |
| **ArliAI** | Free via OpenRouter/Chutes routing | Specialized fine-tunes (Dolphin, DeepHermes, QwQ, OlympicCoder) | Niche/roleplay/coding tunes | arliai.com |
| **OpenCode Zen** ⚠️ | Mostly PAYG; **free stealth/experimental models** for limited periods | Curated coding-agent models (validated/benchmarked) | ⚠️ Free models may train on your data — avoid sensitive code. No lock-in. `opencode/<id>` | opencode.ai/zen |
| **Targon** (Bittensor) | Community confidential-compute access | Open models | Minimal public docs; decentralized | targon.com |
| **DeepInfra** ⚠️ caveat | No standalone free tier; **small free inference quota for signed-in HF users** via Inference Providers | Open models incl. DeepSeek V4 DSpark, Llama, Qwen | Ultra-low-cost pay-per-token hosting, not a free-tier provider on its own (sources conflict: its own HF blog mentions the small free quota, independent reviews say "no free tier"). Route through HuggingFace Inference Providers to use the free quota | deepinfra.com |
| **GoRouter** ⚠️ unverified | $70 credits + check-in bonus | Multi-model gateway | Community-reported (gist, Aug 2026), old GitHub account required. No live page verified this pass — treat as unverified, not a confirmed free tier | — |
| **Tokeness** ⚠️ unverified | ~¥5 free + check-in bonus; paid credits cheap | DeepSeek + multi-model | Community-reported (gist, Aug 2026), described as stable. No live page verified this pass — treat as unverified | — |
| **CatAPI** ⚠️ | Signup credits (unverified) | Multi-model via a **"New API"** gateway panel (OpenAI-compatible reseller front-end) | Self-hosted New-API-style aggregator; not an official provider — verify before funding, treat keys as untrusted | catapi.ai |

> ★ = best of the hidden gems first. Ordering by usefulness, not trust tier — caveated rows (AgentRouter, Bluesminds) sit high because they respond, and keep their ⚠️ markers. aerolink was removed in Sept 2026 for serving Qwen instead of the Claude models it bills for.

### Aggregators (route across many free tiers with one key)

| Tool | What | Link |
|---|---|---|
| **MrFadiAi/free-llm-gateway** | OpenAI-compatible gateway aggregating **24+ providers, 260+ free models** auto-discovered, auto-fallback, rate-limit tracking, dashboard | github.com/MrFadiAi/free-llm-gateway |
| **FreeLLMAPI** | OSS BYOK proxy (29K★). Stacks the free tiers of **16 providers (~1.7B tokens/mo, 110+ models)** behind one `/v1`. Smart routing, auto-failover, per-key rate tracking (avoids 429s), AES-256 key encryption. Live catalog = $19/yr; router free forever | freellmapi.co · github.com/tashfeenahmed/freellmapi |
| **OmniRoute** | OSS (MIT) self-hosted gateway, 71K★. **340 providers, 90+ with free tiers, ~1.5B free tokens/month** pooled into one honest, deduped number (live dashboard). Quota-aware auto-fallback, 19 routing strategies, token compression (RTK + Caveman, 15-95%), MCP + A2A, works with Claude Code/Codex/Cursor/OpenCode/Cline/Copilot. ⚠️ Security caveat: CVE-2026-49352 reported; it proxies your keys and routes traffic through third-party free tiers — vet before pointing production keys at it | github.com/diegosouzapw/OmniRoute |
| **gaca-core** (G.A.C.A.) | OSS "Universal AI Bus" — **87+ free models from 11 providers**, OpenAI-compatible (`/v1/chat/completions`), auto-failover + ranking + rate limiting. Drop-in fallback for any OpenAI client | github.com/gacabartosz/gaca-core |
| **freellm.net** | Directory of **224+ free models / 25 providers**, daily live-verified (real API calls). One-click config for Claude Code / Codex / Gemini CLI / OpenClaw | freellm.net |
| **OrcaRouter** ⚠️ | OpenRouter alternative (MIT-licensed, zero-markup, 100+ models). **Free credits for devs, no card** (PRNewswire May 8, 2026); **free BYOK** (Jul 24); live **voucher drops, student credits, hackathon grants** on the offers page; monthly plans add bonus credits. Credit amounts are promo/voucher-based — check the offers page live before relying | orcarouter.ai/offers |
| **LiteLLM / OpenRouter** | Route + fall back across providers to multiply free quotas | litellm.ai · openrouter.ai |

> Combine the multi-provider free tiers (Groq + Cerebras + Google AI Studio + Chutes + Nineteen + OpenRouter `:free`) behind LiteLLM/free-llm-gateway → effectively continuous free inference.

### Chinese credit-routers / gateways (community-reported, ⚠️ all unverified)

> [!CAUTION]
> ⛔ **Model substitution — read before using any credit gateway (user-tested, Sept 2026).**
> Several "cheap Claude/GPT" gateways do not serve the model they bill for. Tested: **aerolink.lat**
> answers "Opus/Sonnet" requests with **Qwen**; **lumosel.vip** answers with **DeepSeek**. Both show
> token counters that don't match real Opus/Sonnet pricing (credits "last" far longer than real Opus
> would), and both describe themselves as Chinese grey-market ("black-market") proxies. The same
> pattern applies to many of the Chinese credit routers below. How to check any gateway yourself:
> ask it for its model id and knowledge cutoff, run one prompt you've already run on the real
> model and compare, and compare its token count to the official tokenizer for the same text. If
> credits last "too long", you're not getting the model you think. Never send code, keys or
> personal data through these.

> Single source: a community gist updated 11 Aug 2026 ([almahmudbd/...free-apis](https://gist.github.com/almahmudbd/2f35cc768eae59117e8a0ce59beccca3)). None of these had a live page verified this pass — treat every number as a claim, and remember these gateways route your keys through third-party operators. `api.hcnsec.cn` is the Chinese-router lead from MASTER_PROMPT.md. Add in small batches; check-in bonuses and free quotas change weekly.

| Gateway | Community-reported free tier | Notes |
|---|---|---|
| **byNara** | ~5M credits/day + Telegram verify | Sibling of NaraRouter (router.bynara.id); OpenAI-compatible |
| **Future PPO** | ~$60 + check-in bonus | Old GitHub account required |
| **api.hcnsec.cn** | ~4K credits + check-in rewards | "Few models work" per the gist |
| **TabiToken** 🆕 | ~$100 + check-in bonus | Set model in config |
| **TokenLayer** | ~$20, Telegram verify | Paid credits also cheap |
| **AiFamily** | ~¥50 + check-in bonus | Unclear terms |
| **Unity2ai** | ~$2 | Paid credits ~85% cheaper |
| **yunwu.ai** | ~40 credits + check-in | — |
| **SwiftRouter** | ~$10, Discord verify | Gist says "don't buy" — flagged by the author itself |
| **ProRise-Hub** | ~$4 | Unclear |
| **AiWave** | ~¥5 + check-in | — |
| **vsLLM** | ~¥40 + check-in | Unclear |
| **B.Ai** | ~300K credits | — |
| **MonkeyCode-ai** | ~30M tokens/day for coding | Free coding tool (not API); Chinese models |

---

## Table 2 — Trial Credits (Stack These)

| Provider | Credits | Expiry | Models | How |
|---|---|---|---|---|
| **Anthropic** | $5 | 90 days | All Claude incl. Opus 5 | console.anthropic.com |
| **OpenAI** | $5 | 90 days | All GPT incl. GPT-5.5 | platform.openai.com |
| **DeepSeek** | $5 | 30 days | V4 Pro / V4 Flash | platform.deepseek.com |
| **AWS Bedrock** | $300 | 90 days | Claude, Llama, Titan | New AWS account |
| **Google Cloud Vertex AI** | $300 | 90 days | All Gemini models | New GCP account |
| **Azure AI Foundry** | $200 | 30 days | GPT-5.5, Claude, Llama | New Azure account |
| **OpenRouter** | $1 | — | Any model | Signup bonus |
| **Moonshot (Kimi)** | Varies | — | Kimi K2.6 (80.2%) | moonshot.cn new account |
| **xAI (SpaceXAI)** | $25 signup + **$150/mo** | recurring | Grok 4.6/4.5, **Grok Build** (free tier) | console.x.ai. ⚠️ $150/mo needs data-sharing opt-in (irreversible) + $5 prior spend. Don't use for sensitive data. Grok Build itself has a free tier — see [AGENTS.md](./AGENTS.md) Part 1 |
| **Vercel AI Gateway** | $5 / 30 days | refreshes | 40+ providers, one key, no markup | vercel.com/ai-gateway. Free ends after first payment |
| **Fireworks AI** | Signup credits | — | Open models (Llama/Qwen/DeepSeek), fast serving | fireworks.ai |
| **Together AI** | Signup credits (amount unverified) + **$50K startup accelerator** | 100+ open models (Llama/Qwen/DeepSeek), fast serving | together.ai. Also a HF Inference Provider partner. Credit amount from a secondary aggregator, not confirmed on together.ai this pass |
| **Upstage** | Signup credits | — | Solar Pro 2 (102B MoE) | upstage.ai |
| **AI21 Labs** | Signup credits | — | Jamba (SSM-Transformer hybrid, long ctx) | ai21.com |
| **Scaleway** | EU free trial | — | Open models; **Batch API has no rate limit** | scaleway.com |
| **Nebius** | Signup credits | — | Open models (EU); OpenRouter partner | nebius.com |

> **Stack strategy:** AWS ($300) + GCP ($300) + Azure ($200) = **$800+** in cloud AI credits.
> Run Opus 5 ($25/M out) or GPT-5.6 ($30/M out) for months at zero cost.

---

## How to Access Claude Opus 5 For Free

> **Updated 29 Sep 2026:** the current Opus is **Opus 5.5** (Sept 22, $4/$20). Opus is **not** on the Claude.ai free plan — free is Sonnet 5 (daily-capped) plus Haiku. Opus needs Pro/Max, an API trial, or cloud credits. GitHub Copilot Pro+ ($39) also includes Opus 5.5. The old "Opus 4.8 on the free plan" claim was wrong and has been removed; 4.8 is superseded history (still scored 88.6% SWE-bench).

### Ongoing Access

| Method | Limits | How |
|---|---|---|
| **Claude.ai free plan** | Sonnet 5 (daily message cap) — **not Opus** | claude.ai |
| **Puter.js** | None listed | developer.puter.com — free unlimited (GLM/Qwen/etc.; Claude availability is the user-pays model — check the catalog) |
| **Anthropic Open Source** | 6 months Claude Max ($200/mo value) | Open-source maintainers — anthropic.com/open-source |

### Trial / Limited

| Method | Value | Duration | How |
|---|---|---|---|
| **Anthropic API trial** | $5 credits | 90 days | console.anthropic.com |
| **Notion Business Trial** | Unlimited Opus (strong claim, not re-verified this pass — Notion's tiering changed recently, confirm before relying on it) | 30 days | notion.so → start Business trial |
| **AWS Bedrock** | $300 credits | 90 days | Model ID: `anthropic.claude-opus-5` |
| **Google Vertex AI** | $300 credits | 90 days | Model: `claude-opus-5@anthropic` |
| **Azure AI Foundry** | $200 credits | 30 days | Azure AI Studio → Anthropic models |

---

---

## TokenLB — API Marketplace & Developer Credits (caveat, demoted this pass)

**URL:** tokenlb.net — returned a 401 this pass, could not re-verify live.

> Demoted from a plain entry to a caveat this pass. Every number below is vendor-supplied, not independently confirmed: the 19,000+ user count, the weekly model-usage ranking, and the "lower-cost" claim. The credit program also requires you to display a TokenLB attribution link in your own README/docs to qualify — that's the shape of a paid-placement deal, not a neutral free-credit program. The ranking table and user count from a prior pass have been removed; treat anything below as a vendor pitch, not fact.

TokenLB describes itself as a self-service API key marketplace offering access to 40+ AI providers (OpenAI, Anthropic, Gemini, DeepSeek, Qwen, Llama) under one dashboard, with a per-star monthly token-credit program for open-source maintainers who add its attribution link. None of that is independently confirmed this pass.

### Quick Start (as documented by the vendor — unverified)

```python
# TokenLB claims to be OpenAI API-compatible — swap base_url
from openai import OpenAI

client = OpenAI(
    base_url="https://api.tokenlb.net/v1",   # TokenLB endpoint
    api_key="YOUR_TOKENLB_KEY",
)

r = client.chat.completions.create(
    model="claude-opus-4-8",    # or gpt-5.5, deepseek-v4, qwen3-coder, etc.
    messages=[{"role": "user", "content": "Hello"}]
)
print(r.choices[0].message.content)
```

---

## Best Free Model by Use Case

| Use Case | Model | Where | Quality |
|---|---|---|---|
| Code generation | Qwen3-Coder 480B | OpenRouter `:free` | 78% SWE-bench |
| Best free trial quality | Kimi K2.6 | Moonshot trial | 80.2% SWE-bench |
| Fastest inference | Llama 3.3 70B | Groq | ~60%, 320 tok/sec |
| Fast trial for open models | Cerebras-hosted models | Cerebras | $5 signup credit; current sustained-free quota not published |
| Free frontier coding | **DeepSeek V4.1 Flash / Kimi K3 / GLM-5.3-Flash** | **Cline** (free models) · **Freebuff** (6 h/day V4.1 Flash) | ⛔ Not via ZCode — it uploaded users' repos |
| Free 1M ctx chat | GLM-5.2 | chat.z.ai | ~72% SWE-bench |
| Cheapest paid production | DeepSeek V4.1 Flash | DeepSeek API | **$0.60/M out off-peak**, 1M ctx, vision |
| Google ecosystem | Gemini 3.8 Flash | Google AI Studio | 1M ctx, free tier |
| Multi-model single key | Any `:free` | OpenRouter | Varies |
| Huge free context | Space Bunny Alpha (1M) · Ox Alpha (1M) | OpenRouter · TokenRa | Stealth — may log prompts |
| Free-AI routers (Aug 2026) | OmniRoute (1.5B tok/mo pooled) · NaraRouter (5-7M tok/day) | See Table 1B | ⛔ Not aerolink / lumosel — they swap in Qwen/DeepSeek |

---

## Quick Start Code

### Google AI Studio — Gemini 3.1 Flash (best free start)

```python
import google.generativeai as genai
genai.configure(api_key="YOUR_AISTUDIO_KEY")
model = genai.GenerativeModel("gemini-3.1-flash")
print(model.generate_content("Write binary search in Python").text)
```

### OpenRouter — 20+ free models with one key

```python
from openai import OpenAI
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="sk-or-YOUR_KEY",
)
r = client.chat.completions.create(
    model="qwen/qwen3-coder-480b:free",
    messages=[{"role": "user", "content": "Write binary search in Python"}]
)
print(r.choices[0].message.content)
```

### Groq — 320 tok/sec free inference

```python
from groq import Groq
client = Groq(api_key="gsk_YOUR_KEY")
r = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "Hello"}]
)
print(r.choices[0].message.content)
```

### Cerebras — current trial credit

```python
from cerebras.cloud.sdk import Cerebras
client = Cerebras(api_key="YOUR_KEY")
r = client.chat.completions.create(
    model="llama3.3-70b",
    messages=[{"role": "user", "content": "Hello"}]
)
```

### TokenRouter — unified paid gateway (possible unquantified signup credit)

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.tokenrouter.com/v1",
    api_key="YOUR_TOKENROUTER_KEY",
)
# Use a model ID from the live TokenRouter catalog. Check the dashboard price before each run.
response = client.chat.completions.create(
    model="deepseek/deepseek-v4-pro",
    messages=[{"role": "user", "content": "Hello"}],
)
print(response.choices[0].message.content)
```

### Puter.js — free unlimited (browser/Node.js)

```javascript
const result = await puter.ai.chat("Write binary search in Python", {
    model: "glm-5-2"  // free, 1M context
});
console.log(result);
```

---

## Useful Repos

> `cheahjs/free-llm-api-resources` — previously listed here and described as "the canonical community list" — returns a 404 this pass. Removed until a live URL for it turns up; don't call any single list canonical in the meantime.

| Repo | What |
|---|---|
| [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | Permanent free LLM API list (the one every other list copies) |
| [amardeeplakshkar/awesome-free-llm-apis](https://github.com/amardeeplakshkar/awesome-free-llm-apis) | Rate limits, SDK compat, speed tiers |
| [bradAGI/awesome-cli-coding-agents](https://github.com/bradAGI/awesome-cli-coding-agents) | Curated CLI agents directory |
| [open-free-llm-api/awesome-freellm-apis](https://github.com/open-free-llm-api/awesome-freellm-apis) | 🆕 134+ free LLM APIs / keys from 40+ providers, one-click setup for Claude Code/Codex/Gemini CLI — updated Aug 14, 2026 |
| [12britz/awesome-free-models](https://github.com/12britz/awesome-free-models) | 🆕 Free AI models/APIs/tools, self-described as live-verified Aug 7, 2026 |
| [findaicredits.com](https://www.findaicredits.com/) | 🆕 Directory of free AI credits/deals/coupons (OpenAI, Anthropic, GCP, AWS…); surfaced via Instagram Aug 2026 reels claiming Claude/Cursor/Codex sub credits — treat the directory's own claims as leads to verify, not facts |
| [almahmudbd gist — free-apis](https://gist.github.com/almahmudbd/2f35cc768eae59117e8a0ce59beccca3) | 🆕 Community list of credit-gateway signups + Chinese routers (source of the Table 1B community rows); updated Aug 11, 2026 — all numbers are claims, verify before funding |
