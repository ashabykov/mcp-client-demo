"""
MCP Client Demo — connect to an MCP server and list available tools.

Usage:
    uv run python mcp_client_demo.py
"""

import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def run_client():
    MCP_URL = "http://localhost:8000/mcp"
    MCP_TOKEN = "dev-key-1"

    async with streamablehttp_client(
            url=MCP_URL,
            headers={"Authorization": f"Bearer {MCP_TOKEN}"}
    ) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.list_tools()
            for tool in result.tools:
                print(f"- {tool.name}: {tool.description}")


def main():
    asyncio.run(run_client())


if __name__ == "__main__":
    main()
