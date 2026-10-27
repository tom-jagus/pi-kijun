---
id: B007
status: Review
---

# Independent content review

## Outcome

Let the main agent obtain an independent review of documentation and work items,
resolve findings through a bounded exchange, and explain the outcome to the user
without manual copying between sessions.

## Why

Independent review currently requires opening another session and copying
findings and responses between sessions. Automating that exchange should preserve
fresh review context while reducing the user's coordination work, especially
when reviewing draft briefs and slices before implementation.

## Boundaries

Use one reusable `content-review` skill, one read-only `content-reviewer` agent,
and a suitable existing subagent extension. The skill must also work in an
ordinary session without that extension. Keep content review distinct from the
existing `review` skill's assessment of delivery against acceptance criteria.

Allow at most three reviewer invocations per user review request, including the
initial review. Stop earlier when findings are resolved or another invocation
would add nothing. Start each invocation with fresh context; supply previous
findings and responses explicitly for follow-up rather than requiring persistent
reviewer sessions. Do not pass the author's full conversation by default.

Review does not authorize revisions, acceptance, work-record updates, plugin
installation, or Git mutations. Preserve existing authority boundaries. Exclude
automatic review of every response, multiple specialist reviewers, autonomous
revision loops, and general-purpose orchestration.

## Acceptance criteria

- The user can request an independent review of ordinary documentation or work
  items, including draft briefs and slices, without copying messages between
  sessions.
- Review assesses factual support, internal consistency, missing information,
  and readability for the intended audience. It distinguishes material defects
  from optional editorial preferences and reports uncertainty honestly.
- A reader can understand the document's purpose, terminology, decisions, and
  instructions using the document and clearly linked project material, without
  searching external sources for essential definitions or explanations. Review
  flags unnecessary cross-referencing when a short local explanation would help.
  External evidence may still be needed to verify factual claims.
- Draft work-item review checks outcomes, boundaries, assumptions, dependencies,
  and testable acceptance criteria against relevant project decisions. It does
  not treat explicit open questions as automatic defects or proposals as accepted
  decisions.
- The main agent can clarify or challenge findings with evidence through at most
  three reviewer invocations. It seeks justified conclusions rather than forced
  agreement and returns unresolved scope, preference, or authority decisions to
  the user.
- The final report identifies the review scope, invocation count, material
  findings, accepted and rejected findings with reasons, unresolved questions,
  and whether files changed. The user need not supervise each exchange.
- The reviewer cannot mutate project files through its available tools. Review
  findings do not grant the main agent additional editing or acceptance authority.
- The review guidance remains usable in a normal session without the extension.

## Review

Moved to Review at the user's request. S009 is accepted. The combined outcome
still needs verification against this brief's acceptance criteria, including
runtime evidence from S010. This status does not record acceptance.
