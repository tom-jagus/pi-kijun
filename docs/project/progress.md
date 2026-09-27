---
title: Pi Kijun Project Progress
status: active
---

# Project Progress

## Current State

- **Phase:** Project documentation and architecture review.
- **Definition:** Draft; updated with the agreed main-agent working style and
  source, documentation, vault, and Git boundaries; awaiting user acceptance.
- **Implementation:** No Pi Kijun configuration, skills, extensions, or tests
  have been created. Git is initialized on `main` with no commits or remote.
- **Project context:** A concise definition and this progress file have been
  drafted. The earlier decision register remains as historical material pending
  review and retirement; the new definition governs the current proposal.
- **Architecture:** `docs/architecture-draft.md` is a temporary discussion aid,
  now proposing a source tree that mirrors selected paths under `~/.pi/agent/`
  and `~/.agents/skills/`; it is not an adopted file inventory.

## Open Questions

- Which, if any, existing permission extension meets the desired per-change and
  session source-edit approval semantics across all relevant tools and modes?
- Which material project-definition changes need explicit user acceptance
  before further work proceeds? For now, always report changed paths, offer a
  diff, and do not treat unreviewed material scope changes as settled.
- Which Mentor Git conventions still reflect the user's current standards?
  Specify them before implementing mutating Git guidance.
- Which individual resources should be linked into Pi, and how should linkage
  be tested without replacing the existing local settings or runtime data?

## Next Action

Review the updated definition and temporary architecture, particularly the
proposed source-to-user-path mapping. Revise them based on feedback, then retire
the historical decision register once its still useful context is captured.
Only then start configuration or extension work.
