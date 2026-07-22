---
name: ai-evaluation
description: Build repeatable offline and online evaluations for AI quality, safety, latency, cost, and regression control. Use this skill whenever a user is designing, implementing, reviewing, migrating, or troubleshooting work related to evals, benchmark, quality, even without explicitly requesting a formal architecture review.
license: Apache-2.0
compatibility: Runtime-agnostic and vendor-neutral; suitable for agents that support SKILL.md instructions and relative references.
metadata:
  category: ai
  version: 0.1.0-alpha.1
  maturity: alpha
  tags:
    - evals
    - benchmark
    - quality
---

# AI Evaluation

## Objective

Build repeatable offline and online evaluations for AI quality, safety, latency, cost, and regression control.

Apply this workflow to the user's actual product, repository, constraints, and delivery stage. Preserve the simplest design satisfying verified constraints. Mark assumptions instead of silently inventing facts.

## Use when

Use for new designs, specifications, implementation plans, code reviews, migrations, hardening, or incident follow-up involving evals, benchmark, quality.

## Preconditions

1. Identify the product workflow and affected actors.
2. Identify tenant, organization, workspace, user, resource, and machine-identity scopes.
3. Identify trust boundaries, data sensitivity, consistency needs, expected scale, and failure cost.
4. Inspect existing contracts, code, schemas, migrations, tests, and operational constraints when available.
5. Separate facts, decisions, assumptions, risks, and open questions.

## Required workflow

### 1. Frame the decision

- State the problem, current behavior, success criteria, constraints, and non-goals.
- Do not select technology before the domain and trust boundaries are clear.

### 2. Model domain and boundaries

- Define ownership, invariants, states, identities, and authorization scope.
- Trace tenant context across requests, jobs, events, caches, files, analytics, and administrative paths.
- Separate deterministic product rules from provider or AI behavior.

### 3. Compare credible options

Compare correctness, isolation, cost, complexity, scalability, security, privacy, vendor dependence, reversibility, migration, and developer experience. Do not manufacture alternatives when only one safe option exists.

### 4. Specify contracts

Define inputs, outputs, stable identifiers, schemas, errors, authorization, idempotency, concurrency, telemetry, compatibility, and versioning. Prefer machine-readable contracts across public or module boundaries.

### 5. Plan reversible implementation

Break work into vertical slices. Each slice includes implementation, tests, migration or rollout, telemetry, and rollback. Keep launch-critical foundations separate from speculative platform work.

### 6. Verify

Use [references/checklist.md](references/checklist.md). Add normal, negative, cross-tenant, retry, concurrency, and recovery tests where applicable.

## Required artifacts

- Context and decision summary.
- Domain, data, boundary, and contract design.
- Tenant and authorization impact matrix.
- Implementation slices with acceptance criteria.
- Test and quality-gate plan.
- Rollout, migration, recovery, and rollback plan.
- Risks, assumptions, open decisions, and ownership.

## Quality gates

- Tenant context comes from trusted identity and fails closed.
- Authorization is server-side and close to the protected operation.
- Unique constraints, foreign references, caches, search, files, exports, and telemetry preserve tenant scope.
- Duplicate delivery, retries, races, partial failure, and recovery are addressed.
- Logs, events, prompts, and metrics avoid secrets and uncontrolled personal data.
- User-facing text and regional formats are localization-ready.
- Provider-specific behavior stays behind adapters.
- Migration, compatibility, observability, and rollback are explicit.
- Production readiness is claimed only with evidence.

## Failure handling

When evidence is missing, produce a bounded proposal with visible assumptions and a verification plan. Reject requested behavior that weakens tenant isolation, authorization, privacy, integrity, or recoverability, and provide a safer alternative.

## Anti-patterns

- Client-side authorization as the primary control.
- Adding `tenant_id` filters informally after feature development.
- Shared mutable tenant context.
- Provider SDK types leaking into domain contracts.
- Fire-and-forget side effects inside database transactions.
- Hardcoded user text or locale-specific formatting in domain logic.
- Generic claims of infinite scale, compliance, or AI quality without evidence.
- Broad refactoring during incident containment without preserving evidence.

## Output format

1. Context
2. Decision or design
3. Contracts and data
4. Tenant and authorization impact
5. Implementation slices
6. Tests and quality gates
7. Rollout and rollback
8. Risks, assumptions, and open decisions
