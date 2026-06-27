# Free API Access & Model Access — June 2026

> Permanent free API tiers below. For **trial-credit stacking, student/startup programs, free GPU, and subscription-as-API tricks** → [CREDITS.md](./CREDITS.md).
> ✅ **Verified June 27, 2026** — free tiers change weekly; confirm before relying.

---

## Free API Daily Token Budget

![Free API Tiers](./charts/free-api-tiers.png)

---

## Table 1 — Permanent Free API Tiers (No Credit Card)

All endpoints are OpenAI SDK-compatible unless noted.

| Provider | Best Free Models | RPM | RPD | Daily Tokens | Notes |
|---|---|---|---|---|---|
| **Google AI Studio** | Gemini 3.5 Flash, 3.1 Flash (74%), Flash Lite | 15 | 1,500 | ~750K | Best free tier. Multimodal. Not available EU/UK |
| **Groq** | Llama 3.3 70B, Llama 4 Scout, Qwen3-32B, gpt-oss-120b | 30 | 1,000 | 100K | LPU hardware, ultra-fast. Reduced RPD 2026 |
| **Cerebras** | gpt-oss-120b, zai-glm-4.7 | 30 | 14,400 | 1M | Wafer-scale, ~2,600 tok/sec. 8K ctx on free |
| **OpenRouter `:free`** | Qwen3-Coder (78%), gpt-oss-120b, Nemotron Ultra 550B, 22+ models | 20 | 200 | — | 1K RPD with $10 balance. Single key |
| **Mistral** | Mistral Medium 3.5 (128B), Mistral Small 4, Codestral | ~1 RPS | — | 500K | ~1B tokens/month. Non-commercial. EU-hosted |
| **Cloudflare Workers AI** | Llama 3.3 70B, Llama 4 Scout, Kimi K2.7, Gemma 4 26B, GLM-4.7-Flash, 50+ models | — | — | 10K neurons | Edge-distributed, serverless, global |
| **Cohere** | Command A+ (218B), Command A (111B), Command R+ | 20 | 1,000 calls/mo | — | 256K ctx on Command A. Non-commercial |
| **NVIDIA NIM** | Nemotron 3 Super, Nemotron 3 Ultra, DeepSeek-R1, Llama 405B, MiniMax M2.7, 100+ | ~40 | — | — | build.nvidia.com. NVIDIA Dev Program |
| **GitHub Models** | gpt-5, gpt-4.1, gpt-4o, o4-mini, Llama 4 Scout, DeepSeek-R1, 45+ | 10–15 | 50–150 | — | GitHub account only. 8K in / 4K out per req |
| **Z.AI** | GLM-4.7-Flash, GLM-4.6V-Flash (vision) | 1 concurrent | — | — | open.bigmodel.cn. Permanent free |
| **Puter.js** | GLM-5.2 (1M ctx), GLM-5.1, GLM-4.7-Flash | — | — | — | Free unlimited via Puter SDK. User-pays model |
| **HuggingFace Inference** | 1000s of open models via Fireworks/Together/Hyperbolic | Credit-metered | — | 100K credits/mo | Routes to best provider automatically |
| **SambaNova** | DeepSeek-V3.1/V3.2, Llama 3.3 70B, gpt-oss-120b, MiniMax M2.7, Gemma 4 31B | 20 | 20 | 200K | RDU hardware. Ultra-fast. No card required |
| **OVHcloud AI Endpoints** | Qwen3.5-397B, gpt-oss-120b, Llama 3.3 70B, Qwen3-Coder, 13+ EU models | 2/IP | — | — | **No signup, no key.** EU-hosted. GDPR. Anonymous |
| **SiliconFlow** | Qwen3-8B, DeepSeek-R1-Distill-Qwen-7B | 30 | — | 60K TPM | Chinese platform. 200+ paid models also |
| **ModelScope** | Qwen3.5-35B-A3B, Qwen3.5-27B, API-Inference models | dynamic | 2,000 | — | Alibaba Cloud. Real-name verify required |
| **LLM7.io** | DeepSeek-R1, DeepSeek-V3, Gemini Flash Lite, GPT-4o-mini, Qwen2.5-Coder, 30+ | 30 | — | — | **Zero registration** for basic. GDPR-compliant |
| **Kilo Code** | Grok Code Fast, MiniMax M2.5, Nemotron Super, DOLA Seed 2.0, 6+ | ~200/hr | — | — | kilo.ai — auto-router picks best free model |
| **Ollama Cloud** | qwen3-coder:480b, deepseek-v3.1:671b, kimi-k2:1t, gpt-oss:120b, 30+ cloud models | session | session | — | Not OpenAI-compatible. Uses Ollama API |
| **Aion Labs** | Aion 2.5, Aion 2.0, Aion-RP 1.0 | 15 | — | 20K | Roleplay/storytelling specialist. IL-based |
| **AIMLAPI** | 400+ models (GPT, Claude, Gemini, DeepSeek free tier) | — | — | — | One key, 400+ models |
| **TokenLB** | Claude Opus 4.8, GPT-5.5, DeepSeek, Qwen, 40+ providers | — | — | — | Lower-cost reseller. OSS dev credit program |

