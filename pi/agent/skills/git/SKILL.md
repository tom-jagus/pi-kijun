---
name: git
description: Perform a specifically requested Git or GitHub action under the user's standards. Use when asked to create a branch, stage, commit, push, open a PR, merge, tag, or publish a release. Do not load merely because development finished or a state report mentions Git.
---

# Git

Git mutations require a specific request. Follow the global operating contract
and applicable project instructions. Read-only inspection is allowed; this
skill is behavioural guidance, not a technical permission gate.

## Before acting

- Identify the requested outcome and stop at its boundary. A commit does not
  authorize a push or PR; a push does not authorize a PR; creating a PR does not
  authorize merging it. Source-edit and acceptance authority grant none of these.
- Inspect branch, HEAD, working tree, staged and unstaged changes, and project
  policy. Preserve unrelated changes. Check conflicts, in-progress operations,
  and relevant validation. Do not run source-changing checks without edit
  authority.
- Use the configured default branch, `main` if unspecified. For commits or
  pushes to that branch, require the destination to be explicit in the request
  or confirmed before acting. "Commit this" while on `main` requires asking;
  "commit this on main" already supplies confirmation. Check the actual push
  destination, not just the local branch name.
- Read project instructions for whether the project is personal or
  client/collaborative. Do not infer this from repository visibility. Ask when
  the distinction affects the requested action and is not established.
- Clarify missing files, remote, destination, PR, version, or consequences.
  Never force-push the protected default branch, replace tags, or bypass
  repository protections.

## Branches and commits

- Personal projects may work directly on the default branch. Do not create or
  switch branches automatically. Create a branch only when asked; prefer a
  small descriptive name such as `feat/answer-result` or `bugfix/export-path`.
- Client and collaboration projects use separate branches and PRs into the
  default branch. If work is on that branch, ask before creating or switching
  branches. Do not make direct commits there without an explicit exception to
  this policy. Starting development alone grants no branch authority.
- A commit request permits selecting intended changes, staging, and committing,
  subject to the destination rule above. Do not request a second approval of
  the message. Inspect the final staged diff. If staged material or mixed hunks
  make selection unclear, ask rather than including extra content.
- Commit one coherent, reasonably small unit. Derive the subject from the
  staged diff and name the changed behaviour or artifact. Include a new value
  when it distinguishes the result. Avoid vague claims of improvement, jokes,
  metaphors, and type prefixes such as `feat:` or `fix:`. Add a body only for
  important rationale that cannot fit in the subject.
- Report the commit and validation, including anything not checked. Stop; a
  successful commit does not authorize publication.

## Push and pull request

- Push only on request. Verify remote and destination; a configured upstream
  does not remove the explicit-default-branch requirement. Ask for missing
  targets. Do not force-push by default or blindly retry uncertain failures.
- Create a PR only on request. Confirm ambiguous base, head, title, or target
  repository. Creating a PR neither merges nor tags it.
- In client and collaboration projects, every PR into the default branch is a
  release, including bug fixes. Personal projects have no automatic versioning
  requirement; version only releases the user requests.

## Merge, tag, and release

- A release merge or tagging request requires the user's exact
  `MAJOR.MINOR.PATCH` version before mutation. Do not infer the bump, add a `v`,
  force a carry at 10, or choose an initial version. Check that the version fits
  existing releases and that its tag is available. Ask if either is unclear.
- Treat a requested client/collaboration release merge as including its required
  local version tag. A personal merge needs a tag only when requested as a
  release. Prefer a squash merge and check the PR or branch, target, current
  base, validation, and unrelated work. Stop on ambiguity or conflicts.
- A local merge and tag do not authorize a push. Ask for publication authority
  if missing. A remote PR merge itself publishes to the default branch; require
  that remote action and destination to be explicit. Confirm whether the release
  tag should also be published if the request does not say so.
- Tag only the resulting default-branch commit after it exists, never the
  feature-branch commit or PR creation. Verify the target and, when publication
  is requested, that the published tag points to that same commit.
- A PR merged later by someone else does not trigger Pi. Tagging that existing
  merge needs a separate request. Do not retroactively tag bootstrap commits,
  overwrite tags, delete branches, or create a GitHub Release without a specific
  request.
- Remote actions may partially succeed. Report the exact known state if merge,
  tagging, or publication fails. Do not silently retry, claim rollback, or begin
  a different Git action.
