# ⚡ Skills, Plugins & MCP — What's New, Directories, How-To (verified 29 September 2026)

<p align="center"><a href="./README.md">🏠 Home</a> · <a href="https://yash-awasthi.github.io/ToolkitArchive/">🔎 Explorer</a> · <a href="https://yash-awasthi.github.io/ToolkitArchive/benchmarks.html">📊 Benchmarks</a> · <a href="./NEWS.md">📰 News</a> · <a href="./STUDENTS.md">🎓 $0 guide</a> · <a href="./FREE-ACCESS.md">🆓 Free AI</a></p>

> [!NOTE]
> Every star count is live from the GitHub API (29 Sep 2026). Install commands are copied from each
> project's README. ⚠️ Read every `SKILL.md`, plugin and MCP server before installing — they are
> instructions and code your agent will run.

**Contents:** [Sept 2026 wave](#new-skills-plugins--mcps--sept-2026-wave) · [Directories](#skill-directories-where-to-find-skills) · [Install in 60 seconds](#install-a-skill-or-plugin-in-60-seconds) · [How skills work](#how-skills-work) · [Write your own](#write-your-own-skill) · [Builders' setups](#notable-builders-setups) · [Security bundles](#security--red-team-skill-bundles) · [Dev packs](#dev--engineering-skill-packs)

---

## New skills, plugins & MCPs — Sept 2026 wave

> Star counts below are live from the GitHub API (29 Sep 2026). The tools people are actually installing right now, found by repeated searches across GitHub, Reddit,
> YouTube and Instagram (29 Sep 2026). Install commands
> are copied from each project's README — read the `SKILL.md` / source before you run it.

### Design & UI taste (stop the "AI slop" look)

| Tool | What it does | Install |
|---|---|---|
| ★ **Impeccable** (pbakaus) | A full design language for agents: 23 commands, 7 design pillars, in-browser live mode. Built as the successor to Anthropic's `frontend-design` skill. 72K★ | `git submodule add https://github.com/pbakaus/impeccable vendor/impeccable && npx impeccable link --source=vendor/impeccable --providers=claude,cursor` · impeccable.style |
| ★ **Taste Skill** (Leonxlnx) | "Anti-slop" frontend rules — typography, spacing, colour, motion, components. v2 out. 91K★ | `npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"` · tasteskill.dev |
| ★ **Emil Kowalski's skills** | From the maker of Sonner and Vaul: `animate` (picks curves, durations, properties), design-engineering polish, Apple-style design, animation vocabulary | `npx skills@latest add emilkowalski/skills` · emilkowal.ski/skill |
| **UI UX Pro Max** (131K★) | Searchable design-intelligence database: styles, palettes, font pairings, UX rules; generates a design system from a prompt | `npx skills add nextlevelbuilder/ui-ux-pro-max-skill` · uupm.cc |
| **design-taste** (h3nryprod01) | One merged skill combining Emil Kowalski + Impeccable + Taste Skill | github.com/h3nryprod01/design-taste |
| **awesome-design-md** (VoltAgent, 119K★) | `DESIGN.md` files extracted from 59+ real sites (Stripe, Linear, Vercel…) — drop one in your repo and the agent copies that look | github.com/VoltAgent/awesome-design-md |
| **DESIGN.md** (Google Stitch) | Open format for design tokens + rules that agents read, like `AGENTS.md` for design. Stitch exports/imports it; Stitch MCP connects it to Antigravity | stitch.withgoogle.com |
| **Figma MCP** | Official. Agents can now **write to the canvas** (frames, components, variables), read Figma Motion timing/easing, and edit generative plugins/shaders. Write access free during beta, paid seats only; free Starter plan = 6 MCP calls/month | help.figma.com (Figma MCP guide) |
| **Paper** (paper.design) | Design tool built for agents; MCP with 24 read/write tools (sync tokens from Figma, fill UI with live data, export JSX/Tailwind) | `claude plugin marketplace add paper-design/agent-plugins && claude plugin install paper-desktop@paper-design` |
| **Pencil** (pen.dev) | Infinite design canvas inside your IDE; any model can design on it, then sync to code | pen.dev |
| **21st.dev Magic MCP** | Generates UI components in several variants from a prompt; 12K+ component library | 21st.dev/ai |
| **shadcn MCP** | Browse/search/install components from any shadcn registry through the agent | ui.shadcn.com/docs/mcp |
| **Claude Design** (Anthropic Labs, Apr 2026) | Designs, prototypes, slides and one-pagers by talking to Claude | claude.com/product/design |

### Motion, animation & 3D

| Tool | What it does | Install |
|---|---|---|
| ★ **Motion AI Kit** (motion.dev, ex-Framer Motion) | Official skill + MCP: CSS spring generation, full up-to-date docs as MCP resources | motion.dev/docs/ai-kit |
| ★ **GSAP skills** (greensock, official) | Correct GSAP usage: timelines, ScrollTrigger, plugins, React/Vue/Svelte | github.com/greensock/gsap-skills |
| **Anime.js skills / MCP** | Anime.js v4 skill (BowTiedSwan) and an Anime.js MCP server | github.com/BowTiedSwan/animejs-skills |
| ★ **Remotion skills** | Make videos from React code with your agent | `npx skills add remotion-dev/skills` |
| **Three.js skills** (CloudAI-X) | Current Three.js APIs for 3D scenes and interactive experiences | `npx skills add CloudAI-X/threejs-skills` |
| **LerSent001 tools** | Liquid Orb editor (13 animated orb presets → transparent PNG) and **Holo Card**, a Codex skill that turns artwork into interactive holographic cards (parallax, contour glow, Blender export) | lersent001.github.io/orb · github.com/LerSent001/holo-card |

### Browsing & web access for agents

| Tool | What it does | Install |
|---|---|---|
| ★ **Playwright MCP / CLI** | Microsoft's browser driver (38K★). Since Sept 2026 the MCP server and CLI ship **inside the main Playwright package**. CLI is faster for coding agents | `npx playwright` · github.com/microsoft/playwright-mcp |
| ★ **Chrome DevTools MCP** (53K★) | Google's official server: 29 tools for performance traces, network, console, emulation. Can now attach to your running Chrome (with approval) | github.com/ChromeDevTools/chrome-devtools-mcp |
| ★ **Browser Harness** (browser-use) | ~600 lines connecting an LLM straight to your real browser over one CDP websocket; the agent writes missing helpers as it goes (self-healing). 18K★ | github.com/browser-use/browser-harness |
| ★ **Agent-Reach** | One CLI + SKILL.md that lets any agent read and search Twitter/X, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu with no API fees; multi-backend fallback, cookies stay local. 86K★ | github.com/Panniantong/Agent-Reach |
| **agent-browser** (Vercel) | Rust CLI using snapshot refs instead of DOM selectors — cheap on tokens | `npm i -g agent-browser` · `npx skills add vercel-labs/agent-browser` |
| **Stagehand v3** (Browserbase) | 44% faster, built on CDP (no Playwright), act/extract/observe/agent, now in Python/Go/Java/Rust | stagehand.dev |
| **Kernel · Steel · Browserbase** | Hosted browsers for agents (Steel is open source) | kernel.sh · steel.dev · browserbase.com |

### Dev workflow plugins

| Tool | What it does | Install |
|---|---|---|
| ★ **Context7 MCP** (63K★) | Up-to-date library docs so the agent stops hallucinating APIs — the single highest-impact MCP for coding | `claude mcp add context7 -- npx -y @upstash/context7-mcp` |
| ★ **Serena MCP** | IDE-level symbol/reference understanding for agents (semantic code navigation) | github.com/oraios/serena |
| **Everything Claude Code (ECC)** | 64 agents, 261 skills, 84 commands, 103 rules, hooks and MCPs in one harness; v2.2 also sets up Codex and Kimi Code. 269K★ | `/plugin marketplace add affaan-m/everything-claude-code` |
| **Get Shit Done (GSD)** | Spec-driven meta-prompting that fights context rot; works in Claude Code + 13 other runtimes. 64K★ | github.com/gsd-build/get-shit-done |
| **Ralph Wiggum loop** | Official Anthropic plugin (and snarktank/ralph) that keeps an agent looping until the PRD is done | Claude Code official plugins |
| **Official Claude Code plugins** | typescript-lsp, security-guidance, context7, playwright, frontend-design, code-review, feature-dev and 50+ more | `/plugin` → anthropics/claude-code marketplace |

### Memory for agents

| Tool | What it does | Link |
|---|---|---|
| ★ **claude-mem** | Captures each Claude Code session and feeds relevant context into later ones; local. 95K★ | [github.com/thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) |
| **Hindsight** (Vectorize) | Memory split into four networks (facts, experiences, entities, beliefs); 91% on its memory benchmark; plugin for Paperclip | [github.com/vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) |
| **OpenMemory MCP** (Mem0) | Local memory layer shared across Cursor, VS Code, Claude and any MCP client | [mem0.ai/openmemory](https://mem0.ai/openmemory) |
| Claude Code auto-memory | Built in since 2.1 — preferences and patterns persist automatically | — |

### Orchestration & agent runtimes

| Tool | What it does | Link |
|---|---|---|
| **Paperclip** | Node server + React UI that runs a "company" of AI agents: bring your own agents, assign goals, track work. 93K★ | [github.com/paperclipai/paperclip](https://github.com/paperclipai/paperclip) |
| **google/ax + Agent Executor** | Google's open agent orchestration runtime (Go, Kubernetes-style): durable, resumable agents, sandboxing, trajectory branching | [github.com/google/ax](https://github.com/google/ax) |
| **Sakana Fugu Ultra v2** (Sept 11) | Not a tool but an API: one endpoint that orchestrates a pool of frontier models. $5/$30, 1M ctx, DeepSWE 74.3 | [openrouter.ai/sakana/fugu-ultra-v2](https://openrouter.ai/sakana/fugu-ultra-v2) |
| **AgentCrafters.ai** | No-code: build agents in plain English connected to 36 everyday tools (email, reports, reminders). Early-stage (India, 2026) | [agentcrafters.ai](https://agentcrafters.ai) |

### Research & search MCPs

| Tool | Best for |
|---|---|
| **Exa** | Neural/semantic search, papers and companies |
| **Tavily** | Search + extraction in one call, agent docs MCP |
| **Firecrawl MCP** | Scrape/crawl/search with 13 tools, remote-hosted |
| **Brave Search · Perplexity Sonar · Parallel** | Alternatives with MCPs |

---

## Skill directories (where to find skills)

> A **skill** is a portable folder with a `SKILL.md` — the same one works in Claude Code, claude.ai,
> Codex, OpenCode, Cursor and Antigravity. A **plugin** is a Claude Code bundle (skills + commands +
> hooks + MCP). ⚠️ Read every `SKILL.md` and script before installing — it's instructions your agent will follow.

| Directory | Type | Best for | Link |
|---|---|---|---|
| ★ **anthropics/skills** | Official repo | First-party skills (docx, pdf, pptx, xlsx, skill-creator, webapp-testing) and the reference format | [github.com/anthropics/skills](https://github.com/anthropics/skills) |
| ★ **Claude plugin directory** | Official directory (Sept 2026) | Reviewed third-party plugins with MCP 2.0 / MCP Apps support; submission portal for your own | Claude Code `/plugin` |
| ★ **skills.sh** | Leaderboard | What's popular right now, by install count | [skills.sh](https://skills.sh) |
| **localskills.sh** | Registry (npm-style) | Versioned, private and team skills; installs one skill into Claude Code, Cursor and Windsurf at once | [localskills.sh](https://localskills.sh) |
| **SkillsMP** | Aggregator | Searches every skill on GitHub — huge, unreviewed | [skillsmp.com](https://skillsmp.com) |
| **claudemarketplaces.com** | Directory | Plugins, skills and MCP servers in one place | [claudemarketplaces.com](https://claudemarketplaces.com) |
| **aitmpl.com** | Directory | Plugin collections and marketplaces | [aitmpl.com/plugins](https://aitmpl.com/plugins) |
| **awesomeclaude.ai** | Curated list | Human-picked skills by category | [awesomeclaude.ai/awesome-claude-skills](https://awesomeclaude.ai/awesome-claude-skills) |
| **alirezarezvani/claude-skills** | Collection | 345 skills as installable plugins by domain (engineering, marketing, devops) | [github.com/alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) |
| **mhattingpete/claude-skills-marketplace** | Plugin marketplace | Git automation, testing, code review | [github.com/mhattingpete/claude-skills-marketplace](https://github.com/mhattingpete/claude-skills-marketplace) |
| **ClawHub** | Agent registry | OpenClaw skills — review each, third-party skills have shipped malware | — |
| **cursor.directory** | Rules directory | Cursor rules | [cursor.directory](https://cursor.directory) |
| **Awesome lists** | Link collections | ComposioHQ, travisvn, BehiSecc (see Skill Repositories below) | — |

## Install a skill or plugin in 60 seconds

```bash
# Claude Code — a skill is just a folder
git clone https://github.com/anthropics/skills /tmp/skills
cp -r /tmp/skills/skills/pdf ~/.claude/skills/        # personal, all projects
# or copy into .claude/skills/ in a repo and commit it for your team

# Claude Code — plugins from a marketplace
/plugin marketplace add <owner>/<repo>                # any GitHub repo with a marketplace.json
/plugin install <plugin-name>

# One skill into several agents at once
npm install -g @localskills/cli
localskills install <owner>/<skill> --target claude cursor windsurf

# MCP server (tools/data) into Claude Code
claude mcp add github -- npx -y @modelcontextprotocol/server-github
```

- **claude.ai:** Settings → Capabilities → Skills → upload the skill folder as a zip.
- **Codex / OpenCode / Antigravity:** point them at the same skills folder (each has a skills path in its config).
- **Write your own:** ask Claude to use the `skill-creator` skill, or copy an existing `SKILL.md` and edit the name, one-line description and steps. Keep the description specific — it decides when the skill loads.

---

## How skills work

A **skill** is a folder with a `SKILL.md` file (name + one-line description + instructions) and optional
scripts or reference files. At session start the agent sees only each skill's name and description; the
full instructions load only when a task needs them, so you can install hundreds without filling the
context. The format is an open standard (Anthropic, Dec 2025) supported by Claude Code, claude.ai, the
Claude API, Codex, OpenCode, Cursor, Antigravity, Qoder and others.

### Skills vs MCP vs plugins

| | Skill | MCP server | Plugin (Claude Code) |
|---|---|---|---|
| **Is** | Instructions + optional scripts | A service exposing tools/data | A bundle: skills + commands + hooks + MCP servers |
| **Adds** | *How* to do something well | *Access* to a system (GitHub, DB, browser) | Both, installed together |
| **Loads** | Only when relevant | Tool list sits in context while connected | Whatever it bundles |
| **Example** | "Write a .docx in our house style" | GitHub MCP to open PRs | A team plugin with review skills + Sentry MCP |

### Use skills on each platform

| Platform | How |
|---|---|
| **Claude Code** | Put skill folders in `~/.claude/skills/` (all projects) or `.claude/skills/` (this repo); or install plugins with `/plugin marketplace add <repo>` → `/plugin install <name>` |
| **claude.ai / Claude apps** | Settings → Capabilities → Skills → upload a zipped skill folder |
| **Claude API** | Skills via the Agent SDK / API skills support (see Anthropic's Agent Skills docs) |
| **Codex · OpenCode · Cursor · Antigravity · Qoder** | Each reads a skills directory — point it at the same folder |
| **Several agents at once** | `localskills install <owner>/<skill> --target claude cursor windsurf` |

### Write your own skill

```markdown
---
name: api-conventions
description: Use when writing or reviewing HTTP handlers in this repo — enforces our error format and pagination rules.
---

# API conventions

1. Errors return `{ "error": { "code", "message" } }` with the right HTTP status.
2. List endpoints take `?cursor=` and return `next_cursor`.
3. Run `scripts/check_routes.py` before finishing.
```

Save as `.claude/skills/api-conventions/SKILL.md` (plus any `scripts/`). The **description decides when
it loads** — make it specific about *when* to use the skill. Or ask Claude to use the official
`skill-creator` skill to scaffold one for you.

---

## Notable builders' setups

| Builder | Repo | ⭐ (live) | What |
|---|---|---|---|
| **Garry Tan** (YC) | [garrytan/gstack](https://github.com/garrytan/gstack) | 134K | His Claude Code setup: 23 opinionated tools acting as CEO / designer / eng manager / release manager / QA |
| **Garry Tan** | [garrytan/gbrain](https://github.com/garrytan/gbrain) | 30K | Opinionated brain for OpenClaw / Hermes agents |
| **Andrej Karpathy** (principles, packaged by others) | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 216K | Coding-discipline plugin: think before coding, simplicity, surgical changes |
| **Ras Mic** | [michaelshimeles/ralphy](https://github.com/michaelshimeles/ralphy) | 3K | Loop that runs Claude Code / Codex / OpenCode until the PRD is done (last commit Feb 2026) |

```bash
git clone https://github.com/garrytan/gstack
/plugin marketplace add multica-ai/andrej-karpathy-skills
```

---

## Security & red-team skill bundles

> [!CAUTION]
> Dual-use. **Authorized testing, CTFs and bug-bounty programs only** — never run against systems you don't have written permission to test.

| Repo | ⭐ (live) | What (per its README) |
|---|---|---|
| [awarexone/Agentic-Bug-Hunter](https://github.com/awarexone/Agentic-Bug-Hunter) (ex shuvonsec/claude-bug-bounty) | 5.2K | Recon → hunt → validate → report for HackerOne/Bugcrowd/Intigriti; runs on free providers |
| [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | 4.7K | Bug hunting + external red-team skills and report patterns |
| [H-mmer/pentest-agents](https://github.com/H-mmer/pentest-agents) | 1K | Multi-harness bug-bounty agents (last commit Jun 2026) |
| [transilienceai/communitytools](https://github.com/transilienceai/communitytools) | 0.5K | Pentest lifecycle, OWASP Top 10 + LLM Top 10 |
| [Eyadkelleh/awesome-skills-security](https://github.com/Eyadkelleh/awesome-skills-security) | 0.4K | SecLists + PayloadsAllTheThings as agent skills |

---

## Dev & engineering skill packs

| Repo | ⭐ (live) | What |
|---|---|---|
| [obra/superpowers](https://github.com/obra/superpowers) | 292K | Full workflow: brainstorm → plan → subagent execution → TDD → review. Works on Claude Code, Codex, Cursor, Gemini, Copilot, OpenCode, Kimi, Pi |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) (Everything Claude Code) | 269K | 64 agents, 261 skills, hooks, rules, MCPs |
| [anthropics/skills](https://github.com/anthropics/skills) | 179K | Official: docx/pdf/pptx/xlsx, frontend-design, webapp-testing, skill-creator |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 76K | Curated skills + app-integration skills |
| [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) (ex antigravity-awesome-skills) | 47K | Huge installable bundle across dev, security, infra, docs |
| [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | 64K | Spec-driven workflow against context rot |
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | 15K | Curated list |
| [BehiSecc/awesome-claude-skills](https://github.com/BehiSecc/awesome-claude-skills) | 10K | Curated list incl. security |

**Recommended path:** anthropics/skills (official) → superpowers + the Karpathy plugin (discipline) → a design skill (Impeccable or Taste Skill) → browse the [directories](#skill-directories-where-to-find-skills) for anything else. Official docs: [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills) · [Anthropic Engineering deep dive](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills).
