---
name: review
description: Assess a slice or brief against its acceptance criteria, evidence, and relevant constraints. Use for acceptance review, delivery assessment, or checking whether completed slices achieved a brief's outcome. Does not fix findings, redefine criteria, or imply acceptance authority.
---

# Review

Assess the result, not the number of checked tasks. Follow the global operating
contract. Load `work-items` for project records and `development` when technical
inspection or validation needs its guidance; stay in review rather than taking
its implementation path. For an ad hoc code review without a work item, review
the requested change without inventing project records.

## Establish scope and authority

Read the selected item, parent brief when relevant, charter constraints, actual
changes, and available verification evidence. A work index or worker report is
not proof of delivery. Check the current repository rather than relying on a
recorded claim. Do not require every project document for a narrow review.

Identify the acceptance and integration requirements. Default to user
acceptance unless explicitly delegated. Permission to implement, a tool-call
approval, or permission to record findings is not acceptance authority. Review
is read-only unless the user requests or includes maintaining its records.

## Assess each criterion

Distinguish:

- Satisfied criteria, with concrete evidence or reproducible checks.
- Unmet criteria, with specific findings and their effect on the outcome.
- Unverified criteria, with missing evidence or checks that could not run.

Run proportionate non-destructive checks when appropriate. Report failures,
checks not performed, and uncertainty accurately. Technical quality and safety
constraints still matter even if a criterion omitted them; explain any such
finding separately instead of silently inventing a new product requirement.
Never treat an unavailable check as a pass.

For a slice, assess its own result and relevant technical quality. For a brief,
assess the combined result against the brief's outcome-level criteria. All
child slices being Done triggers review, not acceptance. A brief without
slices may be reviewed when direct evidence of its outcome exists.

## Verdict and handoff

Keep the result short: verdict, evidence, and only necessary findings or
follow-up. When record maintenance is in scope, replace the item's Review
section and refresh the index through `work-items`; do not create a separate
review report or paste tool logs.

- If criteria and integration requirements are met but acceptance is not
  delegated, leave the item in Review and request the user's acceptance.
- Mark Done only after user acceptance or under explicit delegated acceptance;
  record the basis. Do not merge, tag, or publish as a side effect.
- If criteria are unmet, return the item to In progress and describe the gap.
  Remaining brief work goes to `refinement`; correctly Done slices stay Done.
- If evidence is missing, leave the item in Review with a concrete blocker or
  return it for further work when that is the agreed disposition.

Do not fix findings, create new slices, change acceptance criteria, or broaden
scope within review. A changed goal is a proposed decision, not a way to pass
the review. Name any transition to refinement or development and proceed only
when the user's request and editing authority cover it.
