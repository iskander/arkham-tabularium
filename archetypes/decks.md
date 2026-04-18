---
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
date: {{ .Date }}
draft: true
description: ""

# --- Deck metadata ---
investigator: ""           # Primary investigator name
class: ""                  # Guardian | Seeker | Rogue | Mystic | Survivor | Neutral
cycle_legal: ""            # Which cycle pool this deck uses (e.g. "Core + Dunwich")
xp_budget: 0              # Total XP spent in the deck shown
taboo: true               # Taboo list applied?

# --- Taxonomy ---
investigators: []
tags: []                   # e.g. ["deck-guide", "mystic", "solo", "true-solo"]
# --- Discussion links (add after publishing) ---
bgg_thread: ""         # https://boardgamegeek.com/thread/XXXXXXX
reddit_thread: ""      # https://www.reddit.com/r/arkhamhorrorlcg/comments/XXXXX
# comments: false      # uncomment to disable the discussion block on this article

---

{{/*
  DECK GUIDE TEMPLATE
*/}}

<div class="stat-block">
  <div class="stat-item"><strong>Investigator</strong> —</div>
  <div class="stat-item"><strong>Class</strong> —</div>
  <div class="stat-item"><strong>XP</strong> —</div>
  <div class="stat-item"><strong>Taboo</strong> —</div>
  <div class="stat-item"><strong>Format</strong> —</div>
</div>

## Concept

_What is this deck trying to do? One paragraph pitch._

## Core engine

The cards that make this deck tick.

## Key upgrades

XP priorities as you progress through a campaign.

| Priority | Card | XP | Why |
|---|---|---|---|
| 1 | — | — | — |

## Mulligan guide

What you need in your opening hand.

## Campaign notes

How the deck evolves scenario to scenario. Notable flex slots.

## Weaknesses & counters

What will wreck this deck. Honest assessment.

## Sample decklist

_Link to ArkhamDB or embed the full list here._
