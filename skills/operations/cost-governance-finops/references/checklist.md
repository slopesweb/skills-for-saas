# Cost Governance and FinOps Review Checklist

## Context

- [ ] The user workflow and business outcome are explicit.
- [ ] Tenant and resource scopes are explicit.
- [ ] Facts, assumptions, decisions, and open questions are separated.
- [ ] Non-goals prevent accidental scope expansion.

## Design

- [ ] Define cost allocation dimensions, unit economics, budgets, forecasts, and anomaly signals.
- [ ] Attribute shared costs without pretending estimates are exact.
- [ ] Connect architecture and product decisions to measurable cost consequences.

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

- [ ] Cost model exists.
- [ ] Allocation policy exists.
- [ ] Budget and alert thresholds exists.
- [ ] Optimization backlog exists.

## Reject when

- Optimizing cost without measuring user impact.
- Treating cloud invoices as sufficient product cost attribution.
- The proposal has no verification or recovery path.
