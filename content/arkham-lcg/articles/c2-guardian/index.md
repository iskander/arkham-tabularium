---
title: "Chapter 2 Class Spotlight: Guardian"
date: 2026-04-19
draft: false
description: A look at how the Chapter 2 evergreen pool implements the Guardian class — where the manual's archetypes land, where they don't, and the implicit themes that emerge from the card design.
tags:
  - class-spotlight
  - guardian
  - chapter-2
  - core-2026
  - evergreen-deck
  - daniela-reyes
  - tommy-muldoon
bgg_thread: https://boardgamegeek.com/thread/3685115/chapter-2-class-spotlight-guardian
reddit_thread: https://www.reddit.com/r/arkhamhorrorlcg/comments/1sqjjw3/arkham_tabularium_chapter_2_class_spotlight/
---

{{< figure src="https://cdn.jsdelivr.net/gh/iskander/arkham-tabularium-assets@main/arkham-lcg/articles/c2-guardian/Guardian.jpg"
    alt="Guardian class banner — Chapter 2 Core"
    width="900" >}}


Now that the entire evergreen pool is out, it's interesting to check how the Core 2026 manual characterizes the Guardian class versus how the class is implemented through its evergreen pool, in terms of card design and archetypes across the Chapter 2 core and Tommy Muldoon's Evergreen deck.

## What the Manual Says

In the Chapter 2 Core manual, guardians are described as "team players who favor combat, protecting their fellow investigators, and building an arsenal for the next big confrontation." It goes on to spell out that they support as well as fight, tanking hits for others and healing damage when needed.

The listed class strengths are: **High Fight Value, Healing, Team Support, Heavy Weaponry, Strong Allies, Enemy Management, and Extra Damage.**

The four named playstyles are: **Enemy "Tank", Melee Fighter, Weapons Expert, and Medic.**

Three of the four playstyles are combat-oriented (Tank, Melee, Weapons Expert), while the Medic slot gestures at a supportive, non-combat identity. The class description explicitly mentions going "toe-to-tentacle" with enemies and makes combat the central pitch — the team support is framed as a consequence of fighting, not a separate mode of play.

## How the Core Set Implements Guardian Identity

**Daniela Reyes, the Mechanic**, is the Core investigator and she is as Guardian as it gets. She has a 5 combat stat, 9 health, 5 sanity — a stat line built for close combat. Her ability triggers when an enemy attacks an investigator at her location, letting her fight back as a free action. Her signature weapon, **Daniela's Wrench**, actually provokes enemy attacks deliberately: exhaust it to make an enemy engage and immediately attack you, then your ability fires and you hit back at +2 combat and +1 damage if that enemy attacked you this round. This is as literal an implementation of "Tank and Retaliate" as it gets. Her signature weakness, **In Harm's Way**, even turns her damage-dealing into a double-edged sword, dealing 1 damage to herself every time she hurts an enemy. Staying in the fight is itself a resource management problem.

The core Guardian card pool fills out the class promise across three pillars:

{{< figure src="https://cdn.jsdelivr.net/gh/iskander/arkham-tabularium-assets@main/arkham-lcg/articles/c2-guardian/Vicious%20Blow.jpg"
    alt="Vicious Blow — emblematic Guardian combat card"
    float="left"
    width="300" >}}

**Combat output.** The weapons are solid. **Machete** (3 resources, +1 combat, +1 damage when fighting alone) is the go-to melee option that rewards good enemy management. **M1911** (3 resources, 4 ammo, +1/+1) is the baseline Firearm and sets an efficient standard. **Vicious Blow** is the skill that defines Guardian as a burst damage class — on a successful attack it deals +1 damage, turning a base 2-damage attack into 3, which solves a huge number of enemy thresholds without wasting actions. **Counterattack (1xp)** is a natural enabler of the Tank identity: fast, cancels an attack, and deals 1 damage. Against attacks of opportunity it's even better, effectively making you immune to counterattack penalties while punishing the enemy. The high-end weapons — **Sledgehammer (3xp)** and **Winchester Model 12 (5xp)** — give the Weapons Expert somewhere to go, though the Sledgehammer has serious action-economy problems with its two-action full swing, and the Winchester's friendly-fire clause on failed shots is a meaningful risk to manage.

**Damage absorption.** **Resilience** (3 resources, 2/2 soak Talent) and **Bodyguard (level 0)** (3 resources, 2/1 ally that can absorb damage for teammates) are the core soak pieces. **Endurance** (2 resources, pay 1 resource for +1 combat or agility, +2 on attacks/evasion) adds a flexible buffer. The level 2 **Bodyguard** upgrade bumps soak to 3/2 and the defeat trigger to 2 damage, making it a needed improvement. The level 0 version is one of the weakest cards in the class — it's genuinely hard to realize full value from 2/1 soak alongside the defeat trigger, and the ally slot is very contested.

