"""
MCP Client Demo — connect to an MCP server and list available tools.

Usage:
    uv run python mcp_client_demo.py
"""

import asyncio
import json

from mcp import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client


async def run_client():
    server_params = StdioServerParameters(
        command="uv",
        args=["run", "server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tool_list = await session.list_tools()
            for tool in tool_list.tools:
                print(tool.name)
                print(tool.description)
                print(json.dumps(tool.inputSchema, indent=2))
                print()


def main():
    asyncio.run(run_client())


if __name__ == "__main__":
    main()
