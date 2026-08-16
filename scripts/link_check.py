#!/usr/bin/env python3
"""Check every URL in the archive's markdown files for dead or redirected links.
Plain requests, no framework. Run: python3 scripts/link_check.py"""
import concurrent.futures as cf
import glob
import os
import re
import sys

import requests

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL_RE = re.compile(r'https?://[^\s)>\]"\']+')
TIMEOUT = 10
WORKERS = 16
HEADERS = {"User-Agent": "Mozilla/5.0 (ToolkitArchive link-check)"}

# Template/placeholder URLs used in docs as fill-in-the-blank examples, not real
# links. They will never resolve and aren't dead links to report.
IGNORE_PATTERNS = [
    re.compile(r'your-coolify\.com'),
    re.compile(r'\$RENDER_DEPLOY_HOOK_ID'),
    re.compile(r'localhost:\d+'),
    re.compile(r'docs\.myservice\.com'),
]


def find_urls():
    """Map each markdown file (relative path) to the URLs it references, in order, deduped."""
    hits = {}
    for path in sorted(glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True)):
        with open(path, encoding="utf-8") as f:
            text = f.read()
        urls = list(dict.fromkeys(m.rstrip(".,;:") for m in URL_RE.findall(text)))
        urls = [u for u in urls if not any(p.search(u) for p in IGNORE_PATTERNS)]
        if urls:
            hits[os.path.relpath(path, ROOT)] = urls
    return hits


def check(url):
    """Return (url, status, detail). status is ok / redirected / dead / error."""
    try:
        r = requests.head(url, timeout=TIMEOUT, allow_redirects=True, headers=HEADERS)
        if r.status_code == 405 or r.status_code >= 400:
            r = requests.get(url, timeout=TIMEOUT, allow_redirects=True, headers=HEADERS)
    except requests.RequestException as e:
        return url, "error", type(e).__name__
    if r.status_code >= 400:
        status = "dead"
    elif r.history:
        status = "redirected"
    else:
        status = "ok"
    detail = str(r.status_code) + (f" -> {r.url}" if r.history else "")
    return url, status, detail


def main():
    by_file = find_urls()
    all_urls = sorted({u for urls in by_file.values() for u in urls})
    print(f"checking {len(all_urls)} unique urls from {len(by_file)} files...")

    results = {}
    with cf.ThreadPoolExecutor(max_workers=WORKERS) as ex:
        for url, status, detail in ex.map(check, all_urls):
            results[url] = (status, detail)

    dead, redirected = {}, {}
    for path, urls in by_file.items():
        for url in urls:
            status, detail = results[url]
            if status in ("dead", "error"):
                dead.setdefault(path, []).append((url, detail))
            elif status == "redirected":
                redirected.setdefault(path, []).append((url, detail))

    if dead:
        print("\n=== dead links (4xx / 5xx / timeout / connection error) ===")
        for path, items in dead.items():
            print(f"\n{path}")
            for url, detail in items:
                print(f"  {url}  [{detail}]")

    if redirected:
        print("\n=== redirected links ===")
        for path, items in redirected.items():
            print(f"\n{path}")
            for url, detail in items:
                print(f"  {url}  [{detail}]")

    print(f"\n{len(all_urls)} urls checked, {len(dead)} files with dead links, "
          f"{len(redirected)} files with redirects.")
    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
