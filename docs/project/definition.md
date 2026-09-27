---
title: Pi Kijun Project Definition
status: draft
version: 0
---

# Project Definition

## Purpose

Pi Kijun is a personal, version-controlled set of standards for working with Pi.
It should help the main agent choose appropriate guidance, preserve useful project
context, respect ownership of changes, and carry out explicitly requested
work without turning Pi into a separate workflow engine.

The aim is a practical daily workflow: critical thinking, clear boundaries,
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

Keep the eventual global agent contract short. Detailed development, project
context, documentation, Git, and domain procedures belong in on-demand skills.
Do not create a skill for every tool or language: add one only for repeatable
standards or methods that general model knowledge does not adequately capture.
Tool familiarity and personal biography do not belong in the global contract.

## Durable Project Context

Configured projects should normally keep two short Markdown documents:

- `docs/project/definition.md`: stable purpose, scope, non-goals, important
  constraints and decisions, and success criteria. Change it when project
  meaning changes, not as an implementation diary.
- `docs/project/progress.md`: current state, meaningful blockers or open
  questions, and the next useful action. Replace stale state instead of
  accumulating a chronological log.

The current project may use other documentation when it has a specific reader
and purpose. A separate decision register is optional, not a requirement for
other projects. Code, tests, and Git history remain the normal record of routine
implementation detail. Project files inform a session but should be checked
against the actual repository before reporting current state.

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

Pi may inspect Git state as needed. It must **never initiate** staging,
committing, pushing, pull-request creation, tagging, merging, or releasing just
because it finished another task. Each requested Git outcome must be specifically
authorized by the user: asking for a commit does not imply a push or pull request;
a source-edit session grant does not imply any Git permission. A request for a
named multi-step outcome may authorize its necessary steps, but Pi should make
those steps and their consequences clear and pause if scope is ambiguous.

When specifically asked to act, Pi should follow the applicable project Git
standards, inspect the actual state and intended changes, stage only relevant
paths, validate appropriately, avoid altering unrelated work, and report the
result. Risky or irreversible operations warrant explicit review before they
run. Exact branch, commit, PR, tag, merge, and release conventions will be set
when the Git workflow is designed; OpenCode Mentor is a source of ideas, not an
automatic policy import.

## Approach and Boundaries

Start with a concise global operating contract, on-demand skills, and the two
project artifacts. Keep ordinary reasoning in the main Pi conversation. Add prompt
shortcuts only if they improve use; do not require subagents, a command for every
workflow, or a custom tool for every operation. Organize repository-owned
resources to mirror their intended locations under `~/.pi/agent/` and, only
when a skill is genuinely shared across agents, `~/.agents/skills/`. Link
individual resources rather than replacing Pi's live agent directory or its
machine-specific settings and runtime data.

Evaluate existing Pi extensions where they add a concrete benefit, particularly
permission prompts with session-scoped grants and line-anchored edits. Review
extension code and behaviour before adoption. An editing extension improves edit
mechanics, not authorization; a permission extension still runs inside Pi with
the user's operating-system privileges. Explicit project trust is required for
project-provided executable configuration.

Do not initially port Mentor's immutable proposal storage, transaction suite,
full Git lifecycle, vault taxonomy, model router, or release machinery. Add
technical enforcement only for a clearly stated guarantee, after checking what
Pi and reviewed extensions already provide. Never represent prompts or an
in-process gate as an operating-system sandbox.

## Initial Implementation Order

1. Agree on this definition and establish concise current progress.
2. Review a temporary repository architecture and plugin shortlist; decide
   what belongs in the first usable version.
3. Build the small global operating contract and project-context/development
   skills, then test automatic workflow selection and manual-first behaviour.
4. Evaluate a permission mechanism for per-change and session source-edit
   grants; test denial, expiry, revocation, and bypass paths before claiming
   enforcement. Evaluate line editing separately.
5. Add documentation/vault and Git guidance incrementally, defining strict Git
   standards before enabling the corresponding mutating workflow.
6. Test the whole process in real work; simplify anything whose friction
   outweighs its benefit.

## Success Criteria

- A new session can recover project scope and current work from concise files.
- Pi chooses relevant guidance without requiring the user to name a workflow.
- Source proposals are manual-first; Pi edits source only with the agreed
  per-change or session authority.
- Pi can update requested documentation and vault notes for review in Neovim
  without treating an unreviewed change as accepted.
- Git mutation occurs only for a specifically requested outcome and follows the
  applicable standards; completing other work never triggers a commit.
- The workflow remains understandable and usable without rebuilding Mentor's
  transaction system or installing unnecessary plugins.
