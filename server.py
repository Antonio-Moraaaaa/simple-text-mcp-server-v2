from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "status": "Simple Text MCP running"
    }

@app.post("/echo")
def echo(data: dict):
    return {
        "text": data.get("text", "")
    }
