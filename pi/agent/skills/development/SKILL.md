---
name: development
description: Work on source code, tests, scripts, configuration, or other implementation files. Use for implementation, debugging, source review, and validation, including manual-first change proposals and source edits explicitly authorized for Pi. Do not load for documentation-only or Git-only requests.
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
  project meaning to project-context instead of silently redefining scope.
- Determine the editing mode **before** a source-writing tool call. The default
  is proposal-only, even if the user asks to implement or fix something. Without
  Pi-edit authority, follow the manual-first path and give a usable proposal;
  do not ask to take over editing instead. Pi may edit only after explicit
  approval for this change or under an unrevoked, current-session source-edit
  grant covering this project and work. If an offered grant's scope or status
  is unclear, ask before editing. A grant for one change does not authorize
  the next; source authority does not authorize Git operations.

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
- This is a behavioural workflow, not a technical enforcement guarantee. Do
  not use a shell, generated command, extension tool, or formatter to bypass
  the editing boundary.

## Validate and conclude

Choose validation proportional to the change. Run suitable non-destructive
checks when appropriate; first assess whether a command may rewrite source,
create significant artifacts, reach external paths, or have other side effects.
Do not run auto-fixes or generators that change source without the applicable
edit authority. Report tests performed, tests not performed, failures, and
remaining uncertainty accurately. Suggest documentation updates only when they
would preserve meaningful context. Never stage, commit, or publish just because
an implementation unit is done.
