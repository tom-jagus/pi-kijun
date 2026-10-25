"""Deterministic resource, setup, and fixture checks. No model calls or login."""

import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import tempfile
import unittest

import smoke


ROOT = Path(__file__).resolve().parents[1]
SKILLS = {
    "brainstorming", "refinement", "development", "review", "work-items",
    "project-context", "documentation", "git", "unslop",
}
STATUSES = {"Draft", "To do", "In progress", "Review", "Done"}


def header(text: str) -> str:
    if not text.startswith("---\n"):
        raise AssertionError("Missing frontmatter")
    value, separator, _ = text[4:].partition("\n---\n")
    if not separator:
        raise AssertionError("Unterminated frontmatter")
    return value


def scalar(text: str, key: str) -> str | None:
    """Read known scalar fields in repository records, not arbitrary YAML."""
    for line in header(text).splitlines():
        if line.startswith(f"{key}:"):
            return line.partition(":")[2].strip().strip("\"'")
    return None


class RecordTests(unittest.TestCase):
    def test_skill_metadata_and_resources(self):
        directories = {path.parent.name for path in
                       (ROOT / "pi/agent/skills").glob("*/SKILL.md")}
        self.assertEqual(directories, SKILLS)
        for name in SKILLS:
            with self.subTest(skill=name):
                text = (ROOT / f"pi/agent/skills/{name}/SKILL.md").read_text()
                self.assertEqual(scalar(text, "name"), name)
                description = scalar(text, "description")
                # Unslop uses a folded YAML description; inspect its body below.
                if description in (">-", ">", "|-", "|"):
                    description = " ".join(line.strip() for line in
                                           header(text).splitlines()[2:])
                self.assertTrue(description)
                self.assertLessEqual(len(description), 1024)
        self.assertTrue((ROOT / "pi/agent/skills/work-items/references/records.md").is_file())

    def test_charter_and_items(self):
        charter = (ROOT / "docs/project/charter.md").read_text()
        headings = re.findall(r"^## (.+)$", charter, re.M)
        self.assertEqual(headings[:4], ["Problem", "Value", "Success", "Boundaries"])
        self.assertIn(headings[4:], ([], ["Risks"]))
        records = {}
        for path in sorted((ROOT / "docs/project/work").glob("*.md")):
            text = path.read_text()
            item_id = scalar(text, "id")
            self.assertRegex(item_id or "", r"^[BS]\d{3,}$")
            self.assertNotIn(item_id, records)
            self.assertTrue(path.name.startswith(f"{item_id}-"))
            self.assertRegex(path.name, r"^[BS]\d{3,}-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
            status = scalar(text, "status")
            self.assertIn(status, STATUSES)
            keys = re.findall(r"^([a-z_]+):", header(text), re.M)
            self.assertEqual(len(keys), len(set(keys)))
            self.assertLessEqual(set(keys),
                                 {"id", "status", "parent", "depends_on", "blocked_by"})
            headings = re.findall(r"^## (.+)$", text, re.M)
            required = (["Outcome", "Why", "Boundaries", "Acceptance criteria"]
                        if item_id.startswith("B") else
                        ["Outcome", "Acceptance criteria", "Tasks"])
            self.assertEqual(headings[:len(required)], required)
            dependencies = re.findall(r"^  - ([BS]\d+)\s*$", header(text), re.M)
            records[item_id] = (path, text, status, dependencies)
        for item_id, (_, text, _, dependencies) in records.items():
            parent = scalar(text, "parent")
            if parent:
                self.assertTrue(item_id.startswith("S"))
                self.assertTrue(parent.startswith("B"))
                self.assertIn(parent, records)
            for dependency in dependencies:
                self.assertIn(dependency, records)
                self.assertNotEqual(dependency, item_id)

        def visit(item_id, chain):
            self.assertNotIn(item_id, chain, "Dependency cycle")
            for dependency in records[item_id][3]:
                visit(dependency, chain | {item_id})

        for item_id in records:
            visit(item_id, set())
        index = (ROOT / "docs/project/work.md").read_text()
        rows = {}
        for line in index.splitlines():
            match = re.match(r"\| \[([BS]\d+)\]\(([^)]+)\) \| (.*?) \| (.*?) \| (.*?) \|$", line)
            if match:
                item_id, target, _, status, blocker = match.groups()
                self.assertNotIn(item_id, rows)
                rows[item_id] = status
                path, text, expected, _ = records[item_id]
                self.assertEqual((ROOT / "docs/project" / target).resolve(), path.resolve())
                self.assertEqual(status, expected)
                self.assertEqual(blocker, scalar(text, "blocked_by") or "None")
        self.assertEqual(set(rows), {key for key, value in records.items()
                                     if value[2] != "Done"})

    def test_links_outside_examples(self):
        paths = [ROOT / "README.md", ROOT / "pi/agent/AGENTS.md"]
        for directory in ("docs", "pi/agent/skills"):
            paths.extend((ROOT / directory).rglob("*.md"))
        for path in paths:
            # Example record links are illustrative, not repository targets.
            prose = re.sub(r"^```[^\n]*\n.*?^```\s*$", "", path.read_text(),
                           flags=re.M | re.S)
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", prose):
                if "://" in target or target.startswith("#"):
                    continue
                with self.subTest(path=str(path.relative_to(ROOT)), target=target):
                    self.assertTrue((path.parent / target.split("#")[0]).exists())
        self.assertFalse((ROOT / "project").exists())
        self.assertFalse((ROOT / "docs/project/definition.md").exists())
        self.assertFalse((ROOT / "docs/project/progress.md").exists())


class SetupTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="pi-kijun-setup-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = self.root / "checkout"
        shutil.copytree(ROOT / "pi", self.repo / "pi")
        shutil.copyfile(ROOT / "setup.sh", self.repo / "setup.sh")
        self.home = self.root / "home"
        self.home.mkdir()
        self.agent = self.home / ".pi/agent"
        self.env = os.environ.copy()
        self.env.update(HOME=str(self.home), PI_CODING_AGENT_DIR=str(self.agent))

    def run_setup(self, *arguments):
        return subprocess.run(["bash", str(self.repo / "setup.sh"), *arguments],
                              cwd=self.repo, env=self.env, text=True,
                              capture_output=True)

    def test_links_all_resources_and_is_idempotent(self):
        self.agent.mkdir(parents=True)
        settings = self.agent / "settings.json"
        settings.write_text('{"machine_owned": true}\n')
        result = self.run_setup()
        self.assertEqual(result.returncode, 0, result.stderr)
        for resource in ["AGENTS.md", *(f"skills/{name}" for name in SKILLS)]:
            link = self.agent / resource
            self.assertTrue(link.is_symlink())
            self.assertEqual(link.resolve(), (self.repo / "pi/agent" / resource).resolve())
        self.assertEqual(settings.read_text(), '{"machine_owned": true}\n')
        second = self.run_setup()
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertEqual(second.stdout.count("Already linked:"), len(SKILLS) + 1)
        self.assertNotIn("\nLinked:", "\n" + second.stdout)

    def test_collision_preflight_preserves_existing_skill(self):
        collision = self.agent / "skills/unslop"
        collision.mkdir(parents=True)
        marker = collision / "SKILL.md"
        marker.write_text("Machine-owned skill\n")
        result = self.run_setup()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Refusing to replace unrelated entry", result.stderr)
        self.assertEqual(marker.read_text(), "Machine-owned skill\n")
        self.assertFalse((self.agent / "AGENTS.md").exists())
        self.assertFalse(any(path.is_symlink() for path in self.agent.rglob("*")))

    def test_duplicate_discovery_is_rejected_before_linking(self):
        duplicate = self.home / ".agents/skills/review"
        duplicate.mkdir(parents=True)
        result = self.run_setup()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Duplicate skill discovery path", result.stderr)
        self.assertFalse(self.agent.exists())

    def test_broken_link_collision_is_preserved(self):
        self.agent.mkdir(parents=True)
        (self.agent / "AGENTS.md").symlink_to(self.root / "missing.md")
        result = self.run_setup()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual((self.agent / "AGENTS.md").readlink(), self.root / "missing.md")
        self.assertFalse((self.agent / "skills").exists())

    def test_relative_agent_path_and_arguments_are_rejected(self):
        self.env["PI_CODING_AGENT_DIR"] = "relative-agent"
        result = self.run_setup()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("must be absolute", result.stderr)
        self.assertFalse((self.repo / "relative-agent").exists())
        self.assertEqual(self.run_setup("unexpected").returncode, 2)


class SmokeFixtureTests(unittest.TestCase):
    def test_agent_copy_includes_references_and_private_fake_auth(self):
        with tempfile.TemporaryDirectory(prefix="pi-kijun-agent-test-") as directory:
            root = Path(directory)
            source_auth = root / "fake-auth.json"
            source_auth.write_text("{}\n")
            agent = root / "agent"
            smoke.prepare_agent(agent, source_auth)
            self.assertEqual(stat.S_IMODE((agent / "auth.json").stat().st_mode), 0o600)
            self.assertEqual({path.name for path in (agent / "skills").iterdir()}, SKILLS)
            self.assertTrue((agent / "skills/work-items/references/records.md").is_file())

    def test_workflow_fixtures(self):
        cases = ("project-state", "brainstorming", "refinement", "draft-boundary",
                 "slice-review", "unverified-review", "brief-review")
        with tempfile.TemporaryDirectory(prefix="pi-kijun-fixture-test-") as directory:
            for case in cases:
                work = Path(directory) / case
                smoke.fixture(work, case)
                self.assertTrue((work / "docs/project/charter.md").is_file())
                self.assertTrue((work / "docs/project/work.md").is_file())
                self.assertFalse((work / "project").exists())
                slice_path = work / "docs/project/work/S001-return-answer.md"
                if case == "brainstorming":
                    self.assertEqual(list((work / "docs/project/work").glob("*.md")), [])
                elif case == "refinement":
                    self.assertFalse(slice_path.exists())
                    self.assertEqual(smoke.item_status(work / "docs/project/work/B001-correct-answer.md"),
                                     "To do")
                else:
                    expected = {"draft-boundary": "Draft", "slice-review": "Review",
                                "unverified-review": "Review", "brief-review": "Done"}.get(case, "To do")
                    self.assertEqual(smoke.item_status(slice_path), expected)
                if case == "brief-review":
                    self.assertFalse((work / "README.md").exists())

    def test_workflow_observers_with_synthetic_results(self):
        skills = {"brainstorming": "brainstorming", "refinement": "refinement",
                  "draft-boundary": "development", "slice-review": "review",
                  "unverified-review": "review"}
        with tempfile.TemporaryDirectory(prefix="pi-kijun-observers-") as directory:
            root = Path(directory)
            agent = root / "agent"
            for case, skill in skills.items():
                with self.subTest(case=case):
                    work = root / case
                    smoke.fixture(work, case)
                    before = smoke.snapshot(work)
                    index = work / "docs/project/work.md"
                    brief = work / "docs/project/work/B001-correct-answer.md"
                    slice_path = work / "docs/project/work/S001-return-answer.md"
                    calls = [{"toolName": "read", "args": {"path": str(path)}}
                             for path in (agent / f"skills/{skill}/SKILL.md",
                                          agent / "skills/work-items/SKILL.md",
                                          brief, slice_path, work / "src/answer.py")]
                    if case == "brainstorming":
                        smoke.put(brief, "---\nid: B001\nstatus: Draft\n---\n\n"
                                  "# Correct answer\n\n## Outcome\n\nReturn the intended value.\n\n"
                                  "## Why\n\nCallers need it.\n\n## Boundaries\n\nKeep the interface.\n\n"
                                  "## Acceptance criteria\n\n- The result matches the accepted value.\n")
                        index.write_text(index.read_text() +
                                         "| [B001](work/B001-correct-answer.md) | Capture work. | Draft | None |\n")
                    elif case == "refinement":
                        smoke.put(slice_path, "---\nid: S001\nstatus: Draft\nparent: B001\n---\n\n"
                                  "# Return answer\n\n## Outcome\n\nReturn 42.\n\n"
                                  "## Acceptance criteria\n\n- answer() returns 42.\n\n"
                                  "## Tasks\n\n- [ ] Update the return value.\n")
                        index.write_text(index.read_text() +
                                         "| [S001](work/S001-return-answer.md) | Prepare work. | Draft | None |\n")
                    elif case == "slice-review":
                        slice_path.write_text(slice_path.read_text().replace("status: Review", "status: Done") +
                                              "\n## Review\n\nSatisfied by source inspection under delegated acceptance.\n")
                        brief.write_text(brief.read_text().replace("status: In progress", "status: Review"))
                        index.write_text("\n".join(line.replace("| In progress |", "| Review |")
                                                  for line in index.read_text().splitlines()
                                                  if "[S001]" not in line) + "\n")
                    elif case == "unverified-review":
                        blocker = "Production confirmation is unavailable."
                        slice_path.write_text(slice_path.read_text().replace(
                            "status: Review", f"status: Review\nblocked_by: {blocker}") +
                            "\n## Review\n\nUnverified: production service confirmation.\n")
                        index.write_text(index.read_text().replace(
                            "| Return 42. | Review | None |", f"| Return 42. | Review | {blocker} |"))
                    after = smoke.snapshot(work)
                    changed = {path for path in before.keys() | after.keys()
                               if before.get(path) != after.get(path)}
                    answer = "The slice is Draft and cannot start." if case == "draft-boundary" else "Recorded."
                    self.assertTrue(smoke.check_workflow(case, work, changed, calls,
                                                        answer, agent, before))
                    self.assertFalse(smoke.check_workflow(case, work, changed | {"README.md"},
                                                         calls, answer, agent, before))

    def test_mocked_review_results_do_not_claim_model_validation(self):
        with tempfile.TemporaryDirectory(prefix="pi-kijun-observer-test-") as directory:
            root = Path(directory)
            work = root / "work"
            smoke.fixture(work, "brief-review")
            agent = root / "agent"
            calls = [{"toolName": "read", "args": {"path": str(agent / f"skills/{name}/SKILL.md")}}
                     for name in ("review", "work-items")]
            brief = work / "docs/project/work/B001-correct-answer.md"
            index = work / "docs/project/work.md"
            calls.extend({"toolName": "read", "args": {"path": str(path)}}
                         for path in (brief, work / "src/answer.py"))
            before = smoke.snapshot(work)
            original = brief.read_text()
            brief.write_text(original.replace("status: Review", "status: In progress") +
                             "\n## Review\n\nUnmet: README.md is missing.\n")
            changed = {"docs/project/work/B001-correct-answer.md", "docs/project/work.md"}
            self.assertFalse(smoke.check_workflow("brief-review", work, changed, calls,
                                                 "Stale index.", agent, before))
            index.write_text(index.read_text().replace("| Review |", "| In progress |"))
            self.assertTrue(smoke.check_workflow("brief-review", work, changed, calls,
                                                "The README is missing.", agent, before))
            valid = brief.read_text()
            brief.write_text(valid.replace("- README.md documents the verified return value.",
                                           "- README.md is optional."))
            self.assertFalse(smoke.check_workflow("brief-review", work, changed, calls,
                                                 "Changed criteria.", agent, before))
            brief.write_text(valid.replace("status: In progress", "status: Done"))
            index.write_text("# Work\n\nAll items complete.\n")
            self.assertFalse(smoke.check_workflow("brief-review", work, changed, calls,
                                                 "Done.", agent, before))


if __name__ == "__main__":
    unittest.main()
