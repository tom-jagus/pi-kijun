---
id: B001
status: Done
---

# Readable project work

## Outcome

Replace narrative progress tracking with concise records and bounded activities
that support discussion, implementation, and acceptance review.

## Why

The user finds current project documentation difficult to read. Recovering work
should not require reconstructing an agent's activity history.

## Boundaries

Use a charter, a work index, briefs, and slices with task checklists. Separate
brainstorming, refinement, development, and review guidance; share record rules
through work-items. Keep implementation approval separate from acceptance and
Git authority. Update implementation-related documentation after acceptance;
allow requested documentation work without separate edit approval. Assess the
rules during ordinary project work, without a formal test suite or pilot.
Do not add orchestration, mandatory sprints, or a board generator.

## Acceptance criteria

- Project purpose and open work can be recovered from short human-readable
  files without a parallel progress narrative.
- Activity guidance limits what each activity produces and when it stops.
- Review assesses outcomes and evidence rather than closing briefs merely
  because their slices are Done.
- The user judges the records and guidance understandable and useful for daily
  work. Suggestions remain proposals until selected, and abandoned work can be
  removed without an archive or an invented completion.

## Review

The charter and linked records make project purpose and work readable without a
progress narrative. Activity skills define output and handoff boundaries;
review assesses brief outcomes separately from slice completion. Brainstorming
supports suggestions without an automatic backlog, and work-items defines
removal of abandoned work.

After the criterion-by-criterion review, the user explicitly accepted B001 and
all retained slices as Done for the delivered development work. The user will
assess the workflow during daily project work. Any shortcomings worth addressing
will become new improvement briefs rather than reopening this accepted brief.
