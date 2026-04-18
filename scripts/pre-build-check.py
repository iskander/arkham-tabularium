#!/usr/bin/env python3
"""
pre-build-check.py — Obsidian → Hugo validation script

Run before `hugo` or `hugo server` to catch common issues
that arise from writing in Obsidian:

  python3 scripts/pre-build-check.py

Exits with code 1 if blocking issues are found, 0 if clean.
"""

import os
import re
import sys
from pathlib import Path

CONTENT_DIR = Path(__file__).parent.parent / "content"

# ── Issue collectors ──────────────────────────────────────────────────────────

errors   = []   # blocking — will break the build
warnings = []   # non-blocking — worth knowing

# ── Patterns to detect ───────────────────────────────────────────────────────

# Obsidian wikilinks: [[Some Article]] or [[Some Article|Display Text]]
RE_WIKILINK   = re.compile(r'\[\[([^\]]+)\]\]')

# Obsidian image embeds: ![[image.jpg]]
RE_WIKI_IMAGE = re.compile(r'!\[\[([^\]]+)\]\]')

# Obsidian-style callouts (incompatible with Hugo)
# > [!note] Title
RE_OB_CALLOUT = re.compile(r'^> \[!(\w+)\]', re.MULTILINE)

# Inline dataview queries (Obsidian plugin, invisible to Hugo)
RE_DATAVIEW   = re.compile(r'```dataview')

# draft: true articles — reminder only, not an error
RE_DRAFT      = re.compile(r'^draft:\s*true', re.MULTILINE)

# Missing alt text in standard img tags
RE_EMPTY_ALT  = re.compile(r'!\[\]\(')

# ── Scan all markdown files ───────────────────────────────────────────────────

md_files = list(CONTENT_DIR.rglob("*.md"))

if not md_files:
    print("⚠  No markdown files found in content/")
    sys.exit(0)

draft_count = 0

for path in sorted(md_files):
    rel = path.relative_to(CONTENT_DIR.parent)
    text = path.read_text(encoding="utf-8")

    # Wikilink images (subset of wikilinks — check first)
    for m in RE_WIKI_IMAGE.finditer(text):
        errors.append(
            f"{rel}: Obsidian image embed  ![[{m.group(1)}]]\n"
            f"  → Replace with: {{{{< figure src=\"{m.group(1)}\" alt=\"…\" >}}}}"
        )

    # Wikilinks (after image check so we don't double-report)
    text_no_img = RE_WIKI_IMAGE.sub("", text)
    for m in RE_WIKILINK.finditer(text_no_img):
        target = m.group(1).split("|")[0].strip()
        display = m.group(1).split("|")[-1].strip()
        errors.append(
            f"{rel}: Wikilink  [[{m.group(1)}]]\n"
            f"  → Replace with standard Markdown: [{display}](relative/path/to/{target.lower().replace(' ', '-')}/)"
        )

    # Obsidian callouts
    for m in RE_OB_CALLOUT.finditer(text):
        callout_type = m.group(1).lower()
        mapped = callout_type if callout_type in ("note", "tip", "spoiler") else "note"
        errors.append(
            f"{rel}: Obsidian callout  > [!{m.group(1)}]\n"
            f"  → Replace with Hugo callout div:\n"
            f"    <div class=\"callout {mapped}\">\n"
            f"      <p class=\"callout-title\">{callout_type.capitalize()}</p>\n"
            f"      <p>…</p>\n"
            f"    </div>"
        )

    # Dataview blocks
    if RE_DATAVIEW.search(text):
        warnings.append(
            f"{rel}: Contains a Dataview query block — will render as a code block in Hugo."
        )

    # Empty alt text
    for m in RE_EMPTY_ALT.finditer(text):
        warnings.append(
            f"{rel}: Image with empty alt text  ![](…) — add a description for accessibility."
        )

    # Draft count
    if RE_DRAFT.search(text):
        draft_count += 1

# ── Report ────────────────────────────────────────────────────────────────────

print(f"\n{'='*60}")
print(f"  Arkham Tabularium — pre-build check")
print(f"  {len(md_files)} files scanned · {draft_count} drafts")
print(f"{'='*60}\n")

if errors:
    print(f"✗  {len(errors)} ERROR(S) — fix before building:\n")
    for e in errors:
        print(f"  • {e}\n")

if warnings:
    print(f"⚠  {len(warnings)} WARNING(S):\n")
    for w in warnings:
        print(f"  · {w}\n")

if not errors and not warnings:
    print("✓  All clear — no issues found.\n")
elif not errors:
    print("✓  No blocking errors. Warnings are non-critical.\n")

if draft_count:
    print(f"ℹ  {draft_count} article(s) still marked draft: true\n")

print(f"{'='*60}\n")

sys.exit(1 if errors else 0)
