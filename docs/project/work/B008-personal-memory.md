---
id: B008
status: Draft
blocked_by: Storage, loading, and ChatGPT migration design remain undecided.
---

# Curated personal memory

## Outcome

Extend Pi Kijun with persistent, user-controlled personal context that reduces
repeated explanation across sessions without expanding the global operating
contract into a personal profile. Include a reviewed migration of useful
information from the user's existing ChatGPT instructions and memories.

The direction is agreed. Storage, loading, update mechanics, and migration need
a dedicated design discussion before implementation or slice refinement.

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
- Memory additions, corrections, and deletions require explicit user approval.
  Automatic extraction or proposals must not silently change active memory.
- Keep personal content and raw ChatGPT exports outside the tracked Kijun
  repository. Kijun may own the mechanism and documentation, not the private
  dataset. Choose private storage, backup, and any versioning separately.
- Review supplied ChatGPT material for relevance, duplication, conflicts,
  sensitivity, and age. Distinguish user statements from model inferences;
  proposed imports are not automatically active instructions or memories.
- Do not import credentials or assume all personal information should be sent
  to every model provider. Define what loads and when as part of the design.
- Do not promise identical model behavior. The outcome is less repetition and
  more consistent use of relevant context, not deterministic compliance.
- Scheduling, messaging, portfolio reviews, research digests, and content
  production are outside this brief. Messaging integration is deferred.

## Acceptance criteria

These criteria are draft requirements for the design discussion, not an
implementation plan or authorization to change behavior files.

- A fresh session can use approved personal context without putting that
  content in the global operating contract or requiring manual repetition.
- The user can inspect the active memory, identify its source, correct or
  remove entries, and understand when changes affect subsequent requests.
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

- Where should private memory live, and how should it be backed up or versioned?
- Which small core, if any, loads in every session, and how is other context
  selected? Is an extension justified or is explicit file loading sufficient?
- How are approved entries distinguished from suggestions, and what provenance
  and freshness information is useful without creating a maintenance burden?
- How do corrections, deletion, concurrent sessions, and conflicting entries
  affect active and future sessions?
- Which ChatGPT material will the user supply, in what format, and what should
  be excluded before the agent reads it? No exports have been inspected yet.
- How can usefulness and context overhead be demonstrated on representative
  sessions while preserving the existing authority boundaries?

## Risks

Incorrect or outdated memories can influence later work. Keep the store small,
make changes reviewable, and settle conflict and correction behavior before
activation. Sensitive information may reach a configured model provider when
loaded; agree the loading and privacy policy before importing personal data.
