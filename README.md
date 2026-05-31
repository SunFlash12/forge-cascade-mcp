# Forge Cascade MCP

Public MCP connector for Forge Cascade enterprise AI memory buyer routes.

This repository exists so MCP directories and automated scanners can evaluate a
public, no-secret server that points agents to Forge Cascade's public discovery,
documentation, OpenAPI, pricing, and enterprise intake surfaces.

## What It Exposes

- Tool: `forge_buyer_routes`
- Resource: `forge://buyer-routes`
- Prompt: `assess_mcp_memory_fit`

The server returns public links only. It does not proxy private customer data,
store secrets, or expose the private Forge deployment.

## Public Forge Routes

- Buyer route: https://sunflash12.github.io/ForgeV3/mcp-agent-memory.html
- MCP manifest: https://sunflash12.github.io/ForgeV3/.well-known/mcp.json
- MCP docs: https://sunflash12.github.io/ForgeV3/mcp.html
- OpenAPI: https://sunflash12.github.io/ForgeV3/openapi.json
- Pricing: https://sunflash12.github.io/ForgeV3/pricing.html
- Enterprise: https://sunflash12.github.io/ForgeV3/enterprise.html

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
- `.well-known/mcp.json`
- `server.json`

Official MCP Registry listing:
https://registry.modelcontextprotocol.io/?search=io.github.SunFlash12%2Fforge-cascade-mcp

## License

MIT
