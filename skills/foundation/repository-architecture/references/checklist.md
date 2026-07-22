# Repository Architecture Review Checklist

## Context

- [ ] The user workflow and business outcome are explicit.
- [ ] Tenant and resource scopes are explicit.
- [ ] Facts, assumptions, decisions, and open questions are separated.
- [ ] Non-goals prevent accidental scope expansion.

## Design

- [ ] Organize by stable ownership and domain boundaries rather than temporary framework conventions.
- [ ] Keep generated files, source contracts, tests, migrations, and operational documentation clearly separated.
- [ ] Define repository-wide rules for agents without forcing every task to load the entire codebase context.

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

- [ ] Repository map exists.
- [ ] Ownership rules exists.
- [ ] Dependency constraints exists.
- [ ] Agent instruction hierarchy exists.

## Reject when

- A miscellaneous shared folder with unrestricted dependencies.
- Duplicating the same decision in many files.
- The proposal has no verification or recovery path.
