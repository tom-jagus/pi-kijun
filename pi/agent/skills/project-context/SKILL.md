---
name: project-context
description: Define or revise a project's scope, report its current state, resume work, or maintain its durable project context. Use when starting a project, changing objectives or constraints, checking progress, recovering a session, or updating docs/project/definition.md or docs/project/progress.md. Do not load for routine implementation merely because project documents exist.
---

# Project Context

Help the user make and recover consequential project decisions without turning
project documentation into a task log. Apply the global operating contract;
this skill does not grant source-edit or Git authority.

## Documents and authority

Configured projects normally use two concise files:

- `docs/project/definition.md` owns stable purpose, scope, non-goals, important
  constraints and decisions, and success criteria. Do not put day-to-day status
  here. A proposed or edited definition is not accepted scope until the user
  accepts it.
- `docs/project/progress.md` owns current phase or focus, meaningful blockers,
  open questions, and the next useful action. Replace stale state rather than
  appending a diary. It is a record, not proof that the repository still matches.

A project may have other relevant instructions or records. Read them when useful,
but do not require or create a separate decision register by default. Never
invent missing scope or silently resolve contradictions between artifacts.

## Writing shape

Use headings that fit the project, not a rigid template or empty placeholders:

- **Definition:** Answer what and why, intended outcomes and scope, non-goals,
  important constraints or accepted choices, and how success will be recognized.
  Keep draft proposals distinct from accepted scope. Link to detailed design
  rather than turning this file into a plan, manual, or implementation diary.
- **Progress:** State the verified current focus, only meaningful blockers or
  unresolved choices, and one useful next action. Distinguish recorded state
  from what the repository actually shows. Replace outdated claims rather than
  accumulating milestones or repeating the definition.

Keep both readable in one sitting. Put setup and usage in the README or a guide,
not in either project-context file; use the `documentation` skill for those.

## Choose the smallest relevant procedure

1. **Define or materially revise:** Establish the problem and intended outcome;
   challenge weak assumptions and unnecessary scope. Identify only the
   objectives, boundaries, constraints, approach, and success criteria needed to
   guide work. Compare alternatives when the choice matters. Consult existing
   accepted context; reopen it only for an explicit change or material new
   evidence. Update the affected documents, not every artifact by habit.
2. **Report state:** Read available project documents and inspect current Git
   state or relevant files when they affect the answer. Separate recorded facts
   from repository observations and inferences. Give the current focus, real
   blockers, and one useful next action. Reporting is read-only; do not edit
   `progress.md` just because the user asked for a status report.
3. **Resume:** Recover enough stable scope, current progress, and working-tree
   state to continue safely. Check whether the recorded next action is still
   viable. Summarize the continuation, not the full history; flag missing or
   inconsistent information instead of guessing.
4. **Update progress:** When asked to record a meaningful change of phase,
   blocker, current work, or next action, check actual state, then revise
   `progress.md` concisely. Routine implementation detail belongs in code,
   tests, or Git history.

An absence of either file does not prevent unrelated repository work. If the
user is establishing durable project context, draft the missing documents; if
not, report the gap only when it matters to the request. With partial or
conflicting context, use what is reliable and ask only questions whose answers
would change a consequential choice.

## Editing and review

For an explicit project-documentation request, inspect the existing files and
preserve unrelated changes. Check factual updates against relevant repository
sources; if the requested claim conflicts with evidence, surface that conflict
instead of writing it as fact. Write the bounded, accurate update, then report
which paths changed and how the user can inspect the result in their editor.
Offer a short explanation of material decisions and uncertainties. Do not treat
writing, silence, or an unchanged frontmatter status as approval; ask for
acceptance before relying on a material scope change as settled. Do not
silently change implementation files, commit, or publish while maintaining
project context.
