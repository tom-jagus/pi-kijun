---
id: S013
status: Done
parent: B008
depends_on:
  - S011
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
- [x] Present the outcome for acceptance before updating project records.

## Review

Accepted under the user's delegated conditional acceptance after S011 was
accepted. The user supplied a summary, reviewed proposed entries against current
references, corrected outdated details, and explicitly approved the private
memory content. Policy and project-specific details were not imported as
instructions. Exposure and retention limitations were explained. An independent
content reviewer found no material issues in the resulting memory; its assessment
was limited to the supplied references and user-confirmed technical details.
