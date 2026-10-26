---
id: S003
status: To do
parent: B002
---

# Demonstrate common workflow interactions

## Outcome

Add a concise set of conversation examples to `docs/workflow.md` that helps the
user express intent and recognize the expected actions and stopping points.

## Acceptance criteria

- A small-fix example shows Pi inspecting relevant files and proposing concrete
  code for manual entry without writing source or creating project records.
  The request to fix something alone is not treated as edit approval.
- A bounded-edit example shows explicit Pi-edit approval, delivery with
  verification evidence, and a stop for user acceptance. Only after acceptance
  does Pi update relevant documentation and existing records automatically.
- A Git example makes clear that edit approval and result acceptance do not
  authorize Git mutations. A separate commit request names its destination
  explicitly and does not authorize a push or PR.
- A brainstorming example ends with suggestions in the conversation and no
  automatic brief, slice, or implementation work.
- Each example identifies the user request, expected Pi response or action,
  and stopping point. Any assumed approval or project policy is stated rather
  than inferred.
- Examples illustrate current rules without introducing required wording,
  special commands, new authority, or guarantees of model compliance. Links
  point to governing guidance instead of repeating the full policy.
- Changes stay within the existing workflow guide, preserve unrelated content,
  and keep the examples short enough to scan without a separate tutorial.

## Tasks

- [ ] Check the contract and relevant activity and Git skills against the four
  scenarios before drafting.
- [ ] Add a clearly labelled examples section to the existing guide, including
  a note that wording is illustrative rather than a required command format.
- [ ] Review every scenario for approval, acceptance, documentation timing,
  Git boundaries, and consistency with B002's criteria.
- [ ] Check Markdown links, prose wrapping, and diff whitespace, then present
  the result for user review without treating delivery as acceptance.
