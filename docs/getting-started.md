# Getting Started

## Use without installing anything

1. Browse `docs/catalog.md`.
2. Select the smallest set of relevant skills.
3. Read each selected `SKILL.md`.
4. Load deeper references only when the workflow points to them.
5. Produce the required artifacts.
6. Verify every quality gate.

## Project-local integration

A runtime-neutral project can use:

```text
my-saas/
├── AGENTS.md
├── docs/
│   ├── decisions/
│   └── specifications/
└── .agent/
    └── skills/
        ├── multi-tenant-architecture/
        ├── api-first-design/
        └── threat-modeling/
```

Copy complete skill directories. Do not copy only `SKILL.md` when it references checklists or evaluations.

## Recommended first bundle

For a serious MVP, start with:

- `saas-project-bootstrap`
- `spec-driven-development`
- `mvp-scope`
- `multi-tenant-architecture`
- `tenant-context-propagation`
- `authentication-design`
- `authorization-rbac-abac`
- `database-schema-design`
- `api-first-design`
- `idempotency-concurrency`
- `threat-modeling`
- `i18n-localization`
- `observability`
- `test-strategy`
- `ci-cd-release`

The bundle is available in `bundles/mvp-foundation.json`.

## Activation prompt

```text
Read the active product specification and current implementation.
Use the selected Skills for SaaS workflows.
Do not broaden the scope.
Preserve tenant isolation, authorization, i18n, observability,
migration safety, and rollback.
Return changed artifacts, validation evidence, assumptions, and risks.
```

## Optional validation

Consumers need no runtime. Repository maintainers can use Python standard-library tools when available:

```bash
python3 tools/validate.py
```
