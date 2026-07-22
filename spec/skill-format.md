# Skills for SaaS Portable Skill Format

## Status

Alpha — format version `1.0-alpha`.

## Goals

- plain-text inspection;
- runtime and vendor independence;
- progressive disclosure;
- machine-readable discovery;
- relative, self-contained resources;
- versioned evaluations;
- safe adaptation to different agents.

## Required directory

```text
<skill-name>/
└── SKILL.md
```

## Recommended directory

```text
<skill-name>/
├── SKILL.md
├── references/
├── evals/
├── scripts/
└── assets/
```

Only `SKILL.md` is universally required. Skills for SaaS core skills also require a checklist and evaluations as a repository quality policy.

## Frontmatter

Supported top-level fields:

- `name` — required;
- `description` — required;
- `license`;
- `compatibility`;
- `allowed-tools`;
- `metadata`.

Unknown top-level fields should be rejected by strict consumers and preserved by tolerant editors only when explicitly configured.

## Name

- lowercase ASCII letters, digits, and single hyphens;
- no leading, trailing, or consecutive hyphens;
- maximum 64 characters;
- must match the directory name.

## Description

The description is the primary discovery and triggering field. It should state:

1. what the skill enables;
2. when it should be selected;
3. related user language or workflow contexts.

Maximum 1024 characters. Angle brackets are prohibited.

## Metadata

Skills for SaaS uses:

- `category`;
- `version`;
- `maturity`;
- `tags`.

Consumers may ignore unknown nested metadata.

## Paths

References must be relative to the skill directory. They must not escape the directory with path traversal.

## Script execution

A consumer must not execute a script merely because a skill references it. Scripts require independent permission, inspection, sandboxing, and tool policy.

## Versioning

The current public skill version is `0.1.0-alpha.1`. Skills follow Semantic Versioning.
