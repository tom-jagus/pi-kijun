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
the same name cannot silently replace it. Launch an asynchronous review to obtain
an addressable run ID and saved session for follow-ups. Use one reviewer turn at
a time:

```js
subagent({
  agent: "content-reviewer",
  task: "Review the specified files for the stated audience and purpose...",
  async: true,
  options: { agentScope: "user", context: "fresh", mission: false }
})
```

Retain the returned run ID and return control while the reviewer runs. Native
completion notification supplies the result and saved session location. Do not
poll or use `bg_wait` for this notification. Read the completed result before
starting a follow-up.

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
including the initial invocation, resumed turns, failures, cancellations,
retries, and checks of authorized revisions. The limit is main-agent guidance,
not a plugin-enforced per-request counter. Do not confuse the plugin's per-run
or per-session spawn budgets with this limit or reset the count after
clarification or compaction.
When recovering an interrupted exchange, recover its count from the conversation;
if that is impossible, ask rather than assuming a fresh allowance.

Read the findings and relevant evidence. Accept supported findings and challenge
unsupported ones with specific sources. Use another invocation only when it can
resolve a material ambiguity, check an authorized revision, or reconsider a
consequential disagreement. Stop early when there are no material findings,
when findings are sufficiently clear to report, or when another exchange would
add nothing. Agreement is not proof, and disagreement is not a reason to consume
all three invocations.

Resume an eligible reviewer session when continuing the same review, such as
clarifying a finding, challenging it with evidence, checking an authorized
revision, or resolving a consequential disagreement. Recheck current files when
relevant; remembered context is not proof that files are unchanged. Use the
retained run ID and provide the main agent's responses, relevant source paths,
and what specifically needs checking. Keep findings and responses
distinguishable, and preserve material objections. Ask the reviewer to explain
which findings remain, changed, or were withdrawn and why.

Inspect the completed run with `subagent({ action: "status", id: runId })`, then
resume it with:

```js
subagent({
  action: "resume",
  id: runId,
  message: "Reconsider F1 against the following evidence..."
})
```

Use the actual retained ID and follow-up question. Resume checks eligibility
and starts a new child from the saved conversation context. It returns a new
run ID; retain that ID for the next turn. Return control and wait for native
completion as with the initial review. The stored reviewer contract is retained;
do not add model, runner, or permission overrides.

Start a fresh session for a separate review with a different purpose or
unrelated target, or when the user requests an assessment without the previous
review discussion. A clarification or revision check within the same review is
not a new review merely because files changed.

If the session cannot be resumed, report the limitation. A fresh invocation may
continue the review when allowance remains: include prior findings, their
identifiers, and the relevant context, and do not present it as a resumed
conversation. Starting a fresh session does not reset the invocation count for
the same user review request. Do not relabel a continuation as a new review to
bypass the limit.

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
