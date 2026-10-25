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
open-work table. There is no separate progress narrative.

The [work-items skill](../pi/agent/skills/work-items/SKILL.md) owns the exact
formats, metadata, relationships, and lifecycle rules. Its
[record shapes](../pi/agent/skills/work-items/references/records.md) provide the
consistent structures. Do not copy the workflow rules into every project.

## Activities and skills

| Activity | Skill | Result and stopping point |
|---|---|---|
| Brainstorming | `brainstorming` | Develop the charter and briefs. Do not automatically create slices or task plans. |
| Refinement | `refinement` | Prepare selected slices, criteria, and task checklists. Do not implement them. |
| Implementation | `development` | Deliver a selected slice and verification evidence. Do not accept your own delivery. |
| Review | `review` | Assess criteria and evidence. Do not fix findings or rewrite criteria to pass. |

`work-items` supplies shared record rules to these activities. `project-context`
recovers or reports current state without changing files. `documentation` owns
user-facing guides and configured vault notes; `git` owns specifically requested
Git actions. The global contract selects guidance from ordinary conversation,
so the user does not need to name skills or use special commands.

A conversation may cover several activities. The agent should name a meaningful
transition and continue when the request covers it. A discussion alone does not
authorize edits, and a refinement request does not implicitly start development.
Record concise conclusions and necessary evidence, not transcripts or a report
for every activity. Small unrelated requests do not require project records.

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

## Checks and live trials

Run the deterministic repository checks without credentials or model calls:

```sh
python -B -m unittest discover -s checks -p 'test_*.py'
bash -n setup.sh
```

The disposable smoke runner exercises model behaviour using a local Pi login.
It uses provider tokens, copies credentials privately into a temporary agent
directory, and removes that directory afterward. It is not an operating-system
sandbox or proof of enforcement. Select the provider, model, and thinking level
explicitly:

```sh
python -B checks/smoke.py --case brainstorming \
  --provider PROVIDER --model MODEL --thinking LEVEL
```

Use `--case all` for all cases. Workflow cases cover brainstorming, refinement,
Draft refusal, slice acceptance, unverified evidence, and brief outcome review.
Existing source-ownership and Git cases remain available. Deterministic checks
validate resources and fixtures, not whether a model follows the instructions;
use fresh-session trials and human inspection for that assessment.
