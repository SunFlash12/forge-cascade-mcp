"""Minimal smoke tests so CI has something to run.

The MCP server itself doesn't have a stable in-process API surface yet
(everything is wired to MCP framework callbacks), so this just confirms
the package imports cleanly and the public URL constants point at the
canonical froggit.ai domain.
"""
from __future__ import annotations


def test_package_imports() -> None:
    import forge_cascade_mcp  # noqa: F401
    from forge_cascade_mcp import server  # noqa: F401


def test_public_urls_use_canonical_domain() -> None:
    """Audit 2026-06-24: domain migrated from forgecascade.org to froggit.ai.
    Any stale URL in the server module is a docs/config bug — lock it.
    """
    import forge_cascade_mcp.server as server_module
    import inspect

    source = inspect.getsource(server_module)
    assert "forgecascade.org" not in source, (
        "forgecascade.org reference left in server module after domain migration"
    )
