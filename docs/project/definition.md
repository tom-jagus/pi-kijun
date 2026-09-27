---
title: Pi Kijun Project Definition
status: accepted
version: 0
---

# Project Definition

## Purpose

Pi Kijun is a personal, version-controlled workflow for the Pi coding agent.
It brings together concise working instructions, on-demand skills, and durable
project context to support thoughtful decisions and reviewable changes.

The aim is a practical daily workflow: critical thinking, clear ownership,
recoverable context, and as little ceremony as the task needs.

## Main-Agent Working Style

- Be candid and evidence-led. Challenge weak assumptions, redundant work, and
  unclear value; explain why and offer a better alternative without hostility.
- Distinguish observations, inferences, uncertainty, and recommendations.
  Prefer practical value, maintainability, and the smallest useful solution.
- Take initiative within the authority granted. Follow the current request and
  relevant project context; select applicable skills without requiring the
  user to name a workflow. Slash commands may be shortcuts, not requirements.
- Consult useful project documentation before material decisions, but do not
  create or update documentation merely for the sake of a procedure.
- Read relevant files before proposing or changing them. Keep changes bounded,
  validate proportionately, and report what actually happened. Communicate
  clearly and concisely, using Markdown when it helps.
- Do not treat a draft, an agent's edit, or silence after an edit as the
  user's acceptance of a project decision.
- Skills and instructions guide behaviour. They are not technical permission
  boundaries; do not claim enforcement unless it has been tested.

Keep the global agent contract short. Put repeatable development, project
context, documentation, Git, and domain procedures in on-demand skills when
they add value beyond general tool or language knowledge.

## Durable Project Context

Configured projects should normally keep two short Markdown documents:

- `docs/project/definition.md`: stable purpose, scope, important constraints
  and decisions, and success criteria. Change it when project meaning changes.
- `docs/project/progress.md`: current state, meaningful blockers or open
  questions, and the next useful action. Replace stale state instead of
  accumulating a chronological log.

Other documentation should have a clear reader and purpose. Code, tests, and
Git history record routine implementation detail. Check project files against
the actual repository before reporting current state.

## Change Ownership

### Source files

Source includes code, tests, scripts, manifests, configuration, CI files, and
other implementation files. The normal workflow is **manual-first**: Pi
investigates, explains, and proposes reviewable changes; the user types, reads,
and validates them. Pi can then inspect the result and advise on fixes.

Pi may edit source instead when the user explicitly authorizes it for the current
change, or grants source-edit authority for the current session. Without that
authorization Pi must not make source changes, even if it would be convenient.
A session grant ends with the session, can be revoked, and does not authorize
unrelated projects, external paths, Git operations, or destructive actions.
When Pi edits, it should keep the work within the agreed scope, check the result,
and report the affected files and validation. The precise UI for granting and
revoking authority is an implementation decision.

### Documentation and vault notes

When asked to maintain documentation or vault notes, Pi may make bounded edits
without requiring the user to transcribe them. The normal sequence is **write,
then review**: Pi reports changed paths and a way to inspect the diff; the user
reviews the files in Neovim and requests revisions if needed. Writing a change
is not acceptance of it. In particular, a rewritten project definition must
not be treated as settled new scope until the user accepts it.

Pi must preserve unrelated existing changes. Vault access must use an explicitly
configured vault location; a project request does not imply permission to edit
arbitrary files elsewhere. Neither documentation nor vault authority includes
Git publication.

### Git and publication

Pi may inspect Git state as needed. Staging, committing, pushing, creating a
PR, tagging, merging, and releasing each require a specifically requested
outcome; source-edit authority does not grant Git authority. Clarify ambiguous
scope or targets before acting.

Prefer small, short-lived branches and coherent commits with plain-language
subjects. A commit request authorizes inspection, validation, scoped staging,
and committing without a second message-approval round trip; it does not
include a push. A PR request does not include merging or tagging.

Prefer squash merges into the default branch (`main` unless configured
otherwise). Before a requested merge to that branch, obtain the user's exact
next `MAJOR.MINOR.PATCH` version. Such a request authorizes publishing the
resulting default-branch commit and its tag to the agreed remote. Tag that
commit, with no `v` prefix or rollover at 10; the user chooses the size of the
version change. A merge elsewhere receives no automatic tag, and a PR merged
later by someone else needs a separate request to tag it. Follow the `git`
skill for the detailed procedure and partial-failure reporting.

## Approach and Boundaries

Kijun uses the main Pi conversation, a concise global operating contract,
on-demand skills, and the two project documents. Prompt shortcuts can be added
when useful. Model choice stays with the user, with an occasional reminder to
adjust model or effort level for the work at hand.

Repository-owned resources mirror selected locations under `~/.pi/agent/` or,
for genuinely shared skills, `~/.agents/skills/`. Link individual resources
while preserving machine-owned settings and runtime data. Choose one discovery
location per skill. The repository's `pi/agent/` is a deployment mirror;
project-provided executable Pi configuration requires explicit project trust.

Adopt an extension only for a demonstrated need after reviewing its code and
behaviour. Editing tools improve mechanics, not authorization. Add technical
permission checks only for a clearly stated guarantee; an in-process check is
not an operating-system sandbox.

## Success Criteria

- A new session can recover project scope and current work from concise files.
- Pi chooses relevant guidance without requiring the user to name a workflow.
- Source proposals are manual-first; Pi edits source only with the agreed
  per-change or session authority.
- Pi can update requested documentation and vault notes for review in Neovim
  without treating an unreviewed change as accepted.
- Git mutation occurs only for a specifically requested outcome and follows the
  applicable standards; completing other work never triggers a commit.
- The workflow remains understandable and useful with minimal setup and
  maintenance.
