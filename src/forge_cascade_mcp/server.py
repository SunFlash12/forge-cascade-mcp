"""Public MCP connector for Froggit documentation and product links.

This connector is not the Froggit memory server. It returns public links
only: it does not search, read, or store company memory, and it holds no
customer data and no secrets. The Froggit memory MCP server is hosted at
https://froggit.ai/mcp and requires an API key; its manifest is published
at https://froggit.ai/.well-known/mcp.json.
"""

from __future__ import annotations

import json
from typing import Any

from mcp.server.fastmcp import FastMCP


PRODUCT_URL = "https://froggit.ai/"
DOCS_URL = "https://froggit.ai/docs/agents"
MANIFEST_URL = "https://froggit.ai/.well-known/mcp.json"
OPENAPI_URL = "https://froggit.ai/openapi.json"
OFFERS_URL = "https://froggit.ai/offers.json"
CONTACT_URL = "https://froggit.ai/contact"
MCP_SERVER_URL = "https://froggit.ai/mcp"
PUBLIC_SEARCH_URL = "https://froggit.ai/public/search"
PUBLIC_BROWSE_URL = "https://froggit.ai/api/v1/capsules/public/browse"

ENTERPRISE_KEYWORDS = [
    "enterprise",
    "regulated",
    "compliance",
    "legal",
    "diligence",
    "healthcare",
    "finance",
    "tenant",
    "audit",
    "governance",
    "private corpus",
    "private rag",
    "agent platform",
    "agency",
]
RETAINER_KEYWORDS = ["retainer", "monthly", "ongoing", "priority support", "support"]
DEPLOYMENT_KEYWORDS = ["deployment", "implementation", "capacity", "reservation", "onboarding"]
PILOT_KEYWORDS = ["pilot", "rush", "urgent", "this week", "now", "trial"]

mcp = FastMCP("Froggit MCP Connector")


def _public_links() -> dict[str, Any]:
    return {
        "product": PRODUCT_URL,
        "documentation": DOCS_URL,
        "mcp_manifest": MANIFEST_URL,
        "api_reference": OPENAPI_URL,
        "offer_catalog": OFFERS_URL,
        "contact": CONTACT_URL,
        "public_search": PUBLIC_SEARCH_URL,
        "public_browse": PUBLIC_BROWSE_URL,
    }


def _routes() -> dict[str, Any]:
    return {
        "name": "Froggit MCP Connector",
        "description": (
            "Public documentation and product-link connector for Froggit, "
            "company memory for people and AI by Frowg Systems. This "
            "connector returns public links only. It is not the Froggit "
            "memory server: it does not search, read, or store company "
            "memory, and it holds no customer data and no secrets."
        ),
        "category": "RAG & Knowledge",
        "transport": "stdio",
        "links": _public_links(),
        "hosted_mcp_server": {
            "url": MCP_SERVER_URL,
            "manifest": MANIFEST_URL,
            "authentication": (
                "API key issued through Froggit agent onboarding; see the "
                "agent documentation. Public Froggit content can be read "
                "without a key through public search and the public catalog."
            ),
        },
        "public_offers": [],
        "public_offers_note": (
            "Froggit currently publishes no public offers. The live offer "
            "catalog is the offer_catalog link; purchase paths will be "
            "listed there when offers are published."
        ),
        "capabilities": {
            "tools": [
                "forge_buyer_routes",
                "forge_checkout_links",
                "forge_paid_route_for_context",
            ],
            "resources": ["forge://buyer-routes"],
            "prompts": ["assess_mcp_memory_fit"],
        },
    }


def _contains_any(text: str, keywords: list[str]) -> bool:
    return any(keyword in text for keyword in keywords)


