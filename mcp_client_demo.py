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
    # ---------------------------------------------------------------------------
    # TODO 1: Define StdioServerParameters to launch the MCP server.
    #
    # StdioServerParameters tells the client how to start the server process.
    # Define StdioServerParameters and set it to the server_params variable.
    # You'll need to specify the command and the arguments to launch server.py.
    # ---------------------------------------------------------------------------
    server_params = StdioServerParameters(
        command="uv",
        args=["run", "server.py"],
    )

    # ---------------------------------------------------------------------------
    # TODO 2: Connect to the server via stdio and initialize the session.
    #
    # Use the stdio_client function to open a connection (remember to pass in
    # 'server_params' from the previous TODO as an argument). Inside the block,
    # open a ClientSession and call .initialize() within it to start the MCP
    # handshake. Both stdio_client and ClientSession are async context managers.
    # (Note: check out the MCP Python SDK documentation if you need a refresher
    # on how to use the stdio_client function.)
    # ---------------------------------------------------------------------------
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # -------------------------------------------------------------------
            # TODO 3: List all available tools and print their names,
            #         descriptions, and input schemas.
            #
            # The session has a method that returns the list of tools the
            # server exposes. Each tool has a name, a description, and an input
            # schema — print all three for every tool.
            # -------------------------------------------------------------------
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
