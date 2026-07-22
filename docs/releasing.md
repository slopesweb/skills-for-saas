# Releasing

## Before tagging

1. Update skill versions when behavior changed.
2. Update `CHANGELOG.md`.
3. Run:
   ```bash
   python3 tools/validate.py
   python3 tools/build_catalog.py --check
   python3 tools/check_links.py
   ```
4. Build deterministic archives:
   ```bash
   python3 tools/package_release.py
   ```
5. Inspect the archive contents.
6. Create and push an annotated tag.

## Tag format

```text
vMAJOR.MINOR.PATCH
v0.1.0-alpha.1
```

## Release contents

- source ZIP;
- source TAR.GZ;
- SHA-256 checksum file;
- release notes from the changelog.
