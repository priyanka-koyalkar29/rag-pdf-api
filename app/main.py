from fastapi import FastAPI
from app.routers import ingest, query

app = FastAPI(
    title="RAG PDF API",
    description="Upload a PDF and ask questions about it",
    version="1.0.0"
)

app.include_router(ingest.router)
app.include_router(query.router)


@app.get("/")
async def root():
    return {"message": "RAG PDF API is running"}
