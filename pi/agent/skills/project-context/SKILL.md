---
name: project-context
description: Recover or report project purpose and current work. Use for status questions, resuming a session, or finding the next useful action from docs/project/charter.md and docs/project/work.md. Does not rewrite records during reporting or own brainstorming, refinement, implementation, or acceptance review.
---

# Project context

Recover enough context to continue without reconstructing a project diary.
Follow the global operating contract. This skill reports and routes work; it
does not grant editing, acceptance, delegation, or Git authority.

## Report or resume

1. Read `docs/project/charter.md` for purpose and boundaries and
   `docs/project/work.md` for open work. Read only the item files relevant to
   the request. Item files own their status; the index is a secondary view.
2. Inspect Git state and relevant repository files when they affect the answer.
   Distinguish recorded claims, verified facts, and inferences. Check that the
   proposed next action still makes sense; do not repeat stale instructions.
3. Summarize the current outcome, active or reviewable work, meaningful
   blockers, and one useful next action. Do not recite every item or history.
4. Report missing records, stale index entries, or conflicts only when material.
   Reporting is read-only. Do not repair records or create a charter merely
   because the user asks where things stand.

Missing project files do not prevent unrelated work. For a project still using
older documents, read what is useful and flag the difference; do not silently
migrate it or treat old and new records as competing sources of truth.

## Route the next activity

- Use `brainstorming` to establish or change charter or brief outcomes, or to
  suggest worthwhile improvements when the next useful work is not defined.
- Use `refinement` to prepare selected slices and task checklists.
- Use `development` to implement or investigate source changes.
- Use `review` to assess delivery against acceptance criteria.
- Use `work-items` for requested record maintenance and automatic updates after
  implementation acceptance, including formats, dependencies, and the index.
  A status report alone does not authorize those updates.

Name a material activity transition. Continue when the user's request already
covers it; ask before expanding scope. Do not duplicate these procedures here
or copy workflow instructions into the project's charter.
