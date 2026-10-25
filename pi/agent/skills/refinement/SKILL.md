---
name: refinement
description: Turn a selected brief or bounded request into small reviewable slices, acceptance criteria, and task checklists. Use to prepare work for implementation or refine follow-up after review. Does not implement work or silently redefine accepted outcomes.
---

# Refinement

Prepare only the selected work for delivery. Follow the global operating
contract and load `work-items` for shared record and lifecycle rules.
Refinement does not grant source-edit, worker-launch, or Git authority.

## Read and bound the work

Read the charter, selected brief or standalone request, relevant slices, and
repository evidence needed to judge feasibility. Check existing work before
creating more. Resolve only questions that affect the selected outcome; send
a genuine change of project purpose or brief outcome to `brainstorming`.

An accepted outcome may still have implementation uncertainty. If uncertainty
prevents a delivery slice from starting, propose a bounded discovery slice
whose acceptance criteria are evidence and a recommendation. Do not disguise
an unresolved product decision as an implementation task.

## Produce a few useful slices

- Define small outcomes that can be inspected or demonstrated independently.
  Prefer end-to-end results over component-only tasks where practical.
- Write observable acceptance criteria, including relevant error cases and
  boundaries. Preserve the brief's intent; do not weaken criteria to fit an
  easy implementation.
- Add only useful implementation tasks inside each slice. The checklist is a
  provisional plan, not a promise to know every step in advance.
- Identify real dependencies, blockers, and shared interfaces. Separate
  independent slices from work that must be sequenced. Do not assume that
  separate files make two changes compatible for concurrent development.
- Leave unresolved or unaccepted slices Draft. Move them to To do only when
  their outcome and criteria have been accepted under the shared rules.

Do not decompose the whole project by default or invent briefs for small
standalone changes. Do not create milestones, detailed design documents,
estimates, new work-item types, or a separate plan file unless the selected
work actually requires and authorizes them.

## Handoff

Update only the affected brief, slices, and index when record maintenance is
requested. Record conclusions and blockers, not the refinement discussion.
After an unsuccessful brief review, add or revise the remaining slices without
reopening correctly completed ones. A request for refinement does not grant
acceptance of changed goals or automatic permission to start development.

End with what is To do, what remains Draft or blocked, and the next useful
slice. If implementation is also requested, name the transition and load
`development`; otherwise stop before source changes or worker assignment.
