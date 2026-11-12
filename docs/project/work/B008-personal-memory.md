---
id: B008
status: In progress
---

# Curated personal memory

## Outcome

Extend Pi Kijun with persistent, user-controlled personal context that reduces
repeated explanation across sessions without expanding the global operating
contract into a personal profile. Include a reviewed migration of useful
information from the user's existing ChatGPT instructions and memories.

Use one private Markdown file alongside Pi's user resources, short global
instructions, and an on-demand `personal-memory` skill. The agent reads memory
when personal context may help or when explicitly asked. Backup remains a
separate decision.

## Why

Stable personal facts and preferences can help the agent make relevant
suggestions without requiring the user to repeat them. They should remain
inspectable and correctable without becoming hidden policy, an unbounded
conversation archive, or a competing source of project decisions.

## Boundaries

- Personal facts and preferences belong in memory. Edit authority, Git rules,
  and acceptance procedures remain in the operating contract and skills.
  Project decisions remain in project records; temporary handoffs and reusable
  procedures retain their existing homes.
- Memory cannot override applicable instructions, grant authority, accept work,
  or turn an inferred preference into an established user decision.
- The agent may propose useful additions or corrections and act on requested
  changes. Additions, corrections, and deletions require explicit user approval;
  an explicit request specifying the change provides that approval. Proposals
  must not silently change active memory.
- Keep the personal Markdown file under `~/.pi/agent` and personal content and
  raw ChatGPT exports outside the tracked Kijun repository. Kijun owns guidance,
  not the private dataset. Backup and any versioning remain undecided.
- Use short global instructions and a `personal-memory` skill, not an extension
  or automatic injection. The whole file enters context when read; instructions
  and skills guide behavior but do not enforce it.
- Review supplied ChatGPT material for relevance, duplication, conflicts,
  sensitivity, and age. Distinguish user statements from model inferences;
  proposed imports are not automatically active instructions or memories.
- Do not import credentials. A read can expose the whole file to the configured
  model provider and retain its contents in session history.
- Do not promise identical model behavior. The outcome is less repetition and
  more consistent use of relevant context, not deterministic compliance.
- Scheduling, messaging, portfolio reviews, research digests, and content
  production are outside this brief. Messaging integration is deferred.

## Acceptance criteria

- A fresh session can use approved personal context without putting that
  content in the global operating contract or requiring manual repetition.
- The user can inspect and edit active memory, identify sources where useful,
  correct or remove entries, and understand the effect on current and future
  sessions.
- An unapproved proposal does not affect active memory. Conflicts with current
  instructions or newer user statements are surfaced rather than silently
  resolved in favor of stored memory.
- Relevant facts are retained without duplicating authoritative project state
  or loading an unrestricted personal history into every request.
- A user-supplied sample of ChatGPT instructions and memories can be reviewed
  into proposed destinations, including memory, policy review, project context,
  and exclusion. The user approves the imported result before activation.
- Personal data is not committed to the Kijun repository. The design explains
  model-provider exposure, storage, deletion, backup, and recovery boundaries.
- Existing installations and working standards remain usable if memory is
  disabled or unavailable, with any loss of personal context made clear.

## Open questions

- Which backup and recovery approach should the user choose, if any?
- Which sanitized ChatGPT sample will the user supply, and in what format?
  No exports have been inspected yet.

## Risks

Incorrect or outdated memories can influence later work. Keep the store small,
make changes reviewable, and settle conflict and correction behavior before
activation. Sensitive information may reach a configured model provider and
remain in session history when loaded. Deleting an entry does not erase copies
in previous sessions or backups.
