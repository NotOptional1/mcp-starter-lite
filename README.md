# MCP Starter Lite (free)

[![tests](../../actions/workflows/test.yml/badge.svg)](../../actions/workflows/test.yml)

The smallest useful MCP server: one tool (`days_until`) with validation, plus 2 tests through a real MCP client. For the Python MCP SDK 2.x (`MCPServer`).

```bash
pip install "mcp>=2" pytest
python -m pytest
python server.py        # stdio
```
Claude Desktop / Claude Code config: `{ "mcpServers": { "starter-lite": { "command": "python3", "args": ["/abs/path/server.py"] } } }`

Local stdio only, no authentication.

## Extend it
Add a function with `@mcp.tool()`; type hints become the input schema and the docstring the description. Raise `ToolError("message")` for failures you expect, so the model sees a clear error.

## Want more?
The full **MCP Server Starter** adds 3 tools, a resource, a prompt, path-traversal-safe file notes and 5 tests: https://gilishe.gumroad.com/l/mcp-server-starter

## Notices
MIT licensed (see LICENSE). Depends on `mcp` (MIT) and `pytest` (MIT), installed separately. Claude and Anthropic are trademarks of Anthropic, PBC; "MCP" refers to the open Model Context Protocol. This project is not affiliated with or endorsed by them. Created with AI assistance (Claude) and tested as described here.
