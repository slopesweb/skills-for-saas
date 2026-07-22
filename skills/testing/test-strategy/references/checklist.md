# Test Strategy — Review Checklist

## Context

- [ ] Product workflow, actors, scopes, current state, target state, constraints, and non-goals are explicit.
- [ ] Assumptions are visible and testable.

## Domain and contracts

- [ ] Data and decision ownership are explicit.
- [ ] Invariants, inputs, outputs, states, stable identifiers, errors, and versions are defined.
- [ ] Public and cross-boundary contracts are machine-readable where practical.

## Security and tenancy

- [ ] Tenant context comes from a trusted source and fails closed.
- [ ] Horizontal and vertical authorization are tested.
- [ ] Admin exceptions are minimal, approved, and audited.
- [ ] Caches, indexes, files, exports, queues, and analytics are tenant-safe.
- [ ] Secrets and personal data do not leak through logs, events, prompts, or errors.

## Reliability and operations

- [ ] Idempotency, concurrency, timeout, retry, backoff, dead-letter, and recovery behavior are bounded.
- [ ] Tenant skew and noisy-neighbor risks are considered.
- [ ] Telemetry maps to user impact.
- [ ] Migration and rollback are verified.

## Delivery evidence

- [ ] Implementation is split into reversible vertical slices.
- [ ] Tests include negative, cross-tenant, retry, concurrency, and migration scenarios where relevant.
- [ ] i18n and stable error codes are preserved.
- [ ] Provider-specific behavior remains behind adapters.
- [ ] Remaining risks and owners are explicit.
