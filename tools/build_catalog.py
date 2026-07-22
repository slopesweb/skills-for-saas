#!/usr/bin/env python3
"""Generate deterministic catalogs from skill metadata."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRONT_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
REPOSITORY_VERSION = "0.1.0-alpha.1"
GENERATED_AT = "2026-07-22T00:00:00Z"

def scalar(front: str, key: str, default: str = "") -> str:
    match = re.search(rf"(?m)^\s*{re.escape(key)}:\s*(.+?)\s*$", front)
    return match.group(1).strip().strip("\"'") if match else default

def tags(front: str) -> list[str]:
    match = re.search(r"(?ms)^\s{2}tags:\s*\n((?:\s{4}- .+\n?)+)", front)
    if not match:
        return []
    return [line.split("-", 1)[1].strip() for line in match.group(1).splitlines()]

def build_skills() -> dict:
    rows = []
    for skill_file in sorted((ROOT / "skills").glob("*/*/SKILL.md")):
        text = skill_file.read_text(encoding="utf-8")
        match = FRONT_RE.match(text)
        if not match:
            continue
        front = match.group(1)
        rows.append({
            "name": scalar(front, "name"),
            "description": scalar(front, "description"),
            "category": scalar(front, "category", skill_file.parent.parent.name),
            "version": scalar(front, "version", "0.0.0"),
            "maturity": scalar(front, "maturity", "experimental"),
            "tags": tags(front),
            "path": skill_file.relative_to(ROOT).as_posix(),
        })
    return {
        "format_version": "1.0-alpha",
        "generated_at": GENERATED_AT,
        "repository_version": REPOSITORY_VERSION,
        "skills": sorted(rows, key=lambda row: row["name"]),
    }

def build_categories(skills: dict) -> dict:
    groups: dict[str, list[str]] = {}
    for skill in skills["skills"]:
        groups.setdefault(skill["category"], []).append(skill["name"])
    return {
        "format_version": "1.0-alpha",
        "categories": [
            {"name": category, "skill_count": len(names), "skills": sorted(names)}
            for category, names in sorted(groups.items())
        ],
    }

def build_bundles() -> dict:
    rows = []
    for path in sorted((ROOT / "bundles").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        rows.append({
            "name": data.get("name", path.stem),
            "version": data.get("version", REPOSITORY_VERSION),
            "description": data.get("description", ""),
            "skills": data.get("skills", []),
            "path": path.relative_to(ROOT).as_posix(),
        })
    return {"format_version": "1.0-alpha", "bundles": rows}

def render(data: dict) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    skills = build_skills()
    outputs = {
        ROOT / "catalog" / "skills.json": render(skills),
        ROOT / "catalog" / "categories.json": render(build_categories(skills)),
        ROOT / "catalog" / "bundles.json": render(build_bundles()),
    }

    stale = []
    for path, content in outputs.items():
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                stale.append(path)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")

    if stale:
        for path in stale:
            print(f"Out of date: {path.relative_to(ROOT)}")
        return 1

    print("Catalogs are current." if args.check else "Catalogs generated.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
