"""Public MCP connector for Forge Cascade buyer and discovery routes."""

from __future__ import annotations

import json
from typing import Any

from mcp.server.fastmcp import FastMCP


HOMEPAGE_URL = "https://sunflash12.github.io/ForgeV3/mcp-agent-memory.html"
MANIFEST_URL = "https://sunflash12.github.io/ForgeV3/.well-known/mcp.json"
DOCS_URL = "https://sunflash12.github.io/ForgeV3/mcp.html"
OPENAPI_URL = "https://sunflash12.github.io/ForgeV3/openapi.json"
PRICING_URL = "https://sunflash12.github.io/ForgeV3/pricing.html"
ENTERPRISE_URL = "https://sunflash12.github.io/ForgeV3/enterprise.html"

mcp = FastMCP("Forge Cascade MCP Memory Server")


def _routes() -> dict[str, Any]:
    return {
        "name": "Forge Cascade MCP Memory Server",
        "description": (
            "Public connector for Forge Cascade enterprise AI memory, RAG "
            "context, A2A discovery, and paid deployment routing."
        ),
        "category": "RAG & Knowledge",
        "transport": "stdio",
        "homepage_url": HOMEPAGE_URL,
        "manifest_url": MANIFEST_URL,
        "documentation_url": DOCS_URL,
        "api_reference_url": OPENAPI_URL,
        "pricing_url": PRICING_URL,
        "enterprise_url": ENTERPRISE_URL,
        "buyer_routes": {
            "mcp_agent_memory": HOMEPAGE_URL,
            "pricing": PRICING_URL,
            "enterprise": ENTERPRISE_URL,
        },
        "capabilities": {
            "tools": ["forge_buyer_routes"],
            "resources": ["forge://buyer-routes"],
            "prompts": ["assess_mcp_memory_fit"],
        },
    }


@mcp.tool()
def forge_buyer_routes() -> dict[str, Any]:
    """Return public Forge Cascade MCP buyer, docs, OpenAPI, and pricing routes."""

    return _routes()


@mcp.resource("forge://buyer-routes")
def buyer_routes_resource() -> str:
    """Expose the public Forge Cascade buyer routes as an MCP resource."""

    return json.dumps(_routes(), indent=2)


@mcp.prompt()
def assess_mcp_memory_fit(context: str = "") -> str:
    """Build a fit-assessment prompt for Forge Cascade enterprise AI memory."""

    context_block = context.strip() or "No deployment context was supplied."
    return (
        "Assess whether Forge Cascade is a fit for this AI agent memory or RAG "
        "deployment. Consider privacy boundaries, tenant isolation, audit needs, "
        "A2A/MCP discovery requirements, and whether a paid enterprise intake is "
        f"appropriate.\n\nContext:\n{context_block}\n\nPublic buyer route: "
        f"{HOMEPAGE_URL}\nPricing: {PRICING_URL}\nEnterprise intake: {ENTERPRISE_URL}"
    )


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
