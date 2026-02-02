from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from query import query_chromadb

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve browser
@app.get("/chroma_browser.html")
def read_browser():
    return FileResponse("static/chroma_browser.html")

# API model
class QueryRequest(BaseModel):
    query: str
    top_k: int = 2

@app.post("/query")
def query_endpoint(request: QueryRequest):
    result = query_chromadb(request.query, request.top_k)
    return {"query": request.query, "top_k": request.top_k, "result": result}
