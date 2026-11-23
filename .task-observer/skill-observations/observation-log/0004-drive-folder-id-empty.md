---
id: 4
title: "dung-video-clip pins a Drive folder id that returns no files from this session's Drive connector"
status: open
type: internal
skill: [dung-video-clip]
proposes_skill: []
target_file: []
siblings_checked: "no skill-families.md registry; kich-ban-tap-quan-an may reference the same Drive toolkit (assumed, not read) — not added until checked"
area: "Section 3, Bo cong cu tren Google Drive — folder id lookup"
date: 2026-11-23
session_context: "Checking toolkit access before starting a first video for a new US English channel"
parked_until:
resolved:
resolution:
reference:
commands_verified: "run — search_files parentId = the pinned folder id returned {}; title contains 'Bo cong cu dung video' found only bo-cong-cu-dung-video.zip (2026-11-13) under a different parent; title contains 'kich-ban-giu-chan' returned nothing"
next_actor:
use_evidence:
escalated:
---

**Issue:** The skill tells the agent to find every toolkit file with `parentId = '<pinned id>'`. From this cloud session's Drive connector that query returned an empty result. A title search found an older zip and README dated 13/11 under another parent, while the skill body cites rules from 14/11 (shotcraft code runner) that a 13/11 bundle cannot contain. An agent following the skill literally gets "no files" and could not tell a wrong or unshared folder id from an empty folder.

**Suggested improvement:** In section 3, add a probe step: if the parentId query is empty, search by a known file title (`00-README`) and compare the parent and modified date against the newest rule date in the skill. If they don't match, stop and ask for the current zip, as the "Khong vao duoc Drive" line already says. Also record the folder id together with which Google account owns it, so a connector bound to another account is recognised.

**Principle:** A skill that pins an external resource by id needs a fallback lookup by content, and a freshness check against the skill's own dates. An empty result from an id lookup is evidence about the lookup, not about the folder.
