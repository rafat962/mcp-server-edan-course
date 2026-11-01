import subprocess
from pathlib import Path

try:
    from mcp.server.mcpserver import MCPServer
except ImportError:
    # Fallback for mcp < 2.0
    from mcp.server.fastmcp import FastMCP as MCPServer

# Initialize MCP server
server = MCPServer("shell-server")


# Expose resource: desktop://mcpreadmen.md
@server.resource(
    "desktop://mcpreadmen.md",
    name="mcpreadmen.md",
    title="Desktop MCP Readme",
    description="Contents of mcpreadmen.md located on the Desktop",
    mime_type="text/markdown",
)
def get_desktop_readme() -> str:
    """Read and return the contents of mcpreadmen.md from the Desktop."""
    candidates = [
        Path.home() / "OneDrive" / "Desktop" / "mcpreadmen.md",
        Path.home() / "Desktop" / "mcpreadmen.md",
        Path.home() / "OneDrive" / "Desktop" / "mcpreadme.md",
        Path.home() / "Desktop" / "mcpreadme.md",
    ]
    for path in candidates:
        if path.is_file():
            return path.read_text(encoding="utf-8")

    return "Error: mcpreadmen.md was not found on your Desktop."


@server.tool(
    name="shell_tool",
    description="Execute a shell command on the system and return the output.",
)
def shell_tool(command: str) -> str:
    """Run a shell command and return stdout and stderr.

    Args:
        command: The command line string to execute.
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=60,
        )
        output_parts = []
        if result.stdout:
            output_parts.append(result.stdout)
        if result.stderr:
            output_parts.append(f"STDERR:\n{result.stderr}")

        if not output_parts:
            return f"Command finished with exit code {result.returncode} with no output."

        return "\n".join(output_parts).strip()
    except subprocess.TimeoutExpired:
        return "Error: Command timed out after 60 seconds."
    except Exception as e:
        return f"Error executing command: {str(e)}"


@server.tool(
    name="terminal_tool",
    description="Execute a terminal command on the system and return the output (alias to shell_tool).",
)
def terminal_tool(command: str) -> str:
    """Alias for shell_tool."""
    return shell_tool(command)


if __name__ == "__main__":
    server.run()
