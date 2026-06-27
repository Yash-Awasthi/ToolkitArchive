# Media Gen, Voice & LLMOps — June 2026

> Image / voice generation, plus the LLMOps stack (observability, eval, gateways) and docs tooling for vibe-coded apps.
> **Video, music, and UI-design AI live in [AGENTS.md](./AGENTS.md) Parts 12–14.** Free tiers verified ~June 2026.

---

## Part 1 — Image Generation

> Big 2026 shift: free now rivals paid. Gemini "Nano Banana Pro" + free Flux (via Krea/OpenArt) get you ~most of the way to Midjourney. Pay only for volume / resolution / commercial license / privacy.

| Tool | Best for | Free tier | Paid entry | API | Link |
|---|---|---|---|---|---|
| **Midjourney v8.1** | Artistic quality (aesthetic king) — still strongest aesthetic | None | $10/mo Basic → $120 Mega | ❌ no public API (subscription-only) | midjourney.com |
| **FLUX.2 Pro** (Black Forest Labs) | **Best photoreal API**, multi-ref consistency, edit ≤4MP | schnell/Klein open-weight (local) | MP-based: ~$0.03 first MP then $0.015/MP (~$0.02–0.06/img) | ✅ | bfl.ai |
| **gpt-image-2** (OpenAI) | Conversational image creation, **95%+ text** accuracy, 4K, web-search/thinking | ChatGPT free (limited) | API (token-based) · Plus $20/mo | ✅ (API + Codex) | openai.com |
| **Imagen 4** (Google) | **Best text rendering** + photorealism, 2K, SynthID | Free in AI Studio | $0.02 Fast · $0.04 Std · $0.06 Ultra /img | ✅ | ai.google.dev |
| **Ideogram v3** | Readable **text in images** (typography king, 90–95%), Style Refs | 10 credits/wk (~40 img) | Plus $15/mo (1,000 credits) | Enterprise | ideogram.ai |
| **MAI-Image-2.5** (Microsoft) | T2I + editing, **#3 on Arena** (beats Nano Banana Pro) | — | $5/$33 per 1M (+ Flash variant) | ✅ Foundry/OpenRouter/Fireworks | microsoft.ai |
| **Recraft** | **Vectors / SVG**, brand systems | 50 credits/day | $10/mo (1,000 credits) | ✅ | recraft.ai |
| **Leonardo AI** | Game/concept art + editing | 150 tokens/day (~20–30 img) | $12/mo | ✅ | leonardo.ai |
| **Krea** | Real-time gen, generous free | 50–100/day | ~$5/mo (annual) | ✅ | krea.ai |
| **Freepik / Magnific** | All-in-one (Flux+Gemini+Ideogram+Runway in one sub) | 20 gen/day | €6–9.99/mo | ✅ | freepik.com |
| **Google Gemini (Nano Banana Pro)** | Free frontier quality | Free in Gemini app / AI Studio | — | ✅ (AI Studio) | gemini.google.com |
| **DALL·E 3 / GPT Image** | In ChatGPT | ChatGPT free (limited) | Plus $20/mo | ✅ | openai.com |
| **Adobe Firefly** | Commercial-safe, integrated | Free credits | Creative Cloud | ✅ | firefly.adobe.com |
| **Stable Diffusion / SDXL / SD3** | Local, fully free | Free (open-weight) | — | self-host | stability.ai |

> **Cheapest API at scale:** Imagen 4 Fast / FLUX.2 Pro (~$0.02/img). **Best text-in-image:** Ideogram v3 / Imagen 4 / gpt-image-2 (95%+). **Strongest aesthetic:** Midjourney v8.1 (no API). **Most generous free:** Krea / Recraft (50/day). **Commercial-safe:** Firefly. ⚠️ Free tiers usually make outputs public + trainable; only paid = private + ownership.

---

## Part 2 — Voice / Audio (TTS · STT · music)

| Tool | What | Free tier | Link |
|---|---|---|---|
| **ElevenLabs** | Best TTS + voice cloning | 10K chars/mo | elevenlabs.io |
| **Alibaba Fun-Realtime-TTS** | **#1 Arena Elo (1,219)** — beats Gemini 3.1 Flash TTS & Cartesia Sonic. 30+ langs, Chinese dialects | API ~$27.6/1M chars | tongyi (FunAudioLLM) |
| **Inworld Realtime TTS-2** | Closed-loop (hears prior audio), NL voice-direction, 100+ langs — built for game NPCs | API ~$35/1M chars | inworld.ai |
| **OpenAI GPT-Realtime-2** | GPT-5-class speech-to-speech — *reasons* before speaking, tool calls mid-speech, preambles | API $32/$64 per 1M audio tok | openai.com |
| **Cartesia** (Sonic) | Ultra-low-latency TTS for agents | Free credits | cartesia.ai |
| **Mistral Voxtral TTS** | **Open-weight** frontier TTS (CC BY-NC), 3s voice clone, ~90ms TTFA, 9 langs. Beats ElevenLabs Flash | Weights free (HF) · API $16/1M chars | mistral.ai |
| **Hume AI TADA** | **MIT** open — text-acoustic dual alignment = *zero hallucinations*, 5x+ faster, ≤700s. 1B EN / 3B multiling | Free (open-weight) | hume.ai |
| **Kyutai Pocket TTS** | **100M params, runs CPU realtime** (even WASM/browser), voice clone, 6 langs. Lightest prod TTS | Free (open-weight) | kyutai.org |
| **MAI-Voice-2** (Microsoft) | TTS, 15 langs, voice clone from short sample (+Flash) | API (Foundry/OpenRouter) | microsoft.ai |
| **MAI-Transcribe-1.5** (Microsoft) | SOTA STT — 5x faster than competitors, 43 langs | API (Foundry/OpenRouter) | microsoft.ai |
| **PlayHT / Play.ai** | TTS + voice agents | Free trial | play.ht |
| **Deepgram** | Fast STT (transcription) | $200 free credit | deepgram.com |
| **AssemblyAI** | STT + audio intelligence | Free credits | assemblyai.com |
| **OpenAI Whisper** | Open-weight STT | Free (self-host) / API | github.com/openai/whisper |
| **Groq Whisper** | Whisper at LPU speed | Free tier (see FREE-ACCESS) | groq.com |
| **Suno / Udio** | Music generation | Free daily credits | suno.com · udio.com |
| **Stability Audio** | Music/SFX | Free tier | stableaudio.com |

