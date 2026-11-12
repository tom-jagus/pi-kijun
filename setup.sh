#!/usr/bin/env bash
# Link only Pi Kijun's own user-level resources. Never replace existing entries.
set -euo pipefail

if (( $# != 0 )); then
  echo "setup.sh takes no arguments" >&2
  exit 2
fi

root=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
source_dir="$root/pi/agent"
agent_dir="${PI_CODING_AGENT_DIR:-$HOME/.pi/agent}"
[[ "$agent_dir" == /* ]] || { echo "Agent directory must be absolute" >&2; exit 1; }
[[ ! -L "$agent_dir" ]] || { echo "Agent directory is a symlink: $agent_dir" >&2; exit 1; }
[[ ! -e "$agent_dir" || -d "$agent_dir" ]] || {
  echo "Agent directory is not a directory: $agent_dir" >&2; exit 1;
}

resources=(
  AGENTS.md
  skills/brainstorming
  skills/refinement
  skills/development
  skills/review
  skills/content-review
  agents/content-reviewer.md
  skills/work-items
  skills/project-context
  skills/personal-memory
  skills/documentation
  skills/git
  skills/unslop
)

present() { [[ -e "$1" || -L "$1" ]]; }
ours() { [[ -L "$2" && $(readlink -- "$2") == "$1" ]]; }

for directory in skills agents; do
  if present "$agent_dir/$directory" &&
     { [[ ! -d "$agent_dir/$directory" ]] || [[ -L "$agent_dir/$directory" ]]; }; then
    echo "Resource directory is not a regular directory: $agent_dir/$directory" >&2
    exit 1
  fi
done

# Check all sources and destinations before creating any links. Races or I/O
# failures can still leave a partial setup; rerunning skips links already made.
for resource in "${resources[@]}"; do
  source="$source_dir/$resource"
  destination="$agent_dir/$resource"

  if [[ "$resource" == AGENTS.md || "$resource" == agents/* ]]; then
    [[ -f "$source" ]] || { echo "Missing source: $source" >&2; exit 1; }
  else
    [[ -f "$source/SKILL.md" ]] || { echo "Missing skill: $source" >&2; exit 1; }
    shared="$HOME/.agents/skills/${resource#skills/}"
    if present "$shared"; then
      echo "Duplicate skill discovery path: $shared" >&2
      exit 1
    fi
  fi

  if present "$destination" && ! ours "$source" "$destination"; then
    echo "Refusing to replace unrelated entry: $destination" >&2
    exit 1
  fi
done

for resource in "${resources[@]}"; do
  source="$source_dir/$resource"
  destination="$agent_dir/$resource"
  if ours "$source" "$destination"; then
    echo "Already linked: $destination"
  else
    mkdir -p -- "$(dirname -- "$destination")"
    ln -s -- "$source" "$destination"
    echo "Linked: $destination -> $source"
  fi
done
