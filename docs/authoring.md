# Skill Authoring

## Choose a durable workflow

A skill should encode a repeatable engineering process with a clear outcome. Avoid one-off answers, generic checklists without context, or complete applications disguised as skills.

## Directory

```text
skills/<category>/<skill-name>/
├── SKILL.md
├── references/
│   └── checklist.md
└── evals/
    └── evals.json
```

## Frontmatter

```yaml
---
name: example-skill
description: Explain the capability and exact trigger conditions.
license: Apache-2.0
compatibility: Runtime-agnostic and vendor-neutral...
metadata:
  category: example
  version: 0.1.0-alpha.1
  maturity: experimental
  tags:
    - example
---
```

Rules:

- Use lowercase kebab-case.
- Keep the name at or below 64 characters.
- Describe both what the skill does and when to use it.
- Keep the description at or below 1024 characters.
- Do not use unsupported top-level keys.
- Do not declare tools unless the skill truly requires them.
- Do not bind the core workflow to a runtime.

## Main document

Use this order:

1. Objective
2. Use when
3. Preconditions
4. Required workflow
5. Required artifacts
6. Quality gates
7. Failure handling
8. Anti-patterns
9. Output format
10. References

Keep the main document focused. Move detailed variants and long examples into `references/`.

## SaaS invariants

Relevant skills must address:

- tenant identity and isolation;
- server-side authorization;
- data ownership and lifecycle;
- idempotency, retries, concurrency, and partial failure;
- stable contracts and versioning;
- observability and auditability;
- i18n and regional formatting;
- migration and rollback;
- cost and operability;
- provider abstraction;
- privacy and security.

## Evaluations

Include at least:

1. normal design or implementation task;
2. constrained or ambiguous task;
3. negative, migration, failure, incident, or adversarial task.

Expected output should describe observable properties rather than exact prose.

## Review

Run optional validation:

```bash
python3 tools/validate.py skills/category/example-skill
```

Then perform domain, tenancy, security, compatibility, and editorial review.
