#!/usr/bin/env python3
"""Rewrite "~12K★"-style star counts in the markdown files with live GitHub numbers.

Handles two shapes:
  [name](https://github.com/owner/repo) (~12K★)      -> count right after a repo link
  | ... github.com/owner/repo ... | ~12K★ | ...       -> table row with exactly one repo link
Uses GITHUB_TOKEN if set. Run: python scripts/update_md_stars.py"""
import glob, json, os, re, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = {}


def stars(repo):
    if repo not in CACHE:
        req = urllib.request.Request(f"https://api.github.com/repos/{repo}", headers={"Accept": "application/vnd.github+json"})
        if os.environ.get("GITHUB_TOKEN"):
            req.add_header("Authorization", f"Bearer {os.environ['GITHUB_TOKEN']}")
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                CACHE[repo] = json.load(r)["stargazers_count"]
        except Exception:
            CACHE[repo] = None
    return CACHE[repo]


def fmt(n):
    return f"{n/1000:.0f}K" if n >= 10000 else (f"{n/1000:.1f}K" if n >= 1000 else str(n))


LINK = r"https://github\.com/([\w.-]+/[\w.-]+?)(?:\.git)?/?"
ADJ = re.compile(r"(\(" + LINK + r"\)\**\s*\()~?[\d.]+K★(\))")
COUNT = re.compile(r"~?[\d.]+K★|~?\d+(?:\.\d+)?K\+?(?= \|)")
changed = 0
for path in glob.glob(os.path.join(ROOT, "*.md")):
    lines = open(path, encoding="utf-8").read().split("\n")
    for i, ln in enumerate(lines):
        new = ADJ.sub(lambda m: m.group(1) + (fmt(stars(m.group(2))) + "★" if stars(m.group(2)) else "?") + m.group(3), ln)
        repos = set(re.findall(LINK, new))
        if ln.startswith("|") and len(repos) == 1 and "K★" in new and not ADJ.search(ln):
            n = stars(repos.pop())
            if n:
                new = re.sub(r"~?[\d.]+K★", fmt(n) + "★", new, count=1)
        if new != ln:
            lines[i] = new; changed += 1
    open(path, "w", encoding="utf-8").write("\n".join(lines))
print(f"updated {changed} lines, {len(CACHE)} repos checked")
