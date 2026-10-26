# Project workflow

This workflow adapts [tanteki-flow](https://github.com/tom-jagus/tanteki-flow)
for personal, agent-assisted projects. It uses progressive refinement and small
reviewable outcomes without mandatory sprints or Scrum roles.

## Project records

```text
docs/
  project/
    charter.md
    work.md
    work/
      B001-readable-project-work.md
      S001-introduce-work-records.md
```

The charter explains the whole project's Problem, Value, Success, and
Boundaries. Risks is optional for material project-wide uncertainties and their
responses. Keep it roughly one screen. It is not a specification, status report,
or copy of the agent's instructions.

A brief defines a bounded outcome contributing to the project, why it matters,
its boundaries, acceptance criteria, and unresolved questions. A slice delivers
or investigates a small independently reviewable part of that outcome.
Standalone slices are allowed. Tasks stay as checklists inside slices unless
they need their own outcome, ownership, or review.

The work index lists open items with links, outcomes, statuses, and blockers.
Each item file owns its status. Completed files remain in place and leave the
open-work table. Remove abandoned or redundant items when the user decides they
are no longer useful, resolving affected links and dependencies. Do not archive
them by default or mark them Done. There is no separate progress narrative.

The [work-items skill](../pi/agent/skills/work-items/SKILL.md) owns the exact
formats, metadata, relationships, and lifecycle rules. Its
[record shapes](../pi/agent/skills/work-items/references/records.md) provide the
consistent structures. Do not copy the workflow rules into every project.

## Activities and skills

| Activity | Skill | Result and stopping point |
|---|---|---|
| Brainstorming | `brainstorming` | Explore outcomes or suggest worthwhile improvements. Capture selected ideas, not an automatic backlog. Do not create slices or task plans. |
| Refinement | `refinement` | Prepare selected slices, criteria, and task checklists. Do not implement them. |
| Implementation | `development` | Deliver a selected slice and verification evidence. Do not accept your own delivery. |
| Review | `review` | Assess criteria and evidence. Do not fix findings or rewrite criteria to pass. |

`work-items` supplies shared record rules to these activities. `project-context`
recovers or reports current state without changing files. `documentation` owns
user-facing guides and configured vault notes; `git` owns specifically requested
Git actions. The global contract selects guidance from ordinary conversation,
so the user does not need to name skills or use special commands.

A conversation may cover several activities. The agent should name a meaningful
transition and continue when the request covers it. Discussion and status
reporting remain read-only. Requests to establish, capture, or refine records
permit their necessary edits without separate approval, but do not implicitly
start development. Record conclusions and necessary evidence, not transcripts
or a report for every activity. Small requests do not require project records.

## Implementation and documentation

Implementation is guided by default. Pi proposes code for the user to enter;
Pi writes implementation files only with explicit approval for the change or
an applicable session grant. Behaviour-defining Markdown, including `AGENTS.md`
and skills, follows the same boundary. If a request to write implementation
files leaves approval unclear, Pi may ask for that bounded approval.

Deliver the implementation, assess it, and wait for the user to accept the
actual result before updating related documentation or work records. Report
findings in the conversation while acceptance is pending, unless recording
interim state is explicitly requested. A recorded status may therefore lag the
actual work; inspect files and the handoff rather than treating status as proof.

After user or explicitly delegated acceptance, automatically update relevant
repository documentation and existing records. No separate documentation
request is needed. Direct requests for documentation or record edits do not
need an implementation first. Report changed paths for editor review. None of
these permissions authorize vault updates or Git mutations.

## Git boundaries

Personal projects may work directly on the default branch. Client and
collaboration projects use separate branches and PRs into that branch; each
such PR is a versioned release, including bug fixes. Personal projects version
only requested releases. Project instructions should establish which policy
applies rather than leaving the agent to infer it from repository visibility.

Commits and pushes to the default branch require the destination to be explicit
or confirmed. Do not create branches automatically. A commit does not imply a
push or PR, and a local merge does not imply publication. The
[Git skill](../pi/agent/skills/git/SKILL.md) owns the exact version and release
rules, including tagging the resulting default-branch commit.

## Status and acceptance

The normal lifecycle is Draft, To do, In progress, Review, Done.

Draft work is not sufficiently defined or accepted to start. To do has accepted
outcomes and clear criteria, but a recorded dependency or blocker may still
prevent starting. In progress means work has started. Review means a result is
available for assessment. Done requires satisfied criteria, the agreed review
and integration requirements, and user acceptance or explicitly delegated
acceptance. Status does not grant editing or Git authority.

Review distinguishes satisfied, unmet, and unverified criteria. Missing evidence
is not a pass. When all slices in a brief's current plan are Done, the brief
enters Review rather than automatically closing. If its outcome is unmet, it
returns to In progress and refinement defines the remaining work. Correctly
completed slices stay Done. Changing criteria requires an explicit decision.

## Concurrent work

Independent To do slices can be assigned to workers once permissions and
execution arrangements are agreed. One coordinator allocates IDs, assigns work,
and maintains the shared index; workers stay within their assigned slices.
Separate worktrees prevent shared-directory collisions but do not make
incompatible changes safe. Shared interfaces and dependencies need coordination.

Kijun currently supplies guidance, not a worker launcher, lock manager, or
technical permission system. Source grants do not silently propagate to workers,
and branch creation, commits, integration, and publication still require the
applicable explicit authority.

## Assessing usefulness

Assess Kijun through ordinary work on real projects. Notice missed guidance,
unwanted writes, unclear records, or unnecessary interruptions, and discuss
specific improvements when they matter. No formal trial or test suite is
required to accept these rules. This does not remove ordinary inspection of
changes or appropriate validation in projects where the skills are used.
