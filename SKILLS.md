# Claude Skills Ecosystem — Reference (June 2026)

> Skills extend Claude agents with reusable, callable capabilities. Each skill is a discrete unit of functionality — invoked by name, loaded lazily into context.
> ✅ **Verified June 27, 2026** — repo star counts drift; confirm on GitHub.

---

## Overview

The Claude skills ecosystem currently indexes **1,400+ skills** across categories spanning API integrations, development workflows, security research, data pipelines, and productivity automation.

Skills are:
- **Lazy-loaded** — only the description lives in context until invoked
- **Composable** — chain skills together in agent workflows
- **Provider-agnostic** — work across Claude models (Haiku, Sonnet, Opus)
- **Reusable** — share and reuse across sessions and teams

**Standard:** Anthropic introduced the Skills format Oct 2025, released it as an **open standard** Dec 2025. Now supported by Claude Code, Claude.ai, the Claude API, OpenAI Codex, Cursor, Gemini CLI / Antigravity, and Windsurf.

---

## What is MCP? (60-second primer)

**MCP (Model Context Protocol)** is the "USB-C of AI agents" — one open standard (Anthropic, Nov 2024; now Linux Foundation) that lets any AI connect to any external tool or data source.

```
AI agent (Claude Code / Cursor / Codex / …)
   │  MCP protocol (JSON-RPC over stdio / SSE / HTTP)
   ▼
MCP server (GitHub / Supabase / Playwright / Notion / …)
   ▼
the real service / DB / browser
```

Each **MCP server** exposes **Tools** (actions), **Resources** (readable data), **Prompts** (templates); the agent decides when to call them. Full MCP reference — 72K+ servers, registries, remote MCP, build-your-own — in [AGENTS.md](./AGENTS.md) Part 5A.

### Skills vs MCP — when to use which

| | **Skill** | **MCP** |
|---|---|---|
| Is a | folder of instructions (`SKILL.md`) + scripts | running server exposing tools |
| Adds | *know-how* — how to do a task well | *capabilities* — access to an external system |
| Loads | lazily into context when relevant | connects at startup via config |
| Example | "write a brand-compliant PDF" | "query my Postgres / control a browser" |
| Use together | a Skill can tell the agent *how* to use an MCP tool | — |

> Rule of thumb: **Skill = teach the model a workflow. MCP = give the model a new hand.** They compose.

---

## How to Use Skills (by platform)

Skills live in a `skills/` folder; each skill is a subfolder with a `SKILL.md` (trigger conditions + instructions) and optional helper files.

| Platform | How to add a skill |
|---|---|
| **Claude Code** | Drop into `~/.claude/skills/` (global, all projects) or `.claude/skills/` (project-only). Or register a marketplace: `/plugin marketplace add anthropics/skills` then install. Restart so it's discovered |
| **Claude.ai** | Settings → Capabilities → enable Skills; upload/enable in Projects with tool-use on |
| **Claude API** | Expose each skill via the `tools` parameter / Agent SDK `Skill` tool |
| **Cursor / Windsurf** | Place in the project `.claude/skills/` (both read the open standard); reload window |
| **OpenAI Codex / Gemini CLI / Antigravity** | Supported via the open Skills standard — point them at the skills dir per their docs |
| **Any MCP agent** | Skills can be surfaced as MCP tools via `mcp-builder` |

```bash
# Fastest start — clone a skill library straight into Claude Code:
git clone https://github.com/Yash-Awasthi/Claude-skill
cp -r Claude-skill/skills/* ~/.claude/skills/     # all 1,374 skills
# or just one:
cp -r Claude-skill/skills/deep-research ~/.claude/skills/
# restart Claude Code → skills trigger automatically on relevant tasks
```

> Skills load **progressively**: at session start the agent sees only each skill's name + description (~100 tokens each); the full `SKILL.md` (<5K tokens) loads only when relevant. That's how one agent hosts hundreds of skills without context bloat.

---

## Skill Categories

### API & Service Integrations (~800+ skills)

The largest category. One skill per external service — covers auth, CRUD, webhooks, and pagination for each provider.

