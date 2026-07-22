# Contributing

Skills for SaaS accepts contributions to skills, evaluations, specifications, schemas, adapters, documentation, and maintenance tools.

## Before proposing a new skill

A skill should encode a durable workflow that appears across SaaS projects. It should not be:

- a one-off answer;
- a complete generated application;
- generic advice without required artifacts;
- a hidden dependency on one framework or provider;
- a duplicate of an existing skill with different wording.

Search `docs/catalog.md` and open a new-skill proposal before large work.

## Required skill structure

```text
skills/<category>/<name>/
├── SKILL.md
├── references/checklist.md
└── evals/evals.json
```

A contribution must:

- use a unique kebab-case name;
- explain capability and trigger conditions;
- define preconditions and a required workflow;
- produce concrete artifacts;
- define quality gates and failure handling;
- include at least three realistic evaluations;
- include a negative, constrained, migration, or incident case;
- preserve tenant isolation and server-side authorization;
- remain runtime-agnostic and vendor-neutral unless explicitly scoped otherwise.

## Validation

Using the repository requires no runtime. Maintainers may optionally run the standard-library tools:

```bash
python3 tools/validate.py
python3 tools/build_catalog.py --check
python3 tools/check_links.py
```

## Pull requests

Keep pull requests focused. Describe:

1. Problem
2. Proposed change
3. Why a new skill or behavior is necessary
4. Compatibility impact
5. Tenant and security impact
6. Evaluation evidence
7. Migration or deprecation impact

Update `CHANGELOG.md` for public behavior or contract changes.

By contributing, you agree that your contribution is licensed under Apache-2.0.
