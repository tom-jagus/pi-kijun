---
id: B003
status: To do
---

# Unfinished-session recovery

## Outcome

Allow a fresh session to recover a pending implementation and its next decision
when the previous session ended before acceptance.

## Why

Implementation-related records normally wait for acceptance. Files and diffs can
show changes, but may not explain what was verified, what remains uncertain, or
which result awaits acceptance. Recovery should not require reconstructing the
previous conversation.

## Boundaries

Explore a lightweight, user-requested handoff under the existing permission to
record interim findings. Prefer existing records where appropriate. Preserve
the acceptance boundary and do not introduce automatic interim writes, a
parallel progress diary, or a mandatory end-of-session ritual. Do not reopen
accepted B001 or S001.

## Acceptance criteria

- On an explicit handoff request, pending work can be captured with enough
  context to identify the result, relevant verification, unresolved issues,
  and next decision.
- A fresh session can distinguish recorded findings from facts it must verify
  against current files and Git state.
- The handoff does not imply acceptance, advance work to Done, or grant source
  or Git authority.
- Guidance covers work with existing items and small requests without items,
  without requiring a brief and slice for every request.
- The result remains concise and does not accumulate routine activity logs.

## Open questions

- Where should a requested handoff live when no work item exists?
- What minimum information is needed to resume reliably without duplicating
  the implementation or existing records?
