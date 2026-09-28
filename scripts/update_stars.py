#!/usr/bin/env python3
"""Refresh data/stars.json with live GitHub star counts.
Uses GITHUB_TOKEN if set (5,000 req/h), otherwise the unauthenticated API (60 req/h).
Run: python scripts/update_stars.py"""
import json, os, urllib.request, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "stars.json")

# group -> [(label, owner/repo)]
REPOS = {
    "agents": [
        ("OpenClaw", "openclaw/openclaw"), ("Hermes Agent", "NousResearch/hermes-agent"),
        ("DeepSeek Harness", "deepseek-ai/deepseek-harness"), ("OpenCode", "anomalyco/opencode"),
        ("Claw Code", "ultraworkers/claw-code"), ("Claude Code", "anthropics/claude-code"),
        ("Codex CLI", "openai/codex"), ("Pi", "earendil-works/pi"), ("Gemini CLI", "google-gemini/gemini-cli"),
        ("OpenHands", "OpenHands/OpenHands"), ("Cline", "cline/cline"), ("Open Interpreter", "openinterpreter/openinterpreter"),
        ("Goose", "aaif-goose/goose"), ("Aider", "Aider-AI/aider"), ("Continue", "continuedev/continue"),
        ("Crush", "charmbracelet/crush"), ("Qwen Code", "QwenLM/qwen-code"), ("Kilo Code", "Kilo-Org/kilocode"),
        ("Grok Build", "xai-org/grok-build"), ("SWE-agent", "SWE-agent/SWE-agent"), ("Freebuff", "CodebuffAI/freebuff"),
        ("Kimi CLI", "MoonshotAI/kimi-cli"), ("Kimi Code", "MoonshotAI/kimi-code"),
    ],
    "skills_mcp": [
        ("superpowers", "obra/superpowers"), ("ECC", "affaan-m/ECC"), ("anthropics/skills", "anthropics/skills"),
        ("UI UX Pro Max", "nextlevelbuilder/ui-ux-pro-max-skill"), ("awesome-design-md", "VoltAgent/awesome-design-md"),
        ("browser-use", "browser-use/browser-use"), ("claude-mem", "thedotmack/claude-mem"),
        ("Paperclip", "paperclipai/paperclip"), ("Taste Skill", "Leonxlnx/taste-skill"),
        ("Agent-Reach", "Panniantong/Agent-Reach"), ("Impeccable", "pbakaus/impeccable"),
        ("OmniRoute", "diegosouzapw/OmniRoute"), ("GSD", "gsd-build/get-shit-done"), ("Context7", "upstash/context7"),
        ("CLIProxyAPI", "router-for-me/CLIProxyAPI"), ("Chrome DevTools MCP", "ChromeDevTools/chrome-devtools-mcp"),
        ("agent-browser", "vercel-labs/agent-browser"), ("emilkowalski/skills", "emilkowalski/skills"),
        ("Hindsight", "vectorize-io/hindsight"), ("Playwright MCP", "microsoft/playwright-mcp"),
        ("Serena", "oraios/serena"), ("Browser Harness", "browser-use/browser-harness"),
        ("GSAP skills", "greensock/gsap-skills"), ("google/ax", "google/ax"), ("laya-mlx", "mizorewww/laya-mlx"),
    ],
    "local": [("Ollama", "ollama/ollama"), ("llama.cpp", "ggml-org/llama.cpp")],
}


def stars(repo):
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}", headers={"Accept": "application/vnd.github+json"})
    tok = os.environ.get("GITHUB_TOKEN")
    if tok:
        req.add_header("Authorization", f"Bearer {tok}")
    with urllib.request.urlopen(req, timeout=20) as r:
        d = json.load(r)
    return d["stargazers_count"], d["full_name"], d["pushed_at"][:10]


out = {"checked": datetime.date.today().isoformat(), "groups": {}}
for group, items in REPOS.items():
    rows = []
    for label, repo in items:
        try:
            n, full, pushed = stars(repo)
            rows.append({"label": label, "repo": full, "stars": n, "pushed": pushed})
        except Exception as e:
            print(f"skip {repo}: {e}")
    out["groups"][group] = sorted(rows, key=lambda r: r["stars"], reverse=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(out, f, indent=1)
print(f"wrote {OUT}")
