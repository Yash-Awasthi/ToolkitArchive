#!/usr/bin/env python3
"""Generate every ToolkitArchive chart from the data/ folder.

Inputs:  data/models.json, data/extra_charts.json, data/stars.json, data/headtohead.json
Refresh: python scripts/update_stars.py   (live GitHub stars)
         node scripts/headtohead.js        (ratings from benchmarks.html)
Run:     python charts/gen_charts.py
"""
import json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
def load(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf-8") as f:
        return json.load(f)
MODELS = load("models.json")
M = MODELS["models"]
EXTRA = load("extra_charts.json")
STARS = load("stars.json")
H2H = load("headtohead.json")
DATE = "29 Sep 2026"

plt.rcParams.update({
    "figure.dpi": 140, "savefig.dpi": 140, "font.size": 12, "font.family": "DejaVu Sans",
    "axes.spines.top": False, "axes.spines.right": False, "axes.spines.left": False,
    "axes.grid": True, "grid.alpha": 0.22, "axes.axisbelow": True,
    "figure.facecolor": "#ffffff", "axes.facecolor": "#fbfaf7",
})
COLORS = {
    "Anthropic": "#d97757", "OpenAI": "#10a37f", "Google": "#4285f4", "xAI": "#3d3d3d",
    "Meta": "#0668e1", "DeepSeek": "#4d6bfe", "Moonshot": "#8b5cf6", "Z.AI": "#c99512",
    "Alibaba": "#ff6a00", "Xiaomi": "#e0703a", "Upstage": "#7c3aed", "Inception": "#0f766e",
    "Microsoft": "#2f9e44", "MiniMax": "#e83e8c", "Other": "#9ca3af",
}
def c(k):
    if k not in COLORS:
        raise KeyError(f"no color for {k!r} — add it to COLORS in charts/gen_charts.py")
    return COLORS[k]
def money(x, _): return f"${x:g}"
def title(ax, t, sub):
    ax.set_title(t, fontweight="bold", fontsize=16, loc="left", pad=26)
    ax.text(0, 1.02, sub, transform=ax.transAxes, fontsize=10, color="#6b7280")
def save(fig, name):
    fig.tight_layout(); fig.savefig(os.path.join(HERE, name)); plt.close(fig); print("wrote", name)
def hbar(rows, key, label_key, colors, xlabel, name, t, sub, fmt="{:g}", xlim=None, h=None):
    rows = sorted(rows, key=lambda r: r[key], reverse=True)
    fig, ax = plt.subplots(figsize=(12, h or 0.42 * len(rows) + 1.8)); y = list(range(len(rows)))
    ax.barh(y, [r[key] for r in rows], color=[colors(r) for r in rows], height=0.7)
    ax.set_yticks(y); ax.set_yticklabels([r[label_key] for r in rows]); ax.invert_yaxis()
    ax.set_xlabel(xlabel)
    if xlim: ax.set_xlim(*xlim)
    span = (xlim[1] - xlim[0]) if xlim else max(r[key] for r in rows)
    for i, r in enumerate(rows):
        ax.text(r[key] + span * 0.008, i, fmt.format(r[key]), va="center", fontsize=9.5)
    title(ax, t, sub); save(fig, name)

# 1. Intelligence vs price
# label offsets for points that share a spot
OFFSETS = {"GPT-6 Astra": (7, 7), "Claude Fable 5.1": (7, -13), "GLM-5.3": (-9, 5), "Qwen 3.8-Max": (9, 5)}
d = [m for m in M if m["aa"] is not None]
fig, ax = plt.subplots(figsize=(13, 8))
ax.axvspan(0.05, 2, color="#10a37f", alpha=0.06)
ax.text(0.07, max(m["aa"] for m in d) + 0.6, "value zone (< $2 / 1M out)", color="#10a37f", fontsize=10)
for m in d:
    ax.scatter(m["out"], m["aa"], s=190, color=c(m["company"]), edgecolor="white", linewidth=1.2, zorder=3,
               marker="D" if m["open"] else "o")
    dx, dy = OFFSETS.get(m["name"], (7, 4))
    ax.annotate(m["name"], (m["out"], m["aa"]), xytext=(dx, dy), textcoords="offset points", fontsize=9,
                ha="right" if dx < 0 else "left")
ax.set_xscale("log"); ax.xaxis.set_major_formatter(FuncFormatter(money))
ax.set_xlabel("Output price ($ / 1M tokens, log scale)"); ax.set_ylabel("Artificial Analysis Intelligence Index")
title(ax, "Intelligence vs price — current models",
      f"AA Intelligence Index v4.3 (independent) vs list output price · ◆ = open weights · {DATE}")
save(fig, "intelligence-vs-price.png")

# 2. Intelligence index bars
hbar(d, "aa", "name", lambda r: c(r["company"]), "Artificial Analysis Intelligence Index",
     "aa-index.png", "Artificial Analysis Intelligence Index",
     f"Independent composite of 10 evals incl. Terminal-Bench 4.0, HLE, GDPval · best effort per model · {DATE}")

# 3. Head-to-head
rows = [{"n": r["n"], "pct": round(r["r"] * 100), "k": r["k"]} for r in H2H["overall"]]
def h2h_color(r):
    n = r["n"]
    for key, co in [("Opus", "Anthropic"), ("Sonnet", "Anthropic"), ("Fable", "Anthropic"), ("GPT", "OpenAI"),
                    ("Gemini", "Google"), ("Kimi", "Moonshot"), ("DeepSeek", "DeepSeek"), ("Qwen", "Alibaba"),
                    ("GLM", "Z.AI"), ("Grok", "xAI"), ("MiMo", "Xiaomi"), ("Muse", "Meta")]:
        if key in n: return c(co)
    return c("Other")
for r in rows: r["label"] = f'{r["n"]}  ({r["k"]} charts)'
hbar(rows, "pct", "label", h2h_color, "Share of head-to-head matchups won (%)", "head-to-head.png",
     "Who's actually best — head-to-head across all benchmarks",
     f'{H2H["benchmarks"]} charts from benchmarks.html · two models on the same chart = one matchup · 6+ charts to rank · {DATE}',
     fmt="{}%", xlim=(0, 105))

# 4. Terminal-Bench 4.0
d = [m for m in M if m["tb4"] is not None]
hbar(d, "tb4", "name", lambda r: c(r["company"]), "Terminal-Bench 4.0 accuracy (%)", "terminal-bench-4.png",
     "Terminal-Bench 4.0 — agentic terminal tasks",
     f"Vendor/aggregated scores (llm-stats, Sept 28). Independent AA run: Sonnet 5.5 63.6, Opus 5.5 59.6 · {DATE}",
     fmt="{:g}%", xlim=(0, 78))

# 5. Output price
hbar(M, "out", "name", lambda r: c(r["company"]), "Output price ($ / 1M tokens)", "output-price.png",
     "Output price — current models", f"List price per 1M output tokens · DeepSeek shown at peak (off-peak is half) · {DATE}",
     fmt="${:g}")

# 6. Context windows
d = [m for m in M if m["ctx_k"]]
hbar(d, "ctx_k", "name", lambda r: c(r["company"]), "Context window (K tokens)", "context-windows.png",
     "Context windows — current models", f"Maximum context in thousands of tokens · {DATE}", fmt="{:g}K")

# 7. GitHub stars (live)
sg = STARS["groups"]
hbar([{"l": r["label"], "s": r["stars"] / 1000} for r in sg["agents"]], "s", "l", lambda r: "#d97757",
     "GitHub stars (thousands)", "github-stars-agents.png", "Coding agents — GitHub stars",
     f'Live from the GitHub API on {STARS["checked"]} · python scripts/update_stars.py', fmt="{:.0f}K")
hbar([{"l": r["label"], "s": r["stars"] / 1000} for r in sg["skills_mcp"]], "s", "l", lambda r: "#4285f4",
     "GitHub stars (thousands)", "github-stars-skills.png", "Skills, plugins & MCP servers — GitHub stars",
     f'Live from the GitHub API on {STARS["checked"]}', fmt="{:.0f}K")

# 8. Coding plans
hbar(EXTRA["coding_plans"]["rows"], "usd", "label", lambda r: c(r["color"]), "USD per month", "coding-plans.png",
     "What coding plans cost", f"Monthly list price · $0 = usable free plan · {DATE}", fmt="${:g}")

# 9. Image + video arenas
hbar(EXTRA["image_arena"]["rows"], "elo", "label", lambda r: c(r["color"]), "Elo (blind human votes)", "image-arena.png",
     "Text-to-image — Artificial Analysis Arena", f"Blind votes on the same prompt · {DATE}", xlim=(950, 1215))
hbar(EXTRA["video_arena"]["rows"], "elo", "label", lambda r: c(r["color"]), "Elo (blind human votes)", "video-arena.png",
     "Text-to-video with audio — Artificial Analysis Arena", f"Blind votes on the same prompt · {DATE}", xlim=(1000, 1250))
