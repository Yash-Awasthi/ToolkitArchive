#!/usr/bin/env python3
"""Generate ToolkitArchive model charts from data/models.json (single source of truth).
API-accessible models only. Run: python3 charts/gen_charts.py
Outputs (charts/): swe-bench.png, all-models-cost.png, cost-input-output.png,
context-windows.png, all-models-scatter.png, claude-effort.png"""
import json, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
with open(os.path.join(ROOT, "data", "models.json")) as f:
    DATA = json.load(f)
M = DATA["models"]

plt.rcParams.update({
    "figure.dpi": 140, "savefig.dpi": 140, "font.size": 12,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.alpha": 0.25, "axes.axisbelow": True,
    "font.family": "DejaVu Sans",
})

# One stable color per company — legend and dots use the SAME map (fixes old chart).
COLORS = {
    "OpenAI": "#10a37f", "Anthropic": "#d97757", "Google": "#4285f4", "xAI": "#111111",
    "Z.AI": "#6a5acd", "Alibaba": "#ff6a00", "Moonshot": "#1e90ff", "MiniMax": "#e83e8c",
    "Mistral": "#fa520f", "DeepSeek": "#4d6bfe", "Xiaomi": "#b8860b", "Meta": "#0668e1",
    "NVIDIA": "#76b900", "StepFun": "#7f8c8d", "Poolside": "#9b59b6",
}
def c(co): return COLORS.get(co, "#999999")
def money(x, _): return f"${x:g}"
def save(fig, name): fig.tight_layout(); fig.savefig(os.path.join(HERE, name)); plt.close(fig)

# ---------- 1. SWE-bench leaderboard ----------
d = sorted(M, key=lambda r: r["swe"], reverse=True)
fig, ax = plt.subplots(figsize=(13, 10)); y = range(len(d))
ax.barh(list(y), [r["swe"] for r in d], color=[c(r["company"]) for r in d])
ax.set_yticks(list(y)); ax.set_yticklabels([r["name"] for r in d]); ax.invert_yaxis()
ax.set_xlabel("SWE-bench Verified (%)"); ax.set_xlim(50, 92)
ax.set_title("SWE-bench Verified — API Models (June 2026)", fontweight="bold", fontsize=16, pad=14)
for i, r in enumerate(d): ax.text(r["swe"]+0.3, i, f'{r["swe"]:g}%', va="center", fontsize=9)
save(fig, "swe-bench.png")

# ---------- 2. Output cost, every model ----------
d = sorted(M, key=lambda r: r["out"], reverse=True)
fig, ax = plt.subplots(figsize=(13, 10)); y = range(len(d))
ax.barh(list(y), [r["out"] for r in d], color=[c(r["company"]) for r in d])
ax.set_yticks(list(y)); ax.set_yticklabels([r["name"] for r in d]); ax.invert_yaxis()
ax.set_xlabel("Output price ($ / 1M tokens)")
ax.set_title("Output Cost — Every API Model (June 2026)", fontweight="bold", fontsize=16, pad=14)
ax.xaxis.set_major_formatter(FuncFormatter(money))
for i, r in enumerate(d): ax.text(r["out"]+0.3, i, f'${r["out"]:g}', va="center", fontsize=9)
ax.margins(x=0.08)
save(fig, "all-models-cost.png")

# ---------- 3. Input vs output (log) ----------
d = sorted(M, key=lambda r: r["out"], reverse=True)
fig, ax = plt.subplots(figsize=(13, 10)); yy = np.arange(len(d)); h = 0.4
ax.barh(yy-h/2, [r["in"] for r in d], height=h, color="#b0b4ba", label="Input $/1M")
ax.barh(yy+h/2, [r["out"] for r in d], height=h, color=[c(r["company"]) for r in d], label="Output $/1M")
ax.set_yticks(yy); ax.set_yticklabels([r["name"] for r in d]); ax.invert_yaxis()
ax.set_xscale("log"); ax.set_xlabel("$ / 1M tokens (log scale)")
ax.set_title("Input vs Output Pricing — API Models (June 2026)", fontweight="bold", fontsize=16, pad=14)
ax.xaxis.set_major_formatter(FuncFormatter(money)); ax.legend(loc="lower right")
save(fig, "cost-input-output.png")

