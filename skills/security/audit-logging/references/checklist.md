# Audit Logging Review Checklist

## Context

- [ ] The user workflow and business outcome are explicit.
- [ ] Tenant and resource scopes are explicit.
- [ ] Facts, assumptions, decisions, and open questions are separated.
- [ ] Non-goals prevent accidental scope expansion.

## Design

- [ ] Record actor, tenant, action, target, decision, time, source, correlation, and safe structured details.
- [ ] Separate audit evidence from operational logs and product analytics.
- [ ] Protect integrity, retention, restricted access, export, and investigation workflows.

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

- [ ] Audit event catalog exists.
- [ ] Audit schema exists.
- [ ] Retention and access policy exists.
- [ ] Verification tests exists.

## Reject when

- Storing secrets or raw sensitive payloads in audit details.
- Allowing application users to modify audit evidence.
- The proposal has no verification or recovery path.
