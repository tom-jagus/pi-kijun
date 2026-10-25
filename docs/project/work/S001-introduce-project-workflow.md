---
id: S001
status: Review
parent: B001
---

# Introduce the project workflow

## Outcome

Make the agreed workflow available through the agent contract, activity skills,
shared record rules, and this project's migrated records.

## Acceptance criteria

- Charter, brief, slice, and index shapes are consistent, with minimal YAML
  metadata and the five agreed status names.
- Brainstorming, refinement, development, and review have explicit scope,
  output limits, and handoff boundaries; work-items owns the shared rules.
- Source-edit, acceptance, delegation, and Git authority remain distinct.
- Setup includes the intended skills without replacing unrelated resources.
- Repository checks cover setup, record consistency, and workflow fixtures;
  model-dependent checks are available with their limitations stated.
- Superseded definition and progress files are removed and links updated.

## Tasks

- [x] Define activity skills and shared record rules.
- [x] Update routing, setup, and related existing guidance.
- [x] Migrate this project to the charter and work records.
- [x] Update and run repository checks.
- [x] Hand the result over for user review.

## Review

Ready for user review. Twelve deterministic checks pass, covering setup,
records, links, fixtures, and smoke-result checks. Bash syntax and
`git diff --check` also pass. These checks do not establish model behaviour.

Model-dependent trials and live activation have not run. Existing live
symlinks reflect checkout edits, but the new skills still need installation.
User acceptance is pending; no Git mutation or external link change was made.
