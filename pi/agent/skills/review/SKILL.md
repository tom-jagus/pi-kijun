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
not proof of delivery. A delivered implementation may still have its previous
recorded status because updates wait for acceptance. Check the actual files and
conversation handoff rather than requiring Review status as a prerequisite.
Do not require every project document for a narrow review.

Identify acceptance and integration requirements. Apply the global contract's
acceptance authority and documentation timing. Review stays read-only while
acceptance is pending unless interim recording is explicitly requested.

## Assess each criterion

Distinguish:

- Satisfied criteria, with concrete evidence or reproducible checks.
- Unmet criteria, with specific findings and their effect on the outcome.
- Unverified criteria, with missing evidence or checks that could not run.

Inspect files and available evidence. Follow the global contract's opt-in rule
for test and validation commands; a review request alone does not authorize them.
Report failures, checks not performed, and uncertainty accurately. Technical
quality and safety still matter even if a criterion omitted them; explain such
findings separately rather than inventing product requirements. Never treat an
unrun or unavailable check as a pass.

For a slice, assess its own result and relevant technical quality. For a brief,
assess the combined result against the brief's outcome-level criteria. All
child slices being Done triggers review, not acceptance. A brief without
slices may be reviewed when direct evidence of its outcome exists.

## Verdict and handoff

Keep the result short: verdict, evidence, and only necessary findings or
follow-up. Report findings in the conversation while acceptance is pending.
If interim recording is explicitly requested, replace the item's Review section
and refresh the index through `work-items`; do not create a separate review
report or paste tool logs.

- If criteria and integration requirements are met, request user acceptance
  unless acceptance was explicitly delegated.
- If criteria are unmet, explain the gap and needed development or refinement.
- If evidence is missing, identify the unverified criterion and required check.

For authorized recording, load `work-items` and follow its status rules; record
acceptance basis and remaining requirements. After acceptance, load
`documentation` for relevant automatic updates.

Report changed paths for editor review. Acceptance and documentation updates do
not authorize a merge, tag, push, or any other Git mutation.

Do not fix findings, create new slices, change acceptance criteria, or broaden
scope within review. A changed goal is a proposed decision, not a way to pass
the review. Name any transition to refinement or development and proceed only
when the user's request and editing authority cover it.
