# Pi Kijun

Pi Kijun is a personal set of working standards for the Pi coding
agent. It keeps a small operating contract, on-demand skills, and durable
project context together without replacing Pi's normal workflow.

## Get started

You need an installed Pi CLI. Cloning this repository does **not** activate
Kijun. To activate it, run this from the repository root:

```sh
./setup.sh
```

The script links Kijun's `AGENTS.md` and nine skills into
`${PI_CODING_AGENT_DIR:-$HOME/.pi/agent}`. It skips links already applied and
refuses collisions or duplicate skill names under `~/.agents/skills/`.
Existing settings, credentials, packages, and sessions are left alone. An
independently installed skill with the same name, including `unslop`, is a
collision; inspect and resolve it yourself before rerunning setup.
Restart Pi or use `/reload` to discover the resources. To roll back, inspect
and remove only the symlinks pointing to this checkout; `setup.sh` does not
remove links.

## Usage

Once the resources have been activated, work with Pi in the usual conversation.
Kijun asks Pi to propose implementation changes for you to enter by default.
Pi edits implementation and behaviour files only with your approval. After you
review and accept the result, Pi updates relevant documentation and work records
without a separate request. Direct documentation requests permit edits without
an additional approval exchange. Git mutations always need a specific request.
Relevant skills supply guidance on demand; no special command is required.

Brainstorming develops the project charter and briefs, or suggests worthwhile
improvements when the next step is unclear. Suggestions do not automatically
become backlog items. Refinement prepares slices and task checklists.
Development implements selected work, and review checks the result against
acceptance criteria. Shared work-item guidance keeps
`docs/project/charter.md`, `docs/project/work.md`, and individual item files
consistent without a separate progress diary.

## Documentation

- [Project charter](docs/project/charter.md) explains the problem, value, success,
  and boundaries.
- [Current work](docs/project/work.md) lists open briefs and slices.
- [Workflow guide](docs/workflow.md) explains activities, records, acceptance,
  documentation timing, and concurrency boundaries.
- [Operating contract](pi/agent/AGENTS.md) and
  [Git skill](pi/agent/skills/git/SKILL.md) define change authority and Git rules.

## License

Licensed under the [MIT License](LICENSE). Copyright (c) 2026 Tom Jagus.
