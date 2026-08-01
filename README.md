In this task, you'll write an MCP client that connects to your MCP server and discovers its available tools.

## Workflow at a glance

👩‍💻
1. Set up your environment
2. Write the client script
3. Implement the client logic
4. Run the script
5. Submit your task

## 1. Set up your environment

Once you log in to your GitHub account, the repository for this task will be added automatically.

1. Confirm that `mcp-client-demo` appears in your account. 
2. Clone the repo locally and open it in your editor.

## 2. Write your client script

Create a file called `mcp_client_demo.py`.

Your script should:

1. Start the MCP server as a subprocess using stdio transport
2. Initialize a client session using the MCP SDK
3. List all tools exposed by the server
4. Print each tool's details — name, description, and input schema 

## 3. Implement the client logic

Your script should roughly follow this flow:

```
# 1. Define StdioServerParameters to launch the MCP server
# 2. Connect via stdio_client and create a ClientSession
# 3. Call session.initialize()
# 4. Call session.list_tools()
# 5. Print each tool's name, description, and input schema
```

## 4. Run the script

Run your client demo from the project root:

```
uv run python mcp_client_demo.py
```

If everything is set up correctly, the script should connect to the server and print the available tools along with their details.

## Optional: Connect your server to a real AI tool

Now try your server in a real developer workflow.

1. Add your MCP server to Claude Code or Cursor using the same stdio command you used in your client script.
2. Restart the tool if needed so it reloads the MCP configuration.
3. Ask a real question, for example:
    - `Which files are risky to change in this repo?`
    - `Show me the hotspot files in this codebase.`
4. Confirm that the tool:
    - Discovers your MCP server
    - Calls the relevant MCP tool
    - Uses the tool result in its answer

## 5. Submit your task

Before submitting, review the submission checklist below.

### ✅ Submission checklist

- [ ]  `mcp_client_demo.py` exists and runs successfully
- [ ]  The script starts the MCP server via stdio
- [ ]  The script initializes a client session
- [ ]  The script lists the server's available tools
- [ ]  The script prints each tool's name, description, and input schema