---

## Table 1B — Hidden Gems / Decentralized & Obscure Free Providers

> Lesser-known but **legitimate** free access. Mostly Bittensor-subnet / decentralized compute + niche aggregators. ⚠️ Don't abuse small free tiers (over-use gets them killed). **Excluded on purpose:** any "deep web" / cracked-key / reverse-engineered-chatbot / shared-account site — those are credential theft or scams and risk bans. Stick to the list below.

| Provider | Free access | Models | Notes | Link |
|---|---|---|---|---|
| **Chutes** (Bittensor SN64) | Free tier (now leans PAYG), no card | SOTA open models *minutes after release* — DeepSeek, Kimi K2, Qwen + image/video/audio | OpenAI-compatible, LiteLLM | chutes.ai |
| **Nineteen / NineteenAI** (SN19) | **Free front-end UIs, no signup**; instant public API | Best open LLMs + image gen + embeddings | Decentralized (Rayon Labs), "fastest inference subnet" | sn19.ai · app.sn19.ai |
| **Targon** (Bittensor) | Community confidential-compute access | Open models | Minimal public docs; decentralized | targon.com |
| **ArliAI** | Free via OpenRouter/Chutes routing | Specialized fine-tunes (Dolphin, DeepHermes, QwQ, OlympicCoder) | Niche/roleplay/coding tunes | arliai.com |
| **Novita AI** | Free credits + free models | Many open models | Appears in aggregator lists | novita.ai |
| **LLM7.io** | **Zero registration** for basic | DeepSeek, Gemini Flash Lite, Qwen-Coder, 30+ | GDPR-friendly | llm7.io |
| **Kilo Code** | ~200 req/hr free, auto-router | Grok Code Fast, MiniMax, Nemotron | kilo.ai picks best free model | kilo.ai |
| **ModelScope** | 2,000 calls/day | Qwen3.5 variants | Alibaba; real-name verify | modelscope.cn |
| **SiliconFlow** | 60K TPM free | Qwen3, DeepSeek-R1-Distill | 200+ paid models too | siliconflow.cn |
| **CatAPI** ⚠️ | Signup credits (unverified) | Multi-model via a **"New API"** gateway panel (OpenAI-compatible reseller front-end) | Self-hosted New-API-style aggregator; not an official provider — verify before funding, treat keys as untrusted | catapi.ai |
| **AgentRouter** | $100 signup credit ($200 via referral) | Claude (Opus/Sonnet), GPT, GLM-5.x — OpenAI-compatible gateway | "Public-welfare" reseller, no markup (retail provider rates). GitHub login. Works w/ Claude Code/Cline/Roo/Kilo. Not for production uptime | agentrouter.org |
| **Bluesminds** | 500 credits signup · 20 RPM · 300 req/day free | GPT-5.5/4o, Gemini, Claude 4.6, Kimi K2.6, DeepSeek, Qwen | Unified gateway (OpenAI/Claude/Gemini-compatible). GPT-4.1 + Qwen Coder cost 0 quota. Claude Code + Codex support | api.bluesminds.com |
| **Voyage AI** | 50M tokens/mo free | Embeddings + rerankers (RAG-tuned) | MongoDB-owned. Generous free tier, OpenAI-compatible | voyageai.com |
| **Jina AI** | 10M tokens free | Embeddings, reranker, reader | Good for RAG testing; reader API turns URLs→LLM text | jina.ai |
| **Pollinations.ai** | Free, server keys unmetered | Text + image + audio + video, single API | Client keys 1 req/hr/IP; server-side keys no rate limit | pollinations.ai |
| **Sarvam AI** | ₹1000 signup credit | Indic-language LLMs + STT/TTS + doc digitization | Indian startup; best for Indian-language tasks | sarvam.ai |

