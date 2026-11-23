---
id: 1
title: "yt-* scoring tools (hookscore.py, title.py) are English-calibrated and misfire on Vietnamese text"
status: open
type: open-source
skill: [yt-script, yt-package, yt-shorts, yt-audit]
proposes_skill: []
target_file: []
siblings_checked: "no skill-families.md registry; yt-* pack checked by tool use — yt-script/yt-package own the tools, yt-shorts and yt-audit call hookscore.py/title.py (added); yt-viral uses hooks.json formula matching (assumed affected, not added until tested); yt-edit/chapters/retention parse timings only (excluded, SKILL.md tool sections)"
area: "hookscore.py ADDRESS/CURIOSITY heuristics; title.py duplicate check"
date: 2026-11-23
session_context: "Installing and smoke-testing youtube-agent-skill for a Vietnamese-language creator"
parked_until:
resolved:
resolution:
reference:
commands_verified: "run — hookscore.py --hook on a Vietnamese hook gave ADDRESS 26 'say you in the first six words' (English-only); title.py flagged duplicate on single letters l, n, v from a Vietnamese title/thumb pair"
next_actor:
use_evidence:
escalated:
---

**Issue:** On a Vietnamese hook and title, hookscore.py told the user to "say 'you'" (English pronoun list), and title.py reported the thumbnail repeating the title "on l, n, v", because its tokenizer splits accented Vietnamese words into stray ASCII letters. The scores look authoritative, but on non-English input they are noise, and the SKILL.md files say "Do not eyeball the hook" with no warning about language.

**Suggested improvement:** In yt-script and yt-package (sections that call the tools), add a language check: for non-English scripts, show the panel only as a rough guide, name the English-only properties (ADDRESS, the formula match), and judge duplication by hand. A local fork could make the tokenizer Unicode-aware (`re.findall(r'\w+', s, re.UNICODE)`) and add a pronoun list per language.

**Principle:** A heuristic scorer packaged with a skill carries the language of its calibration set. When the input is in another language, the skill must say so before presenting the score, or the score's apparent precision misleads.