| Category | Example Skills | Count |
|---|---|---|
| CRM / Sales | salesforce, hubspot, attio, pipedrive, folk, capsule-crm | 40+ |
| Marketing | mailerlite, mailersend, activecampaign, klaviyo, brevo | 30+ |
| Productivity | notion-read/write, airtable, baserow, clickup, asana | 25+ |
| Communication | slackbot, discordbot, teams, telegram, whatsapp | 20+ |
| File / Storage | googledrive, onedrive, dropbox, box, s3 | 15+ |
| Finance | stripe, braintree, quickbooks, xero, plaid | 25+ |
| AI Providers | openai, gemini, groqcloud, mistral-ai, replicate, elevenlabs | 30+ |
| Data / Analytics | bigquery, snowflake, mongodb, postgres, redis | 20+ |
| Developer Tools | github, gitlab, jira, linear, sentry, datadog | 30+ |
| E-commerce | shopify, woocommerce, amazon, ebay, etsy | 20+ |
| HR / Recruiting | workday, greenhouse, lever, ashby, breezy-hr | 15+ |

### Development Workflows (~100 skills)

Purpose-built for software engineering tasks. Used heavily by CLI agents and agentic IDEs.

| Skill | Purpose |
|---|---|
| `code-review-and-quality` | Automated PR review, style enforcement, complexity analysis |
| `test-driven-development` | Generate test suites, assert coverage, red-green-refactor cycles |
| `debugging-and-error-recovery` | Root cause analysis, stack trace interpretation, fix suggestions |
| `git-workflow-and-versioning` | Branch strategy, commit message standards, merge conflict resolution |
| `ci-cd-and-automation` | Pipeline generation for GitHub Actions, GitLab CI, CircleCI |
| `performance-optimization` | Profiling, bottleneck identification, caching strategies |
| `security-and-hardening` | SAST, dependency audit, secrets scanning, OWASP checklist |
| `documentation-and-adrs` | ADR templates, API docs, README generation |
| `spec-driven-development` | Requirements → spec → code workflow (similar to Kiro) |
| `context-engineering` | Optimize prompts, manage context windows, reduce token waste |
| `incremental-implementation` | Break large features into atomic, testable steps |
| `source-driven-development` | Build from source references, maintain provenance |
| `subagent-driven-development` | Spawn and coordinate multiple sub-agents |
| `autonomous-agent-patterns` | ReAct, Plan-and-Execute, reflexion, tool-use patterns |
| `planning-and-task-breakdown` | Decompose tasks, estimate complexity, create work plans |
| `api-and-interface-design` | REST/GraphQL/gRPC API design, OpenAPI spec generation |
| `code-simplification` | Refactor for clarity, reduce duplication, improve readability |
| `deprecation-and-migration` | Safe migration paths, breaking change detection |
| `doubt-driven-development` | Uncertainty-first: flag assumptions before writing code |

### Security & Red Team (~60 skills)

Research and audit skills. Used for authorized penetration testing and vulnerability research.

| Skill | Scope |
|---|---|
| `hunt-xss` | Cross-site scripting detection and payload generation |
| `hunt-sqli` | SQL injection pattern recognition and exploitation |
| `hunt-idor` | Insecure direct object reference mapping |
| `hunt-ssrf` | Server-side request forgery chain discovery |
| `hunt-rce` | Remote code execution vector identification |
| `hunt-oauth` | OAuth flow misconfigurations and token leakage |
| `hunt-graphql` | GraphQL introspection abuse, batching attacks |
| `hunt-llm-ai` | LLM-specific: prompt injection, jailbreak vectors, model DoS |
| `hunt-subdomain` | Subdomain enumeration and takeover detection |
| `hunt-cloud-misconfig` | AWS/GCP/Azure misconfiguration detection |
| `osint-methodology` | OSINT collection framework and source chaining |
| `redteam-mindset` | Attacker perspective, threat modeling, kill chain mapping |
| `bug-bounty` | Scope analysis, severity rating, disclosure templates |
| `web3-audit` | Smart contract audit, reentrancy, access control |
| `apk-redteam-pipeline` | Android APK static/dynamic analysis pipeline |
| `m365-entra-attack` | Microsoft 365 / Entra ID attack surface mapping |

### Data & Document Processing (~50 skills)

