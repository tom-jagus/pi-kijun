# Record shapes

Keep the same required headings across projects. Use short paragraphs and
observable acceptance criteria. For Draft records, state genuine unknowns
rather than filling headings with invented decisions. Add optional sections
only when they carry useful content. Do not copy these instructions into
project files.

## Charter

`docs/project/charter.md` has no required YAML metadata. Its four required
sections are Problem, Value, Success, and Boundaries. Keep it roughly one screen
where practical. Draft scope changes stay explicitly proposed until accepted.

```markdown
# Project name

## Problem

Who encounters the overall problem, and what is difficult today?

## Value

Why is solving it worthwhile? What improves for the user?

## Success

What observable results would show that the project helped?

## Boundaries

What is included, excluded, or materially constrained?
```

An optional `## Risks` section lists significant project-wide risks with their
responses or planned investigations. Brief and slice risks stay in those items.
Do not create a risk register or an acceptance metadata system by default.

## Brief

`docs/project/work/B001-<slug>.md` uses this shape. A brief need not repeat the
charter's overall problem statement. Explain its bounded contribution instead.

```markdown
---
id: B001
status: Draft
---

# Brief title

## Outcome

What bounded improvement or discovery should this work achieve?

## Why

Why does it contribute to the project's purpose?

## Boundaries

What is included, excluded, or constrained for this outcome?

## Acceptance criteria

- State observable outcome-level results, not a list of completed slices.
```

Add `## Open questions`, `## Risks`, or `## Review` only when needed. Capture
accepted consequential choices in the relevant content, not a session log.

## Slice

`docs/project/work/S001-<slug>.md` uses this shape. Omit `parent` for standalone
work.

```markdown
---
id: S001
status: Draft
parent: B001
---

# Slice title

## Outcome

What small result can someone independently inspect or demonstrate?

## Acceptance criteria

- State verifiable results and relevant boundaries.

## Tasks

- [ ] Record the useful implementation steps, not an exhaustive plan.
```

Keep the Tasks heading for consistency. An unchecked checklist is a plan, not
proof that acceptance criteria failed; checked tasks are not proof they passed.
Promote a task into a slice only when it needs an independent outcome, owner,
or review. Add Open questions, Risks, or Review sections only when useful.

Optional metadata, on either item type unless noted:

```yaml
depends_on:
  - S001
blocked_by: Waiting for the export format decision.
```

## Review evidence

Use one short `## Review` section in the item, replacing stale findings rather
than appending a report after every attempt. Identify satisfied, unmet, and
unverified criteria, the evidence or checks supporting the verdict, and any
required follow-up. Omit empty categories. Link to detailed evidence instead
of pasting logs. Identify user acceptance or explicitly delegated acceptance
when marking Done. Proposals to change criteria are not acceptance evidence.

## Work index

`docs/project/work.md` has no required YAML metadata. List all non-Done items and
link to completed files through the work directory when needed. Use exactly
these columns, with one short row per open item. The item files own the data.
Do not add another narrative progress section or an independently maintained
backlog ordering system.

```markdown
# Work

| Item | Outcome | Status | Blocker |
|---|---|---|---|
| [B001](work/B001-readable-work.md) | Make current work readable. | In progress | None |
| [S001](work/S001-work-index.md) | Introduce a linked work index. | To do | None |

Completed items remain in [work/](work/).
```
