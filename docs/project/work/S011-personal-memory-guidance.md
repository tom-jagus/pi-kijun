---
id: S011
status: Done
parent: B008
---

# Support on-demand personal memory

## Outcome

Provide short global instructions and a `personal-memory` skill so Pi can use
and maintain one private Markdown memory file without an extension.

## Acceptance criteria

- Global guidance directs the agent to consider memory when personal context
  may help and to read it on explicit request. It does not inject memory into
  every session or promise that the model will always select it.
- The skill describes a concise, topic-grouped Markdown file under
  `~/.pi/agent`, separate from tracked repository resources. It explains how to
  inspect and manually edit the file, and how a missing or unavailable file
  affects use without preventing ordinary work.
- The agent may propose additions or corrections, and handles requested
  additions, corrections, and deletions. It changes memory only with explicit
  user approval; a request specifying the change provides approval. Proposed
  entries do not become active before approval.
- Guidance distinguishes memory from operating policy and project records,
  treats entries as fallible context, and surfaces consequential conflicts
  with newer statements or instructions. Source and freshness are recorded
  when useful, without requiring a schema for every entry.
- Guidance explains that reading the file exposes its contents to the model
  provider and may retain them in session history. It addresses corrections,
  deletion, stale context in current sessions, and concurrent edits without
  claiming that deletion erases existing copies.
- Setup can discover the skill without replacing existing machine-owned data,
  settings, or unrelated resources. An alternate agent directory is handled
  consistently or its limitation is explicit. No personal content is committed.
- Representative examples cover a relevant request, an explicit read, a
  proposed change, an approved change, and missing memory. Evidence separates
  observed behavior from guarantees and identifies unverified cases.

## Tasks

- [ ] Inspect current global guidance and setup resource rules; settle the exact
  memory path and alternate-agent-directory behavior without replacing data.
- [ ] Obtain bounded Pi-edit approval before changing behavior or setup files.
- [ ] Add the global reminder, skill, and necessary resource discovery changes.
- [ ] Demonstrate representative cases with synthetic content and present the
  result for acceptance, including privacy and behavioral limitations.
- [x] After acceptance, update relevant documentation and records.

## Review

Accepted under the user's delegated conditional acceptance. Global guidance,
private-file behavior, approval boundaries, and privacy limitations are present
in the contract and skill. The user reported that Pi loaded and used the skill
and that a missing memory file was reported. Conversation examples covered
explicit reading, proposed changes, and approved changes using real memory, not
synthetic content. An isolated setup check linked the skill in an alternate
agent directory without creating memory; a conflicting resource was preserved
and prevented link creation. These observations do not guarantee model behavior.
