# Shell / Terminal MCP Server

A simple Model Context Protocol (MCP) server built with the official Python MCP SDK (`mcp`).

This server exposes tools and resources for local execution and file reading.

## Features

### 1. Resources
- **URI**: `desktop://mcpreadmen.md`
- **Name**: `mcpreadmen.md`
- **MIME Type**: `text/markdown`
- **Description**: Dynamically reads and returns the contents of `mcpreadmen.md` from the user's Desktop directory.

### 2. Tools
- **`shell_tool`** (alias **`terminal_tool`**):
  - **Description**: Executes a shell/terminal command on the host system and returns standard output and error.
  - **Parameters**:
    - `command` (`string`, required): The shell command line string to run (e.g. `dir`, `echo hello`, `git status`).

## Requirements

- Python >= 3.10
- `mcp` (`mcp[cli]>=2.3.0`)

## Installation

Using `uv`:
```bash
uv sync
```

Or using standard `pip`:
```bash
pip install "mcp[cli]>=2.3.0"
```

## Running the Server

Run the server via stdio transport:
```bash
uv run python main.py
```

## Connecting to MCP Clients (e.g., Antigravity, Claude Desktop)

In your MCP configuration file (`mcp_config.json`):

```json
{
  "mcpServers": {
    "shell-server": {
      "command": "E:/mcp_servers_Course/shellServer/.venv/Scripts/python.exe",
      "args": [
        "E:/mcp_servers_Course/shellServer/main.py"
      ]
    }
  }
}
```
# mcp-server-edan-course
