# Evaluation

Evaluations test whether a skill improves real task completion without introducing unsafe behavior, excessive complexity, or hidden assumptions.

## Evaluation types

- Structural
- Behavioral
- Security and tenant isolation
- Migration and compatibility
- Reliability and failure recovery
- Efficiency
- Human expert review

## Comparison

For consequential changes, compare the candidate skill with the previous version or no skill under the same task and environment.

Record:

- skill name and version;
- task;
- fixtures;
- agent and model;
- tool permissions;
- assertions;
- result;
- reviewer;
- date;
- duration and cost when available.

## Good assertions

Good assertions are observable:

- tenant context comes from trusted identity;
- duplicate delivery does not repeat the business mutation;
- public error codes remain stable;
- rollback is defined;
- cross-tenant negative tests exist.

Avoid assertions such as “the answer is good” or “the architecture is scalable.”
