# Repository Architecture

## Source layers

### `skills/`

Portable source units. Every skill owns its references, evaluations, scripts, and assets.

### `catalog/`

Generated discovery metadata. Consumers should use the catalog when they need machine-readable search.

### `spec/` and `schemas/`

Public compatibility contracts. These evolve conservatively under semantic versioning.

### `bundles/`

Curated skill lists. A bundle does not create hidden dependencies.

### `templates/`

Starting points for skill authors and SaaS specifications.

### `adapters/`

Thin guidance for mapping portable source into agent products.

### `tools/`

Optional maintenance utilities using the Python standard library. Consumers do not need them.

## Dependency rule

A skill may recommend another skill but must remain understandable and useful alone. Dependencies must be visible, bounded, and never hidden in executable code.

## Source-of-truth rule

- Skill behavior lives in `SKILL.md`.
- Deep guidance lives in the skill's references.
- Evaluation expectations live in `evals/evals.json`.
- Discovery metadata is generated from frontmatter.
- Public format rules live under `spec/`.
