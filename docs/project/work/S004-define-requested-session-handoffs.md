---
id: S004
status: To do
parent: B003
---

# Define requested session handoffs

## Outcome

Recommend a minimal requested-handoff approach for pending implementation,
including where it lives and how a fresh session finds and verifies it.

## Acceptance criteria

- The recommendation covers work with an existing item and small requests
  without items. It compares using existing record sections, a lightweight
  repository handoff document, and conversation-only handoffs against B003's
  durable recovery goal.
- A proposed destination and discovery path are identified for each case,
  without requiring a brief and slice for every small request or silently
  creating another progress-tracking system.
- Minimum handoff content identifies the pending result and affected paths,
  completed and missing verification, unresolved issues, acceptance state,
  and next decision. Existing information is linked rather than duplicated
  where practical.
- The recommendation defines how a requested handoff replaces stale content
  and what should happen after acceptance or abandonment. Removal of useful
  unaccepted information is not assumed to be automatically authorized.
- The resume approach checks the handoff against current files and Git state,
  distinguishes recorded evidence from newly verified facts, and does not
  treat previous-session edit approval as a current-session grant.
- Illustrative handoffs for an existing item and an untracked small change
  show that pending work is not marked Done or represented as accepted.
- The result identifies affected guidance and remaining decisions without
  changing the contract, skills, or workflow guide. The recommendation is
  presented for user selection before dependent delivery slices are finalized.

## Tasks

- [ ] Inspect development, review, project-context, and work-items guidance for
  existing interim-recording and recovery mechanisms.
- [ ] Compare handoff locations and recommend the least additional structure
  that meets the recovery goal.
- [ ] Draft minimal illustrative handoffs and check them against stale files,
  missing verification, pending acceptance, and expired session approval.
- [ ] Present the recommendation and consequential choices in the conversation;
  record findings in the slice only after acceptance or an explicit request
  for interim recording.
