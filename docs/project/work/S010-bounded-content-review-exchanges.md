---
id: S010
status: Done
parent: B007
depends_on:
  - S009
---

# Integrate bounded content-review exchanges

## Outcome

Connect the main agent to the content reviewer through an existing subagent
extension, removing manual message copying while keeping review bounded and its
conclusions visible to the user.

## Acceptance criteria

- A suitable existing extension is selected after checking compatibility, fresh
  context support, tool restrictions, result return, and cancellation. The choice
  and any limitations are explained. Saved reviewer context may be resumed for
  bounded follow-up within the same review; no general orchestration system or
  unbounded reviewer conversation is introduced.
- After explicitly authorized installation and configuration, a user request
  can invoke `content-reviewer` and return its findings to the main agent. Setup
  preserves unrelated machine settings and resources, and activation and rollback
  instructions match the actual integration.
- The initial review receives file paths, purpose, audience, and relevant
  constraints rather than the author's full conversation or a persuasive defense
  of the draft. Resumed follow-ups retain previous findings and receive the main
  agent's responses and source paths for independent verification. Any fresh
  fallback explicitly receives the prior findings and relevant context.
- The initial invocation starts with fresh reviewer context. Follow-ups within
  the same review resume an eligible saved session. Separate reviews or an
  explicitly requested assessment without prior discussion start fresh. If
  resumption is unavailable, report the limitation before using a fresh fallback.
  A user review request uses at most three reviewer invocations in total,
  including the initial review, resumed turns, and failed or retried attempts,
  without resetting the count for a fresh session, clarification, or re-review.
  The workflow stops
  earlier when resolved or when another exchange would add nothing. Evidence
  identifies whether the bound is enforced by runtime code or agent guidance.
- The main agent can accept or challenge findings with evidence. It reports
  unresolved disagreements and asks the user when resolution requires missing
  information, scope choices, preferences, or authority. Agreement alone is not
  treated as proof of correctness.
- The final report states scope, invocation count, material findings, accepted and
  rejected findings with reasons, unresolved questions, and whether files changed.
  Intermediate exchanges do not require routine user supervision.
- The reviewer has no available tool path for mutating project files, including
  unrestricted shell commands, inherited write-capable extensions, or nested
  delegation. Verification describes the tool restriction without claiming an
  operating-system sandbox.
- Review does not expand the main agent's editing, acceptance, documentation,
  work-record, or Git authority. Authorized revisions may be re-reviewed within
  the same invocation limit, but autonomous revision loops are not added.
- Demonstrations cover an initial review, evidence-based clarification, early
  stopping, unresolved disagreement at the invocation limit, and a failed or
  cancelled reviewer invocation. Failure is reported as incomplete review, not a
  clean result, and does not trigger unbounded retries.

## Tasks

- [ ] Inspect available extension options and select the smallest suitable
  existing integration; surface any conflict with the accepted boundaries.
- [ ] Obtain explicit authority for plugin installation and implementation or
  configuration changes before making them.
- [ ] Integrate reviewer discovery, restricted tools, fresh initial reviews,
  resumable follow-ups, and result return without replacing unrelated resources.
- [ ] Add main-agent guidance for evidence-based follow-up, invocation counting,
  stopping, authority boundaries, and the final report.
- [ ] Demonstrate normal, disputed, bounded, failure, and cancellation cases;
  inspect the reviewer's effective tool set and report limitations.
- [ ] Present the implementation for acceptance, then align user documentation
  and records with the accepted result.

## Risks

An extension may inherit tools or extensions beyond its declared agent tool list.
Verify the effective reviewer capabilities rather than treating a read-only
prompt as enforcement. If no existing extension meets the agreed constraints,
return the conflict to the user before expanding implementation scope.

## Review

The user approved fresh initial reviews and resumed follow-ups. Direct async
launch returned an addressable run ID and saved session; resume returned a new
run ID using the same session file. The reviewer recalled its earlier check
phrase and finding without either being supplied in the follow-up. File-based
reviews returned findings to the main agent without manual copying.

A synthetic README test detected the planted overwrite contradiction and unsafe
notes guidance. On resumed clarification, the reviewer retained the contradiction,
accepted deliberate report deletion while retaining a documentation gap, and
withdrew a setup finding after audience clarification. The final report explained
the changes and limits, and stopped after two turns. One independent review of
the modified agent definition, delegation guide, and dependency guide found no
material findings. `git diff --check` passed. The three-turn limit is agent
guidance, not runtime enforcement.

The user accepted the implementation after extended practical use and chose to
close the slice as it stands. Unresolved disagreement at the invocation limit,
a failed or cancelled invocation reported as incomplete, and a complete audit of
the effective read-only tools remain unverified. These unverified cases are not
passes.
