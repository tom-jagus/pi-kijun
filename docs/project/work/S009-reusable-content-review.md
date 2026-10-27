---
id: S009
status: Done
parent: B007
---

# Define reusable content-review guidance

## Outcome

Provide a reusable `content-review` skill and a read-only `content-reviewer`
agent definition for documentation and work items, independently inspectable
before subagent integration.

## Acceptance criteria

- The skill supports ordinary documentation, draft briefs, and slices without
  inventing project records for an ad hoc review. It is usable in a normal
  session without a subagent extension.
- Guidance checks factual support against relevant sources, internal consistency,
  omissions, ambiguity, and readability for the intended audience. Findings name
  locations, explain their consequences, and distinguish material defects,
  optional preferences, and unverified claims. No material findings is a valid
  result.
- Guidance checks that essential terminology, explanations, and instructions are
  understandable using the document and clearly linked project material, without
  external searches. It flags excessive cross-referencing when a short local
  explanation would help, while permitting external evidence for fact-checking.
- Draft work-item review examines outcome clarity, boundaries, assumptions,
  dependencies, open decisions, and testable acceptance criteria. It checks
  relevant project decisions and loads `work-items` for record structure without
  taking authority to maintain records. It judges drafts as drafts and does not
  silently accept proposals or redefine scope.
- The skill remains distinct from delivery acceptance in `review`. It can reuse
  `unslop` for prose assessment without reducing content review to wording edits.
- The `content-reviewer` definition directs the agent to load the skill, inspect
  actual files and relevant supporting sources, and return evidence-based
  findings. Its intended tool set excludes mutation tools and unrestricted shell
  access; runtime restrictions are verified in S010.
- The reviewer does not edit files, accept work, launch further reviewers, or
  inherit the main agent's editing or Git permissions. Follow-up guidance asks it
  to reconsider findings against evidence without requiring agreement.
- The proposed guidance can be applied to representative documentation, a draft
  brief, and a slice, with the resulting assessment and limitations available for
  user review.

## Tasks

- [x] Inspect current contract, review and work-item guidance, setup behavior, and
  the chosen agent-definition format; confirm authority before behaviour edits.
- [x] Write the content-review skill and reviewer definition with the agreed
  scope, evidence requirements, and authority boundaries.
- [x] Assess representative documents using the guidance and identify any
  ambiguity or unnecessary overlap with existing skills.
- [x] Check naming, links, wrapping, and whitespace; present the result for
  acceptance without treating it as activated subagent integration.

## Risks

S008 may change overlapping authority guidance. Recheck accepted rules before
editing and coordinate shared files rather than treating file overlap as a
completion dependency.

## Review

The user accepted the skill and reviewer definition after inspecting both files.
The implementation covers the content, draft-stage, reporting, and authority
criteria in `pi/agent/skills/content-review/SKILL.md` and
`pi/agent/agents/content-reviewer.md`.

Static checks passed for metadata, relative references, wrapping, and whitespace.
A same-session walkthrough covered the workflow guide, this slice, and a
hypothetical draft with task-only criteria and an explicit open question. This
was not an independent subagent test. Activation, effective runtime tool
restrictions, and bounded exchange verification remain in S010.
