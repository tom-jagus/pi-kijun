---
name: development
description: Implement or debug source code, tests, scripts, configuration, and other implementation files. Use for a selected slice or bounded source request, including manual-first proposals and explicitly authorized edits. Use review for acceptance assessment; development does not accept its own delivery.
---

# Development

Help the user understand and implement one coherent change at a time. Follow the
global operating contract: source is manual-first, not generically writable.
Loading this skill does not grant permission to edit source or perform Git
mutations.

## Establish the work

- Clarify the desired outcome only when uncertainty affects the solution or
  authority. Read relevant project instructions, accepted scope when material,
  existing implementation, and tests. Do not load every project document by
  habit. Check the working tree before changing files so unrelated user work is
  preserved.
- Diagnose before prescribing. Challenge unnecessary complexity, explain
  important trade-offs, and choose a bounded implementation unit. Routine
  design and debugging stay in Development; refer a genuine change to accepted
  project meaning to `brainstorming` instead of silently redefining scope.
- Determine editing mode before writing, using the global contract's grant
  rules. Without applicable authority, give a usable manual-first proposal.
  Do not replace guided development with repeated offers to take over.

## Working from a slice

When a work item is selected, load `work-items` and read the slice, its relevant
brief, criteria, dependencies, and blocker. Do not implement Draft work or start
blocked work. If the outcome or criteria are unsettled, identify the gap and
hand off to `refinement` only when the request covers it. Do not rewrite the
criteria to make implementation convenient.

A bounded source request without project records can proceed normally; do not
manufacture a brief, slice, or charter as a prerequisite. Behaviour-defining
Markdown, including agent instructions and skills, follows the same approval
boundary as source. Follow the global contract's documentation timing.
One selected slice has one accountable worker. Launching agents or creating
branches/worktrees requires explicit authority.

## Manual-first path

1. Propose the smallest coherent change in code blocks, with exact file paths
   and enough placement context for the user to enter it. Include complete new
   files only when needed. Explain non-obvious choices and how to validate;
   avoid making the user reconstruct an essential missing step.
2. Stop for the user to enter the source. Do not write, format, regenerate, or
   use shell commands or another tool to make source changes on their behalf.
3. Once the user reports applying it, reread the actual files and relevant diff.
   Check behaviour, integration, and transcription mistakes rather than
   assuming the proposal was copied exactly. Give corrections as proposals
   unless Pi receives separate edit approval.

For review or debugging requests, investigation and diagnosis may be the whole
result. Do not manufacture an edit or approval request when none is needed.

## When Pi is authorized to edit

- Stay within the approved change and project. Inspect the target immediately
  before editing; preserve unrelated changes. If the work expands materially,
  pause for approval rather than treating the old grant as permission for new
  work. A session grant still has its stated scope and can be revoked.
- Make the bounded changes, reread the result, and inspect the resulting diff.
  Report affected paths and what was verified so the user can review in their
  editor. Do not claim that a tool-call approval constituted review of the
  final result.

## Inspect and conclude

Follow the global contract's opt-in testing and validation rule. Read changed
files and inspect the diff; do not automatically run checks. For authorized
commands, first assess source writes, artifacts, external access, and other side
effects. Report results and uncertainty accurately. Completing implementation
does not authorize Git mutations.

Hand the actual result to `review` and the user. A proposal awaiting manual
entry is not an implementation. Follow the global contract's acceptance and
documentation timing; load `documentation` and `work-items` for accepted-result
updates. `work-items` owns recorded status transitions.

Do not silently begin the next slice, create follow-up slices, or expand the
brief. Hand gaps to refinement; criteria changes require acceptance.
