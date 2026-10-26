---
id: S006
status: To do
parent: B004
---

# Diagnose installation without changing it

## Outcome

Provide `./setup.sh --check` as a read-only diagnostic for the current checkout's
Kijun resource links, with clear output and documented limits.

## Acceptance criteria

- Check mode reports the checkout, effective agent directory, and health of
  every expected resource using the same resource list and path rules as
  installation. It respects `PI_CODING_AGENT_DIR` and the default directory.
- Diagnostics distinguish correct links, missing destinations, broken links,
  links to another checkout, and unrelated files or directories. Missing source
  resources and invalid agent or skills directory layouts are also reported.
- Duplicate Kijun skill names under `$HOME/.agents/skills/` are reported,
  including dangling entries, without searching arbitrary configured paths
  or claiming to inspect Pi's complete discovery state.
- Check mode reports all safely inspectable problems rather than stopping at
  the first unhealthy resource. If an invalid directory layout prevents safe
  inspection, it explains the limitation without following it into writes.
- Exit code 0 indicates a healthy installation, 1 indicates installation or
  inspection problems, and 2 indicates invalid command usage. Unsupported
  arguments are rejected without entering installation mode.
- Check mode does not create directories or links, remove or repair entries,
  or change settings or runtime data, including when no installation exists.
- No-argument installation retains its collision checks, preflight-before-link
  behaviour, and ability to skip links already applied. Check mode cannot
  fall through into installation after success or failure.
- README instructions explain how to run the check, interpret its result,
  and understand its scope. Healthy links do not prove skill loading or model
  compliance, and diagnostics never authorize automatic repairs.

## Tasks

- [ ] Inspect setup's path, resource, and collision rules before implementing
  the accepted `--check` interface.
- [ ] Add explicit argument dispatch and read-only diagnostics, sharing resource
  and path definitions without weakening installation safeguards.
- [ ] Validate healthy, absent, broken, conflicting, duplicate, and alternate
  agent-directory cases using isolated temporary fixtures, not the live setup.
- [ ] Verify no-argument installation and rerun behaviour in isolated fixtures,
  and compare fixture state before and after diagnostic runs for unexpected
  writes. Keep validation proportionate; do not add a workflow test framework.
- [ ] Run Bash syntax and diff-whitespace checks and present implementation
  evidence for acceptance before updating related documentation and records.
- [ ] After acceptance, document the command and diagnostic limits in README.