> **TTS 2026 rankings (Artificial Analysis Speech Arena):** Fun-Realtime-TTS (1,219) > Gemini 3.1 Flash TTS (1,214) > Inworld TTS-2 (1,209) > Cartesia Sonic 3.5 (1,203) — within 24 Elo, tightest race ever.
> **Pick:** open-weight/on-device → Voxtral · Hume TADA · Pocket TTS · reasoning voice agents → GPT-Realtime-2 · Inworld TTS-2 · cheapest quality → Fun-Realtime-TTS.
> Full music-gen comparison + licensing tree → [AGENTS.md](./AGENTS.md) Part 13.

---

## Part 3 — LLMOps: Observability · Eval · Gateways

Three camps: **tracing** (Langfuse, LangSmith), **gateways** (Helicone, Portkey — routing/caching/cost, usually zero markup), **eval** (Braintrust, Phoenix).

| Tool | Camp | License | Free tier | Link |
|---|---|---|---|---|
| **Langfuse** | Tracing + prompts + eval | MIT (now ClickHouse-owned) | Hobby 50K obs/mo; **unlimited self-host** | langfuse.com |
| **AgentOps** | Agent tracing — time-travel debugging, multi-agent viz | Apache 2.0 | Free tier; 400+ LLMs | agentops.ai |
| **W&B Weave** | Tracing + eval inside existing W&B console (`@weave.op`) | Apache 2.0 | Free tier | wandb.ai/weave |
| **Laminar** | Agent-first tracing, **OTel-native** (~5% overhead) | Apache 2.0 | Free 1GB; self-host free | laminar.sh |
| **Confident AI** | Eval-first (cloud **DeepEval**) — every trace scored, alerts | OSS core (~12K★) | Free tier | confident-ai.com |
| **Maxim AI** | Agent **simulation** pre-prod + real-time post-deploy | Closed | Free tier | getmaxim.ai |
| **LangSmith** | Tracing (LangChain/Graph) | Closed | 5K traces/mo | smith.langchain.com |
| **Helicone** | Gateway (1-line proxy) | Apache 2.0 | 10K req/mo, 7-day retention; self-host free | helicone.ai |
| **Portkey** | Gateway (multi-provider routing) | MIT | 10K logs/mo | portkey.ai |
| **Braintrust** | Eval-first | Closed | **1M spans/mo, 10K evals** (most generous by volume) | braintrust.dev |
| **Arize Phoenix** | Eval + OTel-native | ELv2 | **Unlimited self-host** | phoenix.arize.com |
| **Opik** (Comet) | Tracing + eval | Apache 2.0 | Free OSS | comet.com/opik |
| **OpenLLMetry** | OTel instrumentation | Apache 2.0 | Free OSS | traceloop.com |
| **Pydantic Logfire** | Tracing (Pydantic AI) | Free tier | — | pydantic.dev/logfire |

> **Zero-cost stack:** self-host Langfuse or Phoenix → no per-unit cost. **Fastest start:** Helicone (change one URL). **By framework:** LangChain→LangSmith · LlamaIndex→Phoenix/Langfuse · raw API→Helicone/Portkey. Combine freely (OTel-based tools interop).

> **2026 funding signals:** Langfuse **acquired by ClickHouse** (Jan 16, $400M Series D, $15B valuation) — still MIT, no pricing change. Braintrust raised **$80M Series B** (Feb 2026, ~$800M valuation; Vercel/Notion/Dropbox customers). Capital is flowing to eval/accountability infra, not just model deployment.

---

## Part 4 — Docs / DevRel / Knowledge

| Tool | What | Free tier | Link |
|---|---|---|---|
| **Mintlify** | AI-native docs (beautiful, fast) | Free tier | mintlify.com |
| **GitBook** | Docs + AI search | Free for OSS/personal | gitbook.com |
| **Docusaurus** | OSS docs framework (Meta) | Free | docusaurus.io |
| **Fern** | SDK + docs from OpenAPI | Free tier | buildwithfern.com |
| **Inkeep / Trieve** | AI answer engine over your docs | Free tier | inkeep.com · trieve.ai |
| **Context7** | Up-to-date lib docs as MCP for agents | Free | context7.com |
| **Kapa AI** | AI assistant grounded in YOUR docs (cites sources, flags gaps). Ingests MD/GitHub/Confluence/YouTube/Zendesk → Slack/Discord/in-app + hosted MCP | Free tier | kapa.ai |
| **Swimm** | **Code-coupled docs** — linked to code snippets, auto-flags/updates on change, CI staleness check | Free tier | swimm.io |

Cross-ref: AI code review / SAST → [AGENTS.md](./AGENTS.md) Part 8 · video/music/UI → Parts 12–14.
