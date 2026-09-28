# 🆓 Free AI Access — Models, APIs & Gateways (verified 29 September 2026)

<p align="center"><a href="./README.md">🏠 Home</a> · <a href="https://yash-awasthi.github.io/ToolkitArchive/">🔎 Explorer</a> · <a href="https://yash-awasthi.github.io/ToolkitArchive/benchmarks.html">📊 Benchmarks</a> · <a href="./NEWS.md">📰 News</a> · <a href="./STUDENTS.md">🎓 $0 guide</a> · <a href="./FREE-ACCESS.md">🆓 Free AI</a></p>

> [!NOTE]
> Every free tier here was re-read from the provider's own page on 29 Sep 2026. Free tiers change
> weekly — treat numbers as a snapshot. Credit stacking, student and startup programs, free GPU and the
> provider trust list are in [CREDITS.md](./CREDITS.md); the $0 student guide is [STUDENTS.md](./STUDENTS.md).

> [!WARNING]
> **Changed since the last pass:** **GitHub Models retired July 30, 2026** · **Chutes** dropped its free tier · **OVHcloud** free access now covers only small models · **LongCat** chat is paid · **ZCode** removed (it uploaded users' repos) · **aerolink.lat / lumosel.vip** serve Qwen/DeepSeek instead of Claude · TokenLB, CatAPI and yunwu.ai no longer resolve.

**Contents:** [Sept 2026 free wave](#september-2026-free-wave-start-here) · [Free API tiers](#table-1--free-api-tiers-no-card) · [Niche providers](#table-1b--decentralised--niche-providers) · [Aggregators](#aggregators-one-key-over-many-free-tiers) · [Chinese routers](#chinese-credit-routers-community-reported--unverified) · [Trial credits](#table-2--trial-credits-stack-these) · [Free Opus](#how-to-use-claude-opus-55-for-free-or-nearly) · [Best free model](#best-free-model-by-use-case) · [Quick start](#quick-start-code) · [Lists](#useful-repos--lists)

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
| ★ **Google AI Studio** | **Gemini 3.8 Flash** (1M ctx, released Sept 2), 3.7 Flash | Rate-limited free tier; free-tier prompts are used to improve Google products. Not in the EU/UK |
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

## Table 1 — Free API tiers (no card)

All OpenAI-SDK-compatible unless noted. Limits read from each provider's page on 29 Sep 2026.

| Provider | Free models / allowance | Limits | Notes |
|---|---|---|---|
| ★ **Google AI Studio / Gemini API** | Gemini 3.8 Flash, 3.7 Flash, Nano Banana 2 (image) and more | Rate-limited free tier (limits per model in AI Studio) | **Best free tier.** Free-tier prompts are used to improve Google products. Not in the EU/UK |
| ★ **OpenRouter `:free`** | 25+ free models: Space Bunny Alpha, Nemotron 3 Ultra, Laguna S/XS 2.1, Inkling, Qwen3.8 27B… | 20 req/min; **50 req/day** (under $10 purchased) → **1,000 req/day** after $10 | One key for everything; stealth/free providers may log prompts |
| ★ **Token Harbor** | `deepseek-v4.1-flash:free`, `qwen3.8-flash:free`, `mimo-v2.6-flash:free` | Free allowance (size not published) | OpenAI + Anthropic compatible, `https://tokenharbor.ai/v1` |
| ★ **Groq** | Qwen 3.8 27B, gpt-oss, Llama and more | Per-model; e.g. Qwen 3.8 27B: 30 RPM, 1,000 req/day, 200K tokens/day (per third-party guides) | Fastest inference; check console.groq.com/docs/rate-limits |
| ★ **Cloudflare Workers AI** | 50+ open models | **10,000 neurons/day**, resets 00:00 UTC | $0.011 per 1K neurons beyond that |
| ★ **NVIDIA build.nvidia.com** | Models marked "Free Endpoint" (Nemotron and others) | Rate-limited | NVIDIA developer account |
| ★ **Mistral** | Mistral API (incl. Voxtral, Codestral) | **$10/month API credit** on the free plan | EU-hosted; Le Chat Pro for students $5.99 |
| **LLM7.io** | DeepSeek V4 Flash, GPT and others | **500K tokens/day** anonymous-tier limits; 1M tokens/day with a key | Zero-registration basic access |
| **NaraRouter** (router.bynara.id) | 12 models incl. Agnes 3 Flash and **Jev** | **7M tokens/day**, 15 req/min | Free forever tier; some paid plans out of stock |
| **Scaleway Generative APIs** | Open models incl. DeepSeek V4 Flash | **1M free tokens** | EU; then €0.40/M for V4 Flash |
| **Hugging Face Inference Providers** | Hundreds of open models across providers | **$0.10/month** credits (free users); PRO $10/mo | Routes to the best provider, no markup |
| **Pollinations.ai** | Text, image, audio, video in one API | Free "Pollen" from quests | Open, community-run |
| **Aion Labs** | Aion models | Daily free credit allowance, no card | Agent jobs, API, browser chat |
| **SiliconFlow** | Some free open models + **$1 credit** | Per model | Chinese platform, 200+ models |
| **BazaarLink** | Free models, auto-switch to paid beyond free use | Per model | TW-based gateway, agent self-registration |
| **Kilo Gateway** | `kilo-auto/free` router + free models | 200 req/h anonymous | See Kilo Code |
| **Ollama Cloud** | Starter cloud models + starter credits | Plan-based | Uses Ollama API; Pro $20/mo |
| **Puter.js** | Hundreds of models in the browser | **User pays** from their own Puter allowance | Free for the developer |
| **Cohere** | Trial API key | Limited, non-commercial | — |
| **Cerebras** | $5 starter credit | Pay as you go after | Very fast; hosts Qwen 3.8 27B, gpt-oss-120b |
| **Novita AI** | Free credits | — | V4 Flash $0.14/M |
| **OVHcloud AI Endpoints** | Only small models free now (Qwen3Guard, SDXL, TTS) | 2 req/IP anonymous | Big models are paid (e.g. Qwen3.5-9B €0.10/M) |
| **TokenRouter** | `:free` IDs (DeepSeek V4 Pro 0813, Qwen 3.8-Max, Nemotron Nano Omni) | Limited capacity | Paid models at list price |
| ~~GitHub Models~~ | **Retired July 30, 2026** | — | Use Copilot Free or OpenRouter instead |

---

## Table 1B — Decentralised & niche providers

> ⚠️ Don't abuse small free tiers — overuse gets them shut down. Anything that resells Claude/GPT for "free credits" gets the model-substitution check below.

| Provider | Free access | Notes | Link |
|---|---|---|---|
| **Voyage AI** (MongoDB) | **200M free tokens** for voyage-4 embeddings/rerank; 50M for domain models | Best free embeddings | [voyageai.com](https://voyageai.com) |
| **Jina AI** | Free trial tokens | Embeddings, reranker, Reader (URL → LLM text) | [jina.ai](https://jina.ai) |
| **ArliAI** | Free tier (12K context, 1 request at a time) | Fine-tunes; Starter $10/mo | [arliai.com](https://arliai.com) |
| **OpenCode Zen** | Free stealth/experimental models (Big Pickle etc.); otherwise pay-as-you-go | ⚠️ Free models may train on your code | [opencode.ai/zen](https://opencode.ai/zen) |
| **Chutes** (Bittensor) | No free tier now — Plus $10/mo or per-token | Open models minutes after release | [chutes.ai](https://chutes.ai) |
| **DeepInfra** | No free tier; small HF-routed quota | Cheap per-token hosting | [deepinfra.com](https://deepinfra.com) |
| **Sarvam AI** | Signup credit | Indic languages, STT/TTS | [sarvam.ai](https://sarvam.ai) |
| **LongCat** (Meituan) | Chat app is now paid (Basic $15/mo); open weights on Hugging Face | Earlier free API quota no longer visible | [longcat.chat](https://longcat.chat) |
| **AgentRouter** ⚠️ | Referral credit (reported $50–$200, shrinking); GitHub account 1+ year old | Unaudited reseller — see check below | [agentrouter.org](https://agentrouter.org) |
| **Bluesminds** ⚠️ | Signup credits reported; paid from $75 | Unaudited reseller | [api.bluesminds.com](https://api.bluesminds.com) |

### Aggregators (one key over many free tiers)

| Tool | What | ⭐ (live) | Link |
|---|---|---|---|
| ★ **OmniRoute** | Self-hosted gateway over 340 providers (90+ free), quota-aware fallback. ⚠️ CVE-2026-49352 reported | 71K | [github.com/diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) |
| ★ **FreeLLMAPI** | Self-hosted proxy stacking 16 providers' free tiers; router free forever (catalog updates $19/yr) | 29K | [github.com/tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) |
| **LiteLLM** | Open-source router/proxy, free self-hosted | 60K | [github.com/BerriAI/litellm](https://github.com/BerriAI/litellm) |
| **OrcaRouter** | Free models at $0 (10 RPM, 50 req/day), vouchers and student credits | — | [orcarouter.ai/offers](https://orcarouter.ai/offers) |
| **freellm.net** | Directory of free models, daily live-verified; Plus $4.99/30 days | — | [freellm.net](https://freellm.net) |
| **Vercel AI Gateway** | One key over many providers, no markup | — | [vercel.com/ai-gateway](https://vercel.com/ai-gateway) |

### Chinese credit routers (community-reported, ⚠️ unverified)

> [!CAUTION]
> ⛔ **Model substitution — read before using any credit gateway (user-tested, Sept 2026).**
> Several "cheap Claude/GPT" gateways do not serve the model they bill for. Tested: **aerolink.lat**
> answers "Opus/Sonnet" requests with **Qwen**; **lumosel.vip** answers with **DeepSeek**. Both show
> token counters that don't match real Opus/Sonnet pricing, and both describe themselves as Chinese
> grey-market proxies. **How to check any gateway:** ask for its model id and knowledge cutoff, run a
> prompt you've already run on the real model and compare, and compare its token count with the
> official tokenizer. If credits last "too long", you're not getting the model you think. Never send
> code, keys or personal data through these.

| Gateway | Claimed free tier | Status 29 Sep |
|---|---|---|
| **TabiToken** | $100–120 via referral, GitHub 1+ yr | Unverified |
| **B.Ai** | $100 in rewards | Live |
| **api.hcnsec.cn** | ~4K credits + check-in | Live, few models work |
| **TokenLayer** · **AiFamily** · **Unity2ai** · **AiWave** · **vsLLM** · **ProRise-Hub** · **Future PPO** | Small credits + check-in | Unverified |
| **SwiftRouter** | ~$10 | Even its own promoter says "don't buy" |
| ~~yunwu.ai~~ · ~~CatAPI~~ · ~~TokenLB~~ | — | No longer resolving |

---

## Table 2 — Trial Credits (stack these)

| Provider | Credit | Validity | Link |
|---|---|---|---|
| **Google Cloud (Vertex)** | $300 | Trial period | [cloud.google.com/free](https://cloud.google.com/free) |
| **Oracle Cloud** | $300 | 30 days (+ Always Free) | [oracle.com/cloud/free](https://oracle.com/cloud/free) |
| **AWS (Bedrock)** | **Up to $200** | 6 months | [aws.amazon.com/free](https://aws.amazon.com/free) |
| **Azure (AI Foundry)** | $200 | 30 days | [azure.microsoft.com/free](https://azure.microsoft.com/free) |
| **AI21** | $10, no card | 7 days | [ai21.com/pricing](https://ai21.com/pricing) |
| **Cerebras** | $5 | — | [cerebras.ai/pricing](https://cerebras.ai/pricing) |
| **Fireworks AI** | $1 | — | [fireworks.ai/pricing](https://fireworks.ai/pricing) |
| **SiliconFlow** | $1 | — | [siliconflow.com/pricing](https://siliconflow.com/pricing) |
| **Anthropic API** | Small new-account credit (commonly $5) | — | [platform.claude.com](https://platform.claude.com) |
| **xAI / SpaceXAI** | Signup credit; extra monthly credit for data-sharing opt-in (irreversible — avoid for sensitive data) | — | [console.x.ai](https://console.x.ai) |
| **Nebius AI Builder Program** | $400+ credits and discounts | Apply | [nebius.com](https://nebius.com) |
| **Upstage** | Free Solar Pro for education/public-interest orgs (1 year); 50% off until Oct 22 | — | [upstage.ai/pricing](https://upstage.ai/pricing) |

> **Stack:** GCP $300 + Oracle $300 + AWS $200 + Azure $200 ≈ **$1,000** to run Claude (Bedrock/Vertex), Gemini, GPT (Azure) and open models for free for weeks. Student programs → [CREDITS.md](./CREDITS.md#part-2--student-programs).

---

## How to use Claude Opus 5.5 for free (or nearly)

Opus is **not** on the Claude.ai free plan (free = Sonnet 5 with daily caps).

| Route | What you get |
|---|---|
| **AWS Bedrock / Google Vertex / Azure** new-account credit | Opus 5.5 at $4/$20 paid from $200–300 of credit |
| **Anthropic API** new-account credit | A few dollars of testing |
| **Claude for Open Source** | **6 months of Claude Max 20x** for qualifying maintainers (reported bar: ~5,000+ GitHub stars) — apply at anthropic.com |
| **GitHub Copilot Pro+** ($39/mo) | Includes Opus 5.5 — cheapest paid route |
| **Claude for Startups** | Credits through partner VCs |

---

## Best Free Model by Use Case

| Use case | Model | Where |
|---|---|---|
| Coding agent, free | **DeepSeek V4.1 Flash** / **Kimi K3** / GLM-5.3-Flash | Cline (free models) · Freebuff · Token Harbor `:free` |
| Huge free context | Space Bunny Alpha (1M) · Ox Alpha (1M) · Gemini 3.8 Flash (1M) | OpenRouter · TokenRa · AI Studio |
| Fastest inference | Qwen 3.8 27B / gpt-oss | Groq · Cerebras |
| Chat with a frontier model | Kimi K3 · Qwen 3.8-Max · Claude Sonnet 5 · GPT-6 Luna | kimi.com · chat.qwen.ai · claude.ai · chatgpt.com |
| Embeddings / RAG | voyage-4 (200M free tokens) | Voyage AI |
| Local, unlimited | Qwen3.8-27B · Laguna XS 2.1 | Ollama / LM Studio ([AGENTS.md](./AGENTS.md#part-10--local-model-runners)) |
| Cheapest paid | DeepSeek V4.1 Flash ($0.60/M out off-peak) · GPT-6 Luna ($0.50) | DeepSeek · OpenAI |

---

## Quick Start Code

```python
# Google AI Studio — Gemini 3.8 Flash (free tier)
from google import genai
client = genai.Client(api_key="YOUR_AISTUDIO_KEY")
print(client.models.generate_content(model="gemini-3.8-flash", contents="Write binary search in Python").text)
```

```python
# Any OpenAI-compatible free endpoint (OpenRouter / Token Harbor / Groq / Cerebras)
from openai import OpenAI
client = OpenAI(base_url="https://tokenharbor.ai/v1", api_key="YOUR_KEY")   # or https://openrouter.ai/api/v1
r = client.chat.completions.create(model="deepseek-v4.1-flash:free",
                                   messages=[{"role": "user", "content": "Write binary search in Python"}])
print(r.choices[0].message.content)
```

```javascript
// Puter.js — user-pays, free for the developer (browser)
const reply = await puter.ai.chat("Write binary search in Python");
```

---

## Useful Repos & Lists

| Repo / site | ⭐ (live) | What |
|---|---|---|
| [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | 8.6K | Permanent free LLM API list |
| [bradAGI/awesome-cli-coding-agents](https://github.com/bradAGI/awesome-cli-coding-agents) | 1.3K | CLI agents directory |
| [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) | — | Free AI coding tools and plans (updated Sept 2026) |
| [findaicredits.com](https://www.findaicredits.com/) | — | Free credits and student deals directory |
| [aifree.dev/student-ai-deals](https://aifree.dev/student-ai-deals) | — | Student deals, checked weekly |
