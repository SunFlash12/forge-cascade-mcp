FROM python:3.12-slim

LABEL org.opencontainers.image.title="Forge Cascade MCP Memory Server"
LABEL org.opencontainers.image.description="Public MCP connector for Forge Cascade enterprise AI memory buyer routes."
LABEL org.opencontainers.image.source="https://github.com/SunFlash12/forge-cascade-mcp"
LABEL org.opencontainers.image.url="https://sunflash12.github.io/ForgeV3/mcp-agent-memory.html"
LABEL org.opencontainers.image.licenses="MIT"

WORKDIR /app

COPY pyproject.toml README.md LICENSE ./
COPY src ./src

RUN pip install --no-cache-dir .

ENTRYPOINT ["forge-cascade-mcp"]