**Incidental clue gathering.** The Core gives the Guardian a thin but interesting investigative thread. **Scene of the Crime** (2 resources, first-action event) gives 1 clue normally, or 2 clues if there's an enemy present — which for a Guardian is almost always the case. That makes it an efficient clue event in practice, and doesn't provoke attacks of opportunity. **Lesson Learned** (1 resource, fast event) triggers after an enemy attacks you to discover a clue. **Right Tool for the Job** (1 resource) tutors for a Tool or Weapon, giving the class some consistency against its hard dependency on drawing weapons early.

## Expanding the Guardian Class

**Tommy Muldoon, the Officer** is the Evergreen Guardian investigator, and his deck takes the class in a noticeably different direction. Tommy has 4 combat, 3 willpower and intellect, 2 agility — flatter but more flexible than Daniela. His ability lets him spend 1 resource (or discard a Firearm he controls) to play a Firearm from hand with 2 bonus ammo. His elder sign places ammo on an asset with uses. Tommy is built around the Firearm ecosystem, not the Tank/Retaliate loop.

The Evergreen deck introduces two new Guardian threads:

{{< figure src="https://cdn.jsdelivr.net/gh/iskander/arkham-tabularium-assets@main/arkham-lcg/articles/c2-guardian/On%20the%20Beat.jpg"
    alt="On the Beat — signature Police-themed Guardian card"
    float="left"
    width="300" >}}

**The Police theme.** Tommy and his deck are heavily Police-coded. **Rookie Cop** soaks and gives a clue on defeat. **Police Dog** is a flexible ally that boosts either attack or investigate skill tests by 1 during attacks or investigations at your location — the level 1 version bumps this to +2, which is genuinely strong given how broadly it applies. **Detective Sherman (3xp)** is a powerhouse ally: +1 combat, absorbs damage from teammates, and exhausts to discover a clue whenever damage is placed on him — meaning he rewards taking hits and then produces investigation value on his way out. **On the Beat (1xp)** is a fast Police Tactic that gives +3 intellect for the rest of your turn, making a 4-intellect Guardian suddenly capable of actually solving locations. **Protective Vest (level 0)** adds an extra hand slot usable only for Firearms and tutors a Firearm or Upgrade on entry — pure setup for a gun-heavy build, with its level 4 upgrade bundling offense, defense, and tutoring into a single card.

**The Firearms ecosystem.** Tommy's deck makes Firearms a real archetype rather than just "pick a weapon." **Service Revolver** works on attacks of opportunity, generating tempo even outside your turn. **Thompson Submachine Gun (4xp)** brings 6 ammo, dispatches normal enemies efficiently, and can spike boss damage with its two-shot sequence. **Stock Ammo Reload (2xp)** places 5 ammo distributed among Firearms you control for just 2 resources — this makes the entire Firearm economy sustainable. **Extended Barrel (1xp)** is a cheap attachment that gives +1 to attacks with its host Firearm: buy it once, keep it forever.

Healing also shows up more explicitly. **Physical Fitness (level 2)** drops to 1 resource, which immediately makes it a good deal — 3 damage healed for 1 resource and a card is solid economy for a class that soaks constantly.

## Class Archetype Breakdown

**Melee Fighter** is reliable at level 0. Machete and Vicious Blow form a clean pairing: the Machete's +1 damage condition rewards clearing threats efficiently, and Vicious Blow turns a normal attack into a reliable 3-damage hit. Counterattack slots naturally here. The gap is at higher XP investment — Sledgehammer (3xp) is awkward. Its full swing needs two actions for a repeatable 2-damage baseline, and the +2 damage bonus requires both success and an exhaust. For a two-handed 3xp card that's a lot of conditions. The Melee Fighter ends up solid at level 0 and a bit stuck on its upgrade path.

{{< figure src="https://cdn.jsdelivr.net/gh/iskander/arkham-tabularium-assets@main/arkham-lcg/articles/c2-guardian/Stock%20Ammo%20Reload.jpg"
    alt="Stock Ammo Reload — sustainability card for the Firearms archetype"
    float="left"
    width="300" >}}

**Weapons Expert (Firearms)** is the best-supported archetype in the combined pool, and it's not particularly close. The Firearm assortment from M1911 to Service Revolver to Thompson SMG is cohesive. Stock Ammo Reload makes ammo sustainable, Extended Barrel is a cheap perpetual upgrade, and Protective Vest handles setup and hand management. Tommy's investigator ability directly enables this by letting you replay Firearms with bonus ammo. The Winchester Model 12 (5xp) is the high-end boss-killer option. The main friction is cost: Firearms are expensive to play and reload, and Guardians don't naturally generate resources well. **Bounty** addresses this better than anything in Core does, but the early game can still be tight before you find it.

