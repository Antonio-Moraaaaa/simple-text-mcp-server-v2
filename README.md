# Simple Text MCP Server

A minimal Model Context Protocol (MCP) server for marketplace testing.

## Tool: echo_text

Input:
```json
{"text":"hello"}
```

Output:
```json
{"text":"hello"}
```

## Requirements
- Python 3.10+

## Install
```bash
pip install .
```

## Run
```bash
simple-text-mcp
```

## Test with MCP Inspector
```bash
npx @modelcontextprotocol/inspector simple-text-mcp
```