# ---------- 4. Context windows (log) ----------
d = sorted(M, key=lambda r: (r["ctx_k"], -r["out"]))
fig, ax = plt.subplots(figsize=(13, 10)); y = range(len(d))
ax.barh(list(y), [r["ctx_k"] for r in d], color=[c(r["company"]) for r in d])
ax.set_yticks(list(y)); ax.set_yticklabels([r["name"] for r in d])
ax.set_xscale("log"); ax.set_xlabel("Context window (K tokens, log scale)")
ax.set_title("Context Windows — API Models (June 2026)", fontweight="bold", fontsize=16, pad=14)
for i, r in enumerate(d):
    lbl = f'{r["ctx_k"]/1000:g}M' if r["ctx_k"] >= 1000 else f'{r["ctx_k"]}K'
    ax.text(r["ctx_k"]*1.05, i, lbl, va="center", fontsize=9)
ax.margins(x=0.12)
save(fig, "context-windows.png")

# ---------- 5. Price vs performance scatter (clear: labeled points, matching legend) ----------
fig, ax = plt.subplots(figsize=(14, 9))
ax.axvspan(0.1, 2.0, color="#2ecc71", alpha=0.07, zorder=0)
ax.text(0.42, 58.5, "value sweet spot\n(<$2/M out)", color="#27ae60", fontsize=10, ha="center")
seen = []
for r in M:
    co = r["company"]
    ax.scatter(r["out"], r["swe"], s=160, color=c(co), edgecolor="white", linewidth=1.0, zorder=3,
               label=co if co not in seen else None)
    seen.append(co)
    ax.annotate(r["name"], (r["out"], r["swe"]), fontsize=8.5, xytext=(5, 4),
                textcoords="offset points", zorder=4)
ax.set_xscale("log"); ax.set_xlabel("Output price ($ / 1M tokens, log scale)")
ax.set_ylabel("SWE-bench Verified (%)"); ax.set_ylim(55, 92)
ax.set_title("Price vs Performance — Every API Model (June 2026)", fontweight="bold", fontsize=16, pad=14)
ax.xaxis.set_major_formatter(FuncFormatter(money))
# legend ordered by company name, colors match dots exactly
handles, labels = ax.get_legend_handles_labels()
order = sorted(range(len(labels)), key=lambda i: labels[i])
ax.legend([handles[i] for i in order], [labels[i] for i in order],
          loc="lower right", ncol=2, fontsize=9, framealpha=0.9, title="Provider")
save(fig, "all-models-scatter.png")

# ---------- 6. Claude effort tiers ----------
ce = DATA["claude_effort"]
fig, ax = plt.subplots(figsize=(11, 6))
shades = ["#f3d6c9", "#eab39a", "#e08e6b", "#d97757", "#b85a3c"]
bars = ax.bar(ce["tiers"], ce["budget_k"], color=shades)
ax.set_ylabel("Relative thinking budget (K tokens, illustrative)")
ax.set_title("Claude Reasoning Effort Tiers (Opus 4.8 hybrid reasoning)", fontweight="bold", fontsize=15, pad=14)
for b, v in zip(bars, ce["budget_k"]):
    ax.text(b.get_x()+b.get_width()/2, v+2, f"~{v}K", ha="center", fontsize=10)
ax.text(0.5, -0.18,
        "Higher effort = more extended-thinking tokens = better on hard tasks, slower + costlier. "
        "Set per request; low for simple edits, max for the hardest reasoning.",
        transform=ax.transAxes, ha="center", fontsize=9, color="#555")
ax.margins(y=0.18)
save(fig, "claude-effort.png")

print("charts written from data/models.json:",
      "swe-bench, all-models-cost, cost-input-output, context-windows,",
      "all-models-scatter, claude-effort")
