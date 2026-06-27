# References — Runnable Repos & Source Tools

> Actual runnable tools, libraries, SDKs, and the proxy/router projects this archive relies on.
> (Replaces the old `references/` directory — clone any repo directly from its link.)

---

## Core Runnable Tools

| Repo | Stars | What it is |
|---|---|---|
| [ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp) | 82K+ | Gold-standard local LLM inference engine (C++) |
| [Mozilla-Ocho/llamafile](https://github.com/Mozilla-Ocho/llamafile) | 24K+ | Ship any model as one executable file |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | 20K+ | Official MCP server for browser automation |
| [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) | 25K+ | AI orchestration SDK (C# / Python / Java) |
| [browserbase/stagehand](https://github.com/browserbase/stagehand) | 12K+ | Natural-language browser control (act/extract/observe/agent) |

---

## Subscription-as-API / Proxy / Router Projects

> Reuse a Claude Code / Copilot / ChatGPT subscription as an API, or route Claude Code to free/cheaper backends.
> ⚠️ Many are reverse-engineered — may violate provider ToS, risk account suspension. Use on your own accounts at your own risk. See [CREDITS.md](./CREDITS.md) Part 4.

| Repo | What it does |
|---|---|
| [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | 38.5K★ — wraps Claude Code / Codex / Gemini / Grok OAuth → OpenAI-compatible API |
| [decolua/9router](https://github.com/decolua/9router) | Routes Claude Code/Codex/Cursor/Cline/Copilot/Antigravity to free Claude/GPT/Gemini via 40+ providers; auto-fallback, taps Kiro/OpenCode-Free/Vertex |
| [Alorse/cc-compatible-models](https://github.com/Alorse/cc-compatible-models) | Reference: configs + pricing for Qwen/DeepSeek/MiniMax/Kimi/GLM/MiMo/StepFun with Claude Code |
| [jodavan/claude-code-proxy](https://github.com/jodavan/claude-code-proxy) | Route each Claude Code tier to a different provider (e.g. GLM for Haiku/Opus via `api.z.ai/api/anthropic`), keep Sonnet on your sub |
| [horselock/claude-code-proxy](https://github.com/horselock/claude-code-proxy) | Standalone OAuth — direct API calls using Claude Code credentials |
| [Rishurajgautam24/free-claude-code](https://github.com/Rishurajgautam24/free-claude-code) | Local FastAPI proxy → NVIDIA NIM / OpenRouter / DeepSeek / Ollama / LM Studio; intercepts trivial requests to save quota |
| [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | ~9.8K★ — OpenAI-compatible BYOK proxy stacking 16 providers' free tiers (~1.7B tok/mo) behind one `/v1`; smart routing, failover, encrypted keys |
| [gacabartosz/gaca-core](https://github.com/gacabartosz/gaca-core) | "Universal AI Bus" — 87+ free models from 11 providers, OpenAI-compatible, auto-failover + ranking + rate limiting |

> ⚠️ Avoid any repo advertising "keygen / activator / unlimited Pro without payment" — classic malware/scam pattern.

---

## Curated Lists (merged into this archive)

Content from these awesome-lists has been folded into the topic files; originals for reference:

| List | Folded into |
|---|---|
| [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) · [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | [FREE-ACCESS.md](./FREE-ACCESS.md) |
| [bradAGI/awesome-cli-coding-agents](https://github.com/bradAGI/awesome-cli-coding-agents) · [PierrunoYT/awesome-ai-dev-tools](https://github.com/PierrunoYT/awesome-ai-dev-tools) | [AGENTS.md](./AGENTS.md) |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | [AGENTS.md](./AGENTS.md) Part 5A |
| [kyrolabs/awesome-agents](https://github.com/kyrolabs/awesome-agents) · [caramaschiHG/awesome-ai-agents-2026](https://github.com/caramaschiHG/awesome-ai-agents-2026) | [AGENTS.md](./AGENTS.md) Part 9 |
| [DmitryScaletta/free-database-services](https://github.com/DmitryScaletta/free-database-services) | [BACKEND.md](./BACKEND.md) |

---

## Primary Sources — June 2026 Additions

> Web-verified (June 27, 2026) for the latest batch of models/tools added across the archive.

**Models** — [Claude Fable 5 / Mythos 5 (Anthropic)](https://www.anthropic.com/news/claude-fable-5-mythos-5) · [Microsoft MAI models (Build 2026)](https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/) · [Kimi K2.7-Code (Moonshot)](https://www.marktechpost.com/2026/06/12/moonshot-ai-releases-kimi-k2-7-code-a-coding-model-reporting-21-8-on-kimi-code-bench-v2-over-k2-6/) · [Meta Muse Spark](https://ai.meta.com/blog/introducing-muse-spark-msl/) · [Apple AFM 3 (WWDC)](https://www.apple.com/newsroom/) · [Gemini Omni (I/O)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/)

**Agents / MCP** — [OpenClaw](https://github.com/openclaw/openclaw) · [Gumloop $50M Series B](https://techcrunch.com/2026/03/12/gumloop-lands-50m-from-benchmark-to-turn-every-employee-into-an-ai-agent-builder/) · [VoltAgent](https://github.com/VoltAgent/voltagent) · [OpenAgents](https://github.com/openagents-org/openagents) · [Anthropic Creative Connectors](https://www.anthropic.com/news/claude-for-creative-work)

**Frontend** — [Claude Design (Anthropic Labs)](https://www.anthropic.com/news/claude-design-anthropic-labs) · [a0.dev (YC W25)](https://news.ycombinator.com/item?id=43015267) · [Cloudflare VibeSDK](https://github.com/cloudflare/vibesdk) · [Blink.new (YC)](https://www.ycombinator.com/companies/blink-new)

**Backend** — [Microsoft Rayfin](https://siliconangle.com/2026/06/02/microsoft-launches-rayfin-let-developers-agents-build-app-backends-fabric/) · [Zilliz Vector Lakebase](https://www.businesswire.com/news/home/20260621822926/en/) · [ScyllaDB Vector Search](https://www.scylladb.com/vector-search/) · [Actian VectorAI DB](https://www.actian.com/databases/vectorai-db/) · [Northflank BYOC](https://northflank.com/features/bring-your-own-cloud)

**Media** — [FLUX.2 Pro pricing](https://bfl.ai/pricing) · [OpenAI gpt-image-2](https://openai.com/index/introducing-chatgpt-images-2-0/) · [Mistral Voxtral TTS](https://mistral.ai/news/voxtral-tts/) · [Hume TADA](https://www.hume.ai/blog/opensource-tada) · [Kyutai Pocket TTS](https://kyutai.org/blog/2026-01-13-pocket-tts) · [Fun-Realtime-TTS #1 Arena](https://artificialanalysis.ai/articles/fun-realtime-tts-new-text-to-speech-model-topping-artificial-analysis-leaderboard) · [GPT-Realtime-2](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/) · [ClickHouse acquires Langfuse](https://siliconangle.com/2026/01/16/database-maker-clickhouse-raises-400m-acquires-ai-observability-startup-langfuse/) · [Braintrust $80M Series B](https://bayelsawatch.com/braintrust-raises-80m-series-b/)

**Free access** — [BazaarLink](https://bazaarlink.ai/free) · [freellm.net](https://freellm.net/) · [OpenCode Zen](https://opencode.ai/zen) · [xAI free credits](https://www.getaiperks.com/en/blogs/22-xai-grok-free-credits) · [Vercel AI Gateway](https://vercel.com/ai-gateway)

> ⚠️ **Not added (research caught these):** *Kluster.ai* was shut down (acquired by MITO, sunset Jun 9 2026) — excluded as a dead free provider. *VoltAgent* star count listed as ~2K (sourced), not the 26K in the source notes (unverified).
