# Independent content-review exchanges

This guidance is for the main agent coordinating a requested independent content
review. The `content-reviewer` returns findings and never coordinates more agents.
Use the unchanged `pi-subagents` plugin with the Kijun reviewer definition.
See [Workflow dependencies](../../../../../docs/dependencies.md) for package
installation, resource filters, activation checks, and rollback.

## Prepare the review

Load `content-review`. Identify target paths, purpose, audience, draft or delivery
stage, and relevant constraints. Use existing context when sufficient. Do not
require the user to restate it or create work records for an ad hoc review.

If `subagents_enable` is available but `subagent` is not, call the loader first.
If neither is available, report that independent review is unavailable. Do not
silently substitute a same-session review or install software. A same-session
assessment is an alternative to offer, not an independent result.

For execution, select `content-reviewer` from user scope so a project agent with
the same name cannot silently replace it. Use one foreground call at a time:

```js
subagent({
  agent: "content-reviewer",
  task: "Review the specified files for the stated audience and purpose...",
  async: false,
  options: { agentScope: "user", context: "fresh", mission: false }
})
```

Use actual paths and context instead of the placeholder task. Omit `output`,
`gate`, acceptance overrides, sharing, worktrees, skill overrides, and runner or
model overrides. The definition supplies selected skills, read-only tools, and
no ambient extensions. Model choice remains with the user. If plugin settings
or runtime requirements prevent this launch contract, report the conflict rather
than switching runners, weakening restrictions, or silently changing models.

The initial task should contain paths, intended use, audience, stage, constraints,
and necessary source references. Do not send the author's whole conversation,
private reasoning, editing grants, or a persuasive defense of the draft. Ask for
material findings with locations, evidence, consequences, and stable identifiers.

## Discuss findings within the limit

Count at most three reviewer invocations for the entire user review request,
including the initial invocation, failures, cancellations, retries, and checks
of authorized revisions. The limit is main-agent guidance, not a plugin-enforced
per-request counter. Do not confuse the plugin's per-run or per-session spawn
budgets with this limit or reset the count after clarification or compaction.
When recovering an interrupted exchange, recover its count from the conversation;
if that is impossible, ask rather than assuming a fresh allowance.

Read the findings and relevant evidence. Accept supported findings and challenge
unsupported ones with specific sources. Use another invocation only when it can
resolve a material ambiguity, check an authorized revision, or reconsider a
consequential disagreement. Stop early when there are no material findings,
when findings are sufficiently clear to report, or when another exchange would
add nothing. Agreement is not proof, and disagreement is not a reason to consume
all three invocations.

Each follow-up is a new `context: "fresh"` invocation, not `resume`, `steer`, a
fork, or a nested workflow. Include prior findings, their identifiers, the main
agent's responses, relevant source paths, and what specifically needs checking.
Keep findings and responses distinguishable; preserve material objections rather
than replacing them with a selective summary. Ask the reviewer to explain which
findings remain, changed, or were withdrawn and why.

Resolve factual misunderstandings without involving the user at every exchange.
Return questions when resolution requires the user's scope choices, preferences,
authority, or information unavailable in the project. At the invocation limit,
report unresolved disagreements and their evidence rather than forcing agreement
or starting a new review request on the user's behalf.

## Failures and authority

Treat a failed, interrupted, cancelled, timed-out, empty, or missing-skill result
as incomplete review, never as no material findings. After cancellation, stop and
report the incomplete result. For other failures, report the diagnostic and
current invocation count; retry only when a clear same-protocol remedy exists
and allowance remains. Do not loop on infrastructure errors or change execution
mode as an unapproved fallback.

Review grants no new permission to revise files, accept work, update records, or
perform Git actions. Do not pass the main agent's permissions to the reviewer.
Use authorized revisions only within the existing scope and invocation limit;
a request for review alone does not authorize a revision loop.

## Report the conclusion

Give the user a concise summary, not the full exchange:

- The reviewed scope and actual reviewer invocation count, including failures.
- Material findings and their consequences.
- Findings the main agent accepted or rejected, with evidence-based reasons.
- Remaining uncertainty, disagreements, and questions needing the user.
- Whether files changed and, if so, which paths under what existing authority.

State explicitly when there are no material findings or when review is
incomplete. Do not describe the reviewer's assessment or the plugin's execution
success as user acceptance of the work.
