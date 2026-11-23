---
id: 3
title: "Runtime estimate in a script deliverable was written before counting words, and was off by 70 percent"
status: open
type: open-source
skill: [yt-script]
proposes_skill: []
target_file: []
siblings_checked: "no skill-families.md registry; only yt-script asks for a runtime estimate (yt-plan sizes hours, excluded, SKILL.md What to hand back) — instance-specific to yt-script"
area: "yt-script What to hand back, runtime estimate at 150 wpm"
date: 2026-11-23
session_context: "First-video script for a new space explainer channel"
parked_until:
resolved:
resolution: 
reference:
commands_verified: "run — per-beat word count found 1057 spoken words (7.0 min) against a written claim of about 1750 words / 12 min; title number and timestamps corrected"
next_actor:
use_evidence:
escalated:
---

**Issue:** The script was written with planned beat timestamps (0:00 to 12:00) and a stated "about 1,750 words, 12 minutes". A count done afterwards found 1,057 spoken words, about 7 minutes. The title carried the number ("in 12 Minutes") too, so the error reached the packaging, and title.py had already approved it. The skill asks for a runtime estimate but ships no tool for it, unlike its other numeric checks.

**Suggested improvement:** In yt-script "What to hand back", require the runtime and beat timestamps to be computed from a word count of the spoken lines, excluding the ON SCREEN notes, never planned up front. Ship a small `runtime.py` beside hookscore.py that prints cumulative timestamps per beat, and have yt-package check that a minutes figure in a title matches it.

**Principle:** Any number a deliverable states about itself (length, count, duration) is measured from the finished artefact, not carried over from the plan, especially when that number is repeated in a second artefact that is checked separately.
