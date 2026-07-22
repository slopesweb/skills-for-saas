# Extension and Plugin Architecture Review Checklist

## Context

- [ ] The user workflow and business outcome are explicit.
- [ ] Tenant and resource scopes are explicit.
- [ ] Facts, assumptions, decisions, and open questions are separated.
- [ ] Non-goals prevent accidental scope expansion.

## Design

- [ ] Define stable capability contracts, lifecycle hooks, permissions, compatibility, and isolation boundaries.
- [ ] Separate trusted first-party extensions from untrusted or tenant-installed extensions.
- [ ] Provide version negotiation, deprecation, observability, and failure containment.

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

- [ ] Extension contract exists.
- [ ] Lifecycle model exists.
- [ ] Permission model exists.
- [ ] Compatibility policy exists.

## Reject when

- Executing arbitrary extension code inside the core process.
- Exposing internal database tables as the plugin API.
- The proposal has no verification or recovery path.
