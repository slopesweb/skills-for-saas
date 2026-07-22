#!/usr/bin/env python3
"""Build deterministic source archives and SHA-256 checksums."""
from __future__ import annotations

import hashlib
import os
import tarfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.1.0-alpha.1"
DIST = ROOT / "dist"
PREFIX = f"skills-for-saas-{VERSION}"
EXCLUDE = {".git", "dist", "__pycache__", ".DS_Store"}

def files():
    return [
        path for path in sorted(ROOT.rglob("*"))
        if path.is_file() and not any(part in EXCLUDE for part in path.parts)
    ]

def main() -> int:
    DIST.mkdir(exist_ok=True)
    zip_path = DIST / f"{PREFIX}.zip"
    tar_path = DIST / f"{PREFIX}.tar.gz"

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in files():
            arcname = (Path(PREFIX) / path.relative_to(ROOT)).as_posix()
            info = zipfile.ZipInfo(arcname, date_time=(2026, 7, 22, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o755 if os.access(path, os.X_OK) else 0o644) << 16
            archive.writestr(info, path.read_bytes())

    with tarfile.open(tar_path, "w:gz", format=tarfile.PAX_FORMAT) as archive:
        for path in files():
            arcname = (Path(PREFIX) / path.relative_to(ROOT)).as_posix()
            info = archive.gettarinfo(str(path), arcname=arcname)
            info.mtime = 1784678400
            with path.open("rb") as handle:
                archive.addfile(info, handle)

    checksum_path = DIST / f"{PREFIX}.sha256"
    checksum_path.write_text(
        f"{hashlib.sha256(zip_path.read_bytes()).hexdigest()}  {zip_path.name}\n"
        f"{hashlib.sha256(tar_path.read_bytes()).hexdigest()}  {tar_path.name}\n",
        encoding="utf-8",
    )
    print(zip_path)
    print(tar_path)
    print(checksum_path)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
