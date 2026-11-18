# Cairn

Cairn helps software projects build on what they learn by making assumptions, decisions, and evidence explicit, connected, and checkable. Designed around a command-line interface and companion skills, it combines checks against declared rules with agent assistance for investigation and review. Cairn builds on Git and GitHub/GitLab to help maintainers understand why choices were made, what was learned, and when earlier reasoning needs revisiting.


[Go read the Cairn manifesto](manifesto.md)

## Local label catalogue

Install the project and initialize a catalogue in an existing project directory:

```bash
uv sync
uv run cairn config labels init --project /path/to/project
uv run cairn config labels check --project /path/to/project
```

Both commands default to the current directory when `--project` is omitted;
they do not search parent directories. `init` creates `.config/cairn/labels.yaml`
from the bundled preset only when the file is absent. Edit that project file
to customize labels. Repeating `init` validates and preserves existing content,
including invalid content. `check` is read-only and never falls back to defaults.

The catalogue uses strict UTF-8 YAML: quote six-digit colors and any strings that
YAML would otherwise interpret as booleans or dates. Validation reports a stable
diagnostic code, field path and source location when available. Commands return
0 on success, 1 for catalogue or filesystem errors, and 2 for CLI usage errors.

These commands work offline. Remote synchronization and issue-assignment checks
are not implemented. See [the implementation notes](devdocs/development/label-catalogue-yaml-and-cli.md)
for the supported format, tests and current limits.

