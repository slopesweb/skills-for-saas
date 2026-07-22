# Skill Catalog

Core skills: **63**

## Ai

- [`agent-tool-design`](../skills/ai/agent-tool-design/SKILL.md) — Design bounded AI agents and tools that complete workflows safely, observably, and with human control.
- [`ai-evaluation`](../skills/ai/ai-evaluation/SKILL.md) — Build repeatable offline and online evaluations for AI quality, safety, latency, cost, and regression control.
- [`ai-feature-specification`](../skills/ai/ai-feature-specification/SKILL.md) — Specify AI features with measurable behavior, model boundaries, data policy, fallback, cost, and evaluation criteria.
- [`ai-safety-governance`](../skills/ai/ai-safety-governance/SKILL.md) — Define risk controls, data boundaries, human oversight, incident handling, and model-change governance.
- [`model-provider-abstraction`](../skills/ai/model-provider-abstraction/SKILL.md) — Support multiple AI model providers without erasing meaningful capability differences.
- [`prompt-contracts`](../skills/ai/prompt-contracts/SKILL.md) — Manage prompts as versioned, testable contracts with structured inputs, outputs, policies, and provenance.
- [`rag-architecture`](../skills/ai/rag-architecture/SKILL.md) — Design retrieval-augmented generation with tenant isolation, provenance, evaluation, and lifecycle management.

## Api

- [`api-first-design`](../skills/api/api-first-design/SKILL.md) — Design stable, tenant-safe APIs from consumer workflows and contracts before implementation.
- [`idempotency-concurrency`](../skills/api/idempotency-concurrency/SKILL.md) — Protect mutating operations from duplicate requests, retries, races, and conflicting replays.
- [`openapi-contracts`](../skills/api/openapi-contracts/SKILL.md) — Create executable OpenAPI contracts driving implementation, SDKs, tests, documentation, and compatibility checks.
- [`pagination-filtering-errors`](../skills/api/pagination-filtering-errors/SKILL.md) — Standardize list APIs and error responses for predictable SDKs and scalable queries.

## Architecture

- [`domain-modeling`](../skills/architecture/domain-modeling/SKILL.md) — Model SaaS domains around business language, invariants, aggregates, commands, events, and policies.
- [`modular-monolith-design`](../skills/architecture/modular-monolith-design/SKILL.md) — Design a deployable monolith with enforceable domain boundaries and a credible path to selective extraction.
- [`scalability-planning`](../skills/architecture/scalability-planning/SKILL.md) — Create an evidence-based scaling plan for SaaS workloads without premature distributed complexity.
- [`service-boundary-design`](../skills/architecture/service-boundary-design/SKILL.md) — Evaluate and define service boundaries using domain ownership, scaling pressure, reliability, and team autonomy.

## Billing

- [`entitlements-feature-gating`](../skills/billing/entitlements-feature-gating/SKILL.md) — Resolve what a tenant may use from plans, add-ons, trials, contracts, limits, and overrides.
- [`subscription-billing`](../skills/billing/subscription-billing/SKILL.md) — Model plans, prices, subscriptions, invoices, payment state, trials, discounts, and provider reconciliation.
- [`usage-metering`](../skills/billing/usage-metering/SKILL.md) — Collect, deduplicate, aggregate, price, and audit tenant usage for limits and billing.

## Data

- [`data-retention-export-deletion`](../skills/data/data-retention-export-deletion/SKILL.md) — Implement tenant-aware retention, portable exports, legal holds, and verifiable deletion.
- [`database-schema-design`](../skills/data/database-schema-design/SKILL.md) — Design tenant-safe relational schemas with explicit invariants, ownership, indexing, and evolution paths.
- [`migrations-zero-downtime`](../skills/data/migrations-zero-downtime/SKILL.md) — Plan backward-compatible database changes using expand, migrate, contract, verification, and rollback stages.
- [`row-level-security`](../skills/data/row-level-security/SKILL.md) — Design and verify database-enforced row-level security for multi-tenant systems.

## Delivery

- [`ci-cd-release`](../skills/delivery/ci-cd-release/SKILL.md) — Build reproducible pipelines with supply-chain controls, progressive delivery, verification, and rollback.
- [`infrastructure-deployment`](../skills/delivery/infrastructure-deployment/SKILL.md) — Design portable, secure, observable infrastructure for SaaS workloads and multiple growth stages.
- [`release-versioning`](../skills/delivery/release-versioning/SKILL.md) — Define semantic versioning, changelogs, deprecations, migrations, compatibility windows, and provenance.

## Events

- [`domain-events`](../skills/events/domain-events/SKILL.md) — Model durable business facts that decouple modules and services without losing semantic clarity.
- [`oauth-integration`](../skills/events/oauth-integration/SKILL.md) — Implement secure multi-tenant OAuth connections, consent, token storage, refresh, revocation, and reconnect.
- [`provider-adapter-design`](../skills/events/provider-adapter-design/SKILL.md) — Create replaceable provider integrations behind stable capability contracts.
- [`transactional-outbox-inbox`](../skills/events/transactional-outbox-inbox/SKILL.md) — Guarantee reliable event publication and idempotent consumption around database transactions.
- [`webhooks-production`](../skills/events/webhooks-production/SKILL.md) — Build tenant-scoped webhook subscriptions and delivery with security, retries, observability, and replay.

## Foundation

