# Security Model

## Threats

- compromised or malicious skill instructions;
- unexpected tool use;
- secret or private-data exposure;
- path traversal in packaging;
- unsafe destructive actions;
- prompt injection inside referenced material;
- generated cross-tenant access flaws;
- tampered catalogs or release archives.

## Controls

- inspectable plain-text source;
- conservative metadata schema;
- repository-contained relative paths;
- no automatic script execution;
- checksummed releases;
- least-privilege agent adapters;
- tenant and authorization quality gates;
- adversarial evaluations;
- private vulnerability reporting.

## Important boundary

A skill cannot enforce security by itself. Enforcement belongs in the consuming tools, APIs, databases, identity systems, sandboxes, approvals, and deployment controls.
