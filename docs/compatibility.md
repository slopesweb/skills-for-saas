# Compatibility

## Portable compatibility levels

### Level 0: Manual

A human reads and follows `SKILL.md`.

### Level 1: Discovery

A consumer indexes `name`, `description`, and metadata.

### Level 2: Progressive loading

A consumer loads the main document and resolves relative references only when needed.

### Level 3: Resources

A consumer supports optional scripts or assets with explicit permission and sandboxing.

### Level 4: Evaluation

A consumer can run evaluation fixtures and record provenance.

## Minimum behavior

A compatible consumer should:

1. parse supported frontmatter;
2. match intent against name and description;
3. load the selected body;
4. preserve relative resource paths;
5. expose the skill version in execution provenance;
6. restrict tools independently of skill instructions;
7. require confirmation before destructive actions.

## Independence

The format is independent of application runtimes, frameworks, programming languages, databases, clouds, and model providers.
