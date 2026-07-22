---
name: repository-architecture
description: Design a repository structure that keeps product specifications, domain boundaries, generated artifacts, tests, and agent instructions coherent at scale. Use this skill whenever a user is designing, implementing, reviewing, migrating, or troubleshooting work involving repository, monorepo, governance, even when they do not explicitly request a formal architecture workflow.
license: Apache-2.0
compatibility: Runtime-agnostic and vendor-neutral; suitable for agents that support SKILL.md instructions and relative references.
metadata:
  category: foundation
  version: 0.1.0-alpha.1
  maturity: alpha
  tags:
    - repository
    - monorepo
    - governance
---

# Repository Architecture

## Objective

Design a repository structure that keeps product specifications, domain boundaries, generated artifacts, tests, and agent instructions coherent at scale.

Apply this skill to the actual product, repository, constraints, and delivery stage. Mark assumptions explicitly and prefer the simplest design that preserves correctness, tenant isolation, security, migration safety, and operability.

## Use when

Use this skill for greenfield planning, implementation, architecture reviews, migrations, production hardening, or incident follow-up related to repository, monorepo, governance.

## Preconditions

1. Identify the user workflow and business outcome.
2. Identify tenant, organization, workspace, user, resource, and machine-identity scopes.
3. Inspect existing specifications, decisions, contracts, code, data, tests, and operational evidence when available.
4. Separate verified facts, constraints, assumptions, decisions, and open questions.
5. Define what successful completion will prove.

## Required workflow

### 1. Frame the problem

State the current behavior, desired behavior, measurable success criteria, constraints, and non-goals.

### 2. Model the design

- Organize by stable ownership and domain boundaries rather than temporary framework conventions.
- Keep generated files, source contracts, tests, migrations, and operational documentation clearly separated.
- Define repository-wide rules for agents without forcing every task to load the entire codebase context.

Also identify ownership, trust boundaries, authorization enforcement, data lifecycle, failure modes, and observability.

### 3. Compare credible options

Compare correctness, isolation, complexity, cost, scalability, reversibility, compatibility, and developer experience. Do not manufacture alternatives when only one safe option exists.

### 4. Define contracts

Specify inputs, outputs, states, identifiers, permissions, errors, idempotency, telemetry, versioning, and migration behavior.

### 5. Plan reversible delivery

Break the work into small vertical slices. Each slice includes implementation, tests, rollout, verification, and rollback or safe-forward recovery.

### 6. Verify

Use [references/checklist.md](references/checklist.md). Include negative, cross-tenant, retry, migration, and failure tests where relevant.

## Required artifacts

- Repository map.
- Ownership rules.
- Dependency constraints.
- Agent instruction hierarchy.

## Quality gates

- Tenant context comes from trusted identity and fails closed.
- Authorization is enforced at the protected operation.
- Public and cross-boundary contracts are versioned.
- Retries, concurrency, partial failure, and recovery are addressed.
- Logs, traces, metrics, and audit events avoid secrets and uncontrolled personal data.
- User-facing behavior remains localization-ready.
- Rollout, migration, compatibility, and rollback are explicit.

## Failure handling

When evidence is missing, produce a bounded proposal with visible assumptions and a verification plan. Reject designs that weaken tenant isolation, authorization, privacy, integrity, recoverability, or user control.

## Anti-patterns

- A miscellaneous shared folder with unrestricted dependencies.
- Duplicating the same decision in many files.
- Hiding critical policy in frontend code or prompts.
- Treating a provider as the product source of truth.
- Claiming production readiness without tests and operational evidence.

## Output format

1. Context
2. Decision or design
3. Contracts and ownership
4. Tenant and security impact
5. Delivery slices
6. Tests and quality gates
7. Rollout and rollback
8. Risks, assumptions, and open decisions
