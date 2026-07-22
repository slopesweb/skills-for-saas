# Optional Maintenance Tools

The skill system requires no runtime.

These maintainer tools use only the Python standard library:

- `validate.py` — validate skill structure and evaluations.
- `build_catalog.py` — regenerate machine-readable catalogs.
- `check_links.py` — verify repository-local Markdown links.
- `package_release.py` — create deterministic release archives and checksums.

They can be replaced by any implementation that follows the public schemas.
