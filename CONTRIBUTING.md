# Contributing

Thanks for your interest in `forge-cascade-mcp`.

## Quick start

```bash
git clone https://github.com/SunFlash12/forge-cascade-mcp
cd forge-cascade-mcp
pip install -e .[dev]
pytest
```

## Development requirements

- Python 3.10+
- `mcp>=1.2.0` (installed as a dependency)

## Style

- Run `ruff check src` before committing.
- Run `ruff format src` to apply formatting.
- Type hints are required on new public functions.

## Tests

Live under `tests/`. The CI workflow (`.github/workflows/ci.yml`) runs
`pytest` on Python 3.10, 3.11, and 3.12 against every push and pull
request. A PR will not be merged if CI is red.

## Reporting security issues

Do not file public issues for security problems — see `SECURITY.md`.

## Pull requests

- One logical change per PR.
- Reference any related issue.
- Add or update tests when behavior changes.
- Keep the README, `.well-known/mcp.json`, and `mcp.json` in sync if a
  PR changes the exposed surface (tools, endpoints, auth posture).
