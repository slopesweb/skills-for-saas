#!/usr/bin/env python3
"""Validate Skills for SaaS without third-party packages."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONT_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

def scalar(front: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", front)
    if not match:
        return None
    value = match.group(1).strip()
    if len(value) >= 2 and value[0] in "'\"" and value[-1] == value[0]:
        value = value[1:-1]
    return value

def top_keys(front: str) -> set[str]:
    keys = set()
    for line in front.splitlines():
        if not line or line.startswith((" ", "\t", "#", "-")):
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):", line)
        if match:
            keys.add(match.group(1))
    return keys

def discover(target: Path) -> list[Path]:
    if (target / "SKILL.md").is_file():
        return [target]
    return sorted({path.parent for path in target.rglob("SKILL.md") if "templates" not in path.parts})

def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    skill_file = path / "SKILL.md"
    if not skill_file.is_file():
        return [f"{path}: SKILL.md not found"]

    text = skill_file.read_text(encoding="utf-8")
    match = FRONT_RE.match(text)
    if not match:
        return [f"{skill_file}: invalid frontmatter delimiters"]

    front = match.group(1)
    unexpected = top_keys(front) - ALLOWED
    if unexpected:
        errors.append(f"{skill_file}: unsupported keys: {', '.join(sorted(unexpected))}")

    name = scalar(front, "name")
    description = scalar(front, "description")
    compatibility = scalar(front, "compatibility")

    if not name:
        errors.append(f"{skill_file}: missing name")
    elif not NAME_RE.fullmatch(name):
        errors.append(f"{skill_file}: invalid kebab-case name {name!r}")
    elif len(name) > 64:
        errors.append(f"{skill_file}: name exceeds 64 characters")
    elif name != path.name:
        errors.append(f"{skill_file}: name does not match directory {path.name!r}")

    if not description:
        errors.append(f"{skill_file}: missing description")
    else:
        if len(description) > 1024:
            errors.append(f"{skill_file}: description exceeds 1024 characters")
        if "<" in description or ">" in description:
            errors.append(f"{skill_file}: description contains angle brackets")

    if compatibility and len(compatibility) > 500:
        errors.append(f"{skill_file}: compatibility exceeds 500 characters")

    body = text[match.end():]
    required_headings = (
        "## Objective",
        "## Required workflow",
        "## Required artifacts",
        "## Quality gates",
        "## Anti-patterns",
    )
    for heading in required_headings:
        if heading not in body:
            errors.append(f"{skill_file}: missing heading {heading}")

    checklist = path / "references" / "checklist.md"
    evals_file = path / "evals" / "evals.json"
    if not checklist.is_file():
        errors.append(f"{path}: references/checklist.md not found")
    if not evals_file.is_file():
        errors.append(f"{path}: evals/evals.json not found")
    else:
        try:
            data = json.loads(evals_file.read_text(encoding="utf-8"))
            if data.get("skill_name") != name:
                errors.append(f"{evals_file}: skill_name mismatch")
            cases = data.get("evals")
            if not isinstance(cases, list) or len(cases) < 3:
                errors.append(f"{evals_file}: at least three evaluations are required")
            elif len({case.get('id') for case in cases if isinstance(case, dict)}) != len(cases):
                errors.append(f"{evals_file}: evaluation IDs must be unique")
        except Exception as exc:
            errors.append(f"{evals_file}: invalid JSON: {exc}")

    for referenced in re.findall(r"\[[^\]]+\]\(([^)]+)\)", body):
        target = referenced.split("#", 1)[0]
        if not target or "://" in target or target.startswith("#"):
            continue
        resolved = (path / target).resolve()
        try:
            resolved.relative_to(path.resolve())
        except ValueError:
            errors.append(f"{skill_file}: reference escapes the skill directory: {referenced}")
            continue
        if not resolved.exists():
            errors.append(f"{skill_file}: missing local reference: {referenced}")

    return errors

def main() -> int:
    target = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / "skills"
    if not target.exists():
        print(f"Target not found: {target}", file=sys.stderr)
        return 2

    skills = discover(target)
    errors: list[str] = []
    names: dict[str, Path] = {}
    for skill in skills:
        errors.extend(validate_skill(skill))
        text = (skill / "SKILL.md").read_text(encoding="utf-8")
        match = FRONT_RE.match(text)
        if match:
            name = scalar(match.group(1), "name")
            if name:
                if name in names:
                    errors.append(f"Duplicate skill name {name}: {names[name]} and {skill}")
                names[name] = skill

    forbidden = [
        ROOT / "package.json",
        ROOT / "bunfig.toml",
        ROOT / "deno.json",
        ROOT / "PROJECT_CONTEXT.md",
    ]
    for path in forbidden:
        if path.exists():
            errors.append(f"Forbidden public repository file exists: {path.name}")

    if errors:
        print(f"Validation failed with {len(errors)} error(s):")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(skills)} skills successfully.")
    print("Runtime-agnostic repository constraints passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