| Skill | Purpose |
|---|---|
| `pdf` | Extract, parse, and manipulate PDF content |
| `excel-automation` | Read/write Excel files, formula generation, pivot tables |
| `docx` | Word document creation and manipulation |
| `pptx` | PowerPoint slide generation |
| `xlsx` | XLSX parsing and generation |
| `deep-research` | Multi-source research synthesis with citations |
| `academic-paper` | Research paper structure, citations, abstract writing |
| `academic-pipeline` | Full research pipeline: literature review → methodology → write-up |
| `image-enhancer` | Image upscaling, restoration, and enhancement |
| `video-downloader` | Extract and process video content |
| `audio-transcribe` | Speech-to-text with speaker diarization |

### Productivity & Content (~80 skills)

| Skill | Purpose |
|---|---|
| `notion-read` / `notion-write` / `notion-update` | Full Notion database CRUD |
| `content-research-writer` | Research + structured content generation |
| `report-writing` | Formal report structure, executive summaries |
| `tailored-resume-generator` | Resume tailoring to job descriptions |
| `internal-comms` | Internal memo, announcement, and update templates |
| `meeting-insights-analyzer` | Extract action items and decisions from meeting notes |
| `lead-research-assistant` | Prospect research, enrichment, and scoring |
| `email-research-workflow` | Email research pipeline with verification |
| `invoice-organizer` | Invoice parsing, categorization, and export |
| `file-organizer` | Directory structure analysis and reorganization |
| `changelog-generator` | Generate changelogs from git history |
| `domain-name-brainstormer` | Brand name generation with availability check |
| `idea-refine` | Structured ideation and concept refinement |
| `interview-me` | Mock interview preparation and feedback |

### Infrastructure & Cloud (~40 skills)

| Skill | Purpose |
|---|---|
| `cloudflare-automation` | DNS, Workers, R2, KV, Pages management |
| `digital-ocean-automation` | Droplets, Spaces, App Platform |
| `neon-automation` | Neon serverless Postgres branching and queries |
| `turso-automation` | Turso SQLite edge database |
| `docker-hub-automation` | Container image management |
| `cloud-iam-deep` | IAM policy analysis and least-privilege enforcement |
| `mcp-builder` | Build MCP servers — tools, resources, prompts |
| `connect-apps` | App connection and OAuth flow setup |

---

## Notable Skills Deep Dive

### `autonomous-agent-patterns`

Implements established agentic reasoning patterns:

- **ReAct** (Reason + Act) — interleave reasoning traces with tool calls
- **Plan-and-Execute** — generate full plan upfront, execute steps sequentially
- **Reflexion** — self-evaluate outputs, iterate on failures
- **LATS** (Language Agent Tree Search) — tree-search over action sequences
- **Multi-agent coordination** — spawning, messaging, result aggregation

### `context-engineering`

Manages the "context budget" problem for long agent runs:

- Token counting and budget estimation
- Summarization strategies (rolling, hierarchical)
- Relevant chunk retrieval vs full-context loading
- System prompt compression patterns
- Lazy skill loading (< 1,000 token descriptions until invoked — same pattern Pi agent uses)

### `mcp-builder`

End-to-end MCP server scaffolding:

- Tool definition with JSON Schema parameters
- Resource URI templates
- Prompt templates
- Server packaging for Claude Desktop / agent frameworks
- Testing harness generation

### `deep-research`

Multi-step research pipeline:

1. Query decomposition into sub-questions
2. Parallel web search across sources
3. Source credibility scoring
4. Cross-reference and contradiction detection
5. Synthesis with inline citations
6. Executive summary generation

---

## Skill Access

Skills are available through:

| Method | How |
|---|---|
| **Claude.ai Projects** | Skills surface in Projects with tool-use enabled |
| **Claude API** | Via `tools` parameter — each skill is a callable tool |
| **Hermes Agent** | Native skill integration — auto-creates skills from experience |
| **Agent SDK** | `Skill` tool in Claude Agent SDK for orchestration |
| **MCP** | Skills exposed as MCP tools for any MCP-compatible agent |

---

## Creating Custom Skills

The `skill-creator` meta-skill generates new skills from natural language descriptions:

```python
# Invoke skill-creator to scaffold a new skill
result = await agent.invoke_skill("skill-creator", {
    "name": "my-service-automation",
    "description": "Automate interactions with MyService API",
    "api_docs_url": "https://docs.myservice.com/api",
    "auth_type": "bearer_token"
})
# Returns: skill manifest, tool definitions, example invocations
```

