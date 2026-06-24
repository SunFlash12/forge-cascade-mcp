# Security Policy

## Supported versions

Only the `main` branch is supported. Previously published container
tags are not patched in place; upgrade to a newer tag instead.

## Reporting a vulnerability

**Please do not file public GitHub issues for security problems.**

Email security reports to **ideanmoslehi@gmail.com** with:

- A description of the issue
- Steps to reproduce (or a proof of concept)
- The version / image tag affected
- Your disclosure timeline preference

You will receive an acknowledgement within 72 hours. Coordinated
disclosure (after a fix is available) is preferred; if you have not
received a response within 7 days, please follow up.

## Scope

In scope:

- The `forge-cascade-mcp` Python server in this repository
- The published Docker image
- The metadata served from `.well-known/`

Out of scope:

- The hosted Forge Cascade backend at `froggit.ai` — report those to
  the same email, but they are tracked separately
- Issues that require non-default configuration or compromised hosts
- Findings in upstream dependencies that already have a CVE; please
  open a normal Dependabot/issue instead
