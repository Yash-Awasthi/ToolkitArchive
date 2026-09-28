# 🛠️ Using AI Well — Chat App Features & Token Efficiency (29 September 2026)

> How to get more out of the apps you already have, and how to make free limits and paid tokens
> last. Plan availability changes often — each feature says which plans had it when checked.

**Contents:** [Claude](#claude-claudeai--desktop--mobile) · [ChatGPT](#chatgpt) · [Gemini](#gemini--notebooklm) ·
[Which app for what](#which-app-for-what) · [Skills, plugins, MCP, tools](#skills-plugins-mcp-and-tools--how-to-use-them) ·
[Token efficiency](#token-efficiency-make-free-limits-last)

---

## Claude (claude.ai · desktop · mobile)

| Feature | What it does | How to use it | Plan |
|---|---|---|---|
| **Projects** | Shared instructions + files across chats. When files get near the context limit it switches to retrieval, so ~10× more material fits | Put your syllabus / codebase notes / style guide in a Project once; every chat inside starts with it | Free (limited) and paid |
| **Artifacts** | Code, docs, diagrams and small apps render live next to the chat. Since June you can highlight part of an artifact and ask for an inline edit | "Make this an artifact" — then share the link or keep iterating | All plans |
| **Memory** | Remembers preferences and context across chats | Tell it once ("I'm a CS student, explain with Python examples") | Paid (check settings) |
| **Cowork → merged into chat** | Claude does multi-step work on your files and apps with a GUI; announced Sept 16 to merge into normal chat, Pro/Max first, then Team and Free | Ask for the whole task ("organise these receipts into a spreadsheet") instead of one step at a time | Rolling out |
| **Claude in Chrome** | Connector that lets Claude navigate, click and fill forms in your browser | Enable in connectors; approve each sensitive action | Paid |
| **Connectors / MCP** | Gmail, Drive, Calendar, GitHub, Notion and any MCP server | Settings → Connectors | Varies |
| **Skills** | Reusable instruction packs (e.g. make a .docx, a slide deck, follow your house style) loaded only when needed | Settings → Capabilities → Skills; upload a skill folder | Check your plan |
| **Research** | Multi-step web research with citations | Toggle Research before asking | Paid |
| **Desktop app** | Mac / Windows / Linux (beta), all plans | claude.ai/download | Free |

Free plan: Sonnet 5 with daily caps + Haiku. Opus 5.5 / Fable 5.1 need Pro ($17/mo annual) or Max.

## ChatGPT

| Feature | What it does | How to use it | Plan |
|---|---|---|---|
| **Scheduled Tasks** | Runs a prompt at a set time or on a trigger — even when you're not in the app. Triggers can include Slack messages, Gmail arrivals and GitHub events | "Every weekday at 8am, summarise new arXiv papers on X" / "Remind me Friday to submit the lab" | Paid tiers; check your plan |
| **ChatGPT Work** | Agent mode's replacement (old Agent mode ended early Aug): breaks a goal into steps, works for hours, asks you to approve important actions | Give an outcome, not steps ("book-compare three laptops under $800 and make a table") | All plans, desktop |
| **Projects** | Shared files, instructions and Project Memory across chats | One Project per course / codebase | All plans |
| **Memory** | Rebuilt memory system (Aug 2026) | Manage in Settings → Personalization | All plans |
| **Canvas** | Side-by-side document/code editing | "Open this in canvas" | All plans |
| **Deep research** | Long cited reports | Pick Deep research in the composer | Limited on free |
| **Codex** | Coding agent in the app, CLI and IDE | chatgpt.com/codex · `npm i -g @openai/codex` | Free (Luna) and paid |
| **Voice / image gen** | Real-time voice, image generation and editing | Voice button · "generate an image of…" | All plans (limits) |

Free/Go plan gets GPT-6 Luna on desktop; Plus ($20) and up get GPT-6 Sol; Pro/Business get GPT-6 Astra.
US college students: 4 months of Plus free until Oct 31 (card required).

## Gemini + NotebookLM

| Feature | What it does | How to use it | Plan |
|---|---|---|---|
| **Scheduled actions** | Recurring or one-off prompts that run on their own ("daily summary of my calendar, to-dos and unread email", "weekend events every Friday") | Ask Gemini to "do this every…" | AI Pro / Ultra |
| **Gems** | Custom Gemini with fixed instructions and attached knowledge — including NotebookLM notebooks that auto-sync | Build a "Tutor for Course X" Gem with your notes attached | Free and paid |
| **Deep Research** | Cited reports; can use your own uploaded files; turn reports into quizzes, visuals and pages in Canvas | Upload lecture PDFs → Deep Research → "make a quiz" | Free tier available |
| **Canvas** | Edit docs/code, build small apps, make quizzes | "Open in Canvas" | Free |
| **NotebookLM** | Answers only from your sources, with citations; audio overviews (podcast of your notes), mind maps, flashcards, quizzes | Upload readings; ask questions; generate an audio overview for revision | Free |
| **Workspace** | Gemini inside Gmail, Docs, Sheets, Drive | Side panel in each app | Plan-dependent |

Free plan runs Gemini 3.8 Flash. Gemini 4 Pro is expected in October.

## Which app for what

| Job | Best pick | Why |
|---|---|---|
| Studying from your own notes | **NotebookLM** | Cites only your sources; audio overviews and quizzes |
| Hard reasoning, maths, science | **ChatGPT** (GPT-6 Astra on Pro) · Claude Opus 5.5 | Astra leads GPQA / FrontierMath |
| Writing, editing, long documents | **Claude** | Strongest on human-preference and work benchmarks |
| Coding | **Claude Code / Opus 5.5**, Codex, or OpenCode + free models | See [AGENTS.md](./AGENTS.md) |
| Recurring automations | **ChatGPT Scheduled Tasks** · **Gemini Scheduled actions** | Claude.ai has no consumer scheduler; Claude Code/Cline Desktop can run cron jobs |
| Research with citations | Gemini Deep Research · ChatGPT deep research · Claude Research | Try the free one first (Gemini) |
| Anything, free | Rotate all three free tiers | Each resets separately |

---

## Skills, plugins, MCP and tools — how to use them

| Thing | What it is | Where it works | How to add one |
|---|---|---|---|
| **Skill** | A folder with a `SKILL.md` (instructions) plus optional scripts. Only its one-line description sits in context until the task needs it | Claude Code, claude.ai, Codex, OpenCode, Cursor, Antigravity, Qoder (open standard) | Claude Code: drop it in `~/.claude/skills/` or `.claude/skills/`. claude.ai: upload in Settings → Capabilities |
| **Plugin** (Claude Code) | A bundle of skills + slash commands + hooks + MCP servers, installed from a marketplace | Claude Code (and Claude apps via the new plugin directory) | `/plugin marketplace add <owner/repo>` then `/plugin install <name>` |
| **MCP server** | Gives the model tools and data (GitHub, database, browser) over a standard protocol | Nearly every agent and chat app | `claude mcp add <name> -- <command>` or the app's Connectors page |
| **Hooks** | Scripts that run automatically on events (before a tool call, after an edit) | Claude Code, Antigravity CLI | `/hooks` or `settings.json` |
| **Slash commands** | Saved prompts you trigger with `/name` | Claude Code, Codex, OpenCode | Markdown file in `.claude/commands/` |

Rules of thumb: prefer a **skill** for "how to do X well", **MCP** for "access to system Y", a **plugin**
to share both with your team. **Read every `SKILL.md` and plugin before installing** — they are
instructions your agent will follow, and a malicious one can exfiltrate code. Where to find them:
[SKILLS.md](./SKILLS.md#skill-directories-where-to-find-skills).

---

## Token efficiency (make free limits last)

Tokens are the unit you pay for (or hit limits on). Every turn resends the whole conversation, so
**context size, not the number of questions, is what drains limits.**

### In any chat app

1. **One topic per chat.** Start a new chat when the topic changes — a 40-message chat costs ~40× more per reply than a fresh one.
2. **Paste the minimum.** The failing function and the error, not the whole repo. Screenshots cost more than text.
3. **Put stable context in a Project / Gem** instead of re-pasting it every chat.
4. **Ask for the format you want** ("answer in 5 bullets", "only the changed lines") — shorter output is cheaper and faster.
5. **Use the small model first** (Haiku / Luna / Flash) and escalate only if it fails.
6. **Edit your last message** instead of adding "no, I meant…" — editing replaces the turn, correcting adds one.
7. **Turn off extended thinking / Deep Research** for simple questions.

### In coding agents (Claude Code, Codex, OpenCode, Cline)

| Do | Why | Command |
|---|---|---|
| Clear between unrelated tasks | Old context is resent every turn | `/clear` |
| Compact at milestones | Turns 10–20K tokens of history into 1–3K | `/compact` (optionally with a focus: `/compact keep the API decisions`) |
| Keep a short project notes file | Saves 500–2,000 tokens of re-explaining per session | `CLAUDE.md` / `AGENTS.md` — under ~200 lines |
| Plan before building | Trial-and-error edits are the biggest waste | Shift+Tab (plan mode) in Claude Code |
| Pick the model per task | Sonnet/Haiku for routine edits, Opus for hard bugs | `/model` |
| Lower effort for easy work | Less thinking = fewer tokens | effort level in `/model` (Claude Code) · `reasoning_effort` in APIs |
| Point at files, don't paste them | The agent reads only the lines it needs | "look at `src/auth.ts:40-80`" |
| Limit MCP servers | Every connected server's tool list sits in context | Disable ones you're not using |
| Check what you're spending | Catch runaway sessions early | `/cost` · `/usage` (Codex) |
| Use subagents for broad searches | Their file dumps stay out of your main context | "use a subagent to find all callers of X" |

### On the API

- **Prompt caching:** cached input costs ~10% of normal (Claude cache reads $0.20/M on Opus/Sonnet 5.5; GPT-6 Astra $1/M cached). Put the stable part (system prompt, docs) first and keep it byte-identical between calls.
- **Batch API:** ~50% off for anything that can wait hours.
- **Off-peak pricing:** DeepSeek is half price outside Mon–Fri 01–04 and 06–10 UTC.
- **Route by difficulty:** ~70% of calls to DeepSeek V4.1 Flash / GPT-6 Luna, ~25% to Sonnet 5.5 / GPT-6 Sol, ~5% to Opus 5.5. Typically 85–95% cheaper than sending everything to the top model.
- **Cap output:** set `max_tokens`; ask for diffs, not whole files.
- **Count before you send:** use the provider's token-counting endpoint for big prompts.
