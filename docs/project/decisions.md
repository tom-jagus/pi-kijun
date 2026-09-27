---
title: Pi Kijun Project Decisions
status: historical-draft
updated_at: 2026-09-21
---

# Historical Decision Draft

This register records the earlier Kijun concept. It is retained temporarily for
review, **not as active authority**: the current project proposal is in
`definition.md`. In particular, DEC-004 and DEC-005 describe a read-only,
transaction-first approach that no longer reflects the agreed direction. Carry
forward only useful rationale, then retire this file after user review.

## DEC-001 — Dedicated Pi Kijun Configuration Repository

- **Date:** 2026-09-21
- **Status:** accepted
- **Decision:** Maintain Pi Kijun as its own personal, version-controlled
  repository at `~/dev/personal/pi-kijun`.
- **Rationale:** The workflow is a substantial independent configuration and
  transaction system. It needs focused documentation, tests, and controlled
  evolution without being coupled to OpenCode Mentor or deployment tooling.
- **Consequences:** Pi Kijun is not initially an npm package, marketplace
  plugin, or replacement agent harness. Deployment/linkage into Pi will be
  determined later.

## DEC-002 — Pi Is the Base Harness

- **Date:** 2026-09-21
- **Status:** accepted
- **Decision:** Build Pi Kijun on Pi rather than migrate to Oh My Pi.
- **Rationale:** Pi's minimal default tool surface and extension model better
  fit a controlled, explicit workflow. Oh My Pi provides useful ideas, but its
  broad batteries-included defaults conflict with Kijun's minimal-authority
  approach.
- **Consequences:** Concepts such as hash-anchored edits, bounded tool output,
  and effective compaction may be adapted when justified, but Pi Kijun must not
  inherit broad autonomous mutation, subagent, or tool surfaces by default.

## DEC-003 — Concise Three-Artifact Project Context

- **Date:** 2026-09-21
- **Status:** accepted
- **Decision:** Use `definition.md`, `progress.md`, and `decisions.md` as
  separate authoritative project artifacts.
- **Rationale:** Stable scope, current operational state, and durable decisions
  change at different rates. Combining them encourages stale context and
  implementation-diary documentation.
- **Consequences:** Documentation records only information that would materially
  improve a future decision or safe continuation. Routine implementation detail
  remains in code, tests, Git history, and issue tracking.

## DEC-004 — Read-Only Default and Minimal Authority

- **Date:** 2026-09-21
- **Status:** accepted
- **Decision:** Pi Kijun defaults to a small read-only tool surface. Generic
  file writes, edits, and unrestricted shell mutation are disabled or blocked.
- **Rationale:** Broad tools make it too easy for an agent to perform changes
  outside the intended review process. A smaller surface is easier to reason
  about and audit.
- **Consequences:** Pi Kijun adds a purpose-specific capability only when Pi's
  existing read-only tools cannot meet a defined need. This in-process policy is
  not an operating-system security boundary against trusted extension code or
  malicious local configuration.

## DEC-005 — Hash-Anchored Preview/Apply Change Transactions

- **Date:** 2026-09-21
- **Status:** accepted
- **Decision:** Allowed file mutations use immutable Preview/Apply transactions
  bound initially to a whole-file SHA-256 freshness hash.
- **Rationale:** A reviewed diff alone does not prevent an older proposal from
  overwriting intervening changes. Whole-file hashing is simple, auditable, and
  fails closed.
- **Consequences:** Every permitted change must use exact preview content,
  explicit human approval, final UI confirmation, policy and hash revalidation,
  atomic application, and single-use proposal state. Block-level anchors are
  deferred until whole-file invalidation proves materially disruptive.

## DEC-006 — Direct Reasoning and Bounded Delegation

- **Date:** 2026-09-21
- **Status:** accepted
- **Decision:** The main Pi conversation handles normal reasoning directly.
  Subagents are not the default routing or execution mechanism.
- **Rationale:** A cheap dispatcher followed by execution subagents duplicates
  context, fragments continuity, increases token use, and broadens the policy
  surface.
- **Consequences:** Delegation may later be used for narrowly scoped,
  independent, preferably read-only investigations or reviews with explicit
  input and output contracts. It must not become an implicit replacement for the
  main workflow.

## DEC-007 — Transparent Cost-Aware Model Escalation

- **Date:** 2026-09-21
- **Status:** accepted
- **Decision:** Use a cost-aware model and reasoning ladder: Luna is the normal
  route; Terra and Sol are escalation routes; Astra is reserved for rare,
  bounded independent audits.
- **Rationale:** The OpenAI subscription model catalogue indicates materially
  different relative costs. Routine work should not consume the highest-cost
  capability, while policy and architecture work need stronger reasoning when
  the cost of a mistake is high.
- **Consequences:** Start routine supervised work with Luna at low or medium
  reasoning. Escalate based on risk, uncertainty, breadth, failed focused
  attempts, or independent-review need—not merely prompt length. Exact model
  ordering and reasoning presets remain operational policy and must be validated
  against representative Pi Kijun tasks before automation is enabled.

## DEC-008 — Deterministic, Visible Model Routing

- **Date:** 2026-09-21
- **Status:** accepted
- **Decision:** Future model routing should use deterministic local rules and
  visible presets or recommendations rather than an LLM router.
- **Rationale:** A routing subagent adds calls, latency, context duplication,
  and a new source of incorrect judgment. Silent automatic switching is hard to
  understand and can defeat prompt-cache efficiency.
- **Consequences:** Routing may later use workflow, explicit commands, task
  boundaries, risk indicators, and observed failures. Manual selection always
  wins. Automatic Astra selection is prohibited; it may only be recommended and
  explicitly approved.

## DEC-009 — Pi Kijun Identity and Startup Header

- **Date:** 2026-09-21
- **Status:** accepted
- **Decision:** Use **Pi Kijun** as the project name and `π 基準` as its visual
  mark. Plan a custom Pi startup header with a large terminal-art rendering on
  process startup and a compact fallback for later sessions or narrow terminals.
- **Rationale:** `kijun` means standard or criterion, expressing the project's
  emphasis on deliberate standards for AI-assisted development. A distinct but
  compact visual identity supports orientation without changing agent behavior.
- **Consequences:** The final terminal-art asset is deferred until a suitable
  high-contrast source image and responsive rendering are prepared. Pi Kijun
  should be described as an unofficial personal workflow/configuration for Pi,
  not an upstream-affiliated product.
