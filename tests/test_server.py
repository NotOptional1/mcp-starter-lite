import asyncio
from datetime import date, timedelta
import server
from mcp.client import Client


def call(args):
    async def go():
        async with Client(server.mcp) as c:
            return await c.call_tool("days_until", args)
    return asyncio.run(go())


def test_days_until():
    d = (date.today() + timedelta(days=10)).isoformat()
    assert call({"target": d}).content[0].text == "10"


def test_bad_date_is_tool_error():
    r = call({"target": "tomorrow"})
    assert r.is_error and "ISO date" in r.content[0].text
