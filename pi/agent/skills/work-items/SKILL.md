---
name: work-items
description: Create or maintain docs/project/charter.md, docs/project/work.md, and brief or slice files in docs/project/work/. Use for work-item formats, IDs, relationships, dependencies, status changes, and index updates alongside the relevant activity skill. Does not decide scope or acceptance.
---

# Work items

Own the shared record format, not the activity's decisions. Follow the global
operating contract. A status never grants source-edit, delegation, or Git
authority. Read [record shapes](references/records.md) before creating or
restructuring records; use the same shapes across projects.

## Files and ownership

- `docs/project/charter.md` explains the whole project's Problem, Value, Success,
  and Boundaries. An optional Risks section records material project-wide
  risks and responses. No status report, general agent rules, or task plan.
- `docs/project/work.md` is a short index of open work. Item files own their status;
  the index is a secondary view, not a second backlog or progress narrative.
- `docs/project/work/B001-<slug>.md` is a brief. A brief defines a bounded outcome
  contributing to the project's purpose, why it matters, its boundaries,
  acceptance criteria, and unresolved questions.
- `docs/project/work/S001-<slug>.md` is a slice, a small independently reviewable
  outcome. Tasks are a checklist inside it, not separate records by default.
  Acceptance criteria describe required results; tasks describe a changeable
  implementation plan. Standalone slices do not require an invented brief.

Use stable, unique B and S IDs, at least three digits, with separate sequences.
Check existing files, Git state, and relevant history for deleted IDs before
allocating an ID; ask if allocation cannot be established safely. Use lowercase
hyphenated slugs. Never encode status in paths, reuse IDs, or rename files just
to change titles.
A slice may have one brief as its parent. Use IDs for relationships. Milestones
are optional grouping targets, not a required parent level; introduce them only
when requested for a real delivery target.

## Minimal metadata

Require only `id` and `status`. Allow `parent` on slices, `depends_on` as a list
of prerequisite item IDs, and `blocked_by` as a short explanation when needed.
Omit unused fields. Do not add timestamps, estimates, priorities, owner fields,
or session details by habit. Describe significant risks in the narrowest useful
record, with a response or investigation rather than an invented mitigation.

## Status meanings

Use exactly `Draft`, `To do`, `In progress`, `Review`, and `Done` in metadata
and the index.

- Draft is captured work that is not sufficiently defined or accepted to start.
  Do not implement it, even if its title suggests an obvious solution.
- To do has an accepted outcome, clear acceptance criteria, and no unresolved
  decision that prevents implementation. Recorded dependencies or blockers can
  still prevent starting. A brief can be To do before it has slices, provided
  its own outcome-level criteria and boundaries are clear.
- In progress has active work and one accountable worker or coordinator. A
  brief enters In progress when its first slice starts or active discovery
  toward its outcome begins, not merely when someone captures an idea.
- Review has a result and evidence ready for assessment. Development hands the
  result over in the conversation, not by prematurely updating records. Record
  Review when interim recording is requested or an accepted result still needs
  agreed integration. Development must not accept its own delivery as Done.
- Done meets the item's criteria and agreed review and integration requirements.
  Default to user acceptance unless the user explicitly delegates acceptance.
  Delegation to review is not delegation to implement fixes or perform Git work.

The normal stages are Draft, To do, In progress, Review, Done. Do not write
interim updates just to visit every status, or advance an item merely because
a file was written. Move Draft to To do only after the user
accepts the outcome and criteria, including through an explicit refinement
request that already specifies them. A request to develop a Draft item does
not settle its missing decisions. Report what prevents starting and refine it
only when the request covers that activity.

Apply implementation status updates after acceptance or when interim recording
is explicitly requested; otherwise report the actual stage in the conversation.
When recording a failed review, use In progress. Missing evidence may leave an
item in Review with a blocker. A material change to the outcome or criteria must
be proposed and accepted; if the definition is no longer settled, use Draft.
Reopening Done requires an explicit decision. Do not silently reopen accepted
work when a new follow-up slice would describe the need better.

## Brief review and dependencies

When all slices in the brief's current plan are Done, start the brief's review
by moving it to Review, not Done, and hand off to `review`. A brief with no
slices is not automatically reviewable. Check evidence against its own outcome
criteria; child completion is not proof. Review may also happen earlier when
requested. If the outcome is unmet, return the brief to In progress and hand
remaining work to `refinement`. Keep correctly completed slices Done.

Before starting an item, inspect its dependencies and blocker. Do not treat a
missing or non-Done dependency as satisfied. Reject self-dependencies, cycles,
and references to missing items. Do not add Blocked, Cancelled, or extra states
without agreeing a workflow change; use `blocked_by` for the current obstacle.

## Remove abandoned work

When the user decides an item is redundant or no longer worth pursuing, remove
its file and index entry rather than adding an abandoned state or archive.
Inspect child items, links, and dependencies first. Remove obsolete references,
but do not silently treat an unmet prerequisite as satisfied. Ask if removing a
parent or dependency leaves useful work without an agreed outcome or plan.

Do not delete items merely because they are old, or mark abandoned work Done.
Keep useful completed records by default. Never reuse deleted IDs or create
placeholder files just to reserve them. Git history preserves committed records;
warn before discarding material that has no recoverable copy.

## Bounded maintenance

1. Read the affected records, index, and relevant repository evidence. Preserve
   unrelated edits and distinguish recorded state from verified facts.
2. Requests to establish, capture, or refine records permit their necessary
   writes without separate edit approval. Discussion, suggestions, and status
   reporting remain read-only. For implementation, wait for user acceptance or
   explicitly delegated acceptance, then update relevant records automatically.
   Before acceptance, record interim state or review findings only when explicitly
   asked. Do not infer completion or acceptance from permission to edit.
   An explicit request to revise the workflow or its records permits those edits
   without implying acceptance of the resulting implementation.
3. Keep all open items in the index, linked to their files, with short outcome,
   status, and blocker columns. Omit Done rows; keep their files in place.
   Order parents beside children where practical. Do not duplicate criteria,
   task lists, review evidence, or child statuses in parent briefs.
4. Refresh the index when item membership, outcome, status, or blocker changes.
   If it disagrees with a file, the file wins. Report and repair drift only when
   maintenance is in scope; otherwise report the discrepancy.
5. Replace stale summaries. Record concise conclusions, unresolved decisions,
   and necessary evidence, never transcripts, routine activity logs, or a
   separate progress report. Keep detailed technical material in linked docs
   only when needed. Report paths changed for editor review.

## Concurrent work

Use one coordinator to allocate IDs, assign slices, and update the shared
index and brief states. Workers return evidence and update only their assigned
slices after acceptance or when interim recording is explicitly requested. The
coordinator reconciles shared records afterward. This is the concurrent-work
exception to updating the index alongside an item. Separate worktrees isolate
files, not incompatible design decisions. Check overlapping changes and
dependencies before parallel assignment. Do not launch workers,
create branches or worktrees, or inherit source/Git permissions implicitly.
This skill defines records; it does not implement locking or orchestration.
