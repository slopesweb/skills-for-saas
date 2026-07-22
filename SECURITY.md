# Security Policy

## Reporting a vulnerability

Do not open a public issue for an unpatched vulnerability.

Use GitHub Private Vulnerability Reporting or a private Security Advisory. Include:

- affected version and path;
- impact;
- minimal reproduction;
- whether secrets, personal data, tenant data, or package integrity may be affected;
- proposed mitigation, when known.

## Response targets

- Acknowledgment: three business days.
- Initial assessment: seven business days.
- Remediation timeline: based on severity and exploitability.

## Skill security rules

The project rejects skills or examples that:

- facilitate unauthorized access or data exfiltration;
- hide destructive side effects;
- weaken tenant isolation or authorization;
- log secrets or raw credentials;
- require unreviewed remote code execution;
- present unsafe defaults as production-ready;
- include real customer or personal data.

## Consumer responsibility

Skills are inspectable instructions, not a security boundary. Enforce permissions, isolation, approvals, secrets management, and destructive-action controls in the consuming environment.
