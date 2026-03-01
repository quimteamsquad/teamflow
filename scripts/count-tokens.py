#!/usr/bin/env python3
"""Count the token cost of the TeamFlow plugin and update the README badge.

Uses tiktoken (cl100k_base) to count tokens across all plugin components:
skills, agents, commands, hooks, templates, and CLAUDE.md.

Usage:
    python scripts/count-tokens.py              # print report
    python scripts/count-tokens.py --update     # also update README.md
    python scripts/count-tokens.py --badge      # also write SVG badge
"""

import glob
import os
import re
import sys

try:
    import tiktoken
except ImportError:
    print("tiktoken not installed. Run: pip install tiktoken")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(ROOT, "README.md")
BADGE_PATH = os.path.join(ROOT, "scripts", "token-badge.svg")
CONTEXT_WINDOW = 200_000
ENCODING = "cl100k_base"
MARKER = "token-count"

CATEGORIES = {
    "skills":    os.path.join(ROOT, "skills", "**", "SKILL.md"),
    "agents":    os.path.join(ROOT, "agents", "*.md"),
    "commands":  os.path.join(ROOT, "commands", "*.md"),
    "hooks":     [
        os.path.join(ROOT, "hooks", "hooks.json"),
        os.path.join(ROOT, "hooks", "scripts", "*.sh"),
    ],
    "templates": os.path.join(ROOT, "templates", "*"),
    "CLAUDE.md": os.path.join(ROOT, "CLAUDE.md"),
}

# ---------------------------------------------------------------------------
# Token counting
# ---------------------------------------------------------------------------

def expand_patterns(patterns):
    """Expand one or more glob patterns into a sorted list of files."""
    if isinstance(patterns, str):
        patterns = [patterns]
    files = set()
    for p in patterns:
        files.update(glob.glob(p, recursive=True))
    return sorted(f for f in files if os.path.isfile(f))


def count_tokens(files, enc):
    """Return total token count for a list of files."""
    total = 0
    for path in files:
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                total += len(enc.encode(f.read()))
        except Exception as e:
            print(f"  skip {path}: {e}", file=sys.stderr)
    return total


def format_tokens(n):
    """Human-friendly token count: 13.1k, 150k, 842."""
    if n >= 100_000:
        return f"{round(n / 1000)}k"
    if n >= 1_000:
        return f"{n / 1000:.1f}k"
    return str(n)

# ---------------------------------------------------------------------------
# Badge SVG
# ---------------------------------------------------------------------------

def badge_color(pct):
    if pct < 30:
        return "#4c1"
    if pct < 50:
        return "#97ca00"
    if pct < 70:
        return "#dfb317"
    return "#e05d44"


def generate_svg(display, pct):
    label = "context cost"
    value = f"{display} tokens"
    desc = f"{display} tokens - {pct}% of context window"
    cw = 7.0
    lw = round(len(label) * cw) + 10
    vw = round(len(value) * cw) + 10
    tw = lw + vw
    color = badge_color(pct)
    lx = lw // 2
    vx = lw + vw // 2
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{tw}" height="20" role="img" aria-label="{desc}">
  <title>{desc}</title>
  <linearGradient id="s" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <clipPath id="r"><rect width="{tw}" height="20" rx="3" fill="#fff"/></clipPath>
  <g clip-path="url(#r)">
    <rect width="{lw}" height="20" fill="#555"/>
    <rect x="{lw}" width="{vw}" height="20" fill="{color}"/>
    <rect width="{tw}" height="20" fill="url(#s)"/>
    <g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" font-size="11">
      <text x="{lx}" y="15" fill="#010101" fill-opacity=".3">{label}</text>
      <text x="{lx}" y="14">{label}</text>
      <text x="{vx}" y="15" fill="#010101" fill-opacity=".3">{value}</text>
      <text x="{vx}" y="14">{value}</text>
    </g>
  </g>
</svg>'''

# ---------------------------------------------------------------------------
# README update
# ---------------------------------------------------------------------------

def update_readme(badge_text):
    marker_re = re.compile(
        rf"(<!--\s*{re.escape(MARKER)}\s*-->).*?(<!--\s*/{re.escape(MARKER)}\s*-->)",
        re.DOTALL,
    )
    with open(README, "r", encoding="utf-8") as f:
        content = f.read()

    replacement = f"\\1\n{badge_text}\n\\2"
    new_content = marker_re.sub(replacement, content)

    if new_content != content:
        with open(README, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("README.md updated.")
    else:
        print("README.md unchanged (markers not found or no change).")

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    do_update = "--update" in sys.argv
    do_badge = "--badge" in sys.argv

    enc = tiktoken.get_encoding(ENCODING)

    results = {}
    grand_total = 0

    for cat, patterns in CATEGORIES.items():
        files = expand_patterns(patterns)
        tokens = count_tokens(files, enc)
        results[cat] = (len(files), tokens)
        grand_total += tokens

    pct = round(grand_total / CONTEXT_WINDOW * 100)
    display = format_tokens(grand_total)

    # Print report
    print(f"{'Component':<12} {'Files':>5} {'Tokens':>8}")
    print("-" * 28)
    for cat, (nfiles, tokens) in results.items():
        print(f"{cat:<12} {nfiles:>5} {tokens:>8}")
    print("-" * 28)
    print(f"{'TOTAL':<12} {sum(n for n, _ in results.values()):>5} {grand_total:>8}")
    print()
    print(f"{display} tokens - {pct}% of {CONTEXT_WINDOW:,} context window")

    # Update README
    if do_update:
        badge_line = f"**{display} tokens** - {pct}% of context window"
        update_readme(badge_line)

    # Write SVG badge
    if do_badge:
        svg = generate_svg(display, pct)
        os.makedirs(os.path.dirname(BADGE_PATH), exist_ok=True)
        with open(BADGE_PATH, "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"Badge SVG written to {BADGE_PATH}")


if __name__ == "__main__":
    main()
