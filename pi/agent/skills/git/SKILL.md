---
name: git
description: Perform a specifically requested Git or GitHub action under the user's standards. Use when asked to create a branch, stage, commit, push, open a PR, merge, tag, or publish a release. Do not load merely because development finished or a state report mentions Git.
---

# Git

Git mutations require a specific request. Follow the global operating contract
and any applicable project instructions. This skill describes behaviour; it is
not a permission gate. Read-only Git inspection does not imply permission to
stage, commit, push, or publish.

## Before acting

- Identify the **requested outcome** and stop at its boundary. A commit does
  not authorize a push or PR; a push does not authorize a PR; creating a PR
  does not authorize merging it. A source-edit grant authorizes none of these.
- Inspect branch, HEAD, working tree, staged and unstaged changes, and relevant
  project policy. Respect unrelated user changes. Check conflicts, in-progress
  Git operations, and validation appropriate to the change. Do not run an
  auto-fix or source generator through Git validation without source-edit
  authority.
- Use the configured default branch (`main` if unspecified). If the action's
  files, remote, destination, PR, version, or consequences are ambiguous, ask
  only for what is missing. No arbitrary force, protected-branch rewrite, tag
  replacement, or bypass of repository protections.

## Local branches and commits

- When asked to start work, prefer a small, descriptive
  `<type>/<kebab-case-work>` branch; `feat/`, `bugfix/`, and `chore/` are
  examples, not an exhaustive allowlist. Do not switch branches merely because
  implementation begins. Avoid normal feature commits directly on the default
  branch; clarify a requested exception, such as project bootstrap.
- A request to **commit** is approval to select intended changes, stage them,
  and commit. Do not request a second approval of the message. Inspect the
  final staged diff and preserve unrelated paths or hunks. If existing staged
  material or mixed changes make selection unclear, stop and ask rather than
  committing or staging extra content.
- Commit one coherent, reasonably small unit. Derive the subject from the
  staged diff: name the changed behaviour or artifact and the meaningful
  result. For a changed output, include the new value when it distinguishes the
  change; for documentation, name the topic documented. Avoid vague adjectives
  like `correct` or `improved` without specifics, jokes, metaphors, generic
  wording, and type prefixes (`feat:`, `fix:`, `chore:`). Keep technical detail
  minimal; add a body only when important rationale cannot fit in the subject.
  Report the commit and validation performed, including anything not checked.
  Stop; do not push because the commit succeeded.

## Push and pull request

- Push only on request. Check local and remote targets; use a configured
  upstream when unambiguous, otherwise ask for remote and destination. No
  force push by default, and never force-push the protected default branch.
  Report remote failures or uncertain outcomes rather than blindly retrying.
- Create a PR only on request. Do not infer the need for one from repository
  visibility or assumed client ownership. Confirm ambiguous base, head, title,
  or target repository. Creating a PR neither merges nor tags it.

## Merge, tag, and release

- For a requested merge into the configured default branch, require the
  user's **exact `MAJOR.MINOR.PATCH` version** before mutation. Do not infer a
  bump from commit count, force a carry at 10, add a `v`, or pick an initial
  version automatically. Check that the tag is available and that the chosen
  version fits the intended state; ask if it conflicts with existing versions.
- Prefer a squash merge. Check the branch or PR, target, remote, validation,
  and current base before merging; stop on ambiguity, conflicts, failing
  required checks, or unrelated work. An explicit merge-to-default request
  authorizes publishing the resulting default-branch commit and its tag to the
  agreed remote. Tag only the **resulting default-branch commit** after it
  exists and verify the published tag points there. Do not auto-tag PR creation
  or a merge into another branch.
- A PR merged later by someone else does not trigger Pi automatically. A
  separate request is needed to tag an existing default-branch commit. Do not
  retroactively tag bootstrap commits, overwrite tags, delete branches, or
  create a GitHub Release without specific instruction.
- Remote operations may partially succeed. If a merge lands but tagging or
  publication fails, report the exact known state and do not silently retry,
  claim rollback, or start a different Git action.
