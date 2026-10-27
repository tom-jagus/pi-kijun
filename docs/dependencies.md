# Workflow dependencies

This guide separates packages needed for Kijun features from optional tools used
in the owner's workflow. A Pi package can supply extensions, skills, and prompt
templates. Installing a package and choosing which resources load are separate
steps.

[`setup.sh`](../setup.sh) links Kijun's own resources only. It does not install
packages or change settings, credentials, model selection, or editor config.
Use Pi's package commands yourself when you choose to add a dependency. Review
third-party code before installation; extensions execute code on your machine.

## Baseline

Kijun needs an installed Pi CLI and Bash to run `setup.sh`. Model-backed work
also needs a configured model and its provider credentials. The current
integration was inspected with Pi 1.4.0 and `pi-subagents` 0.83.0. These are a
known working baseline for the initial independent review, not a claim that all
integration scenarios or other version combinations have been tested.

Without extra packages, Kijun's contract, activity skills, project records, and
same-session content review remain usable. Independent content review needs the
additional package below.

## Independent content review

[`pi-subagents`](https://github.com/nicobailon/pi-subagents) starts the
`content-reviewer` child agent and returns its findings to the main session.
Kijun uses this existing extension without modifying it. The package supports
more workflows than Kijun authorizes; installing it does not authorize other
agents, automatic reviews, or autonomous revision loops.

### Install and configure

1. Follow the [README setup instructions](../README.md#get-started) to link the
   Kijun skill and reviewer definition. Resolve collisions rather than replacing
   unrelated resources.
2. Run `pi list` and inspect your existing package declaration before changing
   it. If `pi-subagents` is absent, install the inspected version:

   ```sh
   pi install npm:pi-subagents@0.83.0
   ```

   If another version is already installed, decide explicitly whether to keep
   it or change it. Compatibility beyond the baseline has not been verified.
3. In the user agent directory's `settings.json`, normally
   `~/.pi/agent/settings.json`, use this entry within the existing `packages`
   array. If `PI_CODING_AGENT_DIR` is set, use that directory instead. Replace
   only the entry for this package, preserving other packages and settings:

   ```json
   {
     "source": "npm:pi-subagents@0.83.0",
     "extensions": ["bundle/index.js"],
     "skills": [],
     "prompts": []
   }
   ```

   This is one array entry, not a replacement settings file. It enables the
   extension and disables the package's bundled skills and prompt templates.
   Kijun supplies its own review skill and agent definition. These package
   filters do not themselves restrict a child agent's tools or remove the
   extension's built-in agents.
4. Restart Pi or use `/reload`. Check for package-loading errors. A trusted
   project's `.pi/settings.json` can override a user-level package entry;
   inspect that file if the effective resources differ from this configuration.

### Verify activation

Run `pi list` to confirm the declaration, then ask Pi:

```text
Independently review docs/dependencies.md for someone setting up Kijun.
```

The main agent should select the user-level `content-reviewer`, launch it, and
return findings without manual copying. Depending on tool activation, it may
first call `subagents_enable` to expose `subagent`. A package declaration alone
is not proof that a reviewer launch succeeds. Missing tools or launch failures
must be reported as unavailable or incomplete review, not a clean result.

The reviewer definition is linked at `agents/content-reviewer.md` in the user
agent directory. Its intended tools are only `read`, `grep`, `find`, and `ls`,
with ambient extensions and nested delegation disabled. For the observed initial
run, the capability audit reported exactly those tools, no MCP tools, and
ambient extensions disabled. This is tool-level restriction, not an
operating-system sandbox or a guarantee about every future launch.

The [delegation guidance](../pi/agent/skills/content-review/references/delegation.md)
requires fresh context and at most three reviewer invocations per user review
request, including failures and retries. The invocation limit is main-agent
guidance, not a runtime-enforced counter. Plain content review stays in the main
session unless independent review is requested. Model choice remains with the
user; the reviewer does not pin a model. A model requiring an extension-based
provider may be incompatible with the restricted launch configuration. Report
that conflict rather than silently weakening restrictions or changing models.

A successful initial review does not verify every exchange case. Follow-up
isolation, evidence-based clarification, disagreement at the invocation limit,
and failure or cancellation handling still need hands-on verification for
[S010](project/work/S010-bounded-content-review-exchanges.md).

### Roll back

If you changed an existing package declaration, restore that entry rather than
removing a package used by other workflows. If you added the package solely for
this feature and no longer need it, remove it with:

```sh
pi remove npm:pi-subagents@0.83.0
```

Restart Pi or use `/reload`, then check `pi list`. Removing the package disables
independent review but leaves Kijun's same-session content-review skill usable.
It does not remove Kijun's resource links. To remove those too, inspect and
remove only symlinks pointing to this checkout, as described in the
[README](../README.md#get-started). Do not delete unrelated agent definitions,
settings, credentials, or session artifacts.

## Optional personal packages

These packages are configured in the owner's workflow, but are not required for
Kijun's core guidance or independent reviewer. Versions below were observed in
the local installation, not established as required or fully tested versions.
Install only the tools you want. The examples pin those observed versions so
that a later installation does not silently select a different release.

| Package | Observed version | Purpose | Without it |
|---|---|---|---|
| [`@ff-labs/pi-fff`](https://github.com/dmtrKovalenko/fff/tree/main/packages/pi-fff) | 0.11.0 | Indexed file and content search through `fffind` and `ffgrep`. | Use Pi's built-in search tools or shell commands. |
| [`pi-nvim`](https://github.com/carderne/pi-nvim) | 0.2.6 | Send files, selections, and prompts from Neovim to Pi. | Work directly in Pi and the editor. |
| [`pi-web-search`](https://github.com/ttttmr/pi-web-search) | 1.7.0 | Provider-backed web search through `web_search`. | Local work remains usable; report unavailable web verification rather than silently substituting another search method. |

Run only the installation commands you choose:

```sh
pi install npm:@ff-labs/pi-fff@0.11.0
pi install npm:pi-nvim@0.2.6
pi install npm:pi-web-search@1.7.0
```

Restart Pi or use `/reload` after installation or configuration changes.

- For `pi-fff`, the default mode adds search tools and file autocomplete. Run
  `/fff-health` in a project to check indexing. No custom configuration is
  required for that mode; consult its linked README before changing indexing
  scope or tool replacement settings.
- For `pi-nvim`, installing the Pi package is only half of the setup. Install
  `carderne/pi-nvim` through your Neovim plugin manager and call
  `require("pi-nvim").setup()` in your editor configuration, following its
  linked README. Run `:PiPing` in Neovim with Pi running to check connectivity.
  Editor changes remain a separate, explicit choice.
- For `pi-web-search`, select a supported model and authenticate its provider.
  No extra package configuration is needed to use the current model. Ask for a
  web search to verify an actual request succeeds; tool availability alone does
  not verify credentials or provider support. A dedicated search model is an
  explicit option in `web-search.json`, not an automatic fallback. Searches
  send queries and supplied URLs to the selected provider and may incur charges.

To remove one of these packages, use `pi remove` with its configured source from
`pi list`, then restart or reload Pi. Restore a prior declaration if you changed
an existing setup instead of removing it. Package removal does not undo separate
Neovim configuration or remove all package-specific configuration and runtime
data. Preserve those resources unless you explicitly choose to remove them.

These optional packages are not inherited by Kijun's restricted reviewer. A
reviewer that needs unavailable external evidence must disclose that limitation.
This list covers the Pi packages above, not every editor plugin, terminal tool,
or machine-local extension in the owner's environment.

## Maintain the list

Before changing a version, inspect release notes, preserve existing resource
filters, and verify the affected feature. Update this guide when a dependency,
required configuration, or verified baseline changes. Do not copy a whole
machine's settings or credentials into the repository. No installation script
or automatic package synchronization is provided.