**Enemy Tank** is implemented in a more limited manner. Daniela does it very well, with her access to Aleksey Saburov, and the retaliate loop is coherent for her specifically. A future non-Daniela Guardian that actually functions as a team Tank will probably require an expansion beyond the evergreen pool. The pieces are there, with Counterattack and Detective Sherman that soaks for the team. But the retaliate payoffs are thin and most of the Tank work operates in Daniela's signature card combination. The archetype is functional but currently investigator-locked.

**Medic** is the least realized archetype relative to the class description. Physical Fitness at level 2 is ok but doesn't help team members. Resilience and Bodyguard soak but heal nothing. There is no Guardian card in either the Core or Evergreen pool that reads as a dedicated healing tool the way Mystic or Seeker horror-heals do. The "Medic" label in the class description appears to mean "I have soak assets so teammates take fewer hits" — which is legitimate team support, but it's not a Medic playstyle in any actionable deck-building sense. If it ever becomes a thing in Guardian, it will be transient in the Current pool.

## Implicit Archetypes and Traits

Looking at the full card pool, a few patterns emerge that the manual Guardian description glosses over entirely.

**Police as a distinct subtheme.** The Evergreen Deck introduces a full Police flavor that is not mentioned, but will always color the Current environment. Police Dog, Rookie Cop, Protective Vest (tagged Armor, Police), On the Beat (Tactic, Police), Detective Sherman (Ally, Detective, Police) — these form a coherent identity around law enforcement aesthetics, tactical investigation, and enemy control. This isn't just flavor text: On the Beat giving +3 to investigate and parley gives a real mechanical identity to the Guardian class. The Police subtheme sketches a fifth playstyle that could be further developed in Chapter 2.

**Investigation through enemy presence.** Across both products, a specific pattern repeats: Guardian cards reward you for being near enemies with investigation benefits. Scene of the Crime gives 2 clues if an enemy is present. Lesson Learned fires after an enemy attacks. Detective Sherman discovers a clue when absorbing damage. On the Beat turns a round with enemy pressure into a high-intellect investigation window. This is a coherent and consistent design thread — the Guardian doesn't avoid enemies to investigate; she investigates because enemies are there. That's a real mechanical identity that deserves to be articulated in the class description and currently isn't.

**Firearm crafting.** The Firearm trait drives a meaningful sub-economy of upgrades, ammo management, and synergy. Extended Barrel, Custom Grip, Stock Ammo Reload, and Iron Sights all interact with the Firearm trait specifically. Protective Vest tutors for Firearms and Upgrades. Tommy's ability gates on Firearms. These firearm customization capabilities expand the class description's "Weapons Expert" playstyle in a way that it only hints at under the vague header of "Heavy Weaponry."

**Economy as a structural class weakness.** This one is a continuation from Chapter 1. Weaknesses are not really addressed in the class description in the manual, which makes sense, but are as much part of the class identity as their strengths, as they impact how every archetype functions. Guardians pay a lot for their gear: M1911 (3), Machete (3), Logan Hastings (4), Bodyguard (3), Thompson (6). The Core only offers Logan Hastings' kill trigger and Emergency Cache for income. Bounty from the Evergreen deck is probably the most important quality-of-life addition the class receives in Chapter 2. The class description talks about "Building an Arsenal"; that will always hinge on the tension of accumulating enough resources.

## Guardian in Chapter 2

The manual defines Guardian identity as combat-first, team-protective, arsenal-building. For the most part, the evergreen pool delivers on that promise. The Firearms Expert archetype has the best-developed mechanical ecosystem in the class, with a clean ladder from cheap sidearms through ammo management to high-end shotguns and machine guns. On the other hand the Tank archetype is real but Daniela-dependent. The Medic archetype is the one that went by the wayside, to be picked up by Seeker and Mystic, it seems.

The Evergreen deck is where the class story gets more interesting. Tommy Muldoon's Police-flavored deck adds a compelling investigation capability that gives more versatility to what the core hinted at as a one-dimensional bruiser class. The Guardian can now flex into clue gathering in a way that feels integrated — Scene of the Crime, On the Beat, Detective Sherman, and Stakeout all pull in the same direction.

It will be interesting to see how the incoming expansions further develop the class. Will there be some real Medic healing support that goes beyond soak? Will more "Strong Allies" be a recurring feature of the class?

---

{{< center >}}
[Introduction]({{< ref "arkham-lcg/articles/c2-introduction" >}}) | [Guardian]({{< ref "arkham-lcg/articles/c2-guardian" >}}) | [Seeker]({{< ref "arkham-lcg/articles/c2-seeker" >}}) | [Rogue]({{< ref "arkham-lcg/articles/c2-rogue" >}}) | [Mystic]({{< ref "arkham-lcg/articles/c2-mystic" >}}) | [Survivor]({{< ref "arkham-lcg/articles/c2-survivor" >}}) | Conclusion
{{< /center >}}
