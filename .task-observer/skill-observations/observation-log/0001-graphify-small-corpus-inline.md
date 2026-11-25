---
id: 1
title: "graphify bootstrap gives no rule for small corpora already read, while upstream skill.md mandates subagents"
status: open
type: open-source
skill: [graphify]
proposes_skill: []
target_file: []
siblings_checked: "none — no skill-families.md registry exists; no other graph-building skill installed"
area: "Bước 2 (Đọc hướng dẫn gốc) — semantic extraction Part B"
date: 2026-11-25
session_context: "graphify run over 8 uploaded handoff markdown files (~500 lines) that were already fully in context"
parked_until:
resolved:
resolution:
reference:
commands_verified: none
next_actor:
use_evidence:
escalated:
---

**Issue:** Upstream graphify skill.md says semantic extraction MUST dispatch general-purpose subagents (one per 20–25 files). The bootstrap skill only covers the case where no subagent tool exists. Here the corpus was 8 short docs already read in full, so a subagent would re-read everything at extra cost, and the harness discourages spawning agents unasked. The agent extracted inline as one chunk and skipped the SPEC_PATH semantic-cache step; nothing in either skill sanctioned that.

**Suggested improvement:** In Bước 2 of the bootstrap skill add: "If the non-code corpus fits one chunk (≤25 files, ≤~6000 lines) and is already in context, extract it inline into graphify-out/.graphify_chunk_01.json with the extraction-spec schema (coverage included), then continue at Step B3.5/Part C; say so in the summary." Also state whether the cache step may be skipped for a one-off scratch build.

**Principle:** A wrapper skill around a tool's own instructions must resolve the cases where the wrapped instructions conflict with the host's cost or delegation rules, not only the case where a capability is missing.
