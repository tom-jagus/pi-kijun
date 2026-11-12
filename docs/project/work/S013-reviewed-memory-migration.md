---
id: S013
status: To do
parent: B008
depends_on:
  - S011
blocked_by: A sanitized ChatGPT sample must be supplied by the user.
---

# Review a personal memory migration

## Outcome

Review a user-supplied ChatGPT sample and propose useful destinations without
silently activating personal information or changing policy.

## Acceptance criteria

- Before receiving material, explain provider and session-history exposure and
  ask the user to exclude credentials and material they do not want shared.
- Review the supplied sample for relevance, duplication, conflicts, sensitivity,
  and age. Distinguish user statements from model inferences and identify
  uncertainty without assuming old entries remain current.
- Present proposed destinations for memory, policy review, project context, or
  exclusion. Do not treat a proposal as an accepted decision or authorization
  to edit policy, project records, or Git state.
- Show the proposed memory entries for explicit approval before activation.
  Keep raw material and personal data outside the tracked repository.
- Explain what was approved, what remains excluded or unresolved, and any
  limitations of deletion from session history or backups.

## Tasks

- [ ] Agree a suitably small sanitized sample and review it only when supplied.
- [ ] Present proposed destinations and memory entries for user decisions.
- [ ] Apply only specifically approved memory changes; seek separate authority
  for any policy or other behavior-file changes.
- [ ] Present the outcome for acceptance before updating project records.
