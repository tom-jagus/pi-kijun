# Pi Kijun

Pi Kijun is a personal set of working standards for the Pi coding
agent. It keeps a small operating contract, on-demand skills, and durable
project context together without replacing Pi's normal workflow.

## Get started

You need an installed Pi CLI. Cloning this repository does **not** activate
Kijun. When ready for a live trial, run this from the repository root:

```sh
./setup.sh
```

The script links Kijun's `AGENTS.md` and four skills into
`${PI_CODING_AGENT_DIR:-$HOME/.pi/agent}`. It skips links already applied and
refuses collisions or duplicate skill names under `~/.agents/skills/`.
Existing settings, credentials, packages, and sessions are left alone.
Restart Pi (or use `/reload`) to discover the resources. To roll back, inspect
and remove only the five symlinks pointing to this checkout; `setup.sh` does
not remove links.

## Usage

Once the resources have been activated, work with Pi in the usual conversation.
Kijun asks Pi to propose source changes for you to enter by default, write
requested documentation for your review, and perform Git mutations only when
specifically asked. Relevant skills supply guidance on demand; no special
command is required.

## Documentation

- [Project definition](docs/project/definition.md) — scope, change boundaries,
  and Git standards.
- [Project progress](docs/project/progress.md) — current development state and
  next action.

## License

Licensed under the [MIT License](LICENSE). Copyright (c) 2026 Tom Jagus.
