# Froggit MCP Connector

Froggit is company memory for people and AI, by Frowg Systems. Access it through MCP, REST, and A2A.

## What this package is, and what it is not

This repository is a small public connector. It returns public documentation
and product links so AI agents, directories, and reviewers can find the
Froggit product surface. It holds no customer data and no secrets.

It is NOT the Froggit memory server. It does not search, read, or store
company memory. The Froggit memory MCP server is hosted by Frowg Systems at
https://froggit.ai/mcp and requires an API key issued through Froggit agent
onboarding. Its manifest is published at
https://froggit.ai/.well-known/mcp.json and the agent documentation is at
https://froggit.ai/docs/agents. Public Froggit content can also be read
without a key through public search (https://froggit.ai/public/search) and
the public catalog (https://froggit.ai/api/v1/capsules/public/browse).

Product: https://froggit.ai/
Documentation: https://froggit.ai/docs/agents
Product MCP manifest: https://froggit.ai/.well-known/mcp.json
Source repository: https://github.com/SunFlash12/forge-cascade-mcp

## What It Exposes

- Tool: `forge_buyer_routes`
- Tool: `forge_checkout_links`
- Tool: `forge_paid_route_for_context`
- Resource: `forge://buyer-routes`
- Prompt: `assess_mcp_memory_fit`

The server returns public links only. It does not proxy private customer data,
store secrets, or expose the private Forge deployment.

`forge_checkout_links` returns Froggit's public purchase links. Froggit
currently publishes no public offers, so it returns the live offer catalog
and contact links instead of checkout paths.

`forge_paid_route_for_context` accepts buyer context, budget, urgency, and
procurement authority signals, then recommends the right next step:
documentation and the public evaluation surface for self-serve review, or
the contact page for evaluator access, pilots, and enterprise onboarding.

## Public Froggit Links

- Product: https://froggit.ai/
- MCP docs: https://froggit.ai/docs/agents
- MCP manifest (hosted memory server): https://froggit.ai/.well-known/mcp.json
- OpenAPI: https://froggit.ai/openapi.json
- Offers JSON (public offer catalog, currently empty): https://froggit.ai/offers.json
- Contact: https://froggit.ai/contact

## Run Locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
forge-cascade-mcp
```

The default transport is the MCP SDK's stdio transport.

## Install From GitHub

```bash
pip install "git+https://github.com/SunFlash12/forge-cascade-mcp.git"
forge-cascade-mcp
```

Claude Desktop / Cursor-style config:

```json
{
  "mcpServers": {
    "forge-cascade": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/SunFlash12/forge-cascade-mcp.git",
        "forge-cascade-mcp"
      ]
    }
  }
}
```

## Run With Docker

```bash
docker run --rm -i ghcr.io/sunflash12/forge-cascade-mcp:latest
```

MCP Find / directory package metadata:

- Package name: `ghcr.io/sunflash12/forge-cascade-mcp`
- Package type: Docker
- Category: `search`

## Directory Metadata

Directory-friendly metadata is available in:

- `mcp.json`
- `llms.txt`
- `LAUNCHGUIDE.md`
- `.well-known/mcp.json`
- `.well-known/mcp/server-card.json`
- `.well-known/mcp/server.json`
- `server.json`
- `smithery.yaml`

Official MCP Registry listing:
https://registry.modelcontextprotocol.io/?search=io.github.SunFlash12%2Fforge-cascade-mcp

The Registry metadata includes `websiteUrl` pointing to the Froggit product
home:
https://froggit.ai/

Live directory and registry proof:

- Glama connector: https://glama.ai/mcp/connectors/io.github.SunFlash12/forge-cascade-mcp
- drio listing: https://www.getdrio.com/mcp/io-github-sunflash12-forge-cascade-mcp
- MCP Server Hub listing: https://mcpserver.dev/s/forge-cascade-mcp-memory-server_uo525w0
- MCPRepository listing: https://mcprepository.com/sunflash12/forge-cascade-mcp
- ToolRoute listing: https://toolroute.io/mcp-servers/forge-cascade-mcp-memory-server
- Docker MCP Registry PR: https://github.com/docker/mcp-registry/pull/3874
- MCP Foundry PR: https://github.com/mcpfoundry/registry/pull/9
- ToolSDK MCP Registry PR: https://github.com/toolsdk-ai/toolsdk-mcp-registry/pull/328
- Awesome MCP Servers PR: https://github.com/punkpeye/awesome-mcp-servers/pull/7173

Smithery and other MCP scanners that cannot complete an authenticated
production scan can use the static server card:
https://raw.githubusercontent.com/SunFlash12/forge-cascade-mcp/main/.well-known/mcp/server-card.json

## License

MIT
