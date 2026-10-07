"""Minimal MCP server (MCP Python SDK 2.x). Run: python server.py  (stdio)."""
from datetime import date
from mcp.server.mcpserver import MCPServer
from mcp.server.mcpserver.exceptions import ToolError

mcp = MCPServer("starter-lite")


@mcp.tool()
def days_until(target: str) -> int:
    """Days from today until an ISO date (YYYY-MM-DD). Negative if in the past."""
    try:
        return (date.fromisoformat(target) - date.today()).days
    except ValueError:
        raise ToolError("target must be an ISO date like 2026-12-31")


if __name__ == "__main__":
    mcp.run()
