# Repository Agent Instructions

This repository is a runtime-agnostic library of SaaS engineering skills.

## Before changing a skill

1. Read `docs/authoring.md`.
2. Read the existing skill, its checklist, and evaluations.
3. Search `catalog/skills.json` for overlapping scope.
4. Keep the skill vendor-neutral unless the scope is explicitly an adapter.
5. Preserve compatibility with the public skill format.
6. Update evaluations when behavior changes.
7. Run the optional validation tools when Python is available.

## Non-negotiable rules

- Do not add a required application runtime.
- Do not add Node.js, Bun, Deno, package-manager, framework, cloud, or database lock-in to the core format.
- Do not move security, tenant isolation, authorization, i18n, observability, migration, or recovery to a later phase when they are foundational.
- Do not commit secrets, customer data, or private project context.
- Do not edit generated catalog files manually.
- Do not expand a pull request beyond its declared scope.

## Completion report

State changed files, validation performed, compatibility impact, security and tenancy impact, and any blocked checks.
