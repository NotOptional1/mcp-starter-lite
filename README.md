# MCP Starter Lite (free)

[![tests](../../actions/workflows/test.yml/badge.svg)](../../actions/workflows/test.yml)

The smallest useful MCP server: one tool (`days_until`) with validation, plus 2 tests through a real MCP client. For the Python MCP SDK 2.x (`MCPServer`).

```bash
pip install "mcp>=2" pytest
python -m pytest
python server.py        # stdio
```
Local stdio only, no authentication.

## Connect it to Claude
First make sure the server works on its own: `python -m pytest` should show 2 passed. Use the **absolute** path to `server.py` and the same Python that has `mcp` installed (if you used a virtualenv, give the full path to that venv's `python`).

**Claude Code** (command line):
```bash
claude mcp add starter-lite -- python3 /abs/path/server.py
claude mcp list          # starter-lite should appear
```
Then ask: "How many days until 2030-01-01?" and approve the `days_until` tool call.

**Claude Desktop:** open Settings > Developer > Edit Config (the file is `claude_desktop_config.json`), add this, save and fully restart the app:
```json
{ "mcpServers": { "starter-lite": { "command": "python3", "args": ["/abs/path/server.py"] } } }
```
If the file already has an `mcpServers` block, add `starter-lite` inside it instead of a second block.

**If it doesn't show up:** a relative path, a Python without `mcp` installed, or invalid JSON in the config are the usual causes. Run `python3 /abs/path/server.py` in a terminal; it should wait silently for input (stop it with Ctrl+C). An import error there is your answer.

What I tested: the server starts and answers tool calls over stdio through the SDK's own client (that is what the 2 tests do). What I did not test: the Claude Desktop and Claude Code steps above, which follow their documented config format; menu names and commands may differ in your version.

## Extend it
Add a function with `@mcp.tool()`; type hints become the input schema and the docstring the description. Raise `ToolError("message")` for failures you expect, so the model sees a clear error.

## Want more?
The full **MCP Server Starter** adds 3 tools, a resource, a prompt, path-traversal-safe file notes and 5 tests: https://gilishe.gumroad.com/l/mcp-server-starter

## Notices
MIT licensed (see LICENSE). Depends on `mcp` (MIT) and `pytest` (MIT), installed separately. Claude and Anthropic are trademarks of Anthropic, PBC; "MCP" refers to the open Model Context Protocol. This project is not affiliated with or endorsed by them. Created with AI assistance (Claude) and tested as described here.
