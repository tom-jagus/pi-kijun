---
id: S005
status: To do
parent: B003
depends_on:
  - S004
blocked_by: Handoff approach awaits discovery and user selection.
---

# Support requested session handoffs

## Outcome

Make the handoff approach selected through S004 usable for capturing pending
implementation on request and recovering it in a fresh session.

## Acceptance criteria

- Guidance supports an explicitly requested handoff for both existing work
  items and small changes without items, using the selected destinations and
  discovery paths without requiring new briefs and slices for small requests.
- A handoff identifies the pending result and affected paths, completed and
  missing verification, unresolved issues, acceptance state, and next decision
  without duplicating existing records unnecessarily.
- Resume guidance locates the handoff, checks it against current files and Git
  state, and distinguishes recorded evidence from newly verified facts.
- Requested handoffs can replace stale content and be resolved after acceptance
  or abandonment according to the selected approach, without accumulating a
  progress diary or silently discarding useful pending information.
- Handoff creation is not automatic. Capturing or reading a handoff does not
  imply acceptance, mark pending work Done, authorize Git mutations, or carry
  a previous session's edit grant into the current session.
- A walkthrough for an existing item and one for a small untracked change show
  capture and fresh-session recovery, including stale files or missing checks.
  These checks assess guidance consistency, not guaranteed model compliance.
- Affected skills, references, and the workflow guide agree on the selected
  approach without introducing a separate activity or mandatory session ritual.

## Tasks

- [ ] Read the accepted S004 recommendation and confirm these criteria and
  boundaries with the user; revise only where the selected approach requires.
- [ ] Identify affected behaviour files and ordinary documentation, and confirm
  applicable edit authority before changing behaviour files.
- [ ] Update the relevant guidance and any necessary references to support
  requested capture, discovery, verification, and handoff resolution.
- [ ] Walk through both tracked and untracked cases, checking acceptance and
  session-approval boundaries as well as recovery of verification gaps.
- [ ] Check links, prose wrapping, and diff whitespace, then present the result
  for acceptance before recording completion.

## Open questions

- Which handoff destinations, discovery paths, and resolution rules will the
  user select from S004's recommendation?
