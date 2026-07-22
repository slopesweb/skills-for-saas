# First Vertical Slice

## Goal

An organization owner invites a member, creates a project, and the member can access only projects belonging to the active organization.

## Requirements

1. Tenant context is derived from verified membership.
2. Invitation acceptance is idempotent.
3. Project creation is idempotent.
4. Cross-tenant requests do not reveal resource existence.
5. Audit events exist for sensitive mutations.
6. Errors use stable machine codes and localized human messages.
7. Negative isolation tests use tenants with colliding local identifiers.

## Non-goals

- Billing
- External integrations
- Multiple regions
