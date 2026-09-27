---
name: documentation
description: Write or revise a project's README, user-facing guides, reference docs, or notes in an explicitly configured vault. Use for README.md and ordinary documentation work. For docs/project/definition.md or docs/project/progress.md, use project-context instead.
---

# Documentation

Make documents useful to their readers without duplicating code or other docs.
Inspect the existing file and relevant repository sources before changing claims,
commands, links, or legal information. Follow the global documentation review
boundary; this skill does not grant source-edit or Git authority.

## README convention

Keep a consistent, simple shape across projects; omit inapplicable sections
rather than filling a template with placeholders:

1. **Overview:** Explain what the repository contains and why it exists in a
   few plain sentences.
2. **Get started:** Give prerequisites and the shortest working install/run
   path when applicable. Use commands that match the repository.
3. **Usage:** Show a minimal example or explain how to use it without restating
   the entire manual.
4. **Documentation:** Link to useful guides or reference material if they exist;
   keep links accurate and avoid duplicating their content.
5. **License and copyright:** Finish with the actual license and its file when
   one has been chosen. Include a copyright notice only with confirmed
   attribution. If either is unknown, ask rather than inventing a license,
   holder, or year; do not silently claim that public source is licensed.

Combine headings when that reads better, but retain the answers. Add badges,
screenshots, contribution instructions, status notes, and sponsor links only
when relevant and supported by real content; never add empty placeholders.

## Other documentation and notes

Write for a clear audience and purpose. Prefer a short explanation and links to
existing authoritative material over repeated facts that can drift. For
project definition or progress, follow `project-context` instead of turning a
README or guide into a second source of project state. Use only an explicitly
configured vault location; preserve the note's existing organization when
editing it.

After requested documentation edits, name the changed paths and what remains
uncertain so the user can review the actual result in their editor. Writing a
draft is not acceptance of a material decision.
