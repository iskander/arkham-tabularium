---
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
date: {{ .Date }}
draft: true
description: ""

# --- Scenario metadata ---
cycle: ""                  # e.g. "The Dunwich Legacy", "Edge of the Earth"
scenario_number: ""        # e.g. "1a", "2"
difficulty: "standard"     # easy | standard | hard | expert
standalone: false          # true if playable standalone

# --- Taxonomy ---
investigators: []          # investigator names used in playthrough, if any
tags: []                   # e.g. ["scenario-review", "dunwich", "horror"]

# --- Review scores (0–10) ---
fun_factor: 0
replayability: 0
thematic_coherence: 0
mechanical_design: 0
# --- Discussion links (add after publishing) ---
bgg_thread: ""         # https://boardgamegeek.com/thread/XXXXXXX
reddit_thread: ""      # https://www.reddit.com/r/arkhamhorrorlcg/comments/XXXXX
# comments: false      # uncomment to disable the discussion block on this article

---

{{/*
  SCENARIO REVIEW TEMPLATE
  Delete sections you don't need.
  Use shortcodes for spoiler/tip/note callouts (see docs/shortcodes.md).
*/}}

<!-- Quick-reference stat block -->
<div class="stat-block">
  <div class="stat-item"><strong>Cycle</strong> —</div>
  <div class="stat-item"><strong>Players</strong> 1–4</div>
  <div class="stat-item"><strong>Difficulty</strong> —</div>
  <div class="stat-item"><strong>Est. time</strong> —</div>
  <div class="stat-item"><strong>Standalone?</strong> No</div>
</div>

## Overview

_A brief, spoiler-free summary of what this scenario is about._

## Encounter deck composition

What does the encounter deck throw at you? Notable mechanics, keyword synergies.

## Narrative & theme

How well does the scenario tell its story? Set dressing, flavour text, agenda/act writing quality.

## Mechanical design

Interesting mechanics, gotchas, pacing, scaling across player counts.

## Verdict

_One or two punchy sentences._

<!-- Rating bar — adjust the width percentages (0–100) -->
<div class="rating-bar">
  <h4>Ratings</h4>
  <div class="rating-row">
    <span class="rating-label">Fun factor</span>
    <div class="rating-track"><div class="rating-fill" style="width: {{ mul .Params.fun_factor 10 }}%"></div></div>
    <span class="rating-score">{{ .Params.fun_factor }}/10</span>
  </div>
  <div class="rating-row">
    <span class="rating-label">Replayability</span>
    <div class="rating-track"><div class="rating-fill" style="width: {{ mul .Params.replayability 10 }}%"></div></div>
    <span class="rating-score">{{ .Params.replayability }}/10</span>
  </div>
  <div class="rating-row">
    <span class="rating-label">Theme</span>
    <div class="rating-track"><div class="rating-fill" style="width: {{ mul .Params.thematic_coherence 10 }}%"></div></div>
    <span class="rating-score">{{ .Params.thematic_coherence }}/10</span>
  </div>
  <div class="rating-row">
    <span class="rating-label">Design</span>
    <div class="rating-track"><div class="rating-fill" style="width: {{ mul .Params.mechanical_design 10 }}%"></div></div>
    <span class="rating-score">{{ .Params.mechanical_design }}/10</span>
  </div>
</div>
