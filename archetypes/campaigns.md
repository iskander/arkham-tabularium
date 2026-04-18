---
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
date: {{ .Date }}
draft: true
description: ""

# --- Campaign metadata ---
campaign: ""               # Campaign name
episode: 1                 # Episode number in this series
players: 1
investigators: []          # Investigators in this playthrough
difficulty: "standard"
outcome: ""                # "victory" | "defeat" | "ongoing"

tags: []
# --- Discussion links (add after publishing) ---
bgg_thread: ""         # https://boardgamegeek.com/thread/XXXXXXX
reddit_thread: ""      # https://www.reddit.com/r/arkhamhorrorlcg/comments/XXXXX
# comments: false      # uncomment to disable the discussion block on this article

---

{{/*
  CAMPAIGN LOG TEMPLATE
  Write these as narrative play reports — not a transcript, but a story with analysis.
*/}}

_Episode {{ .Params.episode }} of a {{ .Params.campaign }} playthrough._

---

## The situation going in

XP spent, trauma carried forward, key campaign log entries.

## What happened

The story. Free-form prose. Be opinionated.

## Key moments

Three or four pivotal decisions, lucky pulls, or catastrophic failures worth highlighting.

## What I'd do differently

Honest post-mortem.

## Status heading into next scenario

Trauma, XP, campaign log state.