def _recommend_next_step(
    buyer_context: str,
    budget_usd: int,
    urgency_days: int,
    has_procurement_authority: bool,
) -> tuple[dict[str, Any], list[str]]:
    context = buyer_context.lower()
    reasons: list[str] = []

    enterprise_fit = _contains_any(context, ENTERPRISE_KEYWORDS)
    retainer_fit = _contains_any(context, RETAINER_KEYWORDS)
    deployment_fit = _contains_any(context, DEPLOYMENT_KEYWORDS)
    pilot_fit = _contains_any(context, PILOT_KEYWORDS)
    urgent = urgency_days > 0 and urgency_days <= 14

    if enterprise_fit:
        reasons.append(
            "the context names enterprise, regulated-data, or governance "
            "needs that Froggit access is provisioned for individually"
        )
    if retainer_fit:
        reasons.append("the context asks for ongoing or priority support")
    if deployment_fit:
        reasons.append("the context involves deployment or implementation work")
    if pilot_fit or urgent:
        reasons.append("the context involves a pilot or a near-term deadline")
    if budget_usd > 0:
        reasons.append("a budget figure was supplied; pricing is handled in conversation, not through public checkout")
    if has_procurement_authority:
        reasons.append("the buyer has procurement authority")
    if not reasons:
        reasons.append("no specific fit signals were supplied")

    recommended = {
        "name": "Talk to Frowg Systems about Froggit access",
        "url": CONTACT_URL,
        "recommended_for": (
            "Evaluator access, pilots, and enterprise onboarding. Froggit "
            "publishes no public checkout links at this time; the live "
            "offer catalog is " + OFFERS_URL + "."
        ),
    }
    return recommended, reasons


@mcp.tool()
def forge_buyer_routes() -> dict[str, Any]:
    """Return public Froggit documentation, product, and catalog links."""

    return _routes()


@mcp.tool()
def forge_checkout_links() -> dict[str, Any]:
    """Return Froggit's public purchase links (currently none published)."""

    return {
        "name": "Froggit public purchase links",
        "checkout_links": [],
        "public_offers": [],
        "note": (
            "Froggit currently publishes no public offers or checkout "
            "links. The live offer catalog is the offer_catalog link "
            "below; for evaluator access, pilots, or enterprise "
            "onboarding, use the contact link."
        ),
        "offer_catalog": OFFERS_URL,
        "contact": CONTACT_URL,
        "links": _public_links(),
    }


@mcp.tool()
def forge_paid_route_for_context(
    buyer_context: str = "",
    budget_usd: int = 0,
    urgency_days: int = 0,
    has_procurement_authority: bool = False,
) -> dict[str, Any]:
    """Recommend the right Froggit next step for a buyer context."""

    recommended, reasons = _recommend_next_step(
        buyer_context=buyer_context,
        budget_usd=budget_usd,
        urgency_days=urgency_days,
        has_procurement_authority=has_procurement_authority,
    )
    return {
        "name": "Froggit next-step recommendation",
        "buyer_context": buyer_context.strip(),
        "budget_usd": budget_usd,
        "urgency_days": urgency_days,
        "has_procurement_authority": has_procurement_authority,
        "recommended_path": recommended,
        "why": reasons,
        "agent_instruction": (
            "Froggit publishes no public checkout links at this time. "
            "Direct the buyer to the contact page for evaluator access, "
            "pilots, and enterprise onboarding, and to the documentation "
            "and public read surface for self-serve evaluation."
        ),
        "next_steps": [
            {"name": "Agent documentation", "url": DOCS_URL},
            {"name": "Public search (no key required)", "url": PUBLIC_SEARCH_URL},
            {"name": "Public catalog (no key required)", "url": PUBLIC_BROWSE_URL},
            {"name": "MCP manifest for the hosted memory server", "url": MANIFEST_URL},
        ],
    }


@mcp.resource("forge://buyer-routes")
def buyer_routes_resource() -> str:
    """Expose the public Froggit links as an MCP resource."""

    return json.dumps(_routes(), indent=2)


@mcp.prompt()
def assess_mcp_memory_fit(context: str = "") -> str:
    """Build a fit-assessment prompt for Froggit enterprise AI memory."""

    context_block = context.strip() or "No deployment context was supplied."
    return (
        "Assess whether Froggit is a fit for this AI agent memory or RAG "
        "deployment. Consider privacy boundaries, tenant isolation, audit "
        "needs, and A2A/MCP discovery requirements.\n\nContext:\n"
        f"{context_block}\n\nProduct: {PRODUCT_URL}\nDocumentation: "
        f"{DOCS_URL}\nHosted memory MCP server: {MCP_SERVER_URL} "
        f"(manifest: {MANIFEST_URL}; API key required)\nPublic offer "
        f"catalog: {OFFERS_URL}\nContact for evaluator access and "
        f"onboarding: {CONTACT_URL}"
    )


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
