#!/usr/bin/env python3
"""Check repository-local Markdown links without network access."""
from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")

def main() -> int:
    errors = []
    for document in ROOT.rglob("*.md"):
        if any(part in {".git", "dist", "__pycache__"} for part in document.parts):
            continue
        text = document.read_text(encoding="utf-8")
        for raw in LINK_RE.findall(text):
            target = raw.split("#", 1)[0].strip()
            if not target or "://" in target or target.startswith(("mailto:", "#")):
                continue
            resolved = (document.parent / unquote(target)).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{document.relative_to(ROOT)}: link escapes repository: {raw}")
                continue
            if not resolved.exists():
                errors.append(f"{document.relative_to(ROOT)}: missing target: {raw}")

    if errors:
        print(f"Found {len(errors)} broken link(s):")
        for error in errors:
            print(f"- {error}")
        return 1

    print("All repository-local Markdown links are valid.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
