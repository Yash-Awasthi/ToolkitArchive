# Frontend / UI Builders & Design-to-Code — June 2026

> Vibe-coding tools that turn a prompt (or a screenshot, or a Figma file) into a running frontend.
> Free tiers move fast — every major builder is now **credit/token metered**. Numbers verified ~June 2026; confirm on vendor pages before relying on them.

---

## Part 1 — Full-Stack AI App Builders (prompt → deployed app)

| Tool | What | Free tier | Paid entry | Model / BYOK | Link |
|---|---|---|---|---|---|
| **Bolt.new** | Browser IDE, full-stack in WebContainers | **1M tokens/mo** (no card) — most generous of the majors, ~2–5 small apps | Pro $25/mo (~13M tokens) | Claude (no BYOK) | bolt.new |
| **Lovable** | Prompt → React + Supabase SaaS, cleanest code | 5 credits/day, ~30/mo cap | Pro from $25/mo (100 credits) | Managed | lovable.dev |
| **Replit Agent** (Agent 4) | Cloud IDE + DB + deploy, 50+ langs, real-browser testing | Starter: daily Agent trial, 1 published app | Core $20–25/mo ($25 credits) · Pro $100/mo | Managed | replit.com |
| **v0** (Vercel) | Polished React/Next UI, auto-deploy to Vercel | Limited free credits | Premium $20/mo (Mini/Pro/Max tiers) | Managed (no model choice) | v0.dev |
| **Create.xyz** ("Anything") | NL → web + mobile apps w/ backend, exportable code | Free try-out tier | Pro/Max (credits) | Managed | create.xyz |
| **Base44** (Wix) | Full-stack internal tools, no-code | Free tier | ~$16/mo | Managed | base44.com |
| **Emergent** | Managed full-stack runtime, GitHub export | Free trial | Credits | Managed | emergent.sh |
| **Mocha** | Prompt → full-stack app | Free tier | Credits | Managed | getmocha.com |
| **Softr** | No-code apps on Airtable/DB | Free tier | ~$59/mo | Managed | softr.io |

> **Credit-burn rule (all of them):** vague prompts, long chats, and error loops eat the free allowance. Plan before prompting. Bolt's 1M tokens/mo is the most usable free runway.

---

## Part 2 — UI Component / Design Generators (prompt or screenshot → components)

| Tool | What | Free | Code export | Stack | Link |
|---|---|---|---|---|---|
| **Subframe** | AI-native visual canvas, real design controls, 1:1 React/Tailwind export (YC, ex-Vercel/Stripe) | Free plan (export/page limits) | React + Tailwind | React/Tailwind only | subframe.com |
| **Magic Patterns** | Screenshot/prompt → React, Figma + MCP import/export (YC S23, a16z) | Free tier | React + Tailwind | React | magicpatterns.com |
| **Polymet** | Component-driven; builds a design system from prompts | Free trial (export = paid) | Yes (paid) | React | polymet.ai |
| **Motiff** | UI generator — **discontinued**, data export until Oct 31 2026 | — | — | — | motiff.com |
| **Galileo AI** | Text → editable UI designs | Free credits | Figma | — | usegalileo.ai |
| **Uizard** | Wireframe/screenshot → editable UI | Free tier | — | — | uizard.io |
| **tldraw "Make Real"** | Draw a wireframe → working HTML | Free (BYOK) | HTML | — | tldraw.com |
| **Codia AI** | Screenshot/Figma → code | Free credits | Multi | — | codia.ai |
| **Visily** | Screenshot/text → wireframes & UI | Free tier | — | — | visily.ai |

---

## Part 3 — Design-to-Code (Figma / mockup → production code)

