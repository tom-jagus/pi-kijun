---
id: B004
status: To do
---

# Read-only installation check

## Outcome

Make it easy to determine whether a Kijun checkout is correctly linked into the
intended Pi agent directory, without changing the installation.

## Why

Setup creates links conservatively, but moving a checkout or changing the agent
directory can leave activation unclear. A diagnostic check would distinguish
installation problems from problems with model behaviour.

## Boundaries

Check Kijun-owned resource links and duplicate names in the standard shared
skill location. Respect the same agent-directory selection as setup and report
which checkout and directory are being examined. Do not repair links, remove
collisions, change settings, or claim to verify model compliance. Do not
reintroduce the removed formal workflow test machinery.

## Acceptance criteria

- The check distinguishes correct links, missing or broken links, links to
  another checkout, and unrelated entries at expected destinations.
- Duplicate Kijun skill names under the standard shared skill location are
  reported clearly.
- Output identifies the checkout and effective agent directory, including an
  explicitly configured agent directory.
- A healthy installation and an installation with problems produce distinct
  exit outcomes and understandable diagnostics.
- Running the check leaves installation resources, settings, and runtime data
  unchanged.
- Usage documentation states the diagnostic scope and does not equate correct
  links with reliable skill discovery or model behaviour.

## Accepted approach

Add `./setup.sh --check` so installation and diagnostics can share the resource
list and path rules. Keep no-argument setup behaviour unchanged. The user
accepted this interface and the outcome and criteria of B004 and S006.
