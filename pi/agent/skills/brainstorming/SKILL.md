---
name: brainstorming
description: Explore a project's purpose, outcomes, boundaries, or possible work. Use for charters, briefs, unsettled ideas, or suggestions when the user asks what is missing, what to improve, or what to do next without a defined outcome. Does not automatically refine slices, plan implementation, or create backlog items from suggestions.
---

# Brainstorming

Explore the problem and useful outcomes before planning implementation. Follow
the global operating contract. Discussion alone does not authorize file edits.
Load `work-items` before creating or maintaining project records.

## Establish the conversation

Read the existing charter and relevant briefs when present. Do not load every
slice or reopen accepted scope without a material conflict or new evidence.
Clarify who benefits, what is difficult, why improvement matters, and what
would demonstrate value. Challenge unnecessary scope and weak assumptions.

Distinguish observations, proposals, accepted decisions, and unresolved
questions. Discuss alternatives when they materially change the outcome or
constraints. Do not force a solution or a detailed design to fill a template.

## Suggest worthwhile next steps

When the user is unsure what else would help, inspect the project's purpose,
relevant implementation, and open work. Look for concrete user problems,
incomplete outcomes, repeated friction, and useful simplifications. This is
exploratory assessment, not acceptance review of existing delivery.

Offer a short ranked set of options. Explain the evidence, expected benefit,
main trade-off, and whether each option is existing work or a new proposal.
Prefer removing needless work over adding features without a clear benefit.
Say when nothing more appears worth doing; do not invent work to fill a list.

Keep suggestions in the conversation until the user chooses to capture or
pursue them. Do not automatically create briefs, slices, or task checklists.

## Record only the useful result

When the user asks to establish, capture, or revise project records, make the
necessary documentation edits without a separate edit-permission question:

- Establish or revise the charter's high-level content using the shared shape.
  Keep proposed scope changes explicit until the user accepts them.
- Capture a brief for a distinct bounded outcome worth revisiting. Update a
  matching brief rather than creating duplicates for each new thought.
- Leave unsettled briefs Draft. Record only the outcome, why it matters,
  boundaries, useful outcome-level criteria, and genuine open questions.
- Preserve concise material risks and accepted choices where they affect the
  work. Do not store the brainstorming transcript, discarded suggestions, or
  a generic list of possible features.

## Stop before refinement

Do not automatically create slices, implementation checklists, estimates,
architecture documents, or source changes. A brief is a useful output even
when its solution is not known. Say what needs deciding next, not everything
that could eventually be built.

When the user also requests refinement, name the transition and load
`refinement`. Ask before expanding scope when the original request does not
cover that activity. Do not ask for a procedural approval already covered by
the user's request. End with the current conclusion and only consequential
open questions; report changed paths if any.
