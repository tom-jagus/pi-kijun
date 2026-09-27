---
title: Pi Kijun Project Progress
status: active
---

# Project Progress

## Current State

- **Phase:** Live workflow evaluation.
- **Definition:** Accepted; records the working style and change boundaries.
- **Implementation:** The global contract and four on-demand skills are linked
  into live Pi through `setup.sh`; all five symlink targets were verified. The
  user restarted Pi and reports that it loaded them. Earlier disposable checks
  covered skill discovery, behavioural boundaries, Git merge/tag handling,
  and setup collisions; the model-dependent runner remains local, not shipped.
  These checks do not establish enforcement. No extensions are installed for
  Kijun. Git is on `first-version` with no remote.
- **Project context:** The two-file definition and progress model is in place;
  stable scope and rationale belong in `definition.md`.
- **Repository guide:** `README.md` explains purpose, setup, use, and document
  links. The repository has an MIT `LICENSE` file.

## Open Questions

- Permission extensions are deferred unless real use shows a need. The
  preliminary review found no verified match for narrow, revocable grants;
  behavioural guidance and human review are not technical enforcement.
- Live resource loading is user-confirmed. This documentation update exercises
  the live write-then-review path; manual-first source work still needs a normal
  live trial. The existing local `0.1.0` tag points to the bootstrap commit,
  so any future default-branch merge needs a different user-chosen version.

## Next Action

Try a low-risk manual-first source request in live Pi and review its response.
If the workflow feels right, decide whether to prepare a release; publishing
would also require an agreed remote and an unused version.
