---
id: S007
status: To do
parent: B005
---

# Remove vault-specific instructions and routing

## Outcome

Remove obsolete personal vault support from Kijun's active guidance while
preserving repository documentation behaviour and general authority boundaries.

## Acceptance criteria

- `pi/agent/skills/documentation/SKILL.md` no longer contains the vault section
  or advertises vault work in its description. Its general documentation and
  README conventions remain intact.
- `pi/agent/AGENTS.md` no longer configures vault-specific authority or routes
  documentation work to vault notes. The development skill no longer includes
  obsolete vault-specific handoff instructions.
- `docs/workflow.md` describes repository documentation without advertising
  vault support or retaining obsolete vault-specific exceptions.
- Active instructions no longer prescribe a vault destination, note naming,
  templates, frontmatter, categories, note suggestions, or Neovim sync handling.
  No replacement reference or skill is created, and the contract and skills
  gain no mention of manual journaling or note-taking as a replacement.
- Automatic documentation maintenance remains scoped to relevant repository
  documentation and records. General source-edit approval, acceptance timing,
  and separately requested Git authority retain their existing meaning.
- A repository search accounts for remaining vault mentions, distinguishing
  work records and historical context from active instructions. No historical
  record is rewritten merely to eliminate the word.
- Actual vault notes, configuration, attachments, external tools, and live
  installation resources are not changed as part of the removal.

## Tasks

- [ ] Inspect vault references across the contract, skills, and workflow guide,
  and confirm edit authority for the behaviour-defining files.
- [ ] Remove vault-specific content and routing from the documentation skill,
  operating contract, and development skill without broadening permissions.
- [ ] Compare remaining documentation guidance with the original to check that
  README conventions, factual checks, and authority rules are preserved.
- [ ] Search for stale active references, check links and prose wrapping, and
  run diff-whitespace checks without inspecting or modifying the actual vault.
- [ ] Present the behaviour changes for acceptance before aligning the workflow
  guide and recording completion under the normal documentation timing rules.