- [`architecture-decision-records`](../skills/foundation/architecture-decision-records/SKILL.md) — Capture consequential technical decisions with context, alternatives, consequences, and review triggers.
- [`project-context`](../skills/foundation/project-context/SKILL.md) — Create and maintain a durable source of truth for humans and AI agents working on a SaaS project.
- [`repository-architecture`](../skills/foundation/repository-architecture/SKILL.md) — Design a repository structure that keeps product specifications, domain boundaries, generated artifacts, tests, and agent instructions coherent at scale.
- [`saas-project-bootstrap`](../skills/foundation/saas-project-bootstrap/SKILL.md) — Transform a product idea into an executable, production-oriented SaaS repository baseline.
- [`saas-skill-creator`](../skills/foundation/saas-skill-creator/SKILL.md) — Create, review, evaluate, package, and improve reusable skills for SaaS engineering workflows.
- [`spec-driven-development`](../skills/foundation/spec-driven-development/SKILL.md) — Turn product intent into versioned, testable specifications that guide humans and AI agents before implementation.

## Identity

- [`authentication-design`](../skills/identity/authentication-design/SKILL.md) — Design secure authentication for users, sessions, recovery, MFA, and enterprise identity.
- [`authorization-rbac-abac`](../skills/identity/authorization-rbac-abac/SKILL.md) — Build auditable authorization combining roles, permissions, relationships, attributes, and policy evaluation.
- [`memberships-and-invitations`](../skills/identity/memberships-and-invitations/SKILL.md) — Model multi-organization membership, invitations, role assignment, ownership transfer, and account linking.
- [`service-accounts-api-keys`](../skills/identity/service-accounts-api-keys/SKILL.md) — Provide machine identities with scoped credentials, rotation, attribution, and tenant-safe authorization.

## Operations

- [`backup-disaster-recovery`](../skills/operations/backup-disaster-recovery/SKILL.md) — Design and test backups, point-in-time recovery, restoration, and disaster recovery for tenant-aware systems.
- [`cost-governance-finops`](../skills/operations/cost-governance-finops/SKILL.md) — Make infrastructure, AI, storage, data transfer, and provider costs visible, attributable, budgeted, and actionable per product and tenant.
- [`incident-response-runbooks`](../skills/operations/incident-response-runbooks/SKILL.md) — Prepare teams to detect, contain, communicate, recover, and learn from SaaS incidents.

## Platform

- [`background-jobs-queues`](../skills/platform/background-jobs-queues/SKILL.md) — Build reliable tenant-aware asynchronous jobs with idempotency, fairness, retries, and operational controls.
- [`configuration-feature-flags`](../skills/platform/configuration-feature-flags/SKILL.md) — Separate deployment configuration, tenant settings, experiments, operational flags, and entitlements.
- [`extension-plugin-architecture`](../skills/platform/extension-plugin-architecture/SKILL.md) — Design safe extension points that let SaaS products add modules, providers, workflows, and integrations without coupling them to the core.
- [`i18n-localization`](../skills/platform/i18n-localization/SKILL.md) — Make SaaS products locale-ready from the first commit across UI, APIs, notifications, and documents.
- [`observability`](../skills/platform/observability/SKILL.md) — Design logs, metrics, traces, audit events, dashboards, and alerts around tenant-safe operational questions.
- [`reliability-slo-resilience`](../skills/platform/reliability-slo-resilience/SKILL.md) — Set measurable reliability objectives and design graceful behavior under dependency, traffic, and partial failures.

## Product

- [`mvp-scope`](../skills/product/mvp-scope/SKILL.md) — Reduce a broad SaaS vision into the smallest coherent product that proves demand without an architectural dead end.
- [`product-analytics`](../skills/product/product-analytics/SKILL.md) — Define privacy-aware product events, metrics, funnels, retention, experiments, and tenant-level insights.

## Security

- [`audit-logging`](../skills/security/audit-logging/SKILL.md) — Design immutable, tenant-aware audit records for sensitive actions, administrative access, policy decisions, and security investigations.
- [`privacy-compliance`](../skills/security/privacy-compliance/SKILL.md) — Translate privacy and compliance obligations into concrete data, access, retention, audit, and evidence controls.
- [`secrets-key-management`](../skills/security/secrets-key-management/SKILL.md) — Manage application secrets, tenant credentials, encryption keys, rotation, and emergency revocation.
- [`threat-modeling`](../skills/security/threat-modeling/SKILL.md) — Identify assets, actors, trust boundaries, abuse cases, controls, and residual risks before implementation.

## Tenancy

- [`multi-tenant-architecture`](../skills/tenancy/multi-tenant-architecture/SKILL.md) — Choose and document a tenancy model balancing isolation, operability, cost, compliance, and growth.
- [`tenant-context-propagation`](../skills/tenancy/tenant-context-propagation/SKILL.md) — Propagate authenticated tenant context safely across HTTP, jobs, events, caches, logs, and internal calls.
- [`tenant-data-isolation`](../skills/tenancy/tenant-data-isolation/SKILL.md) — Enforce tenant data isolation at multiple layers and prove it with adversarial tests.
- [`tenant-lifecycle`](../skills/tenancy/tenant-lifecycle/SKILL.md) — Design safe tenant provisioning, activation, suspension, export, deletion, restoration, and tier migration.

## Testing

- [`contract-testing`](../skills/testing/contract-testing/SKILL.md) — Verify API, event, provider, and module compatibility independently of full-system environments.
- [`multi-tenant-security-testing`](../skills/testing/multi-tenant-security-testing/SKILL.md) — Prove requests, jobs, caches, exports, search, files, analytics, and admin paths cannot leak across tenants.
- [`performance-load-testing`](../skills/testing/performance-load-testing/SKILL.md) — Measure capacity, latency, fairness, and failure behavior under realistic multi-tenant workloads.
- [`test-strategy`](../skills/testing/test-strategy/SKILL.md) — Create a risk-based test strategy spanning unit, integration, contract, end-to-end, performance, migration, and resilience.
