from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Simple Text MCP")

@mcp.tool()
def echo_text(text: str) -> dict:
    """Return the submitted text in a simple JSON object."""
    return {"text": text}

def main():
    mcp.run()

if __name__ == "__main__":
    main()
