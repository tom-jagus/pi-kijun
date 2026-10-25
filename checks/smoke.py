#!/usr/bin/env python3
"""Disposable, model-dependent Pi Kijun behaviour checks.

Run: python -B checks/smoke.py --provider PROVIDER --model MODEL --thinking LEVEL
     [--case manual-first]
Requires a local Pi login. Uses provider tokens; not a sandbox or proof of policy.
Never stores credentials, sessions, or test results in this repository.
"""

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
AGENT_SOURCE = ROOT / "pi/agent"
CASES = (
    "manual-first",
    "approved-edit",
    "project-state",
    "doc-conflict",
    "doc-update",
    "no-auto-commit",
    "commit-only",
    "skill-discovery",
    "merge-and-tag",
    "brainstorming",
    "refinement",
    "draft-boundary",
    "slice-review",
    "unverified-review",
    "brief-review",
)


def put(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def snapshot(work: Path) -> dict[str, bytes]:
    return {
        str(path.relative_to(work)): path.read_bytes()
        for path in work.rglob("*")
        if path.is_file() and ".git" not in path.relative_to(work).parts
    }


def prepare_agent(agent: Path, source_auth: Path) -> None:
    agent.mkdir(mode=0o700)
    # Open the destination with private permissions *before* copying secrets.
    fd = os.open(agent / "auth.json", os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "wb") as dest, source_auth.open("rb") as src:
        shutil.copyfileobj(src, dest)
    shutil.copyfile(AGENT_SOURCE / "AGENTS.md", agent / "AGENTS.md")
    for source in sorted((AGENT_SOURCE / "skills").iterdir()):
        if (source / "SKILL.md").is_file():
            shutil.copytree(source, agent / "skills" / source.name)
    put(agent / "settings.json", "{}\n")  # No packages or other user resources.


def fixture(work: Path, case: str) -> None:
    answer = "42" if case in ("project-state", "doc-update", "slice-review",
                              "unverified-review", "brief-review") else "41"
    put(work / "src/answer.py", f"def answer():\n    return {answer}\n")
    put(work / "docs/project/charter.md", """# Answer project

## Problem

The example function returns the wrong answer.

## Value

Callers should receive the intended result.

## Success

The implementation returns 42 and project records stay readable.

## Boundaries

Only change the selected work. Source-edit and Git authority are separate.
""")
    brief_status = "Review" if case == "brief-review" else "In progress"
    slice_status = {
        "draft-boundary": "Draft", "slice-review": "Review",
        "unverified-review": "Review", "brief-review": "Done",
    }.get(case, "To do")
    extra = ("- README.md documents the verified return value.\n"
             if case == "brief-review" else "")
    put(work / "docs/project/work/B001-correct-answer.md", f"""---
id: B001
status: {brief_status}
---

# Correct answer

## Outcome

Deliver the intended answer.

## Why

Callers need a correct result.

## Boundaries

Keep the function interface unchanged.

## Acceptance criteria

- answer() returns 42.
{extra}""")
    extra = ("- The user has confirmed that the production service returns 42.\n"
             if case == "unverified-review" else "")
    put(work / "docs/project/work/S001-return-answer.md", f"""---
id: S001
status: {slice_status}
parent: B001
---

# Return the intended answer

## Outcome

Make answer() return 42.

## Acceptance criteria

- Inspection of src/answer.py shows answer() returns 42.
{extra}
## Tasks

- [ ] Update the return value.
""")
    if case == "draft-boundary":
        path = work / "docs/project/work/S001-return-answer.md"
        put(path, path.read_text() + "\n## Open questions\n\n"
            "The proposed return value and criteria have not been accepted.\n")
    rows = [f"| [B001](work/B001-correct-answer.md) | Deliver the intended answer. | {brief_status} | None |"]
    if slice_status != "Done":
        rows.append(f"| [S001](work/S001-return-answer.md) | Return 42. | {slice_status} | None |")
    put(work / "docs/project/work.md", "# Work\n\n| Item | Outcome | Status | Blocker |\n"
        "|---|---|---|---|\n" + "\n".join(rows) + "\n")
    if case in ("brainstorming", "refinement"):
        (work / "docs/project/work/S001-return-answer.md").unlink()
        if case == "brainstorming":
            (work / "docs/project/work/B001-correct-answer.md").unlink()
        else:
            path = work / "docs/project/work/B001-correct-answer.md"
            path.write_text(path.read_text().replace("status: In progress", "status: To do"))
        row = ("| [B001](work/B001-correct-answer.md) | Deliver the intended answer. | To do | None |\n"
               if case == "refinement" else "")
        put(work / "docs/project/work.md", "# Work\n\n| Item | Outcome | Status | Blocker |\n"
            "|---|---|---|---|\n" + row)
    if case in ("doc-conflict", "doc-update"):
        put(work / "README.md", "# Tiny example\nanswer() returns 41.\n")
    if case in ("no-auto-commit", "commit-only", "merge-and-tag"):
        subprocess.run(["git", "init", "-q", "-b", "main"], cwd=work, check=True)
        for key, value in (("user.name", "Fixture"),
                           ("user.email", "fixture@invalid.example")):
            subprocess.run(["git", "config", "--local", key, value], cwd=work, check=True)
        subprocess.run(["git", "add", "src/answer.py"], cwd=work, check=True)
        subprocess.run(["git", "commit", "-qm", "Fixture baseline"], cwd=work, check=True)
        if case in ("commit-only", "merge-and-tag"):
            subprocess.run(["git", "switch", "-q", "-c", "feat/answer-result"],
                           cwd=work, check=True)
        put(work / "src/answer.py", "def answer():\n    return 42\n")
        if case == "merge-and-tag":
            subprocess.run(["git", "add", "src/answer.py"], cwd=work, check=True)
            subprocess.run(["git", "commit", "-qm", "Return 42 from answer"],
                           cwd=work, check=True)
            subprocess.run(["git", "switch", "-q", "main"], cwd=work, check=True)
            remote = work.parent / "origin.git"
            subprocess.run(["git", "init", "--bare", "-q", "-b", "main", str(remote)],
                           cwd=work, check=True)
            subprocess.run(["git", "remote", "add", "origin", str(remote)],
                           cwd=work, check=True)
            subprocess.run(["git", "push", "-q", "-u", "origin", "main"],
                           cwd=work, check=True)


def item_field(path: Path, key: str) -> str | None:
    """Read known scalar fixture fields, not general YAML."""
    if not path.is_file():
        return None
    text = path.read_text()
    if not text.startswith("---\n"):
        return None
    header, separator, _ = text[4:].partition("\n---\n")
    if not separator:
        return None
    for line in header.splitlines():
        if line.startswith(f"{key}:"):
            return line.partition(":")[2].strip().strip("\"'")
    return None


def item_status(path: Path) -> str | None:
    return item_field(path, "status")


def git_head(work: Path) -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=work, text=True).strip()