### Aggregators (route across many free tiers with one key)

| Tool | What | Link |
|---|---|---|
| **cheahjs/free-llm-api-resources** | The canonical community list of legitimate free LLM APIs (excludes reverse-engineered/cracked services) | github.com/cheahjs/free-llm-api-resources |
| **MrFadiAi/free-llm-gateway** | OpenAI-compatible gateway aggregating **24+ providers, 260+ free models** auto-discovered, auto-fallback, rate-limit tracking, dashboard | github.com/MrFadiAi/free-llm-gateway |
| **FreeLLMAPI** | OSS BYOK proxy (~9.8K★). Stacks the free tiers of **16 providers (~1.7B tokens/mo, 110+ models)** behind one `/v1`. Smart routing, auto-failover, per-key rate tracking (avoids 429s), AES-256 key encryption. Live catalog = $19/yr; router free forever | freellmapi.co · github.com/tashfeenahmed/freellmapi |
| **gaca-core** (G.A.C.A.) | OSS "Universal AI Bus" — **87+ free models from 11 providers**, OpenAI-compatible (`/v1/chat/completions`), auto-failover + ranking + rate limiting. Drop-in fallback for any OpenAI client | github.com/gacabartosz/gaca-core |
| **LiteLLM / OpenRouter** | Route + fall back across providers to multiply free quotas | litellm.ai · openrouter.ai |

> Combine the multi-provider free tiers (Groq + Cerebras + Google AI Studio + Chutes + Nineteen + OpenRouter `:free`) behind LiteLLM/free-llm-gateway → effectively continuous free inference.

---

## Table 2 — Trial Credits (Stack These)

| Provider | Credits | Expiry | Models | How |
|---|---|---|---|---|
| **Anthropic** | $5 | 90 days | All Claude incl. Opus 4.8 | console.anthropic.com |
| **OpenAI** | $5 | 90 days | All GPT incl. GPT-5.5 | platform.openai.com |
| **DeepSeek** | $5 | 30 days | V4 Pro / V4 Flash | platform.deepseek.com |
| **AWS Bedrock** | $300 | 90 days | Claude, Llama, Titan | New AWS account |
| **Google Cloud Vertex AI** | $300 | 90 days | All Gemini models | New GCP account |
| **Azure AI Foundry** | $200 | 30 days | GPT-5.5, Claude, Llama | New Azure account |
| **OpenRouter** | $1 | — | Any model | Signup bonus |
| **Moonshot (Kimi)** | Varies | — | Kimi K2.6 (80.2%) | moonshot.cn new account |

> **Stack strategy:** AWS ($300) + GCP ($300) + Azure ($200) = **$800+** in cloud AI credits.
> Run Opus 4.8 ($25/M out) or GPT-5.5 ($30/M out) for months at zero cost.

---

## How to Access Claude Opus 4.8 For Free

### Ongoing Access

| Method | Limits | How |
|---|---|---|
| **Claude.ai free plan** | Daily message cap | claude.ai |
| **Puter.js** | None listed | developer.puter.com — free unlimited |
| **Anthropic Open Source** | 6 months Claude Max ($200/mo value) | Open-source maintainers — anthropic.com/open-source |

### Trial / Limited

