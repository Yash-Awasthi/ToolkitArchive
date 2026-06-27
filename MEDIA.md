# Media Gen, Voice & LLMOps — June 2026

> Image / voice generation, plus the LLMOps stack (observability, eval, gateways) and docs tooling for vibe-coded apps.
> **Video, music, and UI-design AI live in [AGENTS.md](./AGENTS.md) Parts 12–14.** Free tiers verified ~June 2026.

---

## Part 1 — Image Generation

> Big 2026 shift: free now rivals paid. Gemini "Nano Banana Pro" + free Flux (via Krea/OpenArt) get you ~most of the way to Midjourney. Pay only for volume / resolution / commercial license / privacy.

| Tool | Best for | Free tier | Paid entry | API | Link |
|---|---|---|---|---|---|
| **Midjourney** | Artistic quality (aesthetic king) | None | $10/mo Basic | ❌ no public API | midjourney.com |
| **FLUX** (Black Forest Labs) | Open-weights + API flexibility | schnell/Klein open-weight (local) | API ~$0.01–0.10/img (Pro ~$0.08) | ✅ | bfl.ai |
| **Ideogram** | Readable **text in images** | 10 credits/wk (~40 img) | Plus $15/mo (1,000 credits) | Enterprise | ideogram.ai |
| **Recraft** | **Vectors / SVG**, brand systems | 50 credits/day | $10/mo (1,000 credits) | ✅ | recraft.ai |
| **Leonardo AI** | Game/concept art + editing | 150 tokens/day (~20–30 img) | $12/mo | ✅ | leonardo.ai |
| **Krea** | Real-time gen, generous free | 50–100/day | ~$5/mo (annual) | ✅ | krea.ai |
| **Freepik / Magnific** | All-in-one (Flux+Gemini+Ideogram+Runway in one sub) | 20 gen/day | €6–9.99/mo | ✅ | freepik.com |
| **Google Gemini (Nano Banana Pro)** | Free frontier quality | Free in Gemini app / AI Studio | — | ✅ (AI Studio) | gemini.google.com |
| **DALL·E 3 / GPT Image** | In ChatGPT | ChatGPT free (limited) | Plus $20/mo | ✅ | openai.com |
| **Adobe Firefly** | Commercial-safe, integrated | Free credits | Creative Cloud | ✅ | firefly.adobe.com |
| **Stable Diffusion / SDXL / SD3** | Local, fully free | Free (open-weight) | — | self-host | stability.ai |

> **Cheapest API at scale:** Flux 2 Pro (~$0.08/img). **Most generous free:** Krea / Recraft (50/day). **Commercial-safe:** Firefly. ⚠️ Free tiers usually make outputs public + trainable; only paid = private + ownership.

---

## Part 2 — Voice / Audio (TTS · STT · music)

| Tool | What | Free tier | Link |
|---|---|---|---|
| **ElevenLabs** | Best TTS + voice cloning | 10K chars/mo | elevenlabs.io |
| **Cartesia** (Sonic) | Ultra-low-latency TTS for agents | Free credits | cartesia.ai |
| **PlayHT / Play.ai** | TTS + voice agents | Free trial | play.ht |
| **Deepgram** | Fast STT (transcription) | $200 free credit | deepgram.com |
| **AssemblyAI** | STT + audio intelligence | Free credits | assemblyai.com |
| **OpenAI Whisper** | Open-weight STT | Free (self-host) / API | github.com/openai/whisper |
| **Groq Whisper** | Whisper at LPU speed | Free tier (see FREE-ACCESS) | groq.com |
| **Suno / Udio** | Music generation | Free daily credits | suno.com · udio.com |
| **Stability Audio** | Music/SFX | Free tier | stableaudio.com |

> Full music-gen comparison + licensing tree → [AGENTS.md](./AGENTS.md) Part 13.

---

## Part 3 — LLMOps: Observability · Eval · Gateways

Three camps: **tracing** (Langfuse, LangSmith), **gateways** (Helicone, Portkey — routing/caching/cost, usually zero markup), **eval** (Braintrust, Phoenix).

| Tool | Camp | License | Free tier | Link |
|---|---|---|---|---|
| **Langfuse** | Tracing + prompts + eval | MIT (now ClickHouse-owned) | Hobby 50K obs/mo; **unlimited self-host** | langfuse.com |
| **LangSmith** | Tracing (LangChain/Graph) | Closed | 5K traces/mo | smith.langchain.com |
| **Helicone** | Gateway (1-line proxy) | Apache 2.0 | 10K req/mo, 7-day retention; self-host free | helicone.ai |
| **Portkey** | Gateway (multi-provider routing) | MIT | 10K logs/mo | portkey.ai |
| **Braintrust** | Eval-first | Closed | **1M spans/mo, 10K evals** (most generous by volume) | braintrust.dev |
| **Arize Phoenix** | Eval + OTel-native | ELv2 | **Unlimited self-host** | phoenix.arize.com |
| **Opik** (Comet) | Tracing + eval | Apache 2.0 | Free OSS | comet.com/opik |
| **OpenLLMetry** | OTel instrumentation | Apache 2.0 | Free OSS | traceloop.com |
| **Pydantic Logfire** | Tracing (Pydantic AI) | Free tier | — | pydantic.dev/logfire |

> **Zero-cost stack:** self-host Langfuse or Phoenix → no per-unit cost. **Fastest start:** Helicone (change one URL). **By framework:** LangChain→LangSmith · LlamaIndex→Phoenix/Langfuse · raw API→Helicone/Portkey. Combine freely (OTel-based tools interop).

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

Cross-ref: AI code review / SAST → [AGENTS.md](./AGENTS.md) Part 8 · video/music/UI → Parts 12–14.
