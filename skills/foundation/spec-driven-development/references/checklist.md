# Spec-Driven Development Review Checklist

## Context

- [ ] The user workflow and business outcome are explicit.
- [ ] Tenant and resource scopes are explicit.
- [ ] Facts, assumptions, decisions, and open questions are separated.
- [ ] Non-goals prevent accidental scope expansion.

## Design

- [ ] Separate product intent, domain rules, public contracts, implementation plans, and operational procedures.
- [ ] Define acceptance criteria before coding and connect each criterion to automated or reviewable evidence.
- [ ] Treat specifications as versioned source artifacts that evolve through explicit decisions rather than chat history.

- [ ] Ownership and trust boundaries are explicit.
- [ ] Contracts define stable identifiers, errors, permissions, and versioning.
- [ ] Failure, retry, concurrency, migration, and rollback behavior are defined.

## Security and tenancy

- [ ] Tenant context comes from a trusted source.
- [ ] Missing or conflicting context fails closed.
- [ ] Horizontal and vertical authorization have negative tests.
- [ ] Administrative access is restricted and audited.
- [ ] Secrets and sensitive payloads are excluded from telemetry.

## Evidence

- [ ] Feature specification exists.
- [ ] Acceptance-criteria matrix exists.
- [ ] Implementation slices exists.
- [ ] Verification report exists.

## Reject when

- Using prompts as the only requirements source.
- Writing implementation details before defining user behavior.
- The proposal has no verification or recovery path.
