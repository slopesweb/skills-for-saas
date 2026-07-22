# OpenAI Codex Adapter

Use `AGENTS.md` as the repository router and store selected skills under `.agent/skills/`. Direct Codex to the relevant skill, project context, active specification, and ADRs. Tool permissions remain controlled by the Codex environment.

## Safety

Review skills before enabling them. Restrict tools, sandbox scripts, protect secrets, and require confirmation for destructive or production actions.
