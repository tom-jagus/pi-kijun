---
id: B007
status: Done
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
initial review and resumed turns. Stop earlier when findings are resolved or
another invocation would add nothing. Start the initial review with fresh
context and resume an eligible saved reviewer session for follow-up within the
same review. Start a fresh session for a separate review or an explicitly
requested assessment without prior discussion. If resume is unavailable, report
the limitation and supply previous findings and relevant context to any fresh
fallback. A fresh session does not reset the same review's invocation count.
Do not pass the author's full conversation or a persuasive defense of the draft.

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

S009 is accepted. The user approved fresh initial reviews with resumed
follow-ups, replacing the earlier fresh-context requirement for every turn.
Initial file-based reviews returned findings without manual copying. A synthetic
README test detected planted defects; a resumed clarification retained a valid
finding, narrowed another to missing reader guidance, and withdrew an
audience-dependent finding. The exchange stopped after two turns. Independent
content review found no material findings in the modified integration guidance.

The user accepted the implementation after extended practical use and chose
to close this brief and S010. Unresolved disagreement at the invocation limit,
failed or cancelled review handling, and a complete effective-tool audit remain
unverified. Acceptance does not turn those missing checks into verified results.