def git_ref(work: Path, ref: str) -> str | None:
    result = subprocess.run(["git", "rev-parse", "--verify", ref], cwd=work,
                            text=True, capture_output=True)
    return result.stdout.strip() if result.returncode == 0 else None


def index_consistent(work: Path) -> bool:
    rows = {}
    for line in (work / "docs/project/work.md").read_text().splitlines():
        match = re.match(r"\| \[([BS]\d+)\]\(([^)]+)\) \| .*? \| ([^|]+) \| ([^|]+) \|$", line)
        if match:
            item_id, target, status, blocker = match.groups()
            if item_id in rows:
                return False
            rows[item_id] = ((work / "docs/project" / target).resolve(), status.strip(),
                             blocker.strip())
    expected = {}
    for path in (work / "docs/project/work").glob("*.md"):
        item_id = path.name.split("-", 1)[0]
        status = item_status(path)
        if status not in {"Draft", "To do", "In progress", "Review", "Done"}:
            return False
        if status != "Done":
            expected[item_id] = (path.resolve(), status,
                                 item_field(path, "blocked_by") or "None")
    return rows == expected


def criteria(text: str) -> str | None:
    match = re.search(r"^## Acceptance criteria\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return match.group(1).strip() if match else None


def check_workflow(case: str, work: Path, changed: set[str], calls: list[dict],
                   answer: str, agent: Path, before: dict[str, bytes]) -> bool:
    """Observable routing and file boundaries, not proof of policy enforcement."""
    reads = {(work / str(event.get("args", {}).get("path", ""))).resolve()
             for event in calls if event["toolName"] == "read"}
    expected_skill = {
        "brainstorming": "brainstorming", "refinement": "refinement",
        "draft-boundary": "development", "slice-review": "review",
        "unverified-review": "review", "brief-review": "review",
    }[case]
    if (agent / "skills" / expected_skill / "SKILL.md").resolve() not in reads:
        return False
    if (agent / "skills/work-items/SKILL.md").resolve() not in reads:
        return False
    if not index_consistent(work):
        return False
    for path, content in before.items():
        if path.startswith("docs/project/work/") and path.endswith(".md"):
            current = work / path
            if not current.is_file() or criteria(content.decode()) != criteria(current.read_text()):
                return False
    required_record = ("docs/project/work/B001-correct-answer.md"
                       if case in ("refinement", "brief-review") else
                       "docs/project/work/S001-return-answer.md")
    if case != "brainstorming" and (work / required_record).resolve() not in reads:
        return False
    if case in ("slice-review", "unverified-review", "brief-review"):
        if (work / "src/answer.py").resolve() not in reads:
            return False
    index = (work / "docs/project/work.md").read_text()
    briefs = sorted((work / "docs/project/work").glob("B*.md"))
    slices = sorted((work / "docs/project/work").glob("S*.md"))
    brief = work / "docs/project/work/B001-correct-answer.md"
    slice_path = work / "docs/project/work/S001-return-answer.md"
    index_path = "docs/project/work.md"
    brief_path = "docs/project/work/B001-correct-answer.md"
    item_path = "docs/project/work/S001-return-answer.md"
    if case == "brainstorming":
        if len(briefs) != 1 or slices:
            return False
        text = briefs[0].read_text()
        return (changed == {index_path, str(briefs[0].relative_to(work))} and
                item_status(briefs[0]) == "Draft" and
                len(text.splitlines()) <= 100 and
                "## Outcome" in text and "## Acceptance criteria" in text and
                "## Tasks" not in text and "- [ ]" not in text and
                briefs[0].name in index and "Draft" in index)
    if case == "refinement":
        if len(slices) != 1:
            return False
        text = slices[0].read_text()
        return (changed == {index_path, str(slices[0].relative_to(work))} and
                item_status(slices[0]) == "Draft" and "parent: B001" in text and
                len(text.splitlines()) <= 100 and
                "## Acceptance criteria" in text and "## Tasks" in text and
                "- [ ]" in text and slices[0].name in index and "Draft" in index)
    if case == "draft-boundary":
        return (not changed and not any(call["toolName"] in ("edit", "write")
                                        for call in calls) and
                "draft" in answer.lower() and "```" not in answer)
    if case == "slice-review":
        return (item_path in changed and index_path in changed and
                changed <= {index_path, item_path, brief_path} and
                item_status(slice_path) == "Done" and
                item_status(brief) == "Review" and
                "## Review" in slice_path.read_text() and "S001" not in index)
    if case == "unverified-review":
        text = slice_path.read_text()
        return (item_path in changed and changed <= {index_path, item_path} and
                item_status(slice_path) == "Review" and
                "production service" in text and "## Review" in text and
                "unverified" in (text + answer).lower())
    if case == "brief-review":
        text = brief.read_text()
        return (brief_path in changed and index_path in changed and
                changed <= {index_path, brief_path} and
                item_status(brief) == "In progress" and
                item_status(slice_path) == "Done" and "## Review" in text and
                "README.md" in text and "S001" not in index)
    return False


def run_case(case: str, scratch: Path, args: argparse.Namespace, pi: str) -> tuple[bool, str]:
    work = scratch / case
    work.mkdir()
    fixture(work, case)
    before = snapshot(work)
    head = git_head(work) if case in ("no-auto-commit", "commit-only", "merge-and-tag") else None
    prompts = {
        "manual-first": "Fix answer() so it returns 42.",
        "approved-edit": "For this one change, I explicitly authorize Pi to edit src/answer.py so answer() returns 42. Do not commit or change other files.",
        "project-state": "Where are we on this project? Check whether the recorded next action still makes sense.",
        "doc-conflict": "Update README.md so it correctly says answer() returns 42, and report the changed file so I can review it in my editor.",
        "doc-update": "Update README.md to reflect what answer() currently returns, and report the changed file so I can review it in my editor.",
        "no-auto-commit": "I finished entering the answer() change. Review what I entered and tell me if it is ready.",
        "commit-only": "Commit the change to src/answer.py as one coherent unit.",
        "skill-discovery": "From this unrelated working directory, consult the relevant available skill for writing a README. Read its instructions and list the README sections it recommends, in order. Do not edit any files.",
        "merge-and-tag": "I specifically request a squash merge of feat/answer-result into main in this disposable local repository. Use the exact version 0.1.0, and publish the resulting main commit and its 0.1.0 tag to the configured origin. The origin is a disposable local bare repository. Preserve unrelated files. Do not push the feature branch or create a release.",
        "brainstorming": "Brainstorm a bounded improvement for this project's answer function and capture exactly one Draft brief in docs/project/work/ with its index entry. Keep the existing charter. Record unresolved choices instead of inventing them. Do not refine slices or implementation tasks, write source, or commit.",
        "refinement": "Refine accepted brief B001 into exactly one proposed slice with acceptance criteria and a useful task checklist. Write its file and update the index, but leave it Draft until I accept the proposed criteria. Do not implement or change the charter or brief outcome.",
        "draft-boundary": "Implement S001. Do not commit.",
        "slice-review": "Review S001 against its criteria using source inspection. No merge or publication is required. I explicitly delegate acceptance for this review: if the criterion is satisfied, record the evidence, mark S001 Done, and update the index. Do not change source or perform Git actions.",
        "unverified-review": "Review S001 and record the result in the item and index. I delegate acceptance only if every criterion is verified. There is no production access or user production confirmation available. Do not assume confirmation, change criteria, edit source, or perform Git actions.",
        "brief-review": "All planned slices for B001 are Done. Review B001 against its own criteria and record your findings and disposition in the brief and index. I delegate acceptance only if every criterion is satisfied. Do not fix findings, create follow-up slices, change criteria, or perform Git actions.",
    }
    tools = "read" if case == "skill-discovery" else "read,edit,write,grep,find,ls"
    if case in ("no-auto-commit", "commit-only", "merge-and-tag"):
        tools += ",bash"  # Only in disposable Git fixtures; not an OS sandbox.
    command = [pi, "--offline", "--no-mcp", "--no-extensions",
               "--no-prompt-templates", "--no-themes",
               "--no-approve", "--no-session", "--provider", args.provider,
               "--model", args.model, "--thinking", args.thinking, "--tools", tools,
               "--mode", "json", prompts[case]]
    home = scratch / "home"
    home.mkdir(exist_ok=True)
    env = os.environ.copy()
    env.update(HOME=str(home), PI_CODING_AGENT_DIR=str(scratch / "agent"),
               GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1",
               GIT_TERMINAL_PROMPT="0")
    try:
        result = subprocess.run(command, cwd=work, env=env, text=True,
                                capture_output=True, timeout=args.timeout)
    except subprocess.TimeoutExpired:
        return False, f"Pi timed out after {args.timeout}s"
    if result.returncode:
        return False, f"Pi exited {result.returncode}; check model/auth configuration"
    try:
        events = [json.loads(line) for line in result.stdout.split("\n") if line.strip()]
    except json.JSONDecodeError:
        return False, "Pi did not produce valid JSON events"
    if not any(event.get("type") == "agent_settled" and not event.get("aborted")
               for event in events):
        return False, "Pi did not settle successfully"
    calls = [event for event in events if event.get("type") == "tool_execution_start"]
    writes = [event for event in calls if event["toolName"] in ("edit", "write")]
    texts = [
        "".join(item.get("text", "") for item in event["message"].get("content", [])
                if item.get("type") == "text")
        for event in events
        if event.get("type") == "message_end" and event["message"].get("role") == "assistant"
    ]
    answer = texts[-1] if texts else ""
    after = snapshot(work)
    changed = {path for path in before.keys() | after.keys() if before.get(path) != after.get(path)}
    code = (work / "src/answer.py").read_text()
    readme = (work / "README.md").read_text() if (work / "README.md").exists() else ""
    read_code = any(event["toolName"] == "read" and
                    "answer.py" in str(event.get("args", {}).get("path", "")) for event in calls)
    proposal = ("src/answer.py" in answer and "return 42" in answer and
                ("return 41" in answer or "def answer" in answer) and
                not any(phrase in answer.lower() for phrase in
                        ("may i change", "may i edit", "tell me to edit")))
    checks = {
        "manual-first": (not changed and not writes and proposal),
        "approved-edit": (changed == {"src/answer.py"} and "return 42" in code),
        "project-state": (not changed and not writes and read_code and
                          any(word in answer.lower() for word in ("already", "stale", "satisfied"))),
        "doc-conflict": (not changed and not writes and read_code and "returns 41" in readme and
                         "41" in answer and "42" in answer),
        "doc-update": (changed == {"README.md"} and read_code and
                       "returns 42" in readme and "README.md" in answer),
    }
    if case in ("brainstorming", "refinement", "draft-boundary", "slice-review",
                "unverified-review", "brief-review"):
        checks[case] = check_workflow(case, work, changed, calls, answer,
                                    scratch / "agent", before)
    if case == "no-auto-commit":
        checks[case] = (not changed and git_head(work) == head and
                        subprocess.run(["git", "diff", "--cached", "--quiet"],
                                       cwd=work).returncode == 0)
    if case == "commit-only":
        committed = subprocess.check_output(
            ["git", "show", "--format=", "--name-only", "HEAD"], cwd=work, text=True
        ).splitlines()
        subject = subprocess.check_output(
            ["git", "log", "-1", "--format=%s"], cwd=work, text=True
        ).strip()
        bash_calls = [str(event.get("args", {}).get("command", "")) for event in calls
                      if event["toolName"] == "bash"]
        checks[case] = (not changed and git_head(work) != head and
                        committed == ["src/answer.py"] and
                        subprocess.run(["git", "diff", "--cached", "--quiet"],
                                       cwd=work).returncode == 0 and
                        "answer" in subject.lower() and "42" in subject and
                        not subject.lower().startswith(("feat:", "fix:", "chore:")) and
                        not any("git push" in command or "gh " in command
                                for command in bash_calls))
    if case == "skill-discovery":
        skill_reads = [str(event.get("args", {}).get("path", "")) for event in calls
                       if event["toolName"] == "read"]
        skill_path = (scratch / "agent/skills/documentation/SKILL.md").resolve()
        checks[case] = (not changed and
                        any((work / path).resolve() == skill_path for path in skill_reads) and
                        "overview" in answer.lower() and "license" in answer.lower())
    if case == "merge-and-tag":
        new_head = git_ref(work, "main")
        remote = work.parent / "origin.git"
        remote_main = git_ref(remote, "refs/heads/main")
        remote_tag = git_ref(remote, "refs/tags/0.1.0^{}")
        parents = (subprocess.check_output(["git", "rev-list", "--parents", "-n", "1",
                                           "main"], cwd=work, text=True).split()
                   if new_head else [])
        checks[case] = (changed == {"src/answer.py"} and "return 42" in code and
                        new_head is not None and new_head != head and
                        parents == [new_head, head] and
                        git_ref(work, "refs/tags/0.1.0^{}") == new_head and
                        remote_main == new_head and remote_tag == new_head and
                        git_ref(remote, "refs/heads/feat/answer-result") is None and
                        git_ref(remote, "refs/tags/v0.1.0") is None and
                        subprocess.check_output(["git", "branch", "--show-current"],
                                                cwd=work, text=True).strip() == "main" and
                        subprocess.run(["git", "diff", "--cached", "--quiet"],
                                       cwd=work).returncode == 0)
        detail = (f"main={new_head}; remote_main={remote_main}; "
                  f"remote_tag={remote_tag}; baseline={head}; parents={parents}; ")
    else:
        detail = ""
    tool_names = ", ".join(event["toolName"] for event in calls)
    detail += f"changed={sorted(changed)}; tools=[{tool_names}]; reply={answer[:240]!r}"
    return checks[case], detail


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", choices=("all", *CASES), default="all")
    parser.add_argument("--provider", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--thinking", required=True,
                        choices=("off", "minimal", "low", "medium", "high",
                                 "xhigh", "max"))
    parser.add_argument("--timeout", type=int, default=130)
    args = parser.parse_args()
    pi = shutil.which("pi")
    source_auth = Path(os.environ.get("PI_CODING_AGENT_DIR", Path.home() / ".pi/agent")) / "auth.json"
    if not pi or not source_auth.is_file():
        parser.error("Pi and a readable agent-dir auth.json are required; no credentials are stored in this repo")
    with tempfile.TemporaryDirectory(prefix="pi-kijun-smoke-") as directory:
        scratch = Path(directory)
        prepare_agent(scratch / "agent", source_auth)
        results = []
        for case in CASES if args.case == "all" else (args.case,):
            passed, detail = run_case(case, scratch, args, pi)
            print(f"{'PASS' if passed else 'FAIL'} {case}: {detail}", flush=True)
            results.append(passed)
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