| Tool | What | Free | Link |
|---|---|---|---|
| **Figma Make** | Figma's native AI prompt-to-app | Included in Figma plans | figma.com |
| **Anima** | Figma/XD → React/Vue/HTML | Free tier | animaapp.com |
| **Locofy** | Figma/Adobe → React/RN/Vue, "Lightning" AI | Free tier | locofy.ai |
| **Builder.io Fusion** | Design-system + codebase aware, visual control, enterprise | ~60–75 Agent credits/mo (15–25/day) | Pro $24/user/mo (500 credits) | builder.io |
| **Quest** | Figma → React, clean code | Free tier | quest.ai |
| **Tempo** | AI + visual editor for React apps | Free tier | tempo.new |

---

## Part 4 — No-Code AI Site Builders (marketing / portfolio / CMS)

| Tool | What | Free tier | Paid entry | Code export | Link |
|---|---|---|---|---|---|
| **Framer** | Design-led sites, Wireframer + Workshop AI | Full editor, 1,000 pages, 10 CMS, 2-page publish | Basic ~$10/mo · Pro $30/mo (+$40/editor seat) | **No export (lock-in)** | framer.com |
| **Webflow** | Content/SEO-heavy, AI Site Builder + AEO audits | Limited (Webflow badge) | Site plans + $19/mo workspace (layered) | Yes | webflow.com |
| **Readdy** | NL → sites, outputs clean code + Figma + built-in backend | 250 credits/mo, 2 projects | Starter ~$11–19/mo · Pro ~$24–40/mo (25 credits/generation) | Yes | readdy.ai |
| **Wix AI** | Prompt → full site | Free (Wix ads) | ~$17/mo | No | wix.com |
| **Durable** | 30-second AI business site | Free trial | ~$15/mo | No | durable.co |
| **Relume** | AI sitemap + wireframes → Figma/Webflow | Free trial | ~$36/mo | To Figma/Webflow | relume.io |
| **Hostinger Horizons** | Prompt → app, cheap | Trial | ~$19/mo | Limited | hostinger.com |

---

## Part 5 — Open-Source / Self-Hostable (zero vendor lock-in, BYOK or local model)

| Tool | What | License | Stars | Cost | Link |
|---|---|---|---|---|---|
| **Dyad** | Local v0/Lovable/Bolt alt, runs on your machine, no sign-up | Apache 2.0 | rising | Free (BYOK; Ollama = $0) · Pro $20/mo | dyad.sh · github.com/dyad-sh/dyad |
| **bolt.diy** | Self-hostable open Bolt.new, 100+ models | MIT | high | Free (BYOK) | github.com/stackblitz-labs/bolt.diy |
| **Onlook** | Visual React/Next editor, live DOM ↔ code, desktop | Apache 2.0 | ~26K | Free | onlook.com |
| **Plasmic** | Visual builder, integrates existing codebase | MIT | — | Free tier | plasmic.app |
| **Reflex** | Full-stack web apps in pure Python | Apache 2.0 | ~29K | Free | reflex.dev |
| **Refine** | Data-rich React apps framework | MIT | ~35K | Free | refine.dev |
| **Silex** | Open visual website builder | AGPL 3.0 | ~2.9K | Free | silex.me |
| **Pythagora** | AI full-stack app dev (GPT Pilot lineage) | — | high | Free (BYOK) | pythagora.ai |

> **Cheapest path to "Lovable but free":** Dyad or bolt.diy + a free LLM key (Google AI Studio / Groq) or local Ollama → unlimited builds at $0. See [FREE-ACCESS.md](./FREE-ACCESS.md).

---

## Pick-by-need

| Need | Pick |
|---|---|
| Most free runway | Bolt.new (1M tokens/mo) |
| Non-technical SaaS MVP | Lovable |
| Real backend / non-JS / deploy | Replit Agent |
| Inside Vercel/Next | v0 |
| Enterprise codebase + design system | Builder.io Fusion |
| Designer who wants real controls | Subframe |
| Screenshot → code | Magic Patterns |
| Marketing/portfolio site | Framer (design) / Webflow (content+SEO) |
| Zero cost, self-host | Dyad / bolt.diy + free key |
