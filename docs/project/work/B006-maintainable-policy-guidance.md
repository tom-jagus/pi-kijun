---
id: B006
status: In progress
blocked_by: Slice 8 review pending.
---

# Maintainable policy guidance

## Outcome

Reduce unnecessary duplication of authority and acceptance rules while keeping
individual skills understandable and usable when loaded on demand.

## Why

Related rules appear in the global contract, activity skills, and workflow
guide. Some repetition provides useful local context, but unnecessary copies
increase the chance that a future policy change leaves contradictory guidance.

## Boundaries

Keep governing rules in the contract, activity-specific consequences in skills,
and user explanations in the guide. Preserve existing editing, acceptance,
documentation, delegation, and Git boundaries. Do not shorten instructions at
the expense of clarity, introduce new policy, or require a formal behavioural
evaluation suite.

## Acceptance criteria

- The responsibility of the contract, skills, and guide is clear for authority
  and acceptance guidance.
- Redundant detail is removed where it adds no activity-specific meaning;
  repetition needed to make a skill usable with the contract is retained.
- Manual-first development, explicit edit approval, separate acceptance, and
  specific Git authority retain their existing meaning.
- Documentation timing and interim-recording exceptions remain consistent
  across affected guidance.
- A reader can follow each affected activity with the contract and explicitly
  linked references, without searching unrelated skills for essential rules.
- The result identifies the material duplication removed and any deliberately
  retained repetition so the user can assess the trade-off.
