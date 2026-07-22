# Maintainer Review Checklist

- [ ] Scope is not duplicated.
- [ ] Name and directory match.
- [ ] Description includes trigger conditions.
- [ ] Workflow produces concrete artifacts.
- [ ] Tenant isolation is addressed where relevant.
- [ ] Authorization is server-side.
- [ ] Idempotency and retries are addressed where relevant.
- [ ] Security and privacy impact is explicit.
- [ ] i18n uses stable codes and externalized human text.
- [ ] Provider-specific concerns stay behind adapters.
- [ ] References remain relative and inside the skill.
- [ ] Evaluations include a failure or negative case.
- [ ] Core source remains runtime-agnostic.
- [ ] Optional tools use no third-party Python packages.
- [ ] Catalog is regenerated.
- [ ] Changelog and versions are correct.
