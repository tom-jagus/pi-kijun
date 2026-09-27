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

## Other documentation

Write for a clear audience and purpose. Prefer a short explanation and links to
authoritative material over repeated facts that can drift. Follow
`project-context` for project definition and progress.

## Vault notes

The configured vault is `~/vaults/default`. Work only within that vault, and
only on requested notes. Leave vault configuration, Git metadata, and attachments
alone unless separately authorized.

Before creating a note, inspect relevant existing category pages and the
matching template in `templates/`. Adapt the template to the requested note,
fill `{{title}}` and `{{date}}`, and write valid frontmatter—never leave
template placeholders in a finished note.

If a developed note has no suitable existing category, consider whether its
subject is a reusable area likely to connect multiple notes. If so, propose a
plain-named category before writing the note: explain its scope and how it
relates to existing categories. Wait for the user's choice. If approved, create
a category page with meaningful scope text, then write the note and its links.
If declined, use another category only when accurate; otherwise write the note
without a category link. Do not interrupt quick inbox or daily captures with
category proposals, or create a category for each product or one-off idea.

- `inbox/`: quick, possibly unfinished thoughts and captures.
- `notes/`: developed notes, including project notes.
- `categories/`: curated category pages, one folder level; use links between
  categories rather than nested directories.
- `daily/`: requested entries named `YYYY-MM-DD.md`.
- `templates/` and `assets/`: supporting files, not ordinary note destinations.

Name new `inbox/` and `notes/` files `YYYY-MM-DD-HHMMSS-<slug>.md`, using local
time. Form the slug from the trimmed title: lowercase it; replace control
characters and `< > : " / \ | ? *` with `-`; replace whitespace and underscores
with `-`; collapse repeated hyphens; and trim leading or trailing periods, hyphens,
and spaces. Use `untitled` if nothing remains. If that filename exists in the same
directory, append `-2`, `-3`, and so on before `.md` until unique.

Give category pages readable, plain-name filenames. Daily filenames remain
`YYYY-MM-DD.md`. Create a missing directory only when its first requested note
needs it.

New notes use simple YAML frontmatter: `aliases`, `tags`, and `created`.
Do not add `type`. Keep `created` unchanged on later edits. Use aliases for
human-readable links to timestamp-named notes. Use tags for cross-cutting
context or workflow state; use `[[links]]` to connect notes to category pages
and category pages to each other. Do not manufacture empty category pages.

Before creating a note, look for the same title or alias and relevant existing
notes. Preserve existing structure when editing. Pi may review and suggest
connections or further structure in both `inbox/` and `notes/`, but moving,
renaming, merging, or deleting notes requires a separate request; Neovim does
not currently auto-update links after a rename.

Project notes should contain a curated summary, selected decisions and lessons,
and dated meaningful status or milestone updates, with links to authoritative
repository documents. Do not mirror project documentation or update the vault
automatically after every project change.

After a consequential decision or reusable insight, Pi may briefly suggest a
note title, destination, and reason. A suggestion is not permission to write.
Requested edits follow write-then-review: report changed paths for Neovim
review. Pi never initiates vault Git actions. Neovim's automatic vault sync is
not yet reconciled with review-before-publication; warn about that limitation
rather than claiming a note cannot be published before review.

After requested documentation edits, name the changed paths and what remains
uncertain so the user can review the actual result in their editor. Writing a
draft is not acceptance of a material decision.