| Method | Value | Duration | How |
|---|---|---|---|
| **Anthropic API trial** | $5 credits | 90 days | console.anthropic.com |
| **Notion Business Trial** | Unlimited Opus | 30 days | notion.so → start Business trial |
| **AWS Bedrock** | $300 credits | 90 days | Model ID: `anthropic.claude-opus-4-8` |
| **Google Vertex AI** | $300 credits | 90 days | Model: `claude-opus-4-8@anthropic` |
| **Azure AI Foundry** | $200 credits | 30 days | Azure AI Studio → Anthropic models |

---

---

## TokenLB — API Marketplace & Developer Credits

**URL:** tokenlb.net · **Users:** 19,000+ · **Providers:** 40+ · **Activation:** minutes

TokenLB is a self-service API key marketplace offering lower-cost access to 40+ AI providers under a single dashboard. Useful for global developers who want cheaper rates, faster key activation, and unified billing across OpenAI, Claude, Gemini, DeepSeek, Qwen, and Llama.

### Why Use TokenLB

| Feature | Detail |
|---|---|
| Single dashboard | Keys, balance, usage logs in one place — no hopping between provider portals |
| Lower cost | Designed for recurring API workloads — better rates than direct provider billing |
| Self-service | Register → fund → generate key → connect app — no manual processing |
| 40+ providers | OpenAI, Anthropic, Gemini, DeepSeek, Qwen, Llama, and more |
| Usage transparency | Per-model usage logs, weekly trends, token breakdowns |

### Weekly Model Rankings (June 26, 2026)

Top 5 models by routed tokens across 19K+ users — real usage signal:

| Rank | Model | Provider | Weekly Tokens | Share |
|---|---|---|---|---|
| 1 | claude-opus-4-8 | Anthropic | 173.2M | 46.7% |
| 2 | claude-opus-4-7 | Anthropic | 76.6M | 20.7% |
| 3 | gpt-5.5 | OpenAI | 56.0M | 15.1% |
| 4 | gpt-5.4-mini | OpenAI | 21.4M | 5.8% |
| 5 | claude-sonnet-4-6 | Anthropic | 17.7M | 4.8% |

> Claude Opus 4.8 dominates at 46.7% of all routed tokens — strong adoption signal.

### Developer Support Program (Free Credits for OSS)

TokenLB offers monthly token credits for open-source maintainers, content creators, and community operators:

| Stars | Monthly Credits |
|---|---|
| 100–499 stars | $20–50 / month |
| 500–1,999 stars | $50–100 / month |
| 2,000–9,999 stars | $100–300 / month |
| 10,000+ stars | Evaluated individually |

**How to apply:** Join t.me/tokenlb and submit your GitHub link + stars + usage scenario. Must display TokenLB attribution link in README/docs.

Community creators (Discord, YouTube, Telegram, newsletters) can also apply.

### Quick Start

```python
# TokenLB is OpenAI API-compatible — swap base_url
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
| Highest daily volume | Llama 3.3 70B | Cerebras | ~60%, 1M tok/day |
| Free 1M ctx chat | GLM-5.2 | chat.z.ai | ~72% SWE-bench |
| Cheapest paid production | DeepSeek V4 Flash | DeepSeek API | 72%, $0.28/M out |
| Google ecosystem | Gemini 3.1 Flash | Google AI Studio | 74% SWE-bench |
| Multi-model single key | Any `:free` | OpenRouter | Varies |

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

### Cerebras — 1M tokens/day free

```python
from cerebras.cloud.sdk import Cerebras
client = Cerebras(api_key="YOUR_KEY")
r = client.chat.completions.create(
    model="llama3.3-70b",
    messages=[{"role": "user", "content": "Hello"}]
)
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

| Repo | What |
|---|---|
| [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | Permanent free LLM API list |
| [amardeeplakshkar/awesome-free-llm-apis](https://github.com/amardeeplakshkar/awesome-free-llm-apis) | Rate limits, SDK compat, speed tiers |
| [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | Free LLM inference resources |
| [bradAGI/awesome-cli-coding-agents](https://github.com/bradAGI/awesome-cli-coding-agents) | Curated CLI agents directory |