Custom skill structure:
```yaml
name: my-service-automation
description: One-line description (lives in context always)
version: 1.0.0
tools:
  - name: create_record
    description: Create a new record in MyService
    parameters:
      type: object
      properties:
        name: {type: string}
        data: {type: object}
      required: [name]
instructions: |
  Full instructions here — only loaded when skill is invoked.
  Can be 10,000+ tokens without impacting idle context usage.
```

---

## Notable Builders' Setups, Skills & Workflows

> Real, installable artifacts from prominent builders — Claude Code setups, agent skills, and autonomous workflows.

| Builder | GitHub | Claude skills / workflows | Other notable repos |
|---|---|---|---|
| **Garry Tan** (YC CEO) | [garrytan](https://github.com/garrytan) | **[gstack](https://github.com/garrytan/gstack)** (~117K★) — his exact Claude Code setup: 23 opinionated tools acting as CEO/Designer/Eng-Manager/Release-Manager/Doc-Engineer/QA · **[gbrain](https://github.com/garrytan/gbrain)** (~24K★) opinionated OpenClaw/Hermes brain · [alphaclaw](https://github.com/garrytan/alphaclaw) OpenClaw harness | gbrain-evals, openclaw |
| **Ras Mic** (Michael Shimeles) | [michaelshimeles](https://github.com/michaelshimeles) | **[ralphy](https://github.com/michaelshimeles/ralphy)** (~2.9K★) — autonomous bash loop running Claude Code + Codex + OpenCode + Cursor + Qwen + Droid until your PRD is done · **[skills](https://github.com/michaelshimeles/skills)** (~220★) his personal skills | [nextjs-starter-kit](https://github.com/michaelshimeles/nextjs-starter-kit) (~3K★), react-starter-kit, hono-starter-kit, youpac-ai |
| **Matt Palmer** (ex-Replit DevRel) | [mattppal](https://github.com/mattppal) | **[formatting-notion-pages](https://github.com/mattppal/formatting-notion-pages)** — agent skill for rich Notion pages · **[shipping-szn](https://github.com/mattppal/shipping-szn)** — auto-changelog (Slack→Mintlify) via Claude Agent SDK · [claude-codes](https://github.com/mattppal/claude-codes), hermes-agent-template | security checklist for vibe-coded apps, fasthtml-guestbook |
| **Andrej Karpathy** | [karpathy](https://github.com/karpathy) | No first-party skill, but his coding principles are packaged as a Claude Code plugin: **[andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** (4 rules: Think-Before-Coding, Simplicity-First, Surgical-Changes, Goal-Driven) — `/plugin marketplace add` or append its `CLAUDE.md` | [nanoGPT](https://github.com/karpathy/nanoGPT), nanochat, llm.c, minGPT, [llm-council](https://github.com/karpathy/llm-council), nn-zero-to-hero |

```bash
# Garry Tan's full Claude Code setup
git clone https://github.com/garrytan/gstack
# Ras Mic's autonomous agent loop
git clone https://github.com/michaelshimeles/ralphy
# Karpathy coding-discipline plugin (in Claude Code)
/plugin marketplace add multica-ai/andrej-karpathy-skills
```

---

## Security & Red-Team Skill Bundles

> Dual-use — **authorized testing, CTF, and bug-bounty only.** Never run on systems you don't have written permission to test.

| Repo | Size | What | Link |
|---|---|---|---|
| **Claude-BugHunter** | 71 skills, 15 cmds, 681 report patterns, 24 vuln classes | Bug hunting + external red-team; scope-in-code, 7-question gate. Sister: **Claude-OSINT** | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) |
| **pentest-agents** | 50 agents, 11 skills, 19 CLI tools, 2 MCP | Multi-harness autonomous bug-bounty (Claude Code/Codex/Gemini/Cursor/Windsurf/Copilot/OpenClaw); 16 BB platforms | [H-mmer/pentest-agents](https://github.com/H-mmer/pentest-agents) |
| **Transilience communitytools** | 26 skills | Full pentest lifecycle, OWASP Top 10 + LLM Top 10, CVSS/CWE/MITRE reports, Kali container setup | [transilienceai/communitytools](https://github.com/transilienceai/communitytools) |
| **claude-bug-bounty** | 20 vuln classes | Recon → hunt → validate → report (HackerOne/Bugcrowd/Intigriti/Immunefi). **Standalone CLI on free providers — no paid sub** | [shuvonsec/claude-bug-bounty](https://github.com/shuvonsec/claude-bug-bounty) |
| **claude-code-pentest** | 6 skills, 43 scripts | Pure-Python, zero deps; recon → exploit chains → MITRE attack trees → report | [Orizon-eu/claude-code-pentest](https://github.com/Orizon-eu/claude-code-pentest) |
| **cybersecurity-claude-skills** | 4 skills | `pentest-recon`, `web-hacking`, `secure-code-review`, `ctf-solver` | [mahmutka/cybersecurity-claude-skills](https://github.com/mahmutka/cybersecurity-claude-skills) |
| **awesome-skills-security** | wordlists/payloads | SecLists + PayloadsAllTheThings packaged as Agent Skills (60+ agents) | [Eyadkelleh/awesome-skills-security](https://github.com/Eyadkelleh/awesome-skills-security) |

---

## Dev / Engineering Skill Packs

| Repo | Size | What | Link |
|---|---|---|---|
| **obra/superpowers** | ~41K★ | Full SDLC framework: brainstorm → worktree → plan → subagent execution → TDD (RED-GREEN-REFACTOR) → review→merge. Works on Claude Code/Codex/Cursor/Gemini/Copilot/OpenCode/Kimi/Pi. `/plugin install superpowers@claude-plugins-official` | [obra/superpowers](https://github.com/obra/superpowers) |
| **antigravity-awesome-skills** | 1,689+ skills | Installer CLI + bundles across dev/test/security/infra/product/docs/QA/MCP | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) |
| **karanb192/awesome-claude-skills** | 50+ verified | TDD, debugging, git workflows, document processing | [karanb192/awesome-claude-skills](https://github.com/karanb192/awesome-claude-skills) |
| **great_cto** | 7 subagents | tech-lead, senior-dev, qa, security-officer, devops, l3-support, auditor — full SDLC pipeline | search "great_cto claude plugin" |
| **Official dev skills** | — | `web-artifacts-builder` (React/Tailwind/shadcn), `frontend-design`, `webapp-testing` (Playwright) | [anthropics/skills](https://github.com/anthropics/skills) |

---

## Skill Repositories

| Repo / Resource | What | Notes |
|---|---|---|
| **[Yash-Awasthi/Claude-skill](https://github.com/Yash-Awasthi/Claude-skill)** | **1,374 ready skills** — clone & drop into `~/.claude/skills/` | Automation (800+ integrations), Security (pentest/recon/OSINT), Engineering, Research, Product, AI/Agents |
| [anthropics/skills](https://github.com/anthropics/skills) | Official Agent Skills | docx/pdf/pptx/xlsx, `webapp-testing`, `skill-creator`, `brand-guidelines` |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 50+ curated skills + how-skills-work explainer | Great starting index |
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | Curated list | Highlights community libraries |
| [obra/superpowers](https://github.com/obra/superpowers) | 20+ battle-tested Claude Code skills | TDD, debugging, `/brainstorm`, `/write-plan`, `/execute-plan` + skills-search |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Karpathy coding-discipline plugin (tens of thousands of installs) | Curbs silent wrong assumptions, over-engineering, orthogonal edits |
| [BehiSecc](https://github.com/BehiSecc/awesome-claude-skills) · [GetBindu](https://github.com/GetBindu/awesome-claude-code-and-skills) | More curated collections | Security, debugging, marketing, bundles |
| **[Official Claude docs — Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills)** | Canonical reference | Spec, authoring, `SKILL.md` format |
| [Anthropic Engineering — "Equipping agents with skills"](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) | Official deep dive | Design + progressive disclosure |
| [Andrej Karpathy](https://github.com/karpathy) | Origin of the coding-discipline rules | Repos: nanoGPT, nanochat, llm.c, llm-council |

> **Recommended path:** start with **[Yash-Awasthi/Claude-skill](https://github.com/Yash-Awasthi/Claude-skill)** (1,374 skills, one clone) for breadth → **anthropics/skills** for production-grade official skills → **obra/superpowers** + the Karpathy skill for coding discipline.

---

## Skill Count by Category (June 2026)

| Category | Skills |
|---|---|
| API & Service Integrations | 800+ |
| Development Workflows | 100+ |
| Security & Red Team | 60+ |
| Productivity & Content | 80+ |
| Data & Document Processing | 50+ |
| Infrastructure & Cloud | 40+ |
| Meta / Orchestration | 20+ |
| **Total** | **1,400+** |
