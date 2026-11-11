---
id: S008
status: Done
parent: B006
---

# Consolidate repeated authority and acceptance guidance

## Outcome

Remove redundant policy detail across the contract, skills, and workflow guide
while preserving the rules and enough local context for each activity.

## Acceptance criteria

- Governing authority rules remain in the global contract. Skills retain their
  activity-specific consequences and essential stopping points, and the guide
  explains the workflow to the user without becoming a competing rule source.
- Removed passages are identified with the retained rule or reference that
  preserves their meaning. Repetition deliberately retained for local clarity
  is explained in the review handoff, not a new permanent policy inventory.
- Manual-first proposals, explicit behaviour-file edit approval, grant scope
  and expiry, acceptance authority, and separately requested Git mutations
  retain their existing meaning and exceptions.
- Documentation and record timing remain consistent, including direct requests,
  explicit interim recording, updates after acceptance, and the distinction
  between recorded status and actual delivery evidence.
- Activity handoffs, delegated acceptance, worker permissions, and default-branch
  Git restrictions retain their meaning. Existing rules are not weakened or
  expanded merely to make passages shorter.
- Each affected activity remains understandable with the global contract and
  references it explicitly requires. Essential instructions are not moved into
  unrelated skills or hidden behind an unclear loading requirement.
- A comparison of representative manual-first, approved-edit, pending-review,
  interim-recording, delegated-review, and Git requests finds no intended
  behaviour change. Checks assess written consistency, not model guarantees.
- Changes are limited to duplicated authority and acceptance guidance. They
  do not reintroduce removed vault support, decide unresolved handoff policy,
  add a policy framework, or impose a formal behavioural test suite.

## Tasks

- [x] Read current guidance and applicable accepted work before editing; identify
  candidate duplication and confirm authority for behaviour-file changes.
- [ ] Map candidate removals to the governing rule and activity-specific meaning
  that must remain. Leave ambiguity or a policy conflict for user decision
  rather than silently resolving it as wording cleanup.
- [ ] Consolidate only passages with a clear retained source, preserving useful
  local reminders and explicit reference-loading instructions.
- [ ] Compare before and after guidance using the representative requests and
  report material removals, retained repetition, and any unresolved concerns.
- [ ] Check links, prose wrapping, and diff whitespace, then present changes for
  acceptance before aligning the guide and recording completion.

## Risks

The handoff work in S005 and vault removal in S007 touch overlapping guidance.
Coordinate those edits rather than implementing them concurrently in the same
files. Recheck current accepted rules at delivery time; this cleanup must not
undo their results. No completion dependency is required merely for file overlap.

## Review

Accepted under the user's explicit delegation after correcting the grant-scope
finding. The contract now requires session grants to cover the current project
and work and requires clarification when grant scope or status is unclear.
The corrected text was reread before acceptance.

The preceding written review covered manual-first, approved-edit, pending-review,
interim-recording, delegated-acceptance, and Git paths. Governing rules remain in
the contract; skills retain activity-specific procedures and stopping points.
The grant-scope correction resolves the identified preservation gap.

The combined commit also contains separately authorized changes, including
opt-in validation and readable item names. Those are distinct scope decisions,
not unintended changes attributed to consolidation. The review does not claim
runtime model compliance. No new tests or validation commands were run.
